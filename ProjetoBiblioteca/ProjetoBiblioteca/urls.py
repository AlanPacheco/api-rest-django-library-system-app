"""ProjetoBiblioteca URL Configuration

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
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from biblioteca_app.api.viewsets import EmprestimoViewSet
from biblioteca_app.api.viewsets import UsuarioViewSet
from biblioteca_app.api.viewsets import LivroViewSet
from biblioteca_app.api.viewsets import SessaoViewSet


router = routers.DefaultRouter()
router.register(r'emprestimos', EmprestimoViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'livros', LivroViewSet)
router.register(r'sessoes', SessaoViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
