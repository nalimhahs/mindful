from django.db import models
from django.conf import settings

# Create your models here.


class Thread(models.Model):

    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=100, blank=True, null=True)


class Post(models.Model):

    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    hidden = models.BooleanField(default=False)
