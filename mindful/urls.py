from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('forum/', include('forum.urls')),
    path('news/', include('news.urls')),
    path('doc/', include('docdash.urls')),
    path('chat/', include('livechat.urls')),
    path('events/', include('events.urls')),
    path('contacts/', include('contact.urls')),
    path('location/', include('location.urls')),
    path('analyse/', include('socialanalysis.urls')),
    path('questionaire/', include('questionaire.urls')),
    path('dash/', include('patientdata.urls')),
    path('appointment/', include('appointment.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
