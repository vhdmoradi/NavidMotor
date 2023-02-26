# Generated by Django 4.1.2 on 2022-12-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0015_remove_headflowdataset_created_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="usage",
        ),
        migrations.AddField(
            model_name="product",
            name="usage",
            field=models.ManyToManyField(to="products.usage"),
        ),
    ]
