# Generated by Django 5.0.6 on 2024-06-19 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='date_created',
        ),
        migrations.AlterField(
            model_name='password',
            name='encrypted_password',
            field=models.CharField(max_length=200),
        ),
    ]
