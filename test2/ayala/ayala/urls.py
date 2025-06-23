"""
URL configuration for ayala project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from list_of_helps.views import index
from list_of_helps import views


from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('subscribe/', views.subscribe_view, name='subscribe'),
    path('subscribe/product.html', views.product_detail, name='product'),
    path('subscribe/product2.html', views.product_detail2, name='product2'),
    path('subscribe/product3.html', views.product_detail3, name='product3'),
    path('subscribe/product4.html', views.product_detail4, name='product4'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
