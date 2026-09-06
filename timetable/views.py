from django.shortcuts import render
from .models import StudentGroup, TimetableEntry


def timetable_list(request):
    groups = StudentGroup.objects.filter(
        is_active=True
    )

    selected_group_id = request.GET.get("group")

    if selected_group_id:
        entries = TimetableEntry.objects.filter(
            group_id=selected_group_id,
            is_active=True
        ).select_related("group")
    else:
        entries = TimetableEntry.objects.filter(
            is_active=True
        ).select_related("group")

    selected_group = None

    if selected_group_id:
        selected_group = groups.filter(
            id=selected_group_id
        ).first()

    return render(
        request,
        "timetable/list.html",
        {
            "groups": groups,
            "entries": entries,
            "selected_group": selected_group,
        }
    )