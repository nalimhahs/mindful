from django.db import models
from django.conf import settings


class ChatRoom(models.Model):

    patient = models.ForeignKey(settings.AUTH_USER_MODEL)
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return patient.username + ':' + doctor.username


class Chat(models.Model):

    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=500)
