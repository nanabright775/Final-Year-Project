# Generated by Django 5.0.6 on 2024-06-25 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing_pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landingpage',
            name='name',
        ),
    ]
