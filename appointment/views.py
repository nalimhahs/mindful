from django.shortcuts import render
from .models import Appointment

def bookings(request):
    bookings = Appointment.objects
    return render(request, 'appointment/booking.html', {'appointment': appointment})

