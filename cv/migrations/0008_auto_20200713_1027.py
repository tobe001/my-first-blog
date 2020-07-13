# Generated by Django 2.2.13 on 2020-07-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0007_volunteering'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteering',
            name='company',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='volunteering',
            name='end_year',
            field=models.IntegerField(default=9999),
        ),
        migrations.AddField(
            model_name='volunteering',
            name='role',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='volunteering',
            name='start_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='volunteering',
            name='text',
            field=models.TextField(default=''),
        ),
    ]