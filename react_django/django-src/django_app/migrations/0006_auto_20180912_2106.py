# Generated by Django 2.1 on 2018-09-12 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0005_auto_20180912_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='portfolio_picture',
        ),
        migrations.AddField(
            model_name='users',
            name='picture',
            field=models.ImageField(blank=True, default='images/d-user.png', upload_to='images/'),
        ),
    ]
