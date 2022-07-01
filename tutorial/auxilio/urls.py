from django.urls import path
from . import views

app_name = "auxilio"

urlpatterns = [
    
    path('upload/', views.uploader, name='uploader'),

    path('', views.file_list, name='file_list'),

    path('excluir/<int:id>/', views.excluir, name='excluir'),

    path('editar/<int:id>/', views.editar, name='editar'),

    path('<int:id>/', views.detail, name='detail'),

]