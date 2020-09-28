#Django
from django.urls import path
from core.erp.views import *

urlpatterns = [
    path('', frontpage, name='base'),
    path('client/', client, name='client'),
    path('product/', product, name='product'),
    path('category/', CategoryList.as_view(), name='category'),
  
] 
 