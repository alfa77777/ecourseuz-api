# Generated by Django 4.2.4 on 2023-08-24 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Card",
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
                ("holder_name", models.CharField(max_length=50)),
                ("number", models.CharField(max_length=16)),
                ("exp_month", models.IntegerField()),
                ("exp_year", models.IntegerField()),
                ("cvc", models.CharField(max_length=10)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cards",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
