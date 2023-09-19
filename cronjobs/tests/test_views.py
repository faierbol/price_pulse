from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIClient

from users.tests.factories import AdminUserFactory, UserFactory

from ..serializers import CronjobSerializer
from .factories import CronjobFactory


class TestCronjob(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = CronjobFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Cronjob instances"""

        resp = self.client.get("/api/v1/cronjobs/cronjob/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Cronjob collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/cronjobs/cronjob/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_list_search(self):
        """Test that Cronjob collection can be searched by"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(
            "/api/v1/cronjobs/cronjob/",
            {
                "task_name__icontains": self.instance.task_name,
            },
        )
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Cronjob instances"""

        resp = self.client.get(f"/api/v1/cronjobs/cronjob/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Cronjob can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/cronjobs/cronjob/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Cronjob"""

        resp = self.client.post("/api/v1/cronjobs/cronjob/")
        self.assertEqual(resp.status_code, 403)

    @patch("cronjobs.views.CronjobViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Cronjob"""

        self.client.force_authenticate(user=self.admin)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = CronjobSerializer(self.instance).data

        resp = self.client.post("/api/v1/cronjobs/cronjob/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Cronjob"""

        resp = self.client.patch(f"/api/v1/cronjobs/cronjob/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Cronjob update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/cronjobs/cronjob/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Cronjob"""

        resp = self.client.delete(f"/api/v1/cronjobs/cronjob/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Cronjob deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/cronjobs/cronjob/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)
