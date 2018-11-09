from django.urls import path
from . import views

urlpatterns = [
    path('', views.Principal, name ='estudiantes'),
    path('crear/', views.crear, name ='crear'),
    path('modificar/', views.modificar, name ='modificar')
]