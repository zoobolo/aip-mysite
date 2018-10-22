"""mainsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.template import loader
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
#    url(r'^$', views.index, name='index'),
#    url(r'^$', views.home, name='home'),
#    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),

    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),  
    url(r'^home/$', views.index, name='home'),  
#    url(r'^index/$', views.index, name='home'),  
#    url(r'^register/$', views.register, name='register'), 
#    url(r'^airport/$', views.getAirportListView.as_view(), name='airport_list'),
]