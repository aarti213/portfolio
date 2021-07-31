from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from myportfolio import views
urlpatterns = [
    path("",views.index,name='home'),
    path("blog.html",views.blog,name='blog')
]