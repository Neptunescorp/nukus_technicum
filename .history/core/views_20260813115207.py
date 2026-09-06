from django.shortcuts import render

from .models import SiteInformation
from specialties.models import Specialty
from teachers.models import Teacher
from news.models import News
from gallery.models import GalleryImage


def home(request):
    information = SiteInformation.objects.first()

    specialties = Specialty.objects.filter(
        is_active=True
    )[:6]

    teachers = Teacher.objects.filter(
        is_active=True
    )[:4]

    news_items = News.objects.filter(
        is_published=True
    )[:3]

    gallery_images = GalleryImage.objects.filter(
        is_active=True
    )[:8]

    return render(
        request,
        "core/home.html",
        {
            "information": information,
            "specialties": specialties,
            "teachers": teachers,
            "news_items": news_items,
            "gallery_images": gallery_images,
        }
    )


def about(request):
    information = SiteInformation.objects.first()

    return render(
        request,
        "core/about.html",
        {
            "information": information
        }
    )


def contact(request):
    information = SiteInformation.objects.first()

    return render(
        request,
        "core/contact.html",
        {
            "information": information
        }
    )