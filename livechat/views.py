from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .forms import ChatForm, NoteForm
from .models import Chat, ChatRoom, Note
from patientdata.models import *


@login_required
def chatView(request, room):

    current_room = get_object_or_404(ChatRoom, pk=room)
    if request.user.id not in (current_room.patient.id, current_room.doctor.id):
        raise Http404('Chat room not found!')
    chats = Chat.objects.filter(room=current_room).order_by('created')
    patientData = PatientData.objects.get(patient=current_room.patient)
    sleepData = SleepData.objects.filter(patient=patientData)
    foodData = FoodData.objects.filter(patient=patientData)
    pressureData = PressureData.objects.filter(patient=patientData)
    notes = Note.objects.filter(room=current_room)

    if request.method == "POST":
        form = ChatForm(request.POST)
        noteform = NoteForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.user = request.user
            chat.room = current_room
            chat.save()
            return redirect('chat-view', room=room)
        
        if noteform.is_valid():
            note = noteform.save(commit=False)
            note.room = current_room
            note.save()
            return redirect('chat-view', room=room)
    else:
        form = ChatForm()
        noteform = NoteForm()

    return render(request, 'livechat/chat-view.html', {'patientData': patientData, 'sleepData': sleepData, 'foodData': foodData, 'pressureData': pressureData, 'chats': chats, 'form': form, 'room': current_room, 'noteform': noteform, 'notes': notes})
