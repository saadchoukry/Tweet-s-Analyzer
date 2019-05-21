# Generated by Django 3.0 on 2019-05-13 21:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0035_auto_20190513_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offstreamresearch',
            name='endDate',
            field=models.DateField(default=datetime.datetime(2019, 5, 13, 21, 20, 18, 497589, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offstreamresearch',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2019, 5, 13, 21, 20, 18, 497589, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='research',
            name='researchDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 13, 21, 20, 18, 497589, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='research',
            name='resultsFile',
            field=models.FileField(default='static/scripts/Twitter_stream/collected_data/default.json', max_length=500000, upload_to='static/scripts/Twitter_stream/collected_data/results_<django.db.models.fields.AutoField>.json'),
        ),
    ]