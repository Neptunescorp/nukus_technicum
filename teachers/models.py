from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(max_length=255)

    position = models.CharField(
        max_length=255,
        blank=True
    )

    department = models.CharField(
        max_length=255,
        blank=True
    )

    biography = models.TextField(
        blank=True
    )

    photo = models.ImageField(
        upload_to="teachers/",
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
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name