# Generated by Django 5.1.3 on 2024-12-20 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="product",
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
                ("name", models.CharField(max_length=100)),
                ("price", models.IntegerField()),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="product/images")),
            ],
        ),
        migrations.CreateModel(
            name="student",
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
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("roll", models.IntegerField()),
                ("city", models.CharField(max_length=100)),
                ("marks", models.IntegerField()),
                ("pass_date", models.DateField()),
            ],
        ),
    ]