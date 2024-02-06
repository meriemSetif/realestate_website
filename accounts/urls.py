from django.urls import path
from . import views

# define your urlpatterns here
urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
]
