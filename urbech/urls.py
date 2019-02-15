from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import pages.views
import news.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pages.views.home, name='home'),
    path('getmorenews', news.views.getmorenews, name='getmorenews'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
