from django.db import models


# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=35)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    is_mvp = models.BooleanField(default=False ,blank=True)
    hire_date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.name}"
