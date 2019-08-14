"""recipease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "recipease"

urlpatterns = [
    path('list_recipes/', views.list_recipes, name="list_recipes"),
    
    # path('', views.index, name="index"),
    path('list_filtered_recipes/<search_query>', views.list_filtered_recipes, name="list_filtered_recipes"),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
