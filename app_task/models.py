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
        # unique_together = (("id", "link_id"),)
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
        # unique_together = (("id", "link_id"),)
    pass


class Task(models.Model):
    """
    任务 = 意图
    """

    pass


class Block(models.Model):
    """
    单元
    "block_id": 881524,
    "bound_slot_id": 267725,
    "fillanytime": false,
    "max_interval": 3,
    "mult_val": 0,
    "name": "申请人信息111",
    "order_id": 10,
    "first_order": 0,
    "position": {
    "x": 390,
    "y": 12,
    "__typename": "dm_block_position_out"
    },
    "precheck": "",
    "rsp_mode": 1,
    "run_once": true,
    "task_id": 201122,
    "type_id": 2,
    "uri": "{\"mock\":\"off\"}",
    "bound_slot": {
    "slot_id": 267725,
    "robot_id": 36615,
    "name": "是否确认",
    "alias": "FHZsjjnL1It68F36ZrUIRHTEKoVcImCx",
    "def_value": "",
    "disposable": true,
    "fill_slot_with_query": false,
    "source_entities": [
      {
        "entity_id": 112719,
        "entity_type": 1,
        "entity_name": "udefine.BDtMoPtC.kyF420ek",
        "entity_desc": "确认试用",
        "entity_detail": "确认是否试用",
        "__typename": "task_entity"
      },
      {
        "entity_id": 112721,
        "entity_type": 1,
        "entity_name": "udefine.BDtMoPtC.M0frpIh8",
        "entity_desc": "申请信息",
        "entity_detail": "",
        "__typename": "task_entity"
      }
    ],
    "bound_blocks": [
      {
        "block_id": 881524,
        "name": "申请人信息",
        "__typename": "dm_block"
      }
    ],
    "__typename": "dm_slot"
    },
    "block_relations": [
    {
      "rlat_id": 1157814,
      "task_id": 201122,
      "rlat_order": 0,
      "task": {
        "task_id": 201122,
        "name": "吾来线索收集",
        "__typename": "dm_task"
      },
      "from_block_id": 881524,
      "from_block": {
        "block_id": 881524,
        "task_id": 201122,
        "name": "申请人信息",
        "__typename": "dm_block"
      },
      "to_block_id": 0,
      "to_block": null,
      "value": "*",
      "app_id": "54086",
      "condition": "{\"operator\":\"*\",\"value\":\"\"}",
      "entity": null,
      "__typename": "dm_block_relation"
    },
    {
      "rlat_id": 1157815,
      "task_id": 201122,
      "rlat_order": 0,
      "task": {
        "task_id": 201122,
        "name": "吾来线索收集",
        "__typename": "dm_task"
      },
      "from_block_id": 881524,
      "from_block": {
        "block_id": 881524,
        "task_id": 201122,
        "name": "申请人信息",
        "__typename": "dm_block"
      },
      "to_block_id": 881523,
      "to_block": {
        "block_id": 881523,
        "task_id": 201122,
        "name": "欢迎再次申请",
        "__typename": "dm_block"
      },
      "value": "否",
      "app_id": "54086",
      "condition": "{\"operator\":\"N\",\"value\":\"否\"}",
      "entity": null,
      "__typename": "dm_block_relation"
    },
    {
      "rlat_id": 1157816,
      "task_id": 201122,
      "rlat_order": 0,
      "task": {
        "task_id": 201122,
        "name": "吾来线索收集",
        "__typename": "dm_task"
      },
      "from_block_id": 881524,
      "from_block": {
        "block_id": 881524,
        "task_id": 201122,
        "name": "申请人信息",
        "__typename": "dm_block"
      },
      "to_block_id": 881522,
      "to_block": {
        "block_id": 881522,
        "task_id": 201122,
        "name": "申请人姓名",
        "__typename": "dm_block"
      },
      "value": "是",
      "app_id": "54086",
      "condition": "{\"operator\":\"N\",\"value\":\"是\"}",
      "entity": null,
      "__typename": "dm_block_relation"
    }
    ],
    "block_responses": [
        {
          "resp_id": 489621,
          "block_id": 881524,
          "status_id": 2,
          "response": "{\"Content\":\"嗨，你是想申请试用账号吗?\"}",
          "type_id": 0,
          "rsp_once": false,
          "__typename": "dm_response"
        }
    ],
    "block_deferred": {
        "drsp_id": 710473,
        "block_id": 881524,
        "deferred_time": 0,
        "response": "{\"Content\":\"\"}",
        "__typename": "dm_deferred"
    },
    "block_shortcut": {
        "sco_id": 710467,
        "block_id": 881524,
        "shortcut_options": "是$$否$$你好",
        "__typename": "dm_shortcut"
    }
    """
    class Meta:
        db_table = 'action_response'  # 表名
        verbose_name = "响应"
        verbose_name_plural = "响应"
        # index_together = [["function_en",],]
        # unique_together = (("id", "link_id"),)

    pass


class BoundSlot(models.Model):
    """
    词槽
    """
    pass


class BlockResponse(models.Model):
    """
    响应
    """
    pass


class BlockRelation(models.Model):
    """
    单元跳转关系
    """
    pass


class BlockDeferred(models.Model):
    """
    延期设置
    """
    pass


class BlockShortcut(models.Model):
    """
    预置回复
    """
    pass


class Position(models.Model):
    """
    位置信息
    """
    x = models.IntegerField(verbose_name='x坐标')
    y = models.IntegerField(verbose_name='y坐标')
    pass


class ViewSize(models.Model):
    """
    视图设置
    """
    pass
