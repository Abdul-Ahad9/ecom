# Generated by Django 3.1.5 on 2021-05-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='body',
        ),
        migrations.AddField(
            model_name='data',
            name='about_des',
            field=models.CharField(default='', max_length=240),
        ),
        migrations.AddField(
            model_name='data',
            name='about_ful_des',
            field=models.CharField(default='', max_length=1200),
        ),
        migrations.AddField(
            model_name='data',
            name='mission',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='data',
            name='name',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='data',
            name='subtitle',
            field=models.CharField(default='', max_length=35),
        ),
        migrations.AddField(
            model_name='data',
            name='vision',
            field=models.CharField(default='', max_length=400),
        ),
    ]
