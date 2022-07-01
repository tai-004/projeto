from django.urls import path
from . import views

urlpatterns = [
    path('', views.template, name="template"),
    path('index/', views.index, name="index"),
    path('historico', views.historico, name="historico"),
    path('agroindrustria', views.agroindrustria, name="agroindrustria"),
    path('agropecuaria', views.agropecuaria, name="agropecuaria"),
    path('informatica', views.informatica, name="informatica"),
    path('hierarquia', views.hierarquia, name="hierarquia"),
    path('engresso', views.engresso, name="engresso"),
    path('contato', views.contato, name="contato"),
    path('desenvolvedores', views.desenvolvedores, name="desenvolvedores"),
    path('superior', views.superior, name="superior"),
]
