from graphene import Node
import graphene
from graphene_django.types import DjangoObjectType

from ingredients.models import Category, Ingredient


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (Node,)
        fields = "__all__"
        filter_fields = ["name", "ingredients"]


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        interfaces = (Node,)
        fields = "__all__"
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "notes": ["exact", "icontains"],
            "category": ["exact"],
            "category__name": ["exact"],
        }


class Query(object):
    # category = Node.Field(CategoryNode)
    # all_categories = CategoryNode

    # ingredient = Node.Field(IngredientNode)
    # all_ingredients = IngredientNode
    all_ingredients = graphene.List(IngredientNode)
    ingredient = graphene.Field(IngredientNode, key_id=graphene.Int())

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()

    def resolve_ingredient(self, info, key_id):
        return Ingredient.objects.get(pk=key_id)
