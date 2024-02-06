from django.urls import path
from . import views

# define your urlpatterns here
urlpatterns = [
    path("contact", views.contact, name="contact"),

]
