# Generated by Django 2.2.13 on 2020-07-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0015_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
