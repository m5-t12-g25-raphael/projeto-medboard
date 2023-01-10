
# Generated by Django 4.1.5 on 2023-01-09 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("birth_date", models.DateField()),
                ("patient_code", models.CharField(max_length=10)),
                ("password", models.CharField(max_length=10)),
            ],
        ),
    ]