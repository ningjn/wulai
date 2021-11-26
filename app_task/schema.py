from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from app_task.mutations import AppMutation, RobotMutation, TaskMutation, EntityMutation, SlotMutation, BlockMutation
from app_task.types import AppType, RobotType, TaskType, BlockType, SlotType, EntityType


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

    pass


class Mutation(object):
    # 应用
    upsert_app = AppMutation.Field()

    # 机器人
    upsert_robot = RobotMutation.Field()

    # 任务/意图
    upsert_task = TaskMutation.Field()

    # 单元
    upsert_block = BlockMutation.Field()

    # 词槽
    upsert_slot = SlotMutation.Field()

    # 实体
    upsert_entity = EntityMutation.Field()

    pass
