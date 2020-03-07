from django.shortcuts import render, redirect
from .models import Question, Answer, QuestionGroup
from .forms import AnswerForm


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
                return redirect('complete-view', qg=qg, pk=next_pk.pk)
            return redirect('answer-view', qg=qg, pk=next_pk.pk)
    else:
        form = AnswerForm()
    return render(request, 'questionaire/questionaire.html', {'question': question, 'form': form})


def startQuiz(request, qg):

    group = QuestionGroup.objects.get(pk=qg)
    next_pk = Question.objects.filter(group=qg, pk__gt=-1)[:1].get()
    return render(request, 'questionaire/start.html', {'group': group, 'next_pk': next_pk})


def quizComplete(request, qg):
    pass
