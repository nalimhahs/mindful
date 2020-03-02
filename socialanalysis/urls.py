from django.urls import path
from .views import analyseSocialsView

urlpatterns = [
    path('', analyseSocialsView, name='analyse'),
]
