from django.shortcuts import render
from .models import PatientData, SleepData, FoodData, PressureData


def getPatientDataView(request):

    patientData = PatientData.objects.filter(patient=request.user)
    sleepData = SleepData.objects.filter(patient=patientData)
    foodData = FoodData.objects.filter(patient=patientData)
    pressureData = PressureData.objects.filter(patient=patientData)

    return render(request, 'patientdata/data-dash.html', {'patientData': patientData, 'sleepData': sleepData, 'foodData': foodData, 'pressureData': pressureData})
