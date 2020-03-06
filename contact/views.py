from django.shortcuts import render
from .models import Contact

def contacts(request):
    contacts = Contact.objects
    return render(request, 'contacts/contacts.html', {'contacts': contacts})
