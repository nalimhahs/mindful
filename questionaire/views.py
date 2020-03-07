from django.shortcuts import render, redirect
from .models import Question, Answer, QuestionGroup
from .forms import AnswerForm
from patientdata.models import PatientData

def getAnswer(request, qg, pk):

    question = Question.objects.get(pk=pk)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            Answer.objects.update_or_create(user=request.user, question=question, defaults={'answer': answer})
            try:
                next_pk = Question.objects.filter(group=qg, pk__gt=pk)[:1].get()
            except:
                return redirect('complete-view', qg=qg)
            return redirect('answer-view', qg=qg, pk=next_pk.pk)
    else:
        form = AnswerForm()
    return render(request, 'questionaire/questionaire.html', {'question': question, 'form': form})


def startQuiz(request, qg):

    group = QuestionGroup.objects.get(pk=qg)
    next_pk = Question.objects.filter(group=qg, pk__gt=-1)[:1].get()
    return render(request, 'questionaire/start.html', {'group': group, 'next_pk': next_pk})


def quizComplete(request, qg):

    scores = Answer.objects.filter(user=request.user)
    flag = 0
    evaluation = 0
    for score in scores:
        evaluation += score.answer
    message = ""
    if evaluation > 10:
        message = "You're doing awesome!"
    elif evaluation > 5:
        message = "Looks like you're doing ok. Please do reach out if you need any help!"
        flag = 1
    else:
        message = "We really suggest you see a trained practitioner! Follow the prompts to connect with one."
        flag = 1

    if qg == 1:
        PatientData.objects.update_or_create(patient=request.user, defaults={'anxiety_quiz_score': evaluation})
    elif qg == 2:
        PatientData.objects.update_or_create(patient=request.user, defaults={'depression_quiz_score': evaluation})
    elif qg==3:
        PatientData.objects.update_or_create(patient=request.user, defaults={'lifestyle_quiz_score': evaluation})
    
    return render(request, 'questionaire/end.html', {'score': evaluation, 'message': message, 'flag': flag})
