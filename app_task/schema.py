from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from app_task.mutations import AppMutation
from app_task.types import AppType


class Query(object):
    app = relay.Node.Field(AppType)
    all_apps = DjangoFilterConnectionField(AppType)


class Mutation(object):
    upsert_app = AppMutation.Field()
    pass
