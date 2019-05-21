# Generated by Django 3.0 on 2019-05-13 00:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0031_auto_20190513_0018'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='posts',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='posts',
            name='tweet',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='location',
        ),
        migrations.AlterField(
            model_name='offstreamresearch',
            name='endDate',
            field=models.DateField(default=datetime.datetime(2019, 5, 13, 0, 7, 42, 641148, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offstreamresearch',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2019, 5, 13, 0, 7, 42, 641148, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='research',
            name='researchDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 13, 0, 7, 42, 640152, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='researchtype',
            name='type',
            field=models.CharField(choices=[('Stream', 'Stream'), ('OffStream', 'OffStream')], default='Stream', max_length=10),
        ),
        migrations.DeleteModel(
            name='Contains',
        ),
        migrations.DeleteModel(
            name='Hashtag',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
        migrations.DeleteModel(
            name='Tweet',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
