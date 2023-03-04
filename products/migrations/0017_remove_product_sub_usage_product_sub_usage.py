# Generated by Django 4.1.2 on 2022-12-17 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0016_remove_product_usage_product_usage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="sub_usage",
        ),
        migrations.AddField(
            model_name="product",
            name="sub_usage",
            field=models.ManyToManyField(to="products.subusage"),
        ),
    ]
