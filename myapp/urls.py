from django.contrib import admin
from django.urls import path,include 
from django.conf.urls import url 
from django.conf import settings
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('backlog/<backlog_id>/',views.backlog,name='backlog'),
    path('forms',views.forms,name='forms'),
    path('',views.home,name='home'),
    path('calendar',views.calendar,name='calendar'),
    path('liste/', views.liste, name='liste'),
    path('maps/', views.maps, name='maps'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)