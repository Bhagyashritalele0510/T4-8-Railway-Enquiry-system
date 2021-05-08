from django.contrib import admin
from django.urls import path,include
import features
from . import views
app_name='home'
urlpatterns = [
    path('',views.home,name="hom" ),
     path('search/',features.views.search),
    path('search/trains',features.views.getTrains),
    path('schedule/',features.views.schedule),
    path('schedule/trains',features.views.getTinfo),
    path('pnr/',features.views.pnr,name="pnr"),
    #path('logout/',views.logout ),
    ]