from django.shortcuts import render
from .models import Appointment

#def bookings(request):
#    bookings = Appointment.objects
#    return render(request, 'appointment/booking.html', {'appointment': appointment})
def bookings(request):
    if request.method == "POST":  
        form = AppointmentForm(request.POST)  
        if form.is_valid():  
            try:  
                appointment = form.save(commit=False)
                appointment.patient = request.user
                appointment.save()
                return redirect('data-dash')  
            except:  
                pass  
    else:  
        form = AppointmentForm()
    return render(request, 'appointment/booking.html', {'form': form})
