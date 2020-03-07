from django.db import models
from django.conf import settings


class QuestionGroup(models.Model):

    title = models.CharField(max_length=20)
    desc = models.TextField(max_length=200)

    def __str__(self):
        return self.title


class Question(models.Model):

    group = models.ForeignKey(QuestionGroup, on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self):
        return self.group.title + ':' + self.question[:10]


class Answer(models.Model):

    CHOICES = [(2, 'Never'),
               (1, 'Rarely'),
               (0, 'Sometimes'),
               (-1, 'Often'),
               (2, 'Very Often'), ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField(choices=CHOICES)

    class Meta:
        unique_together = ('user', 'question')
