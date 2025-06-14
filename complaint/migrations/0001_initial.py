# Generated by Django 5.1.4 on 2025-06-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Complaint",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="complaint_photos/"
                    ),
                ),
                ("date_of_incident", models.DateField()),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                (
                    "tracking_code",
                    models.CharField(editable=False, max_length=12, unique=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("yet", "Yet to see"),
                            ("accepted", "Accepted"),
                            ("solved", "Solved"),
                        ],
                        default="yet",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
