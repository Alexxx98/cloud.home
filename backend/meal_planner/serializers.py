from rest_framework.serializers import ModelSerializer
from .models import MealPlan, Recipe, Ingredient


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class MealPlanSerializer(ModelSerializer):
    class Meta:
        model = MealPlan
        fields = '__all__'


