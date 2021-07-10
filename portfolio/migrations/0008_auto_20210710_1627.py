# Generated by Django 3.1.7 on 2021-07-10 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20210707_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='friendly_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fast_delivery',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='modified_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='testimonial',
        ),
        migrations.RemoveField(
            model_name='product',
            name='user_description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='user_name',
        ),
        migrations.AddField(
            model_name='category',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='product',
            name='complexity',
            field=models.DecimalField(choices=[(1, 'Normal'), (1.5, 'Advanced'), (2, 'Complex')], decimal_places=1, default=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('logo', 'Logo'), ('poster', 'Poster'), ('icon', 'Icon'), ('banner', 'Banner')], max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.category'),
        ),
    ]