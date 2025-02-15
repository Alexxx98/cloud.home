from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .serializers import (
    IngredientSerializer, 
    RecipeSerializer,
    MealPlanSerializer,
)
from .models import (
    Ingredient,
    Recipe,
    MealPlan
)

# Ingredient views
class IngredientListCreate(ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetail(RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


# Recipes views
class RecipesListCreate(ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


# Meal plans views
class MealPlansListCreate(ListCreateAPIView):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer


class MealPlanDetail(RetrieveUpdateDestroyAPIView):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer
