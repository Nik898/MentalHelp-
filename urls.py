"""djangoProject4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import Models_acm
from . import visualization


urlpatterns = [
    path('', Models_acm.homepage, name='HomePage'),
    path('test/', Models_acm.home, name='test_home'),
    path('result/', Models_acm.calculate, name='test_result'),
    path('graphs/', visualization.visual, name='Visualization'),
    path('graphs1/', Models_acm.frequency, name='Frequency'),
    path('graphs2/', visualization.waa, name='wa'),
    path('graphs3/', visualization.graph3, name='graphs3'),
    path('graphs4/', visualization.graph4, name='graphs4'),
    path('graphs5/', visualization.graph5, name='graphs5'),
]
