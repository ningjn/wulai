import ingredients.schema
import graphene
from graphene_django.debug import DjangoDebug

import app_task.schema


class Query(
    ingredients.schema.Query,
    app_task.schema.Query,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(
    app_task.schema.Mutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)


