# Generated by Django 5.0.4 on 2024-05-15 12:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0005_remove_click_browser_remove_click_device_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturl',
            name='browser',
        ),
        migrations.RemoveField(
            model_name='shorturl',
            name='device',
        ),
        migrations.RemoveField(
            model_name='shorturl',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='shorturl',
            name='referer',
        ),
        migrations.RemoveField(
            model_name='shorturl',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='click',
            name='browser',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='click',
            name='device',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='click',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='click',
            name='referer',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='click',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
