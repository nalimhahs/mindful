from django.db import models
from django.conf import settings


class PatientData(models.Model):

    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # socialdata = models.ForeignKey()
    # anxiety_quiz = models.ForeignKey()
    # depression_quiz = models.ForeignKey()
    current_medications = models.CharField(max_length=100)
    # chatbot_data = models.
    # pressure_data = models.CharField()
    # food_data = models.ForeignKey()

    def __str__(self):
        return self.patient.first_name


class SleepData(models.Model):

    patient = models.ForeignKey(PatientData, on_delete=models.CASCADE)
    light = models.IntegerField()
    deep = models.IntegerField()
    rem = models.IntegerField()
    awake = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.date