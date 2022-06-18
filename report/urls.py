from urllib import request
from django.urls import path
from . import views
app_name = "report"
urlpatterns = [
    path("", views.report, name="report"),
    path("report", views.report_test, name="rep")
]