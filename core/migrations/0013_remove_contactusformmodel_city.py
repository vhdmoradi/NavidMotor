# Generated by Django 4.1.2 on 2022-10-30 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_rename_contactusform_contactusformmodel"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contactusformmodel",
            name="city",
        ),
    ]
