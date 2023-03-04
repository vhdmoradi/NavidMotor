# Generated by Django 4.1.2 on 2022-10-24 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_sitedatakeyvalue_key"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactUsForm",
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
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=250)),
                ("message_body", models.TextField()),
            ],
        ),
    ]
