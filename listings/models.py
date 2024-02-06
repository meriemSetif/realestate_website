from django.db import models
from instructors.models import Instructor


# Create your models here.
class Listing(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=35)
    city = models.CharField(max_length=35)
    address = models.CharField(max_length=35)
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=35)
    zipcode = models.CharField(max_length=35)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    square_feets = models.IntegerField()
    garage = models.IntegerField(default=0)
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    main_img = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_5 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_6 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.title}"
