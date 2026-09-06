from django.urls import path
from .views import specialty_list, specialty_detail


urlpatterns = [
    path("", specialty_list, name="specialty_list"),
    path(
        "<int:pk>/",
        specialty_detail,
        name="specialty_detail"
    ),
]