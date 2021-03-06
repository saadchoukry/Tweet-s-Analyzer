# Generated by Django 3.0 on 2019-05-19 22:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0049_auto_20190519_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='numberOfNodes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='offstreamresearch',
            name='since',
            field=models.DateField(default=datetime.datetime(2019, 5, 19, 22, 11, 32, 561647, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='research',
            name='researchDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 19, 22, 11, 32, 560651, tzinfo=utc)),
        ),
    ]
