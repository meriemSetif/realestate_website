from django.urls import path
from . import views

app_name = "realtors"

urlpatterns = [
    path("", views.index, name="realtors"),
    path("<int:id>", views.realtor, name="realtor"),
    path("search", views.search, name="search"),
]
