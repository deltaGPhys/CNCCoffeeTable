"""table URL Configuration

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
#import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from . import views

app_name = 'coffee'
urlpatterns = [
    url(r'^$',view=views.IndexView,name='index'),
    url(r'^addPattern/$',view=views.AddPatternView,name='addPattern'),
    url(r'^loadPattern/$',view=views.LoadPatternView,name='loadPattern'),
    url(r'^editPattern/$',view=views.EditPatternView,name='editPattern'),
    url(r'^countPatterns/$',view=views.CountPatternsView,name='countPatterns'),
    url(r'^openGcode/$',view=views.OpenGcodeView,name='openGcode'),
    url(r'^sendLine/$',view=views.SendLineView,name='sendLine'),

    ]
