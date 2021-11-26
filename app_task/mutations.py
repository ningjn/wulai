import graphene
from django.utils import timezone
from graphene import relay
from graphql_relay import from_global_id

from app_task.models import App, Robot, Task, Block, Slot, Entity
from app_task.types import AppType, RobotType, TaskType, BlockType, SlotType, EntityType


class AppInput(graphene.InputObjectType):
    """
    应用输入
    """
    id = graphene.ID()
    app_name = graphene.String()  # '名称'
    app_logo = graphene.String()  # '图标'
    app_remark = graphene.String()  # '备注'
    app_hash = graphene.String()  # 'Hash'
    app_key = graphene.String()  # 'Key'
    pass


class AppMutation(relay.ClientIDMutation):
    """
    应用Mutation
    """

    class Input:
        obj = AppInput(required=True)

    result = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        if obj.get('id') is None:
            new_obj = App.objects.create(
                app_name=obj.get('app_name', ''),
                app_logo=obj.get('app_logo', ''),
                app_remark=obj.get('app_remark', ''),
                app_hash=obj.get('app_hash', ''),
                app_key=obj.get('app_key', ''),
            )
        else:
            app_type, app_id = from_global_id(obj.get('app_id'))
            new_obj, flag = App.objects.get(pk=app_id)
            new_obj.app_name = obj.get('app_name', '')
            new_obj.app_logo = obj.get('app_logo', '')
            new_obj.app_remark = obj.get('app_remark', '')
            new_obj.db_insert_time = timezone.now()
            new_obj.app_hash = obj.get('app_hash', '')
            new_obj.app_key = obj.get('app_key', '')
            new_obj.save()

        return AppMutation(result=new_obj)

    pass


class RobotInput(graphene.InputObjectType):
    """
    机器人输入
    """
    id = graphene.ID()
    robot_name = graphene.String()  # 名称
    robot_logo = graphene.String()  # 图标
    robot_detail = graphene.String()  # 描述
    robot_status = graphene.Int()  # 状态

    robot_ttl = graphene.Int()  # 闲置等待时长
    odst_threshold = graphene.Float()  # 智能填槽阈值

    pos_status = graphene.Int()  # 自动添加预置回复
    pos_num = graphene.Int()  # 推荐个数
    pos_source = graphene.String()  # 推荐源

    goback_action = graphene.Int()  # 是否可以回退
    exit_action = graphene.Int()  # 是否主动退出
    exit_rsp_mode = graphene.Int()  # 退出响应模式

    app_id = graphene.ID()  # 应用id
    pass


