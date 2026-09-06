from django.contrib import admin
from .models import StudentGroup, TimetableEntry


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(TimetableEntry)
class TimetableEntryAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "group",
        "lesson_number",
        "start_time",
        "end_time",
        "subject",
        "teacher",
        "room",
        "is_active",
    )

    list_filter = (
        "date",
        "group",
        "is_active",
    )

    search_fields = (
        "subject",
        "teacher",
        "room",
        "group__name",
    )

    ordering = (
        "date",
        "group",
        "lesson_number",
    )