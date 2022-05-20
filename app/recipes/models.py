from django.db import models


class IngredientModel(models.Model):
    title = models.CharField(max_length=20, help_text='Ingredient title')
    measure_unit = models.CharField(max_length=4, help_text='Measure unit')
    amount = models.IntegerField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class RecipeModel(models.Model):
    title = models.CharField(max_length=20, help_text='Recipe title')
    desc = models.CharField(max_length=250, help_text='Recipe description')
    ingredients = models.ManyToManyField(IngredientModel)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
