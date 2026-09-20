from django.urls import path

from .views import top_students_list


app_name = "top_students"


urlpatterns = [
    path(
        "",
        top_students_list,
        name="list"
    ),
]