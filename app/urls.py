from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('users/list', views.userList),    
    path('users/add',  views.userAdd),    
    path('users/edit', views.userEdit),    
    path('labels/list',views.labelList),    
    path('labels/add', views.labelAdd),    
    path('labels/edit',views.labelEdit),    
    path('stocks/list',views.stockList),    
    path('stocks/add', views.stockAdd),    
    path('stocks/edit',views.stockEdit),    
    path('bills/list', views.billList),    
    path('bills/add',  views.billAdd),    
    path('bills/edit', views.billEdit),    
       
]