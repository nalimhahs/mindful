from django.urls import path
from . import views

urlpatterns = [
    path('<int:qg>', views.startQuiz, name='start-view'),
    path('<int:qg>/<int:pk>', views.getAnswer, name='answer-view'),
    path('<int:qg>/complete', views.startQuiz, name='complete-view'),
]
