import graphene
from django.utils import timezone
from graphene import relay
from graphql_relay import from_global_id

from app_task.models import \
    App, \
    BlockDeferred, \
    BlockRelation, \
    BlockResponse, \
    BlockShortcut, \
    Robot, \
    Task, \
    Block, \
    Slot, \
    Entity, \
    Trigger, \
    TriggerInfo
from app_task.types import \
    AppType, \
    BlockDeferredType, \
    BlockRelationType, \
    BlockResponseType, \
    BlockShortcutType, \
    RobotType, \
    TaskType, \
    BlockType, \
    SlotType, \
    EntityType, \
    TriggerInfoType, \
    TriggerType


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


class AppUpsertMutation(relay.ClientIDMutation):
    """
    应用（Upsert）
    """

    class Input:
        obj = AppInput(required=True)

    result = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        if obj.get('id') is None:
            new_or_find_obj = App.objects.create(
                app_name=obj.get('app_name', ''),
                app_logo=obj.get('app_logo', ''),
                app_remark=obj.get('app_remark', ''),
                app_hash=obj.get('app_hash', ''),
                app_key=obj.get('app_key', ''),
            )
        else:
            app_type, app_id = from_global_id(obj.get('id'))
            new_or_find_obj = App.objects.get(pk=app_id)
            new_or_find_obj.app_name = obj.get('app_name', '')
            new_or_find_obj.app_logo = obj.get('app_logo', '')
            new_or_find_obj.app_remark = obj.get('app_remark', '')
            new_or_find_obj.db_insert_time = timezone.now()
            new_or_find_obj.app_hash = obj.get('app_hash', '')
            new_or_find_obj.app_key = obj.get('app_key', '')
            new_or_find_obj.save()

        return AppUpsertMutation(result=new_or_find_obj)

    pass


class AppDeleteMutation(relay.ClientIDMutation):
    """
    应用（Delete）
    """

    class Input:
        obj = AppInput(required=True)

    result = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        obj_type, obj_id = from_global_id(obj.get('id'))
        new_or_find_obj = App.objects.get(pk=obj_id)
        new_or_find_obj.delete()

        return AppDeleteMutation(result=new_or_find_obj)
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


