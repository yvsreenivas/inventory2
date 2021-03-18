from django.contrib import admin
from django.urls import path, include
from stocks import views

urlpatterns = [
    path('list_items/', views.list_items, name='list_items'),
    path('add_items/', views.add_items, name='add_items'),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
    path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
    path('issue_items/<str:pk>/', views.issue_items, name="issue_items"),
    path('issue_items2/<str:pk>/', views.issue_items2, name="issue_items2"),
    path('receive_items/<str:pk>/', views.receive_items, name="receive_items"),
    path('parts_create/', views.PartsMasterCreateView.as_view(), name='parts_create'),
    path('parts/', views.PartsMasterListView.as_view(), name='parts'),
    path('part/<int:pk>', views.PartsMasterDetailView.as_view(),
         name='part-detail'),  

]
