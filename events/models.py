from django.db import models
from django.conf import settings


class Events(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
