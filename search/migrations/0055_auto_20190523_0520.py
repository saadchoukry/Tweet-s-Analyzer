# Generated by Django 3.0 on 2019-05-23 04:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0054_auto_20190523_0324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bykeywords',
            old_name='keywords',
            new_name='keywords1',
        ),
        migrations.AlterField(
            model_name='offstreamresearch',
            name='since',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 5, 23, 4, 20, 34, 521152, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='research',
            name='researchDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 23, 4, 20, 34, 521152, tzinfo=utc)),
        ),
    ]
