from django.urls import path
from .views import add_product,show_product,update_product,delete_product,home_view


urlpatterns=[
    path('add/',add_product,name='add'),
    path('show/',show_product,name='show'),
    path('update/<int:id>/',update_product,name='update'),
    path('delete/<int:id>/',delete_product,name='delete'),
    path('',home_view,name='home')
]