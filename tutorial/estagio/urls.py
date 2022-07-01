from django.urls import path
from . import views

app_name = "estagio"

urlpatterns = [
    
    path('upload3/', views.postar, name='postar'),

    path('', views.index, name='index'),

    path('excluir/<int:id>/', views.excluir, name='excluir'),

    path('editar/<int:id>/', views.editar, name='editar'),

    path('<int:id>/', views.detail, name='detail'),

]