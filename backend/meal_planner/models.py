from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=64, unique=True)
    ingredient_type = models.CharField(max_length=64)
    calories = models.IntegerField(default=0)
    protein  = models.DecimalField(defualt=0.0, decimal_places=1)
    carbohydrate = models.DecimalField(default=0.0, decimal_places=1)
    fat = models.DecimalField(default=0.0, decimal_places=1)

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    name = models.CharField()
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='ingredients'
    )
    servings = models.IntegerField(default=1)
    content = models.TextField()

    def __str__(self):
        return f'{self.name}'
    

class MealPlan(models.Model):
    name=models.CharField(max_length=64)
    recipes = models.ManyToManyField(
        Recipe,
        related_name='recipes'
    )

    def __str__(self):
        return f'{self.name}'
