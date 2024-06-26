"""
URL configuration for EastFenceFlower project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static

from EastFenceFlower import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('login.urls'), name='login about'),
                  # new
                  path('', include('users.urls'), name='user about'),
                  path('', include('orders.urls'), name='order about'),
                  path('', include('goods.urls'), name='goods about'),
                  path('', include('flowers.urls'), name='flower about'),
                  path('', include('manager.urls'), name='manager about'),
                  path('', include('operate.urls'), name='operate about'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
