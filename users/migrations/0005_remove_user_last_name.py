# Generated by Django 4.2.7 on 2023-11-22 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
