from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage),
    path('logout', views.logoutPage, name = 'logout')
]