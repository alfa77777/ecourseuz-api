# Generated by Django 4.2.4 on 2023-08-11 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0009_merge_20230811_1749"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]