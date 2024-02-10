from django.contrib import admin
from .models import Listing


# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "is_published",
        "price",
        "list_date",
        "realtor",
    )
    list_display_links = (
        "id",
        "title",
        "list_date",
    )
    list_filter = ("title", "list_date")
    list_editable = ("is_published", "price")
    search_fields = ("title", "description", "list_date", "price")


admin.site.register(Listing, ListingAdmin)
