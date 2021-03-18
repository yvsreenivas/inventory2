from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'school_indents'

urlpatterns = [
	path('create/<int:indent_no>/', views.IndentMasterDetailView.as_view(), name='indentmaster_detail'),
    path('create/', views.IndentMasterCreate.as_view(), name='indentmaster_create'),
	path('', views.HomepageView.as_view(), name='homepage'),
]
