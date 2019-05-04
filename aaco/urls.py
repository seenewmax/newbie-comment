"""aaco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
import event.views


urlpatterns = [
    path('', views.main, name='main'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('help/', views.help, name='help'),
    path('host_mogakco/', views.host_mogakco, name='host_mogakco'),
    path('show_by_region/', views.show_by_region, name='show_by_region'),
    path('show_by_subject/', views.show_by_subject, name='show_by_subject'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('somewhere/', views.somewhere, name='somewhere'),
    path('event/main', event.views.main, name='event_main'),
    path('event/<int:post_id>', event.views.show, name='show'),
    path('event/new', event.views.new, name='new'),
    path('event/postcreate', event.views.postcreate, name='postcreate'),
    path('event/commentcreate/<int:post_id>', event.views.commentcreate, name='commentcreate'),
]

