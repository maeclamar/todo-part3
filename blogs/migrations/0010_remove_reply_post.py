# Generated by Django 2.2.4 on 2020-03-04 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_reply_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='post',
        ),
    ]