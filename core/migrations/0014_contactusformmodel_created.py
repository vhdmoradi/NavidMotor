# Generated by Django 4.1.2 on 2022-11-05 06:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_remove_contactusformmodel_city"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactusformmodel",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]