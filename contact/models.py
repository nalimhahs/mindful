from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=30)
    address=models.TextField(max_length=60)
    phoneno=models.IntegerField()

    def __str__(self):
        return self.name

