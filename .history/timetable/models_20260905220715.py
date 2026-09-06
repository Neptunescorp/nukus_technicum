from django.db import models


class StudentGroup(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = "Student Group"
        verbose_name_plural = "Student Groups"
        ordering = ["name"]

    def __str__(self):
        return self.name


class TimetableEntry(models.Model):
    group = models.ForeignKey(
        StudentGroup,
        on_delete=models.CASCADE,
        related_name="timetable_entries"
    )

    date = models.DateField()

    lesson_number = models.PositiveSmallIntegerField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    subject = models.CharField(
        max_length=200
    )

    teacher = models.CharField(
        max_length=200,
        blank=True
    )

    room = models.CharField(
        max_length=50,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Timetable Entry"
        verbose_name_plural = "Timetable Entries"

        ordering = [
            "date",
            "group",
            "lesson_number"
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "group",
                    "date",
                    "lesson_number"
                ],
                name="unique_group_date_lesson"
            )
        ]

    def __str__(self):
        return (
            f"{self.group} - "
            f"{self.date} - "
            f"{self.lesson_number}. "
            f"{self.subject}"
        )