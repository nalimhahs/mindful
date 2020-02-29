from django.db import models
from django.conf import settings


class News(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,)
    body = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
