from django.urls import path
from .views import *

urlpatterns = [
    path('dash/', doctorMainDashboard, name='doc-main-dash'),
]
