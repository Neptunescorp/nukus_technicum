from django.db import models


class AdmissionInformation(models.Model):
    title = models.CharField(
        max_length=255,
        default="Admission Information"
    )

    description = models.TextField(
        blank=True
    )

    requirements = models.TextField(
        blank=True
    )

    required_documents = models.TextField(
        blank=True
    )

    important_dates = models.TextField(
        blank=True
    )

    application_process = models.TextField(
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Admission Information"
        verbose_name_plural = "Admission Information"

    def __str__(self):
        return self.title