# Generated by Django 4.1.2 on 2022-11-02 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("salesnetwork", "0006_remove_agency_latitude_remove_agency_longitude"),
    ]

    operations = [
        migrations.AddField(
            model_name="agency",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=9, null=True
            ),
        ),
        migrations.AddField(
            model_name="agency",
            name="longitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=9, null=True
            ),
        ),
    ]
