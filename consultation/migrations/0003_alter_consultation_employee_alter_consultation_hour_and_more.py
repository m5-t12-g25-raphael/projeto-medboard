# Generated by Django 4.1.5 on 2023-01-12 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("consultation", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consultation",
            name="employee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="consults",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="consultation",
            name="hour",
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name="consultation",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="consultation",
                to="patient.patient",
            ),
        ),
    ]