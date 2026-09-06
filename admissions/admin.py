from django.contrib import admin
from .models import AdmissionInformation


@admin.register(AdmissionInformation)
class AdmissionInformationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )