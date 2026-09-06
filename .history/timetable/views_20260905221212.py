

from django.shortcuts import render
from .models import StudentGroup, TimetableEntry


def timetable_list(request):
    groups = StudentGroup.objects.filter(
        is_active=True
    )

    entries = TimetableEntry.objects.filter(
        is_active=True
    ).select_related("group")

    return render(
        request,
        "timetable/list.html",
        {
            "groups": groups,
            "entries": entries,
        }
    )