# Generated by Django 4.1.2 on 2022-10-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("salesnetwork", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cities",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="provinces",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]