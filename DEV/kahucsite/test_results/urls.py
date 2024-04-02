from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

# para aceder à pagina usar results/
urlpatterns = [
    path('', views.test_results, name='viewresults'),
]


urlpatterns += staticfiles_urlpatterns()
