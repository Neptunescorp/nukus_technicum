from django.db import models


class SiteInformation(models.Model):
    name = models.CharField(
        max_length=255,
        default="Nukus Shahar 3-sonli Texnikum"
    )
    short_description = models.TextField(blank=True)
    about = models.TextField(blank=True)

    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)

    logo = models.ImageField(
        upload_to="site/",
        blank=True,
        null=True
    )

    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Information"
        verbose_name_plural = "Site Information"

    def __str__(self):
        return self.name