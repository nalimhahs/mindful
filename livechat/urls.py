from django.urls import path
from .views import chatView

urlpatterns = [
    path('<int:room>', chatView, name='chat-view')
]
