from django.shortcuts import render, redirect
from .models import PatientData, SleepData, FoodData, PressureData
from forum.models import Thread, Post
from django.contrib.auth.decorators import login_required
from users.models import CustomUser as User
from livechat.models import ChatRoom

@login_required
def getPatientDataView(request):

    patientData = PatientData.objects.get(patient=request.user)
    sleepData = SleepData.objects.filter(patient=patientData)
    foodData = FoodData.objects.filter(patient=patientData)
    pressureData = PressureData.objects.filter(patient=patientData)
    threads = Thread.objects.filter(
        post__in=Post.objects.filter(user=request.user))
    chats = ChatRoom.objects.filter(patient=request.user)
    return render(request, 'patientdata/data-dash.html', {'patientData': patientData, 'sleepData': sleepData, 'foodData': foodData, 'pressureData': pressureData, 'threads': threads, 'chats': chats})


def getAllDoctorsView(request):

    docs = User.objects.filter(is_doc=True)
    return render(request, 'patientdata/doclist.html', {'docs': docs, })


def sendRequestToDoc(request, doc_id):

    doc = User.objects.get(pk=doc_id)
    chat, created = ChatRoom.objects.get_or_create(doctor=doc, patient=request.user, defaults={})
    if not created:
        return redirect('chat-view', room=chat.id)
    return render(request, 'patientdata/req-success.html', {'doc': doc, })

