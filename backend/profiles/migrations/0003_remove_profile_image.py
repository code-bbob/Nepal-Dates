# Generated by Django 5.0.1 on 2024-02-15 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profileimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
