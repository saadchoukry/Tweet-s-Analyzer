# Generated by Django 3.0 on 2019-05-29 22:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0058_auto_20190529_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offstreamresearch',
            name='since',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 5, 29, 22, 53, 35, 604345, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='research',
            name='researchDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 29, 22, 53, 35, 604345, tzinfo=utc)),
        ),
    ]
