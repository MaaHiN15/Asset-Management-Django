from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('users/list', views.userList, name='userList'),    
    path('users/add',  views.userAdd),    
    path('users/edit', views.userEdit),    
    path('users/delete', views.userDelete),    
    path('labels/list',views.labelList, name='labelList'),    
    path('labels/add', views.labelAdd),
    path('labels/delete',views.labelDelete),    
    path('stocks/list',views.stockList),    
    path('stocks/add', views.stockAdd),    
    path('stocks/edit',views.stockEdit),    
    path('bills/list', views.billList),    
    path('bills/add',  views.billAdd),    
    path('bills/edit', views.billEdit),    
       
]