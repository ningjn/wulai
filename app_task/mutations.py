import graphene
from django.utils import timezone
from graphene import relay

from app_task.models import App, Robot
from app_task.types import AppType, RobotType


class AppInput(graphene.InputObjectType):
    id = graphene.ID()
    app_name = graphene.String()  # '名称'
    app_logo = graphene.String()  # '图标'
    app_remark = graphene.String()  # '备注'
    app_hash = graphene.String()  # 'Hash'
    app_key = graphene.String()  # 'Key'
    pass


class AppMutation(relay.ClientIDMutation):
    class Input:
        obj = AppInput(required=True)

    app = graphene.Field(AppType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        if obj.get('id') is None:
            new_obj = App.objects.create(
                app_name=obj.get('app_name', ''),
                app_logo=obj.get('app_logo', ''),
                app_remark=obj.get('app_remark', ''),
                app_hash=obj.get('app_hash', ''),
                app_key=obj.get('app_key', ''),
            )
        else:
            new_obj, flag = App.objects.get_or_create(pk=obj.get('id'))
            new_obj.app_name = obj.get('app_name', '')
            new_obj.app_logo = obj.get('app_logo', '')
            new_obj.app_remark = obj.get('app_remark', '')
            new_obj.db_insert_time = timezone.now()
            new_obj.app_hash = obj.get('app_hash', '')
            new_obj.app_key = obj.get('app_key', '')
            new_obj.save()

        return AppMutation(app=new_obj)

    pass


class RobotInput(graphene.InputObjectType):
    id = graphene.ID()
    robot_name = graphene.String()  # 名称
    robot_logo = graphene.String()  # 图标
    robot_detail = graphene.String()  # 描述
    robot_status = graphene.Int()  # 状态

    robot_ttl = graphene.Int()  # 闲置等待时长
    odst_threshold = graphene.Float()  # 智能填槽阈值

    pos_status = graphene.Int()  # 自动添加预置回复
    pos_num = graphene.Int()  # 推荐个数
    pos_source = graphene.String()  # 推荐源

    goback_action = graphene.Int()  # 是否可以回退
    exit_action = graphene.Int()  # 是否主动退出
    exit_rsp_mode = graphene.Int()  # 退出响应模式

    app_id = graphene.BigInt()  # 应用id
    pass


class RobotMutation(relay.ClientIDMutation):
    class Input:
        obj = RobotInput(required=True)
    
    robot = graphene.Field(RobotType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, obj):
        if obj.get('id') is None:
            new_obj = Robot.objects.create(
                robot_name=obj.get('robot_name', ''),
                robot_logo=obj.get('robot_logo', ''),
                robot_detail=obj.get('robot_detail', ''),
                robot_status=obj.get('robot_status', 0),

                robot_ttl=obj.get('robot_ttl', 0),
                odst_threshold=obj.get('odst_threshold', 0),

                pos_status=obj.get('pos_status', 0),
                pos_num=obj.get('pos_num', 0),
                pos_source=obj.get('pos_source', ''),

                goback_action=obj.get('goback_action', 0),
                exit_action=obj.get('exit_action', 0),
                exit_rsp_mode=obj.get('exit_rsp_mode', 0),

                app_id=obj.get('app_id', 0),
            )
        else:
            new_obj, flag = Robot.objects.get_or_create(pk=obj.get('id'))
            new_obj.robot_name=obj.get('robot_name', '')
            new_obj.robot_logo=obj.get('robot_logo', '')
            new_obj.robot_detail=obj.get('robot_detail', '')
            new_obj.robot_status=obj.get('robot_status', 0)

            new_obj.robot_ttl=obj.get('robot_ttl', 0)
            new_obj.odst_threshold=obj.get('odst_threshold', 0)

            new_obj.pos_status=obj.get('pos_status', 0)
            new_obj.pos_num=obj.get('pos_num', 0)
            new_obj.pos_source=obj.get('pos_source', '')

            new_obj.goback_action=obj.get('goback_action', 0)
            new_obj.exit_action=obj.get('exit_action', 0)
            new_obj.exit_rsp_mode=obj.get('exit_rsp_mode', 0)

            new_obj.app_id=obj.get('app_id', 0)
            new_obj.save()

        return AppMutation(app=new_obj)
    pass
