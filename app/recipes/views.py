from django.shortcuts import render
from django.http import HttpResponse
from .models import RecipeModel

def index(request):
    latest_recipes = RecipeModel.objects.order_by('title')[:5]
    output = ', '.join([r.desc for r in latest_recipes])
    return HttpResponse(output)
    
def details(request, recipe_id):
    return HttpResponse('Details')