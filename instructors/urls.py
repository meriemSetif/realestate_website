from django.urls import path
from . import views

app_name = "instructors"

urlpatterns = [
    path("", views.index, name="instructors"),
    path("<int:id>", views.instructor, name="instructor"),
    path("search", views.search, name="search"),
]
