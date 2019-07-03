"""dropkindle URL Configuration

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
from django.conf.urls import url
from dk_user import views as user_views
from dk_dropbox import views as dropbox_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/', user_views.dk_index),
    url(r'^login/', user_views.dk_login),
    url(r'^register/', user_views.dk_register),
    url(r'^logout/', user_views.dk_logout),
    url(r'^start-oauth2/', dropbox_views.dropbox_auth_start),
    url(r'^oauth2/', dropbox_views.dropbox_auth_finish),
]

