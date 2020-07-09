# Generated by Django 2.2.13 on 2020-07-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='course_title',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='education',
            name='end_year',
            field=models.IntegerField(default=9999),
        ),
        migrations.AddField(
            model_name='education',
            name='institution',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='education',
            name='start_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='education',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
