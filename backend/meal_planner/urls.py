from django.urls import path
from .views import (
    IngredientListCreate,
    IngredientDetail,
    RecipesListCreate,
    RecipeDetail,
    MealPlansListCreate,
    MealPlanDetail
)


urlpatterns = [
    path('ingredients/', IngredientListCreate.as_view()),
    path('ingredients/<int:pk>', IngredientDetail.as_view()),
    path('recipes/', RecipesListCreate.as_view()),
    path('recipes/<int:pk>', RecipeDetail.as_view()),
    path('meal_plans/', MealPlansListCreate.as_view()),
    path('meal_plans/<int:pk>', MealPlanDetail.as_view()),
]