# Generated by Django 4.2.4 on 2023-09-04 11:20

import course.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0017_alter_courseapply_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="coursecontent",
            name="time",
            field=models.PositiveIntegerField(default=0),
        ),
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
            name="video",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="course_content/",
                validators=[course.utils.validate_video],
            ),
        ),
        migrations.CreateModel(
            name="CourseSection",
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
                ("title", models.CharField(max_length=126)),
                ("position", models.PositiveIntegerField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sections",
                        to="course.course",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="coursecontent",
            name="section",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contents",
                to="course.coursesection",
            ),
        ),
    ]
