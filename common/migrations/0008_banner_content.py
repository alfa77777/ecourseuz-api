# Generated by Django 4.2.4 on 2023-08-09 13:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0007_remove_contactus_location_contactus_lat_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="banner",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
