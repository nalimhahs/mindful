from django.shortcuts import render
from .models import Question

def allquestion(request):
    questions=Question.objects.all()
    return render(request,'questionaire/questionaire.html',{'questions':questions})


