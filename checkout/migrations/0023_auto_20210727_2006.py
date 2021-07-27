# Generated by Django 3.1.13 on 2021-07-27 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0022_order_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, default='default', max_length=254),
        ),
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address1',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.category'),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='friendly_name',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='name',
            field=models.CharField(default='', max_length=254),
        ),
    ]
