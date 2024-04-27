from django.urls import path
from account import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.user_login, name='login'),
    path('login_eng/', views.user_login, name='login_eng'),
    path('signup/', views.user_signup, name='signup'),
    path('signup_eng/', views.user_signup, name='signup_eng'),
    path('logout/', views.user_logout, name='logout'),
    path('fpv/', views.fpv, name='fpv'),
]

