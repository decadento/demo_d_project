from django.urls import path
from account import views
from django.contrib.auth import views as auth_views
from account.views import SignUpView

from account.views import (
    SignUpView
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

