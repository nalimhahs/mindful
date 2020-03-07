from django.db import models
from django.conf import settings


class PatientData(models.Model):

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # socialdata = models.ForeignKey()
    anxiety_quiz_score = models.IntegerField(blank=True, null=True)
    depression_quiz_score = models.IntegerField(blank=True, null=True)
    lifestyle_quiz_score = models.IntegerField(blank=True, null=True)
    current_medications = models.CharField(max_length=100, blank=True, null=True)
    # chatbot_data = models.

    def __str__(self):
        return self.patient.username


class FoodData(models.Model):

    choices = ((1, 'Very poor'), (2, 'poor'), (3, 'fair'), (4, 'good'), (5, 'very good'))
    appetite = models.IntegerField(choices=choices)
    date = models.DateField()
    patient = models.ForeignKey(PatientData, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.patient.username + ':' + str(self.date)


class PressureData(models.Model):

    sys = models.IntegerField()
    dia = models.IntegerField()
    patient = models.ForeignKey(
        PatientData, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.patient.patient.username + ':' + str(self.date)


class SleepData(models.Model):

    patient = models.ForeignKey(PatientData, on_delete=models.CASCADE)
    light = models.IntegerField()
    deep = models.IntegerField()
    rem = models.IntegerField()
    awake = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.patient.patient.username + ':' + str(self.date)
