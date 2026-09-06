from django.urls import path
from .views import teacher_list, teacher_detail


urlpatterns = [
    path("", teacher_list, name="teacher_list"),

    path(
        "<int:pk>/",
        teacher_detail,
        name="teacher_detail"
    ),
]