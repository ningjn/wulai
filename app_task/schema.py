import graphene

from app_task.models import App
from app_task.mutations import AppMutation
from app_task.types import AppType


class Query(object):
    get_task_robots = graphene.List(AppType)

    def resolve_get_task_robots(self, info, **kwargs):
        return App.objects.all()
    pass


class Mutation(object):
    upsert_app = AppMutation.Field()
    pass
