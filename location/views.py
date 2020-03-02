from django.shortcuts import render

def locationfinder(request):
    return render(request, 'location/hospitallocation.html')
