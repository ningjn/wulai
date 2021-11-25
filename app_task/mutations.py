import graphene
from django.utils import timezone
from graphene import relay

from app_task.models import App
from app_task.types import AppType


class AppMutation(relay.ClientIDMutation):
    class Input:
        id = graphene.ID()
        app_name = graphene.String()  # '名称'
        app_logo = graphene.String()  # '图标'
        app_remark = graphene.String()  # '备注'
        app_hash = graphene.String()  # 'Hash'
        app_key = graphene.String()  # 'Key'

    app = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **obj):
        if obj.get('id') is None:
            new_obj = App.objects.create(
                app_name=obj.get('app_name', ''),
                app_logo=obj.get('app_logo', ''),
                app_remark=obj.get('app_remark', ''),
                app_hash=obj.get('app_hash', ''),
                app_key=obj.get('app_key', ''),
            )
        else:
            new_obj, flag = App.objects.get_or_create(pk=obj.get('id', 0))
            new_obj.app_name = obj.get('app_name', '')
            new_obj.app_logo = obj.get('app_logo', '')
            new_obj.app_remark = obj.get('app_remark', '')
            new_obj.db_insert_time = timezone.now()
            new_obj.app_hash = obj.get('app_hash', '')
            new_obj.app_key = obj.get('app_key', '')
            new_obj.save()

        return AppMutation(app=new_obj)

    pass
