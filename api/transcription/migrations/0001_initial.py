# Generated by Django 4.1.5 on 2023-01-21 10:42

import django.core.validators
from django.db import migrations, models
import transcription.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="File",
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
                ("transcript", models.TextField(blank=True, null=True)),
                (
                    "file",
                    models.FileField(
                        upload_to=transcription.models.unique_filename,
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["mp3", "mp4"]
                            )
                        ],
                    ),
                ),
            ],
        ),
    ]
