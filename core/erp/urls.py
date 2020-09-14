#Django
from django.urls import path
from core.erp import views

urlpatterns = [
    path('',views.frontpage, name='base'),
    path('client/',views.client, name='client'),
    path('product/',views.product, name='product'),
  
] 
