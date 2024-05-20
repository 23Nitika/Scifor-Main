# Generated by Django 4.2.9 on 2024-05-15 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0050_week_topic"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("bio", models.TextField(blank=True)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, upload_to="profile_pics"),
                ),
                ("mobile_number", models.CharField(blank=True, max_length=15)),
                ("language", models.CharField(blank=True, max_length=50)),
                ("linkedin_profile", models.URLField(blank=True)),
                ("twitter_profile", models.URLField(blank=True)),
                ("facebook_profile", models.URLField(blank=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]