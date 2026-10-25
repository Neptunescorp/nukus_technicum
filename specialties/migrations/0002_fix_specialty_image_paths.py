from django.db import migrations


def fix_specialty_image_paths(apps, schema_editor):
    Specialty = apps.get_model("specialties", "Specialty")

    image_fixes = {
        "Avtomobil servisi": "specialties/service-card-18.webp",
        "Metalǵa qayta islew beriw": "specialties/welder.jpg",
        "Moda hám islep shıǵarıw": (
            "specialties/depositphotos_204441298-stock-photo-young-female-tailor-using-sewing.jpg"
        ),
        "Robototexnika": "specialties/robotatexnika.jpg",
        "Sanlı maǵlıwmatlar hám olardı qayta islew": (
            "specialties/pexels-luis-gomes-166706-546819-scaled.jpg"
        ),
    }

    for name, filename in image_fixes.items():
        Specialty.objects.filter(name=name).update(image=filename)


class Migration(migrations.Migration):
    dependencies = [
        ("specialties", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(fix_specialty_image_paths, migrations.RunPython.noop),
    ]