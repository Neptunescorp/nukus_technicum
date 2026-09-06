from django.urls import path

from .views import timetable_list


urlpatterns = [
    path(
        "",
        timetable_list,
        name="timetable_list"
    ),
]