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

    day_order = {
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6,
    }

    entries = sorted(
        entries,
        key=lambda entry: (
            day_order.get(entry.day, 99),
            entry.lesson_number,
            entry.start_time,
        )
    )

    # Group entries by day
    timetable_by_day = {}

    for entry in entries:
        if entry.day not in timetable_by_day:
            timetable_by_day[entry.day] = []

        timetable_by_day[entry.day].append(entry)

    ordered_days = sorted(
        timetable_by_day.keys(),
        key=lambda day: day_order.get(day, 99)
    )

    return render(
        request,
        "timetable/list.html",
        {
            "groups": groups,
            "entries": entries,
            "selected_group": selected_group,
            "timetable_by_day": timetable_by_day,
            "ordered_days": ordered_days,
        }
    )