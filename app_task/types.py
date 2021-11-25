from graphene_django.types import DjangoObjectType

from app_task.models import App


class AppType(DjangoObjectType):
    class Meta:
        model = App


