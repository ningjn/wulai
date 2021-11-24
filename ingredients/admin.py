from django.contrib import admin

from ingredients.models import Ingredient, Category


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_editable = ("name", "category")


admin.site.register(Category)
