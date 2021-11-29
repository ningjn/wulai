from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from app_task.mutations import \
    AppUpsertMutation, \
    AppDeleteMutation, \
    BlockDeferredUpsertMutation, \
    BlockRelationUpsertMutation, \
    BlockResponseUpsertMutation, \
    BlockShortcutUpsertMutation, \
    RobotUpsertMutation, \
    TaskUpsertMutation, \
    EntityUpsertMutation, \
    SlotUpsertMutation, \
    BlockUpsertMutation, \
    TriggerInfoUpsertMutation, \
    TriggerUpsertMutation, RobotDeleteMutation, TaskDeleteMutation, BlockDeleteMutation, SlotDeleteMutation, \
    EntityDeleteMutation, BlockResponseDeleteMutation, TriggerInfoDeleteMutation, TriggerDeleteMutation, \
    BlockShortcutDeleteMutation, BlockDeferredDeleteMutation, BlockRelationDeleteMutation
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


class Query(object):
    # 应用
    app = relay.Node.Field(AppType)
    all_apps = DjangoFilterConnectionField(AppType)

    # 机器人
    robot = relay.Node.Field(RobotType)
    all_robots = DjangoFilterConnectionField(RobotType)

    # 任务/意图
    task = relay.Node.Field(TaskType)
    all_tasks = DjangoFilterConnectionField(TaskType)

    # 单元
    block = relay.Node.Field(BlockType)
    all_blocks = DjangoFilterConnectionField(BlockType)

    # 词槽
    slot = relay.Node.Field(SlotType)
    all_slots = DjangoFilterConnectionField(SlotType)

    # 实体
    entity = relay.Node.Field(EntityType)
    all_entities = DjangoFilterConnectionField(EntityType)

    # 单元响应处理
    block_response = relay.Node.Field(BlockResponseType)
    all_block_responses = DjangoFilterConnectionField(BlockResponseType)

    # 单元跳转关系
    block_relation = relay.Node.Field(BlockRelationType)
    all_block_relations = DjangoFilterConnectionField(BlockRelationType)

    # 延期设置
    block_deferred = relay.Node.Field(BlockDeferredType)
    all_block_deferreds = DjangoFilterConnectionField(BlockDeferredType)

    # 预置回复
    block_shortcut = relay.Node.Field(BlockShortcutType)
    all_block_shortcuts = DjangoFilterConnectionField(BlockShortcutType)

    # 触发器
    trigger = relay.Node.Field(TriggerType)
    all_triggers = DjangoFilterConnectionField(TriggerType)

    # 触发器信息
    trigger_info = relay.Node.Field(TriggerInfoType)
    all_trigger_infoes = DjangoFilterConnectionField(TriggerInfoType)

    pass


class Mutation(object):
    # 应用
    upsert_app = AppUpsertMutation.Field()
    delete_app = AppDeleteMutation.Field()

    # 机器人
    upsert_robot = RobotUpsertMutation.Field()
    delete_robot = RobotDeleteMutation.Field()

    # 任务/意图
    upsert_task = TaskUpsertMutation.Field()
    delete_task = TaskDeleteMutation.Field()

    # 单元
    upsert_block = BlockUpsertMutation.Field()
    delete_block = BlockDeleteMutation.Field()

    # 词槽
    upsert_slot = SlotUpsertMutation.Field()
    delete_slot = SlotDeleteMutation.Field()

    # 实体
    upsert_entity = EntityUpsertMutation.Field()
    delete_entity = EntityDeleteMutation.Field()

    # 单元响应处理
    upsert_block_response = BlockResponseUpsertMutation.Field()
    delete_block_response = BlockResponseDeleteMutation.Field()

    # 单元跳转关系
    upsert_block_relation = BlockRelationUpsertMutation.Field()
    delete_block_relation = BlockRelationDeleteMutation.Field()

    # 延期设置
    upsert_block_deferred = BlockDeferredUpsertMutation.Field()
    delete_block_deferred = BlockDeferredDeleteMutation.Field()

    # 预置回复
    upsert_block_shortcut = BlockShortcutUpsertMutation.Field()
    delete_block_shortcut = BlockShortcutDeleteMutation.Field()

    # 触发器
    upsert_trigger = TriggerUpsertMutation.Field()
    delete_trigger = TriggerDeleteMutation.Field()

    # 触发器信息
    upsert_trigger_info = TriggerInfoUpsertMutation.Field()
    delete_trigger_info = TriggerInfoDeleteMutation.Field()

    pass
