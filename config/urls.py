from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("core.urls")),

    path(
        "specialties/",
        include("specialties.urls")
    ),

    path(
        "teachers/",
        include("teachers.urls")
    ),

    path(
        "news/",
        include("news.urls")
    ),

    path(
        "gallery/",
        include("gallery.urls")
    ),

    path(
        "admissions/",
        include("admissions.urls")
    ),

    path(
    "timetable/",
    include("timetable.urls")
    ),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )