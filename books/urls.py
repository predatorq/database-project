from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('reg/', views.reg, name='check'),
    path('add/', views.add),
    path('delete/', views.delete),
    path('change/', views.change),
    path('check/', views.check),
    

]