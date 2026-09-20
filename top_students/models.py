from django.db import models

from timetable.models import StudentGroup


class TopStudent(models.Model):

    full_name = models.CharField(
        max_length=200
    )

    group = models.ForeignKey(
        StudentGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="top_students"
    )

    photo = models.ImageField(
        upload_to="top_students/",
        blank=True,
        null=True
    )

    achievement = models.TextField(
        blank=True
    )

    average_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    academic_year = models.CharField(
        max_length=20,
        blank=True
    )

    position = models.PositiveSmallIntegerField(
        default=1
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Top Student"
        verbose_name_plural = "Top Students"
        ordering = [
            "position",
            "-average_score",
            "full_name",
        ]

    def __str__(self):
        return self.full_name