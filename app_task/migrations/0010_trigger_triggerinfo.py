# Generated by Django 3.2.9 on 2021-11-27 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_task', '0009_auto_20211127_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_task.block', verbose_name='next_block')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_task.task', verbose_name='关联任务（意图）')),
            ],
            options={
                'verbose_name': '预置回复',
                'verbose_name_plural': '预置回复',
                'db_table': 'bot_trigger',
            },
        ),
        migrations.CreateModel(
            name='TriggerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=255, verbose_name='内容')),
                ('trigger_type', models.IntegerField(default=4, verbose_name='类型')),
                ('trigger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_task.trigger', verbose_name='归属block')),
            ],
            options={
                'verbose_name': '预置回复',
                'verbose_name_plural': '预置回复',
                'db_table': 'bot_trigger_info',
            },
        ),
    ]