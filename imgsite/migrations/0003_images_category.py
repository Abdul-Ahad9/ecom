# Generated by Django 3.1.5 on 2021-05-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgsite', '0002_auto_20210519_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
    ]
