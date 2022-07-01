from django.urls import path
from . import views


# namespace
app_name = "file_upload"

urlpatterns = [

  
    # Upload Files Using Model Form
    path('upload2/', views.model_form_upload, name='model_form_upload'),

    # View File List
    path('', views.file_list, name='file_list'),
    path('excluir/<int:id>', views.excluir, name='excluir'),

    path('editar/<int:id>/', views.editar, name='editar'),
    path('<int:id>/', views.detail, name='detail'),
]  