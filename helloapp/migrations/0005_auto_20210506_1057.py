# Generated by Django 3.1.5 on 2021-05-06 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloapp', '0004_auto_20210506_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='image2',
            field=models.ImageField(default='', upload_to='helloapp/images'),
        ),
        migrations.AddField(
            model_name='data',
            name='image3',
            field=models.ImageField(default='', upload_to='helloapp/images'),
        ),
    ]