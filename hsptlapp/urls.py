from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
       path('',views.home,name='home'),
       path('about',views.about,name='about'),
       path('special',views.special,name='special'),
       path('gal',views.gal,name='gal'),
       path('con',views.con,name='con'),
       path('homes',views.homes,name='homes'),
       path('log',views.log,name='log'),
       path('sign',views.sign,name='sign'),
       path('out',views.out,name='out'),
       
    
]
