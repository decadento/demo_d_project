from django.urls import path
from . import views

urlpatterns = [
  path('start', views.start_quiz_view, name='start'),
  path('get-questions/start', views.get_questions, {'is_start': True}, name='get-questions'),
  path('get-questions', views.get_questions, {'is_start': False}, name='get-questions'),
  path('get-answer', views.get_answer, name='get-answer'),
  path('get-finish', views.get_finish, name='get-finish'),

  path('start_eng', views.start_quiz_view_eng, name='start_eng'),
  path('get-questions_eng/start', views.get_questions_eng, {'is_start': True}, name='get-questions_eng'),
  path('get-questions_eng', views.get_questions_eng, {'is_start': False}, name='get-questions_eng'),
  path('get-answer_eng', views.get_answer_eng, name='get-answer_eng'),
  path('get-finish_eng', views.get_finish_eng, name='get-finish_eng'),
]