class RobotMutation(relay.ClientIDMutation):
    """
    机器人Mutation
    """

    class Input:
        obj = RobotInput(required=True)

    result = graphene.Field(RobotType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        if obj.get('id') is None:
            app_type, app_id = from_global_id(obj.get('app_id'))

            new_obj = Robot.objects.create(
                robot_name=obj.get('robot_name', ''),
                robot_logo=obj.get('robot_logo', ''),
                robot_detail=obj.get('robot_detail', ''),
                robot_status=obj.get('robot_status', 0),

                robot_ttl=obj.get('robot_ttl', 0),
                odst_threshold=obj.get('odst_threshold', 0),

                pos_status=obj.get('pos_status', 0),
                pos_num=obj.get('pos_num', 0),
                pos_source=obj.get('pos_source', ''),

                goback_action=obj.get('goback_action', 0),
                exit_action=obj.get('exit_action', 0),
                exit_rsp_mode=obj.get('exit_rsp_mode', 0),

                app_id=app_id,
            )
        else:
            robot_type, robot_id = from_global_id(obj.get('id'))
            app_type, app_id = from_global_id(obj.get('app_id'))

            new_obj, flag = Robot.objects.get(pk=robot_id)
            new_obj.robot_name = obj.get('robot_name', '')
            new_obj.robot_logo = obj.get('robot_logo', '')
            new_obj.robot_detail = obj.get('robot_detail', '')
            new_obj.robot_status = obj.get('robot_status', 0)

            new_obj.robot_ttl = obj.get('robot_ttl', 0)
            new_obj.odst_threshold = obj.get('odst_threshold', 0)

            new_obj.pos_status = obj.get('pos_status', 0)
            new_obj.pos_num = obj.get('pos_num', 0)
            new_obj.pos_source = obj.get('pos_source', '')

            new_obj.goback_action = obj.get('goback_action', 0)
            new_obj.exit_action = obj.get('exit_action', 0)
            new_obj.exit_rsp_mode = obj.get('exit_rsp_mode', 0)

            new_obj.app_id = app_id
            new_obj.save()

        return RobotMutation(result=new_obj)

    pass


class TaskInput(graphene.InputObjectType):
    """
    任务/意图输入
    """
    id = graphene.ID()

    robot_id = graphene.ID()  # 机器人
    version = graphene.Int()  # 版本
    name = graphene.String()  # 名称
    task_status = graphene.Int()  # 状态

    # 0开启，1关闭
    default_end_block_mult_val = graphene.Int()  # 中断保留词槽
    # 0开启，1关闭
    trigger_faq = graphene.Int()  # 是否触发知识点
    ttl = graphene.Int()  # 闲置等待时长
    threshold = graphene.Float()  # 智能填槽阈值


class TaskMutation(relay.ClientIDMutation):
    """
    任务/意图Mutation
    """

    class Input:
        obj = TaskInput(required=True)

    result = graphene.Field(TaskType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        if obj.get('id') is None:
            robot_type, robot_id = from_global_id(obj.get('robot_id'))

            new_obj = Task.objects.create(
                robot_id=robot_id,
                version=obj.get('version', 0),
                name=obj.get('name', ''),
                task_status=obj.get('task_status', 0),
                default_end_block_mult_val=obj.get('default_end_block_mult_val', 0),
                trigger_faq=obj.get('trigger_faq', 0),
                ttl=obj.get('ttl', 0),
                threshold=obj.get('threshold', 0),
            )
        else:
            task_type, task_id = from_global_id(obj.get('id'))
            robot_type, robot_id = from_global_id(obj.get('robot_id'))

            new_obj, flag = Task.objects.get(pk=task_id)
            new_obj.robot_id = robot_id
            new_obj.version = obj.get('version', 0)
            new_obj.name = obj.get('name', '')
            new_obj.task_status = obj.get('task_status', 0)
            new_obj.default_end_block_mult_val = obj.get('default_end_block_mult_val', 0)
            new_obj.trigger_faq = obj.get('trigger_faq', 0)
            new_obj.ttl = obj.get('ttl', 0)
            new_obj.threshold = obj.get('threshold', 0)

            new_obj.save()

        return TaskMutation(result=new_obj)

    pass


class BlockInput(graphene.InputObjectType):
    """
    单元输入
    """
    id = graphene.ID()
    bound_slot_id = graphene.ID()  # 关联词槽
    task_id = graphene.ID()  # 关联任务（意图）

    name = graphene.String()  # 单元名称
    type_id = graphene.Int()  # 类型
    uri = graphene.String()  # 跳转意图

    # 对话策略
    max_interval = graphene.Int()  # 尝试询问次数
    mult_val = graphene.Int()  # 机器人得到多个值时，向用户澄清
    fill_any_time = graphene.Boolean()  # 仅在当前单元询问时填槽
    order_id = graphene.Int()  # 未知
    rsp_mode = graphene.Int()  # 未知
    first_order = graphene.Int()  # 未知
    pre_check = graphene.String()  # 未知
    run_once = graphene.Boolean()  # 运行一次
    disable_exit = graphene.Int()  # 允许退出
    disable_goback = graphene.Int()  # 允许后退
    pass


class BlockMutation(relay.ClientIDMutation):
    """
    单元Mutation
    """

    class Input:
        obj = BlockInput(required=True)

    result = graphene.Field(BlockType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        if obj.get('id') is None:
            bound_slot_type, bound_slot_id = from_global_id(obj.get('bound_slot_id'))
            task_type, task_id = from_global_id(obj.get('task_id'))

            new_obj = Block.objects.create(
                bound_slot_id=bound_slot_id,
                task_id=task_id,
                name=obj.get('name', ''),
                type_id=obj.get('type_id', 0),
                uri=obj.get('uri', ''),
                max_interval=obj.get('max_interval', 0),
                mult_val=obj.get('mult_val', 0),
                fill_any_time=obj.get('fill_any_time', False),
                order_id=obj.get('order_id', 0),
                rsp_mode=obj.get('rsp_mode', 0),
                first_order=obj.get('first_order', 0),
                pre_check=obj.get('pre_check', ''),
                run_once=obj.get('run_once', False),
                disable_exit=obj.get('disable_exit', 0),
                disable_goback=obj.get('disable_goback', 0),
            )
        else:
            block_type, block_id = from_global_id(obj.get('id'))
            bound_slot_type, bound_slot_id = from_global_id(obj.get('bound_slot_id'))
            task_type, task_id = from_global_id(obj.get('task_id'))

            new_obj, flag = Block.objects.get(pk=block_id)

            new_obj.bound_slot_id = bound_slot_id
            new_obj.task_id = task_id
            new_obj.name = obj.get('name', '')
            new_obj.type_id = obj.get('type_id', 0)
            new_obj.uri = obj.get('uri', '')
            new_obj.max_interval = obj.get('max_interval', 0)
            new_obj.mult_val = obj.get('mult_val', 0)
            new_obj.fill_any_time = obj.get('fill_any_time', False)
            new_obj.order_id = obj.get('order_id', 0)
            new_obj.rsp_mode = obj.get('rsp_mode', 0)
            new_obj.first_order = obj.get('first_order', 0)
            new_obj.pre_check = obj.get('pre_check', '')
            new_obj.run_once = obj.get('run_once', False)
            new_obj.disable_exit=obj.get('disable_exit', 0)
            new_obj.disable_goback=obj.get('disable_goback', 0)
            new_obj.save()

        return BlockMutation(result=new_obj)

    pass


class SlotInput(graphene.InputObjectType):
    """
    词槽输入
    """
    id = graphene.ID()
    robot_id = graphene.ID()  # 关联机器人

    name = graphene.String()  # 名称
    alias = graphene.String()  # alias
    disposable = graphene.Boolean()  #
    fill_slot_with_query = graphene.Boolean()  #

    source_entities = graphene.List(graphene.String)  # 实体id

    pass


class SlotMutation(relay.ClientIDMutation):
    """
    词槽Mutation
    """

    class Input:
        obj = SlotInput(required=True)

    result = graphene.Field(SlotType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        if obj.get('id') is None:
            robot_type, robot_id = from_global_id(obj.get('robot_id'))

            new_obj = Slot.objects.create(
                robot_id=robot_id,
                name=obj.get('name', ''),
                alias=obj.get('alias', ''),
                disposable=obj.get('disposable', False),
                fill_slot_with_query=obj.get('fill_slot_with_query', False),
            )
        else:
            slot_type, slot_id = from_global_id(obj.get('id'))
            robot_type, robot_id = from_global_id(obj.get('robot_id'))

            new_obj, flag = Slot.objects.get(pk=slot_id)

            new_obj.robot_id = robot_id
            new_obj.name = obj.get('name', '')
            new_obj.alias = obj.get('alias', '')
            new_obj.disposable = obj.get('disposable', False)
            new_obj.fill_slot_with_query = obj.get('fill_slot_with_query', False)

            new_obj.save()

        return SlotMutation(result=new_obj)

    pass


class EntityInput(graphene.InputObjectType):
    """
    实体输入
    """
    id = graphene.ID()

    entity_name = graphene.String()  # 名称
    entity_desc = graphene.String()  # entity_desc
    entity_detail = graphene.String()  # entity_detail
    entity_type = graphene.Int()  # entity_type

    pass


class EntityMutation(relay.ClientIDMutation):
    """
    实体Mutation
    """

    class Input:
        obj = EntityInput(required=True)

    result = graphene.Field(EntityType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        if obj.get('id') is None:
            new_obj = Entity.objects.create(
                entity_name=obj.get('entity_name', ''),
                entity_desc=obj.get('entity_desc', ''),
                entity_detail=obj.get('entity_detail', ''),
                entity_type=obj.get('entity_type', 0)
            )
        else:
            entity_type, entity_id = from_global_id(obj.get('id'))

            new_obj, flag = Entity.objects.get(pk=entity_id)

            new_obj.entity_name = obj.get('entity_name', ''),
            new_obj.entity_desc = obj.get('entity_desc', ''),
            new_obj.entity_detail = obj.get('entity_detail', ''),
            new_obj.entity_type = obj.get('entity_type', 0)

            new_obj.save()

        return EntityMutation(result=new_obj)

    pass
