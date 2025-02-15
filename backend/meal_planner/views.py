from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

# Create your views here.
class IngredientView(APIView):
    def get(self):
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'result': 'Ingredient successfully added'},
                status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

