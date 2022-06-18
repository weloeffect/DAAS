from urllib import request
from django.urls import path
from . import views
app_name = "commentary"
urlpatterns =[
    path("", views.view, name="comment"),
    path("success", views.insert_comment, name="insert"),
    # path("test", views.test, name="test"),
]