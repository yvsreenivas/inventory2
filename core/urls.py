from django.urls import path, include
from django.conf.urls import url
from core import views

app_name = "core"

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('', views.home, name='home'),
]
