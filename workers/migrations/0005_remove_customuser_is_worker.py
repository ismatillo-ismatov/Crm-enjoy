# Generated by Django 4.2.9 on 2024-01-18 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0004_worker_is_worker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_worker',
        ),
    ]
