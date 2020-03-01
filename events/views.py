from django.shortcuts import render, get_object_or_404
from .models import Events


def allevents(request):
    events = Events.objects
    return render(request, 'events/allevents.html', {'events': events})


def detail(request, events_id):
    events=Events.objects
    eventsdetail = get_object_or_404(Events, pk=events_id)
    return render(request, 'events/detail.html', {'event': eventsdetail, 'events':events})
