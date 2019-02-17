from django.shortcuts import render
from .models import FrontPage
from news.models import News
from catalog.models import Catalog
from recipes.models import Recipes
from django.template.response import TemplateResponse

def home(request):
    frontPage = FrontPage.objects.filter(title="frontpage").all()[:1].get()
    # frontPage = [item[0] for item in frontPage.all]
    catalog = Catalog.objects.all()[:3]
    news = News.objects.order_by('-id').all()[:2]
    recipes = Recipes.objects.all()[:3]
    return render(request, 'frontpage/frontpage.html', {'frontpage': frontPage , 'catalog' : catalog , "news" : news , 'recipes' : recipes })

def getentity(request):
    entity_type = request.POST.get('entity_type')
    entity_id = request.POST.get('entity_id')
    if entity_type == 'product' :
        product = Catalog.objects.filter(id__exact=int(entity_id)).get()
        response = TemplateResponse(request, 'partials/product_popup.html', {'product': product})
        return response
    if entity_type == 'news' :
        news =    News.objects.filter(id__exact=int(entity_id)).get()
        response = TemplateResponse(request, 'partials/news_popup.html', {'news': news})
        return response
    if entity_type == 'recipe' :
        recipe =    Recipes.objects.filter(id__exact=int(entity_id)).get()
        response = TemplateResponse(request, 'partials/recipe_popup.html', {'recipe': recipe})
        return response
