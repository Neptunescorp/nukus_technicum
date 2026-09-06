from django.shortcuts import render, get_object_or_404
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.filter(
        is_active=True
    )

    return render(
        request,
        "teachers/list.html",
        {
            "teachers": teachers
        }
    )


def teacher_detail(request, pk):
    teacher = get_object_or_404(
        Teacher,
        pk=pk,
        is_active=True
    )

    return render(
        request,
        "teachers/detail.html",
        {
            "teacher": teacher
        }
    )