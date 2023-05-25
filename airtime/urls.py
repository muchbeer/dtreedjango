from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_airtime, name='view_airtime'),
    path('add/', views.add, name='add'),
    path('upload', views.upload, name='upload')
]