# Generated by Django 3.2.9 on 2021-11-29 01:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=255, verbose_name='名称')),
                ('app_logo', models.CharField(max_length=255, verbose_name='图标')),
                ('app_remark', models.CharField(max_length=255, verbose_name='备注')),
                ('db_insert_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='插入时间')),
                ('app_hash', models.CharField(max_length=255, verbose_name='Hash')),
                ('app_key', models.CharField(max_length=255, verbose_name='Key')),
            ],
            options={
                'verbose_name': '应用',
                'verbose_name_plural': '应用',
                'db_table': 'bot_app',
            },
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='单元名称')),
                ('type_id', models.IntegerField(verbose_name='类型')),
                ('uri', models.CharField(max_length=255, verbose_name='跳转意图')),
                ('max_interval', models.IntegerField(verbose_name='尝试询问次数')),
                ('mult_val', models.IntegerField(verbose_name='机器人得到多个值时，向用户澄清')),
                ('fill_any_time', models.BooleanField(verbose_name='仅在当前单元询问时填槽')),
                ('order_id', models.IntegerField(verbose_name='未知')),
                ('rsp_mode', models.IntegerField(verbose_name='未知')),
                ('first_order', models.IntegerField(verbose_name='未知')),
                ('pre_check', models.CharField(max_length=255, verbose_name='未知')),
                ('run_once', models.BooleanField(verbose_name='运行一次')),
                ('disable_exit', models.IntegerField(default=0, verbose_name='允许退出')),
                ('disable_goback', models.IntegerField(default=0, verbose_name='允许后退')),
                ('position_x', models.IntegerField(default=0, verbose_name='x坐标')),
                ('position_y', models.IntegerField(default=0, verbose_name='y坐标')),
            ],
            options={
                'verbose_name': '单元',
                'verbose_name_plural': '单元',
                'db_table': 'bot_block',
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_name', models.CharField(max_length=255, verbose_name='名称')),
                ('entity_desc', models.CharField(max_length=255, verbose_name='entity_desc')),
                ('entity_detail', models.CharField(max_length=255, verbose_name='entity_detail')),
                ('entity_type', models.IntegerField(verbose_name='entity_type')),
            ],
            options={
                'verbose_name': '实例',
                'verbose_name_plural': '实例',
                'db_table': 'bot_entity',
            },
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('robot_name', models.CharField(max_length=255, verbose_name='名称')),
                ('robot_logo', models.CharField(max_length=255, verbose_name='图标')),
                ('robot_detail', models.CharField(max_length=255, verbose_name='描述')),
                ('robot_status', models.IntegerField(default=1, verbose_name='状态')),
                ('robot_ttl', models.IntegerField(verbose_name='闲置等待时长')),
                ('odst_threshold', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='智能填槽阈值')),
                ('pos_status', models.IntegerField(default=1, verbose_name='自动添加预置回复')),
                ('pos_num', models.IntegerField(default=3, verbose_name='推荐个数')),
                ('pos_source', models.CharField(default='["popular","personal","entity"]', max_length=255, verbose_name='推荐源')),
                ('goback_action', models.IntegerField(default=1, verbose_name='是否可以回退')),
                ('exit_action', models.IntegerField(default=1, verbose_name='是否主动退出')),
                ('exit_rsp_mode', models.IntegerField(default=1, verbose_name='退出响应模式')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_task.app')),
            ],
            options={
                'verbose_name': '场景',
                'verbose_name_plural': '场景',
                'db_table': 'bot_robot',
            },
        ),
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
            options={
                'verbose_name': '意图',
                'verbose_name_plural': '意图',
                'db_table': 'bot_task',
            },
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_x', models.IntegerField(default=0, verbose_name='x坐标')),
                ('position_y', models.IntegerField(default=0, verbose_name='y坐标')),
                ('next_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_task.block', verbose_name='next_block')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_task.task', verbose_name='关联任务（意图）')),
            ],
            options={
                'verbose_name': '触发器',
                'verbose_name_plural': '触发器',
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
                'verbose_name': '触发器信息',
                'verbose_name_plural': '触发器信息',
                'db_table': 'bot_trigger_info',
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('alias', models.CharField(max_length=255, verbose_name='alias')),
                ('disposable', models.BooleanField(default=False)),
                ('fill_slot_with_query', models.BooleanField(default=False)),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_task.robot', verbose_name='关联机器人')),
                ('source_entities', models.ManyToManyField(to='app_task.Entity')),
            ],
            options={
                'verbose_name': '词槽',
                'verbose_name_plural': '词槽',
                'db_table': 'bot_slot',
            },
        ),
        migrations.CreateModel(
            name='BlockShortcut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortcut_options', models.CharField(default='', max_length=255, verbose_name='操作')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_task.block', verbose_name='单元')),
            ],
            options={
                'verbose_name': '预置回复',
                'verbose_name_plural': '预置回复',
                'db_table': 'bot_block_shortcut',
            },
        ),
        migrations.CreateModel(
            name='BlockResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(default='', max_length=255, verbose_name='响应规则')),
                ('rsp_once', models.BooleanField(default=False, verbose_name='响应一次')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_task.block', verbose_name='单元')),
            ],
            options={
                'verbose_name': '单元响应处理',
                'verbose_name_plural': '单元响应处理',
                'db_table': 'bot_block_response',
            },
        ),
        migrations.CreateModel(
            name='BlockRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(default='', max_length=255, verbose_name='条件')),
                ('value', models.CharField(default='', max_length=255, verbose_name='值')),
                ('from_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_block', to='app_task.block', verbose_name='起点')),
                ('to_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_block', to='app_task.block', verbose_name='终点')),
            ],
            options={
                'verbose_name': '单元跳转关系',
                'verbose_name_plural': '单元跳转关系',
                'db_table': 'bot_block_relation',
            },
        ),
        migrations.CreateModel(
            name='BlockDeferred',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deferred_time', models.IntegerField(verbose_name='次数')),
                ('response', models.CharField(default='', max_length=255, verbose_name='操作')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_task.block', verbose_name='单元')),
            ],
            options={
                'verbose_name': '延期设置',
                'verbose_name_plural': '延期设置',
                'db_table': 'bot_block_deferred',
            },
        ),
        migrations.AddField(
            model_name='block',
            name='block_relations',
            field=models.ManyToManyField(through='app_task.BlockRelation', to='app_task.Block', verbose_name='单元跳转关系'),
        ),
        migrations.AddField(
            model_name='block',
            name='bound_slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_task.slot', verbose_name='关联词槽'),
        ),
        migrations.AddField(
            model_name='block',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_task.task', verbose_name='关联任务（意图）'),
        ),
    ]
