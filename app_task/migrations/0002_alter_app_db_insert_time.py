# Generated by Django 3.2.9 on 2021-11-24 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='db_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 17, 38, 58, 742959), verbose_name='插入时间'),
        ),
    ]