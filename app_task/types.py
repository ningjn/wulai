from graphene_django.types import DjangoObjectType
from graphene import relay

from app_task.models import App, Robot


class AppType(DjangoObjectType):
    """
    应用
    """
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
    class Meta:
        model = Robot
        interfaces = [relay.Node,]
        filter_fields = {
            'robot_name': ['exact',]
        }
    pass
