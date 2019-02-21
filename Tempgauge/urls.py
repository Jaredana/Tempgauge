"""Tempgauge URL Configuration

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
from django.urls import path, include
from django.contrib import admin
from temperatures import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path(r'', views.index, name ='index'),
    url(r'^my_logout', views.my_logout, name='my_logout'),
    url(r'^logged', views.logged, name='logged'),
	path(r'welcome', views.welcome, name = 'welcome'),
    url(r'^welcome/schools/Sabin/refreshdetail.html$', views.refreshdetail, name='getdata'),
    url(r'^welcome/schools/Sabin/refreshdetail.html/download$', views.download_data, name='download_data'),
    url(r'^gotodetail', views.gotodetail, name='gotodetail'),
	path(r'welcome/schools/<school>/index.html$', views.detail, name='school'),
	#url(r'index', views.index, name='index'),
]
