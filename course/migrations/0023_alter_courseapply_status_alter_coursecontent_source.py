# Generated by Django 4.2.4 on 2023-09-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0022_alter_courseapply_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courseapply",
            name="status",
            field=models.CharField(
                choices=[("Unpaid", "Unpaid"), ("Paid", "Paid")],
                default="Unpaid",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="coursecontent",
            name="source",
            field=models.URLField(blank=True, null=True),
        ),
    ]
