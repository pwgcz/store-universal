# Generated by Django 3.0.8 on 2020-09-22 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0003_auto_20200901_1339"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=256, verbose_name="first_name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=256, verbose_name="last_name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True, max_length=256, null=True, verbose_name="phone"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_name",
            field=models.CharField(
                blank=True, max_length=256, verbose_name="user_name"
            ),
        ),
    ]
