from django.contrib import admin
from .models import StudentGroup, TimetableEntry


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
    ordering = ("name",)


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
        "updated_at",
    )

    list_filter = (
        "date",
        "group",
        "is_active",
        "teacher",
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

    list_editable = (
        "subject",
        "teacher",
        "room",
        "is_active",
    )

    autocomplete_fields = ("group",)

    fieldsets = (
        (
            "Lesson Information",
            {
                "fields": (
                    "group",
                    "date",
                    "lesson_number",
                    "start_time",
                    "end_time",
                )
            },
        ),
        (
            "Lesson Details",
            {
                "fields": (
                    "subject",
                    "teacher",
                    "room",
                )
            },
        ),
        (
            "Status",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
    )

    readonly_fields = ("updated_at",)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("group")