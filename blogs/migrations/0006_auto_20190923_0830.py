# Generated by Django 2.2.4 on 2019-09-22 23:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20190920_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_date',
            field=models.DateField(default=datetime.date(2019, 9, 23)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateField(default=datetime.date(2019, 9, 23)),
        ),
    ]
