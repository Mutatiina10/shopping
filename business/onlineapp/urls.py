from django.urls import path
from .import views



#these are the app URLs 

urlpatterns = [
    #path('', views.index, name='index'),
    path('',views.products, name='product_list'),
]