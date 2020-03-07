from django.db import models
from django.conf import settings
from patientdata.models import PatientData
from django.utils import timezone

class Appointment(models.Model):
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='app_patient')
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='app_doctor')
    time = models.DateTimeField(default=timezone.now)
    
    