# Generated by Django 4.1 on 2023-03-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic_manager', '0002_reply_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
