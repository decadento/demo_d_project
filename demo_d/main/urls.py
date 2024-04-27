from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('learn', views.learn, name='learn'),
    path('categories', views.categories, name='categories'),
    path('landing_eng', views.landing_eng, name='landing_eng')
]
