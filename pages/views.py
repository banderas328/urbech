from django.shortcuts import render
from .models import FrontPage
from news.models import News
from catalog.models import Catalog
from recipes.models import Recipes

def home(request):
    frontPage = FrontPage.objects.filter(title="frontpage").all()[:1].get()
    # frontPage = [item[0] for item in frontPage.all]
    catalog = Catalog.objects.all()[:3]
    news = News.objects.all()[:2]
    recipes = Recipes.objects.all()[:3]
    return render(request, 'frontpage/frontpage.html', {'frontpage': frontPage , 'catalog' : catalog , "news" : news , 'recipes' : recipes })

