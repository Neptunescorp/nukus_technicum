from django.shortcuts import render

from .models import TopStudent


def top_students_list(request):

    students = TopStudent.objects.filter(
        is_active=True
    ).select_related("group")

    return render(
        request,
        "top_students/list.html",
        {
            "students": students,
        }
    )