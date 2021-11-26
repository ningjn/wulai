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


# class BlockResponse(models.Model):
#     """
#     响应
#     """
#     pass
#
#
# class BlockRelation(models.Model):
#     """
#     单元跳转关系
#     """
#     pass
#
#
# class BlockDeferred(models.Model):
#     """
#     延期设置
#     """
#     pass
#
#
# class BlockShortcut(models.Model):
#     """
#     预置回复
#     """
#     pass
#
#
# class Position(models.Model):
#     """
#     位置信息
#     """
#     x = models.IntegerField(verbose_name='x坐标')
#     y = models.IntegerField(verbose_name='y坐标')
#     pass
#
#
# class ViewSize(models.Model):
#     """
#     视图设置
#     """
#     width = models.IntegerField(verbose_name='宽度')
#     height = models.IntegerField(verbose_name='高度')
#     pass
#
#
# class Trigger(models.Model):
#     next_block = models.ForeignKey('Block')
#     pass
