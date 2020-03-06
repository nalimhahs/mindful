from django.urls import path
from . import views

urlpatterns = [
    path('', views.allquestion, name='question'),
]
