from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test_hall_of_fame, name='halloffame_tests'),
    path('quiz/', views.quiz_hall_of_fame, name='halloffame_quiz'),
]


urlpatterns += staticfiles_urlpatterns()
