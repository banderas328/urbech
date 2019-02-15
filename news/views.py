from django.shortcuts import render
from .models import News
from django.core import serializers
from django.shortcuts import render
from django.template.response import TemplateResponse


def getmorenews(request):
    news_id = request.POST.get('news_id')
    news = News.objects.filter(id__gt=news_id)[:2]
    response = TemplateResponse(request, 'partials/news.html', {'news': news})
    return response