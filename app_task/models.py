from django.db import models
from django.utils import timezone

# Create your models here.


# 应用
class App(models.Model):
    app_name = models.CharField(max_length=255, verbose_name='名称')
    app_logo = models.CharField(max_length=255, verbose_name='图标')
    app_remark = models.CharField(max_length=255, verbose_name='备注')
    db_insert_time = models.DateTimeField(verbose_name='插入时间', default=timezone.now)

    # 其他----暂时无用途
    app_hash = models.CharField(max_length=255, verbose_name='Hash')
    app_key = models.CharField(max_length=255, verbose_name='Key')

    class Meta:
        db_table = 'bot_app'  # 表名
        verbose_name = "应用"
        verbose_name_plural = "应用"
        # index_together = [["function_en",],]
        # unique_together = (("nfvo_id", "link_id"),)
    pass


# 场景 scene = robot
# 场景是介于任务对话和意图之间的层级。场景可以用来管理彼此联系的一系列“意图”。
class Robot(models.Model):
    robot_name = models.CharField(max_length=255, verbose_name='名称')
    robot_logo = models.CharField(max_length=255, verbose_name='图标')
    robot_detail = models.CharField(max_length=255, verbose_name='描述')
    robot_status = models.IntegerField(default=1, verbose_name='状态')

    robot_ttl = models.IntegerField(verbose_name='闲置等待时长')
    odst_threshold = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='智能填槽阈值')

    pos_status = models.IntegerField(default=1, verbose_name='自动添加预置回复')
    pos_num = models.IntegerField(default=3, verbose_name='推荐个数')
    pos_source = models.CharField(max_length=255, default='["popular","personal","entity"]', verbose_name='推荐源')

    goback_action = models.IntegerField(default=1, verbose_name='是否可以回退')
    exit_action = models.IntegerField(default=1, verbose_name='是否主动退出')
    exit_rsp_mode = models.IntegerField(default=1, verbose_name='退出响应模式')
    app = models.ForeignKey('App', on_delete=models.CASCADE)

    class Meta:
        db_table = 'bot_robot'  # 表名
        verbose_name = "场景"
        verbose_name_plural = "场景"
        # index_together = [["function_en",],]
        # unique_together = (("nfvo_id", "link_id"),)
    pass


#
# class RobotActionTrigger(models.Model):
#
#     trigger_action = models.IntegerField(verbose_name='trigger_action')
#     content = models.CharField(max_length=255, verbose_name='描述')
#     robot = models.ForeignKey('Robot', on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'bot_action_trigger'  # 表名
#         verbose_name = "触发器"
#         verbose_name_plural = "触发器"
#         # index_together = [["function_en",],]
#         # unique_together = (("id", "link_id"),)
#     pass
#
#
# class RobotActionResponse(models.Model):
#
#     action_type = models.IntegerField(verbose_name='action_type')
#     type_id = models.IntegerField(verbose_name='type_id')
#     response = models.CharField(max_length=255, verbose_name='描述')
#     robot = models.ForeignKey('Robot', on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'bot_action_response'  # 表名
#         verbose_name = "响应"
#         verbose_name_plural = "响应"
#         # index_together = [["function_en",],]
#         # unique_together = (("id", "link_id"),)
#     pass


class Task(models.Model):
    """
    任务 = 意图
    "max_pause_ln": 3,
    "clarify": "",
    "pause": "",
    "is_label": 0,
    """
    robot = models.ForeignKey('Robot', verbose_name='关联机器人', on_delete=models.CASCADE)
    version = models.IntegerField(default=0, verbose_name='版本')
    name = models.CharField(max_length=255, verbose_name='名称')
    task_status = models.IntegerField(default=1, verbose_name='状态')

    # ----------中断策略
    # 0开启，1关闭
    default_end_block_mult_val = models.IntegerField(default=0, verbose_name='中断保留词槽')
    # 0开启，1关闭
    trigger_faq = models.IntegerField(default=0, verbose_name='是否触发知识点')
    ttl = models.IntegerField(verbose_name='闲置等待时长')
    threshold = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='智能填槽阈值')

    class Meta:
        db_table = 'bot_task'  # 表名
        verbose_name = "意图"
        verbose_name_plural = "意图"
        # index_together = [["function_en",],]
        # unique_together = (("id", "link_id"),)
    pass


class Block(models.Model):
    bound_slot = models.ForeignKey('Slot', verbose_name='关联词槽', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='单元名称')
    task = models.ForeignKey('Task', verbose_name='关联任务（意图）', on_delete=models.CASCADE)
    type_id = models.IntegerField(verbose_name='类型')
    # 1：消息发送单元
    # 2：询问填槽单元
    # 3：静默填槽单元
    # 4：终点单元
    # 5：多槽接口单元
    # 6：单槽接口单元
    # 9：词槽运算单元
    # 11：词槽记录单元
    # 13：表格读取单元
    # 14：表格写入单元
    # 15：属性读取单元
    # 16：属性写入单元

    # 记录一些值，目前不知道干什么
    uri = models.CharField(max_length=255, verbose_name='跳转意图')

    # 对话策略
    max_interval = models.IntegerField(verbose_name='尝试询问次数')
    mult_val = models.IntegerField(verbose_name='机器人得到多个值时，向用户澄清')
    fill_any_time = models.BooleanField(verbose_name='仅在当前单元询问时填槽')
    order_id = models.IntegerField(verbose_name='未知')
    rsp_mode = models.IntegerField(verbose_name='未知')
    first_order = models.IntegerField(verbose_name='未知')
    pre_check = models.CharField(max_length=255, verbose_name='未知')
    run_once = models.BooleanField(verbose_name='运行一次')
    disable_exit = models.IntegerField(default=0, verbose_name='允许退出')
    disable_goback = models.IntegerField(default=0, verbose_name='允许后退')


    # 视图位置信息
    position_x = models.IntegerField(default=0, verbose_name='x坐标')
    position_y = models.IntegerField(default=0, verbose_name='y坐标')

    # 单元跳转关系
    block_relations = models.ManyToManyField('self', through='BlockRelation', symmetrical=False, verbose_name='单元跳转关系')

    class Meta:
        db_table = 'bot_block'  # 表名
        verbose_name = "单元"
        verbose_name_plural = "单元"
        # index_together = [["function_en",],]
        # unique_together = (("id", "link_id"),)

    pass


