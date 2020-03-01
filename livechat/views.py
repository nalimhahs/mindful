from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .forms import ChatForm
from .models import Chat, ChatRoom


@login_required
def chatView(request, room):

    current_room = get_object_or_404(ChatRoom, pk=room)
    if request.user != current_room.patient or request.user != current_room.doctor:
        return Http404('Chat room not found!')
    chats = Chat.objects.filter(room=current_room).order_by('created')

    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.user = request.user
            chat.room = room
            chat.save()
            return redirect('chat-view', pk=room)
    else:
        form = ChatForm()

    return render(request, 'livechat/chat-view.html', {'chats': chats, 'form': form, 'room': room})
