# Generated by Django 3.1.13 on 2021-07-15 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20210714_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='friendly_name',
        ),
    ]