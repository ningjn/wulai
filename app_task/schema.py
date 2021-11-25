from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from app_task.mutations import AppMutation, RobotMutation
from app_task.types import AppType, RobotType


class Query(object):
    app = relay.Node.Field(AppType)
    all_apps = DjangoFilterConnectionField(AppType)

    robot = relay.Node.Field(RobotType)
    all_robots = DjangoFilterConnectionField(RobotType)


class Mutation(object):
    upsert_app = AppMutation.Field()
    upsert_robot = RobotMutation.Field()
    pass
