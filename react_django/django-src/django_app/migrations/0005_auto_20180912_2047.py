# Generated by Django 2.1 on 2018-09-12 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0004_auto_20180912_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='picture',
        ),
        migrations.AddField(
            model_name='clients',
            name='portfolio_picture',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
    ]
