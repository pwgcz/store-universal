# Generated by Django 3.0.8 on 2020-09-04 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_web', '0011_auto_20200904_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='discount',
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
    ]
