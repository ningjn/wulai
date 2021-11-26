import graphene
from graphene_django import DjangoListField
from graphene_django.types import DjangoObjectType
from graphene import relay

from app_task.models import App, Robot, Task, Block, Slot, Entity


class AppType(DjangoObjectType):
    """
    应用
    """
    pk = graphene.ID(source='pk')

    class Meta:
        model = App
        interfaces = [relay.Node,]
        filter_fields = {
            'app_name': ['exact', 'icontains', 'istartswith'],
        }


class RobotType(DjangoObjectType):
    """
    机器人/场景
    """
    pk = graphene.ID(source='pk')

    class Meta:
        model = Robot
        interfaces = [relay.Node,]
        filter_fields = {
            'robot_name': ['exact',]
        }
    pass


class BlockType(DjangoObjectType):
    """
    单元
    """
    pk = graphene.ID(source='pk')

    class Meta:
        model = Block
        interfaces = [relay.Node,]
        filter_fields = {
            'name': ['exact',]
        }
    pass


class TaskType(DjangoObjectType):
    """
    意图
    """
    pk = graphene.ID(source='pk')
    blocks = graphene.List(BlockType)
    # blocks = DjangoListField(BlockType)

    class Meta:
        model = Task
        interfaces = [relay.Node,]
        filter_fields = {
            'robot_id': ['exact',]
        }
    pass


class SlotType(DjangoObjectType):
    """
    词槽
    """
    pk = graphene.ID(source='pk')

    class Meta:
        model = Slot
        interfaces = [relay.Node,]
        filter_fields = {
            'robot_id': ['exact',]
        }
    pass


class EntityType(DjangoObjectType):
    """
    实体
    """
    pk = graphene.ID(source='pk')

    class Meta:
        model = Entity
        interfaces = [relay.Node,]
        filter_fields = {
            'entity_name': ['exact',]
        }
    pass
