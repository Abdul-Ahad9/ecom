# Generated by Django 3.1.5 on 2021-05-14 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videosite', '0002_auto_20210511_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='video',
            field=models.FileField(default='', upload_to='media/videosite'),
        ),
    ]
