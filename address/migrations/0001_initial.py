# Generated by Django 4.1.5 on 2023-01-09 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("hospital", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Addres",
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
                ("street", models.CharField(max_length=100)),
                ("number", models.IntegerField(unique=True)),
                ("district", models.CharField(max_length=50)),
                ("cep", models.IntegerField()),
                (
                    "hospital",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="address",
                        to="hospital.hospital",
                    ),
                ),
            ],
        ),
    ]
