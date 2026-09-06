from django.shortcuts import render
from .models import GalleryImage


def gallery_list(request):
    images = GalleryImage.objects.filter(
        is_active=True
    )

    return render(
        request,
        "gallery/list.html",
        {
            "images": images
        }
    )