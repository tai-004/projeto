from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post, name='post'),
    path('create-post/', views.create_post, name='create_post'),
    
]
