from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=64, unique=True)
    ingredient_type = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.ingredient_type}, {self.name}'


class Recipe(models.Model):
    name = models.CharField()
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='ingredients'
    )
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
