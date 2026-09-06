from django.shortcuts import render

from .models import AdmissionInformation


def admissions(request):
    information = AdmissionInformation.objects.filter(
        is_active=True
    ).first()

    return render(
        request,
        "admissions/index.html",
        {
            "information": information
        }
    )