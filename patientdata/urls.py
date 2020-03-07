from django.urls import path
from .views import getPatientDataView, getAllDoctorsView, sendRequestToDoc

urlpatterns = [
    path('', getPatientDataView, name='data-dash'),
    path('doclist', getAllDoctorsView, name='doclist-dash'),
    path('doclist/book/<int:doc_id>', sendRequestToDoc, name='docreq-dash'),
]
