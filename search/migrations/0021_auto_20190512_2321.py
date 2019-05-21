# Generated by Django 3.0 on 2019-05-12 22:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0020_auto_20190512_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offstreamresearch',
            name='endDate',
            field=models.DateField(default=datetime.datetime(2019, 5, 12, 22, 21, 18, 44683, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offstreamresearch',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2019, 5, 12, 22, 21, 18, 44683, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='research',
            name='researchDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 12, 22, 21, 18, 44683, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Contains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='search.Hashtag')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='search.Tweet')),
            ],
        ),
    ]
