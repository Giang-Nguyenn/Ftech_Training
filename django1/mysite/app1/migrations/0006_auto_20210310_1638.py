# Generated by Django 3.1.6 on 2021-03-10 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20210310_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='post',
            name='postCreate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 3, 10, 16, 38, 43, 76571)),
        ),
    ]
