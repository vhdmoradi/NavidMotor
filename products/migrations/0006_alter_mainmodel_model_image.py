# Generated by Django 4.1.2 on 2022-12-03 12:37

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_mainmodel_model_image_usage_usage_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mainmodel",
            name="model_image",
            field=models.ImageField(
                default="images/etabloc3.png",
                help_text="تصویر مدل الکتروپمپ",
                upload_to=products.models.path_and_rename_image,
                verbose_name="تصویر مدل الکتروپمپ",
            ),
        ),
    ]
