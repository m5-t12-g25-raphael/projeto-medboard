# Generated by Django 4.1.5 on 2023-01-11 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("roles", "0001_initial"),
        ("contact", "0003_remove_contact_employee_remove_contact_hospital_and_more"),
        ("employee", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="contact",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employees",
                to="contact.contact",
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employees",
                to="roles.role",
            ),
        ),
    ]
