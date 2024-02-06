from os import name
from django.db import models
from django.contrib.auth.models import User
from listings.models import Listing
# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=35)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
