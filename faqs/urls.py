from urllib import request
from django.urls import path
from . import views
app_name = "faqs"
urlpatterns = [
    path("", views.faqs, name="faqs")
]