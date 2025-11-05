from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('request/new/', views.create_request, name='create_request'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('request/<int:pk>/cancel/', views.cancel_request, name='cancel_request'),
]