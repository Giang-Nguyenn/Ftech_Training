# Generated by Django 3.1.6 on 2021-03-08 07:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='create',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2021, 3, 8, 14, 48, 30, 313143)),
        ),
    ]