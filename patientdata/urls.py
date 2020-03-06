from django.urls import path
from .views import getPatientDataView

urlpatterns = [
    path('', getPatientDataView, name='data-dash'),
]
