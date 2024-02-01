from django.urls import path
from . import views

from account.views import (
    SignUpView
)

urlpatterns = [
    path('account/', views.login, name='account'),
    path('login/', views.login, name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]

