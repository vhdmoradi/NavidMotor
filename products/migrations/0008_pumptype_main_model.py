# Generated by Django 4.1.2 on 2022-12-05 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_alter_mainmodel_model_image_alter_usage_usage_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="pumptype",
            name="main_model",
            field=models.ForeignKey(
                default="3f5b4e9a-9f32-41d4-896d-e3af08c6ab49",
                on_delete=django.db.models.deletion.CASCADE,
                to="products.mainmodel",
            ),
        ),
    ]