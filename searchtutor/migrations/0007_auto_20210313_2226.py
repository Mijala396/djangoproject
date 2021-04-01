# Generated by Django 3.1.7 on 2021-03-13 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchtutor', '0006_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessions',
            name='session_date',
            field=models.DateField(default=datetime.date(2021, 3, 13)),
        ),
        migrations.AlterField(
            model_name='sessions',
            name='session_duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sessions',
            name='session_time',
            field=models.TimeField(default=datetime.time(16, 41, 47, 151803)),
        ),
    ]
