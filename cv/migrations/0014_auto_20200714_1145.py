# Generated by Django 2.2.13 on 2020-07-14 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0013_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='reference',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='reference',
            name='phone',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='reference',
            name='relevance',
            field=models.CharField(default='', max_length=100),
        ),
    ]