from django.urls import path, include

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # done
    path('confirm/', views.confirm, name='confirm'),  # done
    path('login/', views.login_page, name='login'),  # todo
    path('logout/', views.logout_view, name='logout'),  # todo
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('password_reset/', views.reset_password_get_email, name='password_reset'),  # done
    path('reset/<uidb64>/<token>/', views.change_password_from_reset, name='password_reset_confirm'),  # done
    path('importxml/', views.importxml, name='importxml'),  # TEMPORARIO
    path("profile/", views.profile, name="profile"),
    path('createquiz/', include('quiz.urls', namespace='quiz')),
]
# /<uidb64>/<token>/
