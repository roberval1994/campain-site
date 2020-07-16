from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index, name='Index'),
    path('Index.html', views.Index, name='Index'),
    path('about_me.html', views.about_me, name='about_me'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)