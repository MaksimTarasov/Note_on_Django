
from django.urls import path, include
from . import views

urlpatterns = [
  
    path('', views.index),
    path('all_data/', views.data_out),
    path('index_new/', views.CP.as_view())
  
]