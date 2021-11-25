from graphene_django.types import DjangoObjectType
from graphene import relay

from app_task.models import App


class AppType(DjangoObjectType):
    class Meta:
        model = App
        interfaces = (relay.Node,)
        filter_fields = {
            'app_name': ['exact', 'icontains', 'istartswith'],
        }

