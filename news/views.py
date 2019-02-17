from .models import News
from django.template.response import TemplateResponse


def getmorenews(request):
    news_id = request.POST.get('news_id')
    news = News.objects.filter(id__lt=int(news_id)).order_by('-id')[:2]
    response = TemplateResponse(request, 'partials/news.html', {'news': news})
    return response