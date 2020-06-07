from sys import path

from django.urls import path
from . import views


urlpatterns = [

    path('', views.login, name='home-page'),
    path('register/', views.register, name='user-register'),
    path('view-employees/',views.viewemployees,name="view-employees")
 ]