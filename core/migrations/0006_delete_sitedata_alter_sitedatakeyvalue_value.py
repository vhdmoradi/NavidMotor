# Generated by Django 4.1.2 on 2022-10-20 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_sitedatakeyvalue"),
    ]

    operations = [
        migrations.DeleteModel(
            name="SiteData",
        ),
        migrations.AlterField(
            model_name="sitedatakeyvalue",
            name="value",
            field=models.TextField(verbose_name="متن"),
        ),
    ]
