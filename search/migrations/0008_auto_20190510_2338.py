# Generated by Django 3.0 on 2019-05-10 22:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20190510_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='limitTweetsNumber',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='offstreamresearch',
            name='endDate',
            field=models.DateField(default=datetime.datetime(2019, 5, 10, 22, 38, 39, 781119, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offstreamresearch',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2019, 5, 10, 22, 38, 39, 781119, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='research',
            name='researchDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 10, 22, 38, 39, 777121, tzinfo=utc)),
        ),
    ]
