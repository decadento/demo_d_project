from django.urls import path
from account import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('landing', views.landing, name='landing'),
    path('landing_eng', views.landing_eng, name='landing_eng'),
    path('login/', views.user_login, name='login'),
    path('login_eng/', views.user_login_eng, name='login_eng'),
    path('signup/', views.user_signup, name='signup'),
    path('signup_eng/', views.user_signup_eng, name='signup_eng'),
    path('logout/', views.user_logout, name='logout'),
    path('logout_eng/', views.user_logout_eng, name='logout_eng'),
    path('fpv/', views.fpv, name='fpv'),
    path('fpv_eng/', views.fpv_eng, name='fpv_eng'),
]

