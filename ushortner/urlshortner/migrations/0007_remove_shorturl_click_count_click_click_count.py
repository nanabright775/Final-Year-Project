# Generated by Django 5.0.4 on 2024-05-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0006_remove_shorturl_browser_remove_shorturl_device_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturl',
            name='click_count',
        ),
        migrations.AddField(
            model_name='click',
            name='click_count',
            field=models.IntegerField(default=0),
        ),
    ]