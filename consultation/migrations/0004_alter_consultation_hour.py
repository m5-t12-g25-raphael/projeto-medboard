# Generated by Django 4.1.5 on 2023-01-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("consultation", "0003_alter_consultation_patient"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consultation",
            name="hour",
            field=models.TimeField(),
        ),
    ]
