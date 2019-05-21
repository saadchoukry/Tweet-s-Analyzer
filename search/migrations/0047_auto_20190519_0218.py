# Generated by Django 3.0 on 2019-05-19 01:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0046_auto_20190519_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='byscreenname',
            name='screenName',
        ),
        migrations.AddField(
            model_name='byscreenname',
            name='screen',
            field=models.TextField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='offstreamresearch',
            name='since',
            field=models.DateField(default=datetime.datetime(2019, 5, 19, 1, 18, 26, 695043, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='research',
            name='researchDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 19, 1, 18, 26, 695043, tzinfo=utc)),
        ),
    ]
