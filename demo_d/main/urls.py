from django.urls import path
from . import views

urlpatterns = [
    path('landing', views.landing, name='landing'),
    path('landing_eng', views.landing_eng, name='landing_eng'),
    path('learn', views.learn, name='learn'),
    path('learn_eng', views.learn_eng, name='learn_eng'),
    path('categories', views.categories, name='categories'),
    path('categories_eng', views.categories_eng, name='categories_eng'),   
]
