from django.shortcuts import render

from .models import Timetable


def timetable_list(request):
    timetables = Timetable.objects.filter(
        is_active=True
    )

    return render(
        request,
        "timetable/list.html",
        {
            "timetables": timetables
        }
    )