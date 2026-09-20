from django.contrib import admin

from .models import TopStudent


@admin.register(TopStudent)
class TopStudentAdmin(admin.ModelAdmin):

    list_display = (
        "position",
        "full_name",
        "group",
        "average_score",
        "academic_year",
        "is_active",
    )

    list_filter = (
        "group",
        "academic_year",
        "is_active",
    )

    search_fields = (
        "full_name",
        "achievement",
        "group__name",
    )

    ordering = (
        "position",
        "-average_score",
        "full_name",
    )

    list_editable = (
        "is_active",
    )