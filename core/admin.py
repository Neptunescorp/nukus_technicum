from django.contrib import admin
from .models import SiteInformation


@admin.register(SiteInformation)
class SiteInformationAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "updated_at")