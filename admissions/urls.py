from django.urls import path

from .views import admissions


urlpatterns = [
    path("", admissions, name="admissions"),
]