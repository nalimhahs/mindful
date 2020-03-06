from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.decorators import is_doctor
from forum.models import Post, Thread
from livechat.models import ChatRoom, Chat
from datetime import datetime, timedelta

@login_required
@is_doctor
def doctorMainDashboard(request):

    active_threads = Thread.objects.filter(
        post__in=Post.objects.filter(user=request.user)).order_by('-created')
    patient_count = ChatRoom.objects.filter(doctor=request.user)
    # availability_status_of _doctor
    recent_chats = ChatRoom.objects.filter(doctor=request.user)
    # patiient_sentiment
    # new_stuff_to_publish
    # approval_stuff_for_chats
    patient_interaction = []
    for i in range(7):
        patient_interaction.append(Chat.objects.filter(room__doctor=request.user, created=datetime.now()-timedelta(days=i)))
    # doc_rating

    return render(request, 'docdash/home.html', {'active_threads': active_threads})


@login_required
@is_doctor
def listAllActiveThreads(request):

    active_threads = Thread.objects.filter(
        post__in=Post.objects.filter(user=request.user)).order_by('-created')

    return render(request, 'docdash/allthreads.html', {'active_threads': active_threads})
