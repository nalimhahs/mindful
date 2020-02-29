from django.urls import path
from .views import *

urlpatterns = [
    path('', ListAllThreadsView.as_view(), name='all-threads'),
    path('new', CreateNewThreadView.as_view(), name='new-thread'),
    path('<int:pk>', ShowThreadView.as_view(), name='show-thread'),
    # path('<int:pk>/add', CreatePostView.as_view(), name='create-post')
]
