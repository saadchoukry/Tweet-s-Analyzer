# Generated by Django 3.0 on 2019-06-01 00:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0067_auto_20190601_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offstreamresearch',
            name='since',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 6, 1, 0, 0, 3, 252237, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='research',
            name='researchDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 0, 0, 3, 236614, tzinfo=utc)),
        ),
    ]