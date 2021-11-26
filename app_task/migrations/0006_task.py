# Generated by Django 3.2.9 on 2021-11-26 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_task', '0005_robot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(default=0, verbose_name='版本')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('task_status', models.IntegerField(default=1, verbose_name='状态')),
                ('default_end_block_mult_val', models.IntegerField(default=0, verbose_name='中断保留词槽')),
                ('trigger_faq', models.IntegerField(default=0, verbose_name='是否触发知识点')),
                ('ttl', models.IntegerField(verbose_name='闲置等待时长')),
                ('threshold', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='智能填槽阈值')),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_task.robot', verbose_name='关联机器人')),
            ],
        ),
    ]
