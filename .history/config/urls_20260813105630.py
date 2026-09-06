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
        include("news.urls"))
]