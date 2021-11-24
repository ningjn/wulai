import graphene
from graphene_django.types import DjangoObjectType
from django.utils import timezone

from app_task.models import App


class AppType(DjangoObjectType):
    class Meta:
        model = App


class AppInput(graphene.InputObjectType):
    id = graphene.ID()
    app_name = graphene.String()  # '名称'
    app_logo = graphene.String()  # '图标'
    app_remark = graphene.String()  # '备注'
    app_hash = graphene.String()  # 'Hash'
    app_key = graphene.String()  # 'Key'


class AppMutation(graphene.Mutation):
    class Arguments:
        obj = AppInput(required=True)

    app = graphene.Field(AppType)

    @staticmethod
    def mutate(root, info, obj):
        if obj.get('id') is None:
            new_obj = App.objects.create(
                app_name=obj.app_name,
                app_logo=obj.app_logo,
                app_remark=obj.app_remark,
                app_hash=obj.app_hash,
                app_key=obj.app_key,
            )
        else:
            new_obj, flag = App.objects.get_or_create(pk=obj.id)
            new_obj.app_name = obj.app_name
            new_obj.app_logo = obj.app_logo
            new_obj.app_remark = obj.app_remark
            new_obj.db_insert_time = timezone.now()
            new_obj.app_hash = obj.app_hash
            new_obj.app_key = obj.app_key
            new_obj.save()

        return AppMutation(app=new_obj)

    pass


class Query(object):
    get_task_robots = graphene.List(AppType)

    def resolve_get_task_robots(self, info, **kwargs):
        return App.objects.all()

    pass


class Mutation(object):
    upsert_app = AppMutation.Field()
    pass
