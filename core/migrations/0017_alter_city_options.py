# Generated by Django 4.1.7 on 2023-03-06 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_alter_contactusformmodel_created"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="city",
            options={"verbose_name_plural": "cities"},
        ),
    ]
