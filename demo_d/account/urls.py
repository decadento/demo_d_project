from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.login, name='account'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')
]

