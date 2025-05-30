"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),  # Ana sayfa URL'si
    path('referanslar/', views.portfolio, name='portfolio'),  # referanslar sayfası URL'si
    path('kariyer/', views.contact, name='contact'),
    path('hizmetlerimiz/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('hakkimizda/', views.about, name='about'),
    path('vizyon-misyon/', views.vision, name='vision'),
    path('blog1/', views.blog1, name='blog1'),
    path('blog2/', views.blog2, name='blog2'),
    path('blog3/', views.blog3, name='blog3'),
]
