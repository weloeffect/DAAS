from urllib import request
from django.urls import path
from . import views
app_name = "home"
urlpatterns = [
    path("", views.home, name="home"),
    # path("w", views.home1, name="home1"),
    # path("home", views.test2, name="hom")
]