from django.db import models
from django.conf import settings


class PatientData(models.Model):

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # socialdata = models.ForeignKey()
    anxiety_quiz_score = models.IntegerField()
    depression_quiz_score = models.IntegerField()
    current_medications = models.CharField(max_length=100)
    # chatbot_data = models.

    def __str__(self):
        return self.patient.username


class FoodData(models.Model):

    consumption = models.IntegerField(choices=range(1, 10))
    date = models.DateField()
    patient = models.ForeignKey(PatientData, on_delete=models.CASCADE)


class PressureData(models.Model):

    data = models.IntegerField()
    patient = models.ForeignKey(
        PatientData, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.patient.username + ':' + str(date)


class SleepData(models.Model):

    patient = models.ForeignKey(PatientData, on_delete=models.CASCADE)
    light = models.IntegerField()
    deep = models.IntegerField()
    rem = models.IntegerField()
    awake = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.patient.username + ':' + str(date)
