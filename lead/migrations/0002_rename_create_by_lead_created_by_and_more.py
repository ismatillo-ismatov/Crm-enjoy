# Generated by Django 4.2.9 on 2024-01-13 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='create_by',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='lead',
            old_name='create_date',
            new_name='created_date',
        ),
    ]
