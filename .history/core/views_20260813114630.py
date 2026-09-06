from django.shortcuts import render

from .models import SiteInformation


def about(request):
    information = SiteInformation.objects.first()

    return render(
        request,
        "core/about.html",
        {
            "information": information
        }
    )