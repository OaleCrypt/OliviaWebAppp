# Generated by Django 5.0.6 on 2024-06-19 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soc', '0002_remove_alert_timestamp_alter_alert_destination_ip_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='comments',
            new_name='details',
        ),
        migrations.RenameField(
            model_name='incident',
            old_name='status',
            new_name='severity',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='destination_ip',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='source_ip',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='alert',
        ),
        migrations.AddField(
            model_name='alert',
            name='name',
            field=models.CharField(default='Unnamed Alert', max_length=255),
        ),
        migrations.AddField(
            model_name='alert',
            name='severity',
            field=models.CharField(default='low', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alert',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 6, 19, 21, 12, 51, 285894, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='name',
            field=models.CharField(default='Unnamed Incident', max_length=255),
        ),
        migrations.AddField(
            model_name='incident',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 6, 19, 21, 14, 28, 100465, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
