# Generated by Django 4.1 on 2023-03-13 07:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('topic_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]