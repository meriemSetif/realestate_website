from django.contrib import admin
from .models import Instructor


# Register your models here.
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "photo", "email", "is_mvp")
    list_display_links = ("id", "email")
    list_editable = ("name", "is_mvp")
    list_per_page = 10
    search_fields = ("name", "email", "description")



admin.site.register(Instructor, InstructorAdmin)
