# Generated by Django 4.2.4 on 2023-08-11 12:10

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0009_alter_blog_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="description",
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
