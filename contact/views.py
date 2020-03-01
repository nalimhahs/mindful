from django.shortcuts import render
from .models import Contact

def contacts(request):
    contacts = Contact.objects
    return render(request, 'contact/contacts.html', {'contacts': contacts})
