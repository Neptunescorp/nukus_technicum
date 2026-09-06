from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=255)

    short_description = models.TextField(
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    duration = models.CharField(
        max_length=100,
        blank=True
    )

    admission_requirements = models.TextField(
        blank=True
    )

    career_opportunities = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="specialties/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name