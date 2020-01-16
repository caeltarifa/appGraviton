"""appGraviton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from apps.datagen import views
from apps.mapgen import views
from appGraviton.views import principal_presentacion, despues_login, denegar_login

urlpatterns = [
    path('', principal_presentacion, name='principal_presentacion'),
    path('bienvenido/', despues_login, name='despues_login'),
    path('admin/', admin.site.urls),
    path('datagen/',include('apps.datagen.urls')),
    path('datagen/postdetail/<int:pk>/', views.post_detail , name='post_detail'),
    path('mapgen/',include('apps.mapgen.urls')),
    path('obs/',include('apps.obs.urls')),
    path('accounts/login',denegar_login),
]


#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
