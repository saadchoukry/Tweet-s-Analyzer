# Generated by Django 3.0 on 2019-05-25 00:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0056_auto_20190523_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offstreamresearch',
            name='since',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 5, 25, 0, 3, 51, 307618, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='research',
            name='researchDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 25, 0, 3, 51, 306621, tzinfo=utc)),
        ),
    ]