# Generated by Django 5.1.4 on 2025-01-18 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Demoapp', '0002_login_phone_alter_login_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='phone',
        ),
    ]
