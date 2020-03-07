from django.db import models
from django.conf import settings
from patientdata.models import PatientData
from django.utils import timezone

class Appointment(models.Model):
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor')
    date = models.DateField(default=timezone.now)
    time = models.AutoDateTimeField(default=timezone.now)
    
    