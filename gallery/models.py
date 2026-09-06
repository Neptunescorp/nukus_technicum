from django.db import models


class GalleryImage(models.Model):
    title = models.CharField(
        max_length=255,
        blank=True
    )

    image = models.ImageField(
        upload_to="gallery/"
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title or f"Gallery Image {self.id}"