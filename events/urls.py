from django.urls import path
from . import views

urlpatterns = [
    path('', views.allevents, name='allevents'),
    path('<int:events_id>/', views.detail, name='detail'),
]
