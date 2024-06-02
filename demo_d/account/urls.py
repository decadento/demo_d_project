

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
    path('turniket/', views.turniket, name='turniket'),
    path('turniket_eng/', views.turniket_eng, name='turniket_eng'),
    path('at4/', views.at4, name='at4'),
    path('at4_eng/', views.at4_eng, name='at4_eng'),
    path('m2a2/', views.m2a2, name='m2a2'),
    path('m2a2_eng/', views.m2a2_eng, name='m2a2_eng'),
    path('osint/', views.osint, name='osint'),
    path('osint_eng/', views.osint_eng, name='osint_eng'),
    path('emergency_pack/', views.emergency_pack, name='emergency_pack'),
    path('emergency_pack_eng/', views.emergency_pack_eng, name='emergency_pack_eng'),
]

