from django.shortcuts import render
from .models import PatientData, SleepData, FoodData, PressureData
from forum.models import Thread, Post
from django.contrib.auth.decorators import login_required

@login_required
def getPatientDataView(request):

    patientData = PatientData.objects.get(patient=request.user)
    sleepData = SleepData.objects.filter(patient=patientData)
    foodData = FoodData.objects.filter(patient=patientData)
    pressureData = PressureData.objects.filter(patient=patientData)
    threads = Thread.objects.filter(post__in=Post.objects.filter(user=request.user))

    return render(request, 'patientdata/data-dash.html', {'patientData': patientData, 'sleepData': sleepData, 'foodData': foodData, 'pressureData': pressureData, 'threads': threads})