class RobotUpsertMutation(relay.ClientIDMutation):
    """
    机器人（Upsert）
    """

    class Input:
        obj = RobotInput(required=True)

    result = graphene.Field(RobotType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        if obj.get('id') is None:
            app_type, app_id = from_global_id(obj.get('app_id'))

            new_or_find_obj = Robot.objects.create(
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

            new_or_find_obj = Robot.objects.get(pk=robot_id)
            new_or_find_obj.robot_name = obj.get('robot_name', '')
            new_or_find_obj.robot_logo = obj.get('robot_logo', '')
            new_or_find_obj.robot_detail = obj.get('robot_detail', '')
            new_or_find_obj.robot_status = obj.get('robot_status', 0)

            new_or_find_obj.robot_ttl = obj.get('robot_ttl', 0)
            new_or_find_obj.odst_threshold = obj.get('odst_threshold', 0)

            new_or_find_obj.pos_status = obj.get('pos_status', 0)
            new_or_find_obj.pos_num = obj.get('pos_num', 0)
            new_or_find_obj.pos_source = obj.get('pos_source', '')

            new_or_find_obj.goback_action = obj.get('goback_action', 0)
            new_or_find_obj.exit_action = obj.get('exit_action', 0)
            new_or_find_obj.exit_rsp_mode = obj.get('exit_rsp_mode', 0)

            new_or_find_obj.app_id = app_id
            new_or_find_obj.save()

        return RobotUpsertMutation(result=new_or_find_obj)

    pass


class RobotDeleteMutation(relay.ClientIDMutation):
    """
    机器人（Delete）
    """

    class Input:
        obj = AppInput(required=True)

    result = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        obj_type, obj_id = from_global_id(obj.get('id'))
        new_or_find_obj = App.objects.get(pk=obj_id)
        new_or_find_obj.delete()

        return RobotDeleteMutation(result=new_or_find_obj)
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


class TaskUpsertMutation(relay.ClientIDMutation):
    """
    任务/意图（Upsert）
    """

    class Input:
        obj = TaskInput(required=True)

    result = graphene.Field(TaskType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        if obj.get('id') is None:
            robot_type, robot_id = from_global_id(obj.get('robot_id'))

            new_or_find_obj = Task.objects.create(
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

            new_or_find_obj = Task.objects.get(pk=task_id)
            new_or_find_obj.robot_id = robot_id
            new_or_find_obj.version = obj.get('version', 0)
            new_or_find_obj.name = obj.get('name', '')
            new_or_find_obj.task_status = obj.get('task_status', 0)
            new_or_find_obj.default_end_block_mult_val = obj.get('default_end_block_mult_val', 0)
            new_or_find_obj.trigger_faq = obj.get('trigger_faq', 0)
            new_or_find_obj.ttl = obj.get('ttl', 0)
            new_or_find_obj.threshold = obj.get('threshold', 0)

            new_or_find_obj.save()

        return TaskUpsertMutation(result=new_or_find_obj)

    pass


class TaskDeleteMutation(relay.ClientIDMutation):
    """
    任务/意图（Delete）
    """

    class Input:
        obj = AppInput(required=True)

    result = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        obj_type, obj_id = from_global_id(obj.get('id'))
        new_or_find_obj = App.objects.get(pk=obj_id)
        new_or_find_obj.delete()

        return TaskDeleteMutation(result=new_or_find_obj)
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

    # 位置
    position_x = graphene.Int()  # position_x
    position_y = graphene.Int()  # position_y
    pass


class BlockUpsertMutation(relay.ClientIDMutation):
    """
    单元（Upsert）
    """

    class Input:
        obj = BlockInput(required=True)

    result = graphene.Field(BlockType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        if obj.get('id') is None:
            bound_slot_type, bound_slot_id = from_global_id(obj.get('bound_slot_id'))
            task_type, task_id = from_global_id(obj.get('task_id'))

            new_or_find_obj = Block.objects.create(
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
                position_x=obj.get('position_x', 0),
                position_y=obj.get('position_y', 0),
            )
        else:
            block_type, block_id = from_global_id(obj.get('id'))
            bound_slot_type, bound_slot_id = from_global_id(obj.get('bound_slot_id'))
            task_type, task_id = from_global_id(obj.get('task_id'))

            new_or_find_obj = Block.objects.get(pk=block_id)

            new_or_find_obj.bound_slot_id = bound_slot_id
            new_or_find_obj.task_id = task_id
            new_or_find_obj.name = obj.get('name', '')
            new_or_find_obj.type_id = obj.get('type_id', 0)
            new_or_find_obj.uri = obj.get('uri', '')
            new_or_find_obj.max_interval = obj.get('max_interval', 0)
            new_or_find_obj.mult_val = obj.get('mult_val', 0)
            new_or_find_obj.fill_any_time = obj.get('fill_any_time', False)
            new_or_find_obj.order_id = obj.get('order_id', 0)
            new_or_find_obj.rsp_mode = obj.get('rsp_mode', 0)
            new_or_find_obj.first_order = obj.get('first_order', 0)
            new_or_find_obj.pre_check = obj.get('pre_check', '')
            new_or_find_obj.run_once = obj.get('run_once', False)
            new_or_find_obj.disable_exit = obj.get('disable_exit', 0)
            new_or_find_obj.disable_goback = obj.get('disable_goback', 0)
            new_or_find_obj.position_x = obj.get('position_x', 0)
            new_or_find_obj.position_y = obj.get('position_y', 0)
            new_or_find_obj.save()

        return BlockUpsertMutation(result=new_or_find_obj)

    pass


class BlockDeleteMutation(relay.ClientIDMutation):
    """
    单元（Delete）
    """

    class Input:
        obj = AppInput(required=True)

    result = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        obj_type, obj_id = from_global_id(obj.get('id'))
        new_or_find_obj = App.objects.get(pk=obj_id)
        new_or_find_obj.delete()

        return BlockDeleteMutation(result=new_or_find_obj)
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


class SlotUpsertMutation(relay.ClientIDMutation):
    """
    词槽（Upsert）
    """

    class Input:
        obj = SlotInput(required=True)

    result = graphene.Field(SlotType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        if obj.get('id') is None:
            robot_type, robot_id = from_global_id(obj.get('robot_id'))

            new_or_find_obj = Slot.objects.create(
                robot_id=robot_id,
                name=obj.get('name', ''),
                alias=obj.get('alias', ''),
                disposable=obj.get('disposable', False),
                fill_slot_with_query=obj.get('fill_slot_with_query', False),
            )
        else:
            slot_type, slot_id = from_global_id(obj.get('id'))
            robot_type, robot_id = from_global_id(obj.get('robot_id'))

            new_or_find_obj = Slot.objects.get(pk=slot_id)

            new_or_find_obj.robot_id = robot_id
            new_or_find_obj.name = obj.get('name', '')
            new_or_find_obj.alias = obj.get('alias', '')
            new_or_find_obj.disposable = obj.get('disposable', False)
            new_or_find_obj.fill_slot_with_query = obj.get('fill_slot_with_query', False)

            new_or_find_obj.save()

        return SlotUpsertMutation(result=new_or_find_obj)

    pass


class SlotDeleteMutation(relay.ClientIDMutation):
    """
    词槽（Delete）
    """

    class Input:
        obj = AppInput(required=True)

    result = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        obj_type, obj_id = from_global_id(obj.get('id'))
        new_or_find_obj = App.objects.get(pk=obj_id)
        new_or_find_obj.delete()

        return SlotDeleteMutation(result=new_or_find_obj)
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


class EntityUpsertMutation(relay.ClientIDMutation):
    """
    实体（Upsert）
    """

    class Input:
        obj = EntityInput(required=True)

    result = graphene.Field(EntityType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        if obj.get('id') is None:
            new_or_find_obj = Entity.objects.create(
                entity_name=obj.get('entity_name', ''),
                entity_desc=obj.get('entity_desc', ''),
                entity_detail=obj.get('entity_detail', ''),
                entity_type=obj.get('entity_type', 0)
            )
        else:
            entity_type, entity_id = from_global_id(obj.get('id'))

            new_or_find_obj = Entity.objects.get(pk=entity_id)

            new_or_find_obj.entity_name = obj.get('entity_name', ''),
            new_or_find_obj.entity_desc = obj.get('entity_desc', ''),
            new_or_find_obj.entity_detail = obj.get('entity_detail', ''),
            new_or_find_obj.entity_type = obj.get('entity_type', 0)

            new_or_find_obj.save()

        return EntityUpsertMutation(result=new_or_find_obj)

    pass


class EntityDeleteMutation(relay.ClientIDMutation):
    """
    实体（Delete）
    """

    class Input:
        obj = AppInput(required=True)

    result = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        obj_type, obj_id = from_global_id(obj.get('id'))
        new_or_find_obj = App.objects.get(pk=obj_id)
        new_or_find_obj.delete()

        return EntityDeleteMutation(result=new_or_find_obj)
    pass


class BlockResponseInput(graphene.InputObjectType):
    """
    单元响应处理输入
    """
    id = graphene.ID()
    block_id = graphene.ID()  # 单元id

    response = graphene.String()  # 响应规则
    rsp_once = graphene.Boolean()  # 响应一次
    pass


class BlockResponseUpsertMutation(relay.ClientIDMutation):
    """
    单元响应处理（Upsert）
    """

    class Input:
        obj = BlockResponseInput(required=True)

    result = graphene.Field(BlockResponseType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        block_type, block_id = from_global_id(obj.get('block_id'))

        if obj.get('id') is None:
            new_or_find_obj = BlockResponse.objects.create(
                block_id=block_id,
                response=obj.get('response', ''),
                rsp_once=obj.get('rsp_once', False),
            )
        else:
            response_type, response_id = from_global_id(obj.get('id'))

            new_or_find_obj = BlockResponse.objects.get(pk=response_id)

            new_or_find_obj.block_id = block_id
            new_or_find_obj.response = obj.get('response', '')
            new_or_find_obj.rsp_once = obj.get('rsp_once', False)

            new_or_find_obj.save()

        return BlockResponseUpsertMutation(result=new_or_find_obj)

    pass


class BlockResponseDeleteMutation(relay.ClientIDMutation):
    """
    单元响应处理（Delete）
    """

    class Input:
        obj = AppInput(required=True)

    result = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        obj_type, obj_id = from_global_id(obj.get('id'))
        new_or_find_obj = App.objects.get(pk=obj_id)
        new_or_find_obj.delete()

        return BlockResponseDeleteMutation(result=new_or_find_obj)
    pass


class BlockRelationInput(graphene.InputObjectType):
    """
    单元跳转关系输入
    """
    id = graphene.ID()
    from_block_id = graphene.ID()  # from单元id
    to_block_id = graphene.ID()  # to单元id

    condition = graphene.String()  # 条件
    value = graphene.String()  # 值
    pass


class BlockRelationUpsertMutation(relay.ClientIDMutation):
    """
    单元跳转关系（Upsert）
    """

    class Input:
        obj = BlockRelationInput(required=True)

    result = graphene.Field(BlockRelationType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        from_block_type, from_block_id = from_global_id(obj.get('block_id'))
        to_block_type, to_block_id = from_global_id(obj.get('to_block_id'))

        if obj.get('id') is None:
            new_or_find_obj = BlockRelation.objects.create(
                from_block_id=from_block_id,
                to_block_id=to_block_id,
                condition=obj.get('condition', ''),
                value=obj.get('value', ''),
            )
        else:
            block_relation_type, block_relation_id = from_global_id(obj.get('id'))

            new_or_find_obj = BlockRelation.objects.get(pk=block_relation_id)

            new_or_find_obj.from_block_id = from_block_id
            new_or_find_obj.to_block_id = to_block_id
            new_or_find_obj.condition = obj.get('condition', '')
            new_or_find_obj.value = obj.get('value', '')

            new_or_find_obj.save()

        return BlockRelationUpsertMutation(result=new_or_find_obj)

    pass


class BlockRelationDeleteMutation(relay.ClientIDMutation):
    """
    单元跳转关系（Delete）
    """

    class Input:
        obj = AppInput(required=True)

    result = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        obj_type, obj_id = from_global_id(obj.get('id'))
        new_or_find_obj = App.objects.get(pk=obj_id)
        new_or_find_obj.delete()

        return BlockRelationDeleteMutation(result=new_or_find_obj)
    pass


class BlockDeferredInput(graphene.InputObjectType):
    """
    延期设置输入
    """
    id = graphene.ID()
    block_id = graphene.ID()  # 单元id

    response = graphene.String()  # 操作
    deferred_time = graphene.Int()  # 次数
    pass


class BlockDeferredUpsertMutation(relay.ClientIDMutation):
    """
    延期设置（Upsert）
    """

    class Input:
        obj = BlockDeferredInput(required=True)

    result = graphene.Field(BlockDeferredType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        block_type, block_id = from_global_id(obj.get('block_id'))
        if obj.get('id') is None:
            new_or_find_obj = BlockDeferred.objects.create(
                block_id=block_id,
                response=obj.get('response', ''),
                deferred_time=obj.get('deferred_time', 0),
            )
        else:
            block_deferred_type, block_deferred_id = from_global_id(obj.get('id'))

            new_or_find_obj = BlockDeferred.objects.get(pk=block_deferred_id)

            new_or_find_obj.block_id = block_id
            new_or_find_obj.response = obj.get('response', '')
            new_or_find_obj.deferred_time = obj.get('deferred_time', 0)

            new_or_find_obj.save()

        return BlockDeferredUpsertMutation(result=new_or_find_obj)

    pass


class BlockDeferredDeleteMutation(relay.ClientIDMutation):
    """
    延期设置（Delete）
    """

    class Input:
        obj = AppInput(required=True)

    result = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        obj_type, obj_id = from_global_id(obj.get('id'))
        new_or_find_obj = App.objects.get(pk=obj_id)
        new_or_find_obj.delete()

        return BlockDeferredDeleteMutation(result=new_or_find_obj)
    pass


class BlockShortcutInput(graphene.InputObjectType):
    """
    预置回复输入
    """
    id = graphene.ID()
    block_id = graphene.ID()  # 单元id

    shortcut_options = graphene.String()  # 操作
    pass


class BlockShortcutUpsertMutation(relay.ClientIDMutation):
    """
    预置回复（Upsert）
    """

    class Input:
        obj = BlockShortcutInput(required=True)

    result = graphene.Field(BlockShortcutType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        block_type, block_id = from_global_id(obj.get('block_id'))
        if obj.get('id') is None:
            new_or_find_obj = BlockShortcut.objects.create(
                block_id=block_id,
                shortcut_options=obj.get('shortcut_options', ''),
            )
        else:
            block_shortcut_type, block_shortcut_id = from_global_id(obj.get('id'))

            new_or_find_obj = BlockShortcut.objects.get(pk=block_shortcut_id)

            new_or_find_obj.block_id = block_id
            new_or_find_obj.shortcut_options = obj.get('shortcut_options', '')

            new_or_find_obj.save()

        return BlockShortcutUpsertMutation(result=new_or_find_obj)

    pass


class BlockShortcutDeleteMutation(relay.ClientIDMutation):
    """
    预置回复（Delete）
    """

    class Input:
        obj = AppInput(required=True)

    result = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        obj_type, obj_id = from_global_id(obj.get('id'))
        new_or_find_obj = App.objects.get(pk=obj_id)
        new_or_find_obj.delete()

        return BlockShortcutDeleteMutation(result=new_or_find_obj)
    pass


class TriggerInput(graphene.InputObjectType):
    """
    触发器输入
    """
    id = graphene.ID()
    task_id = graphene.ID()  # 关联任务（意图）
    next_block_id = graphene.ID()  # 单元

    # 位置
    position_x = graphene.Int()  # position_x
    position_y = graphene.Int()  # position_y
    pass


class TriggerUpsertMutation(relay.ClientIDMutation):
    """
    触发器（Upsert）
    """

    class Input:
        obj = TriggerInput(required=True)

    result = graphene.Field(TriggerType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        task_type, task_id = from_global_id(obj.get('task_id'))
        next_block_type, next_block_id = from_global_id(obj.get('next_block_id'))

        if obj.get('id') is None:
            new_or_find_obj = Trigger.objects.create(
                task_id=task_id,
                next_block_id=next_block_id,
                position_x=obj.get('position_x', 0),
                position_y=obj.get('position_y', 0),
            )
        else:
            trigger_type, trigger_id = from_global_id(obj.get('id'))

            new_or_find_obj = Trigger.objects.get(pk=trigger_id)

            new_or_find_obj.task_id = task_id
            new_or_find_obj.next_block_id = next_block_id
            new_or_find_obj.position_x = obj.get('position_x', 0)
            new_or_find_obj.position_y = obj.get('position_y', 0)

            new_or_find_obj.save()

        return TriggerUpsertMutation(result=new_or_find_obj)

    pass


class TriggerDeleteMutation(relay.ClientIDMutation):
    """
    触发器（Delete）
    """

    class Input:
        obj = AppInput(required=True)

    result = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        obj_type, obj_id = from_global_id(obj.get('id'))
        new_or_find_obj = App.objects.get(pk=obj_id)
        new_or_find_obj.delete()

        return TriggerDeleteMutation(result=new_or_find_obj)
    pass


class TriggerInfoInput(graphene.InputObjectType):
    """
    触发器信息输入
    """
    id = graphene.ID()
    trigger_id = graphene.ID()

    content = graphene.String()  # 内容
    trigger_type = graphene.Int()  # 类型
    pass


class TriggerInfoUpsertMutation(relay.ClientIDMutation):
    """
    触发器信息（Upsert）
    """

    class Input:
        obj = TriggerInfoInput(required=True)

    result = graphene.Field(TriggerInfoType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        trigger_type, trigger_id = from_global_id(obj.get('block_id'))

        if obj.get('id') is None:
            new_or_find_obj = TriggerInfo.objects.create(
                trigger_id=trigger_id,
                content=obj.get('content', ''),
                trigger_type=obj.get('trigger_type', 0),
            )
        else:
            trigger_info_type, trigger_info_id = from_global_id(obj.get('id'))

            new_or_find_obj = TriggerInfo.objects.get(pk=trigger_info_id)

            new_or_find_obj.trigger_id = trigger_id
            new_or_find_obj.content = obj.get('content', '')
            new_or_find_obj.trigger_type = obj.get('trigger_type', 0)

            new_or_find_obj.save()

        return TriggerInfoUpsertMutation(result=new_or_find_obj)

    pass


class TriggerInfoDeleteMutation(relay.ClientIDMutation):
    """
    触发器信息（Delete）
    """

    class Input:
        obj = AppInput(required=True)

    result = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        obj_type, obj_id = from_global_id(obj.get('id'))
        new_or_find_obj = App.objects.get(pk=obj_id)
        new_or_find_obj.delete()

        return TriggerInfoDeleteMutation(result=new_or_find_obj)
    pass
