# Generated by Django 4.2.7 on 2023-11-22 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userType',
            field=models.CharField(choices=[('seeker', 'Seeker'), ('listener', 'Listener')], default='seeker', max_length=10),
        ),
    ]
