from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("timetable", "0003_alter_timetableentry_day"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timetableentry",
            name="day",
            field=models.CharField(
                choices=[
                    ("monday", "Dúyshembi"),
                    ("tuesday", "Seyshembi"),
                    ("wednesday", "Sárshembi"),
                    ("thursday", "Beishembi"),
                    ("friday", "Juma"),
                    ("saturday", "Shembi"),
                ],
                max_length=20,
            ),
        ),
    ]