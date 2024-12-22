# Generated by Django 5.1.3 on 2024-12-20 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_remove_student_pass_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="car",
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
                ("car_name", models.CharField(max_length=100)),
                ("car_speed", models.IntegerField(default=50)),
            ],
        ),
    ]
