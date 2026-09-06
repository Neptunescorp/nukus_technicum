from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "position",
        "department",
        "is_active",
    )

    list_filter = (
        "is_active",
        "department",
    )

    search_fields = (
        "full_name",
        "department",
    )