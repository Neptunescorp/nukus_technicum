from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render

from .models import News


def news_list(request):
    news_items = News.objects.filter(
        is_published=True
    )

    return render(
        request,
        "news/list.html",
        {
            "news_items": news_items
        }
    )


def news_detail(request, pk):
    news_item = get_object_or_404(
        News,
        pk=pk,
        is_published=True
    )

    return render(
        request,
        "news/detail.html",
        {
            "news_item": news_item
        }
    )