from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["vendor", "name", "price", "url", "scraped_at"]
    search_fields = ["vendor", "name", "price", "url", "scraped_at"]
    list_select_related = True


admin.site.register(Product, ProductAdmin)
