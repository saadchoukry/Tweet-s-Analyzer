# Generated by Django 3.0 on 2019-05-13 23:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0041_auto_20190514_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offstreamresearch',
            name='endDate',
            field=models.DateField(default=datetime.datetime(2019, 5, 13, 23, 7, 44, 649910, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offstreamresearch',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2019, 5, 13, 23, 7, 44, 649910, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='research',
            name='researchDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 13, 23, 7, 44, 648913, tzinfo=utc)),
        ),
    ]
