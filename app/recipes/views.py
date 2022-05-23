from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import RecipeModel


def index(request):
    latest_recipes = RecipeModel.objects.order_by('title')[:5]
    context = {'latest_recipes': latest_recipes}
    return render(request, 'recipes/index.html', context)


def detail(request, recipes_id):
    recipe = get_object_or_404(RecipeModel, pk=recipes_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})
