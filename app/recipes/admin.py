from django.contrib import admin
from .models import RecipeModel, IngredientModel


class IngredientModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'measure_unit', 'amount')
    search_fields = ['title']


class RecipeModelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                 {'fields': ['title']}),
        ('Recipe description', {'fields': ['desc'], 'classes': ['collapse']}),
        ('Ingredients',        {'fields': ['ingredients']}),
    ]
    list_display = ('title', 'desc')
    search_fields = ['title', 'desc']


admin.site.register(RecipeModel, RecipeModelAdmin)
admin.site.register(IngredientModel, IngredientModelAdmin)
