# Generated by Django 5.1.1 on 2024-09-11 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_created_accounts_and_transactions"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="address",
        ),
        migrations.RemoveField(
            model_name="user",
            name="date_of_birth",
        ),
        migrations.RemoveField(
            model_name="user",
            name="gender",
        ),
        migrations.RemoveField(
            model_name="user",
            name="phone_number",
        ),
    ]
