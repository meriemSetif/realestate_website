from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'listing',
        'message',
        'contact_date'
    )
    list_display_links = (
        'listing',
    )
    list_editable = (
        'message',
    )



# Register your models here.
admin.site.register(Contact,ContactAdmin)
