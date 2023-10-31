# Generated by Django 4.2.4 on 2023-08-09 08:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0005_alter_applicationform_category_delete_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="aboutus",
            name="video_file",
            field=models.FileField(blank=True, null=True, upload_to="about/videos/"),
        ),
        migrations.AddField(
            model_name="aboutus",
            name="video_poster",
            field=models.ImageField(blank=True, null=True, upload_to="about/images/"),
        ),
        migrations.AlterField(
            model_name="aboutus",
            name="image",
            field=models.ImageField(upload_to="about/images/"),
        ),
    ]
