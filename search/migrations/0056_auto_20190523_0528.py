# Generated by Django 3.0 on 2019-05-23 04:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0055_auto_20190523_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offstreamresearch',
            name='since',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 5, 23, 4, 28, 24, 315623, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='research',
            name='researchDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 23, 4, 28, 24, 315623, tzinfo=utc)),
        ),
    ]