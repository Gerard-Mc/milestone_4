# Generated by Django 3.1.7 on 2021-07-11 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_auto_20210711_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.DecimalField(choices=[(1, 'Logo'), (2, 'Poster'), (3, 'Icon'), (4, 'Banner')], decimal_places=0, max_digits=1),
        ),
    ]
