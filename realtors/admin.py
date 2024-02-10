from django.contrib import admin
from .models import realtor


# Register your models here.
class realtorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "photo", "email", "is_mvp")
    list_display_links = ("id", "email")
    list_editable = ("name", "is_mvp")
    list_per_page = 10
    search_fields = ("name", "email", "description")



admin.site.register(realtor, realtorAdmin)
