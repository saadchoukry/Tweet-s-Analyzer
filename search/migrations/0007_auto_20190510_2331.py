# Generated by Django 3.0 on 2019-05-10 22:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20190510_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offstreamresearch',
            name='endDate',
            field=models.DateField(default=datetime.datetime(2019, 5, 10, 22, 31, 55, 370804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offstreamresearch',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2019, 5, 10, 22, 31, 55, 370804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='research',
            name='researchDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 10, 22, 31, 55, 370804, tzinfo=utc)),
        ),
    ]