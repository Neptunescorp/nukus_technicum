from django.db import models


class Timetable(models.Model):
    title = models.CharField(
        max_length=255,
        default="Class Timetable"
    )

    description = models.TextField(
        blank=True
    )

    timetable_file = models.FileField(
        upload_to="timetables/",
        blank=True,
        null=True
    )

    timetable_image = models.ImageField(
        upload_to="timetables/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Timetable"
        verbose_name_plural = "Timetables"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title