class Slot(models.Model):
    """
    词槽
    """
    robot = models.ForeignKey('Robot', verbose_name='关联机器人', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='名称')
    alias = models.CharField(max_length=255, verbose_name='alias')
    disposable = models.BooleanField(default=False)
    fill_slot_with_query = models.BooleanField(default=False)
    source_entities = models.ManyToManyField('Entity')

    class Meta:
        db_table = 'bot_slot'  # 表名
        verbose_name = "词槽"
        verbose_name_plural = "词槽"
        # index_together = [["function_en",],]
        # unique_together = (("nfvo_id", "link_id"),)
    pass


class Entity(models.Model):
    entity_name = models.CharField(max_length=255, verbose_name='名称')
    entity_desc = models.CharField(max_length=255, verbose_name='entity_desc')
    entity_detail = models.CharField(max_length=255, verbose_name='entity_detail')
    entity_type = models.IntegerField(verbose_name='entity_type')

    class Meta:
        db_table = 'bot_entity'  # 表名
        verbose_name = "实例"
        verbose_name_plural = "实例"
        # index_together = [["function_en",],]
        # unique_together = (("nfvo_id", "link_id"),)
    pass


class BlockResponse(models.Model):
    """
    单元响应处理
    """
    block = models.ForeignKey('Block', on_delete=models.CASCADE, verbose_name='单元')
    response = models.CharField(default='', max_length=255, verbose_name='响应规则')
    rsp_once = models.BooleanField(default=False, verbose_name='响应一次')

    class Meta:
        db_table = 'bot_block_response'  # 表名
        verbose_name = "单元响应处理"
        verbose_name_plural = "单元响应处理"
        # index_together = [["function_en",],]
        # unique_together = (("nfvo_id", "link_id"),)
    pass


class BlockRelation(models.Model):
    """
    单元跳转关系
    """
    from_block = models.ForeignKey('Block', related_name='from_block', on_delete=models.CASCADE, verbose_name='起点')
    to_block = models.ForeignKey('Block', related_name='to_block', on_delete=models.CASCADE, verbose_name='终点')
    condition = models.CharField(default='', max_length=255, verbose_name='条件')
    value = models.CharField(default='', max_length=255, verbose_name='值')

    class Meta:
        db_table = 'bot_block_relation'  # 表名
        verbose_name = "单元跳转关系"
        verbose_name_plural = "单元跳转关系"
        # index_together = [["function_en",],]
        # unique_together = (("nfvo_id", "link_id"),)
    pass


class BlockDeferred(models.Model):
    """
    延期设置
    """
    block = models.ForeignKey('Block', on_delete=models.CASCADE, verbose_name='单元')
    deferred_time = models.IntegerField(verbose_name='次数')
    response = models.CharField(default='', max_length=255, verbose_name='操作')

    class Meta:
        db_table = 'bot_block_deferred'  # 表名
        verbose_name = "延期设置"
        verbose_name_plural = "延期设置"
        # index_together = [["function_en",],]
        # unique_together = (("nfvo_id", "link_id"),)

    pass


class BlockShortcut(models.Model):
    """
    预置回复
    """
    block = models.ForeignKey('Block', on_delete=models.CASCADE, verbose_name='单元')
    shortcut_options = models.CharField(default='', max_length=255, verbose_name='操作')

    class Meta:
        db_table = 'bot_block_shortcut'  # 表名
        verbose_name = "预置回复"
        verbose_name_plural = "预置回复"
        # index_together = [["function_en",],]
        # unique_together = (("nfvo_id", "link_id"),)
    pass


class Trigger(models.Model):
    """
    触发器
    """
    task = models.ForeignKey('Task', verbose_name='关联任务（意图）', on_delete=models.CASCADE)
    next_block = models.ForeignKey('Block', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='next_block')

    # 视图位置信息
    position_x = models.IntegerField(default=0, verbose_name='x坐标')
    position_y = models.IntegerField(default=0, verbose_name='y坐标')

    class Meta:
        db_table = 'bot_trigger'  # 表名
        verbose_name = "触发器"
        verbose_name_plural = "触发器"
        # index_together = [["function_en",],]
        # unique_together = (("nfvo_id", "link_id"),)
    pass


class TriggerInfo(models.Model):
    """
    触发器信息
    """
    trigger = models.ForeignKey('Trigger', on_delete=models.CASCADE, verbose_name='归属block')

    content = models.CharField(default='', max_length=255, verbose_name='内容')
    trigger_type = models.IntegerField(default=4, verbose_name='类型')
    # 4：equal，keyword
    # 3：match，keyword
    # 2：question
    # 1：sentenceNotation

    class Meta:
        db_table = 'bot_trigger_info'  # 表名
        verbose_name = "触发器信息"
        verbose_name_plural = "触发器信息"
        # index_together = [["function_en",],]
        # unique_together = (("nfvo_id", "link_id"),)
    pass

