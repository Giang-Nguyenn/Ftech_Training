# Generated by Django 3.1.6 on 2021-03-10 06:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210308_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='create',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2021, 3, 10, 13, 31, 22, 636579)),
        ),
    ]
