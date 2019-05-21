# Generated by Django 3.0 on 2019-05-14 21:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0044_auto_20190514_0146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='streamingresearch',
            options={},
        ),
        migrations.AlterField(
            model_name='offstreamresearch',
            name='endDate',
            field=models.DateField(default=datetime.datetime(2019, 5, 14, 21, 32, 11, 942517, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offstreamresearch',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2019, 5, 14, 21, 32, 11, 942517, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='research',
            name='researchDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 21, 32, 11, 938515, tzinfo=utc)),
        ),
    ]