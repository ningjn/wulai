from django.db import models

# Create your models here.


# 场景 scene = robot
# 场景是介于任务对话和意图之间的层级。场景可以用来管理彼此联系的一系列“意图”。
class Robot(models.Model):
    """
    "robot_id": 36603,
    "robot_name": "报名活动",
    "robot_logo": "1",
    "robot_detail": "报名活动场景",
    "robot_status": 1,
    "pos_status": 1,
    "pos_num": 3,
    "pos_source": "[\"popular\",\"personal\",\"entity\"]",
    "v2_robot_id": 36603,
    "odst_threshold": 0.7,
    "robot_ttl": 600,
    "goback_action": 1,
    "exit_action": 1,
    "exit_rsp_mode": 1,
    "actionTrigger": [
      {
        "tid": 106384,
        "trigger_action": 1,
        "content": "上一步",
        "__typename": "robotActionTrigger"
      },
      {
        "tid": 106385,
        "trigger_action": 2,
        "content": "退出",
        "__typename": "robotActionTrigger"
      }
    ],
    "actionResponse": [
      {
        "resp_id": 106126,
        "action_type": 1,
        "response": "{\"Content\":\"不能再往回了\"}",
        "type_id": 0,
        "__typename": "robotActionResponse"
      },
      {
        "resp_id": 106127,
        "action_type": 2,
        "response": "{\"Content\":\"已退出\"}",
        "type_id": 0,
        "__typename": "robotActionResponse"
      }
    ],
    "__typename": "TaskRobotOut"
    """
    robot_name = models.CharField(max_length=255, verbose_name='名称')
    robot_logo = models.CharField(max_length=255, verbose_name='图标')
    robot_detail = models.CharField(max_length=255, verbose_name='描述')
    robot_status = models.IntegerField(default=1, verbose_name='状态')

    robot_ttl = models.IntegerField(verbose_name='闲置等待时长')
    odst_threshold = models.DecimalField(verbose_name='智能填槽阈值')

    pos_status = models.IntegerField(default=1, verbose_name='自动添加预置回复')
    pos_num = models.IntegerField(default=3, verbose_name='推荐个数')
    pos_source = models.CharField(max_length=255, default='["popular","personal","entity"]', verbose_name='推荐源')

    goback_action = models.IntegerField(default=1, verbose_name='是否可以回退')
    exit_action = models.IntegerField(default=1, verbose_name='是否主动退出')
    exit_rsp_mode = models.IntegerField(default=1, verbose_name='退出响应模式')

    class Meta:
        db_table = 'robot'  # 表名
        verbose_name = "场景"
        verbose_name_plural = "场景"
        # index_together = [["function_en",],]
        # unique_together = (("nfvo_id", "link_id"),)
    pass


class RobotActionTrigger(models.Model):

    trigger_action = models.IntegerField(verbose_name='trigger_action')
    content = models.CharField(max_length=255, verbose_name='描述')
    robot = models.ForeignKey('Robot', on_delete=models.CASCADE)

    class Meta:
        db_table = 'action_trigger'  # 表名
        verbose_name = "触发器"
        verbose_name_plural = "触发器"
        # index_together = [["function_en",],]
        # unique_together = (("nfvo_id", "link_id"),)
    pass


class RobotActionResponse(models.Model):

    action_type = models.IntegerField(verbose_name='action_type')
    type_id = models.IntegerField(verbose_name='type_id')
    response = models.CharField(max_length=255, verbose_name='描述')
    robot = models.ForeignKey('Robot', on_delete=models.CASCADE)

    class Meta:
        db_table = 'action_response'  # 表名
        verbose_name = "响应"
        verbose_name_plural = "响应"
        # index_together = [["function_en",],]
        # unique_together = (("nfvo_id", "link_id"),)
    pass
