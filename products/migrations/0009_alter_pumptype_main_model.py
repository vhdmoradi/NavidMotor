# Generated by Django 4.1.2 on 2022-12-05 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0008_pumptype_main_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pumptype",
            name="main_model",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="products.mainmodel"
            ),
        ),
    ]
