"""kahucsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from kahucsite import views

handler404 = 'kahucsite.views.my_custom_page_not_found_view'
handler500 = 'kahucsite.views.my_custom_error_view'
handler403 = 'kahucsite.views.my_custom_permission_denied_view'
handler400 = 'kahucsite.views.my_custom_bad_request_view'

urlpatterns = [
    path('', views.home_redirect),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('users/', include("users.urls")),
    path('create_test/', include("create_test.urls")),
    path('createquiz/', include("quiz.urls")),
    path('solve_test/', include("solve_test.urls")),
    path('review_quiz/', include("review_quiz.urls")),
    path('results/', include('test_results.urls')),
    path('historic_quiz/', include('historic_quiz.urls')),
    path('halloffame/', include('hall_of_fame.urls')),
    path('about_us/', views.about_us, name='about_us'),
]
