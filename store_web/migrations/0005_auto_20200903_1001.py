# Generated by Django 3.0.8 on 2020-09-03 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store_web", "0004_auto_20200902_1235"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="product",
        ),
        migrations.AddField(
            model_name="cartitem",
            name="product",
            field=models.ManyToManyField(to="store_web.Product"),
        ),
    ]
