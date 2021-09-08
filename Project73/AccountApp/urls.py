from django.urls import path
from .views import registerview,logoutview,loginview

urlpatterns=[
    path('register/',registerview,name='register'),
    path('login/',loginview,name='login'),
    path('logout/',logoutview,name='logout')


]