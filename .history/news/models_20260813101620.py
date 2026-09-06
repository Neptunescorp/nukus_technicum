from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)

    short_description = models.TextField(
        blank=True
    )

    content = models.TextField()

    image = models.ImageField(
        upload_to="news/",
        blank=True,
        null=True
    )

    published_at = models.DateTimeField(
        auto_now_add=True
    )

    is_published = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title