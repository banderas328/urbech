from .models import Recipes
from django.template.response import TemplateResponse


def getmorerecipes(request):
    recipe_id = request.POST.get('recipe_id')
    recipes = Recipes.objects.filter(id__gt=int(recipe_id))[:3]
    response = TemplateResponse(request, 'partials/recipes.html', {'recipes': recipes})
    return response
