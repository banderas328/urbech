from .models import Catalog
from django.template.response import TemplateResponse


def getmoreproducts(request):
    product_id = request.POST.get('product_id')
    catalog = Catalog.objects.filter(id__gt=int(product_id))[:2]
    response = TemplateResponse(request, 'partials/catalog.html', {'catalog': catalog})
    return response
