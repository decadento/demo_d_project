from django.urls import path
from account import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.index, name='landing'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('tac_med/', views.index, name='tac_med'),
]

