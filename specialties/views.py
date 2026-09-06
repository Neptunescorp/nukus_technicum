from django.shortcuts import render
from .models import Specialty


def specialty_list(request):
    specialties = Specialty.objects.filter(
        is_active=True
    )

    return render(
        request,
        "specialties/list.html",
        {
            "specialties": specialties
        }
    )


def specialty_detail(request, pk):
    specialty = Specialty.objects.get(
        pk=pk,
        is_active=True
    )

    return render(
        request,
        "specialties/detail.html",
        {
            "specialty": specialty
        }
    )