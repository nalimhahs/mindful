from django.shortcuts import render
from .forms import UsernameForm
from .services import get_all_tweets
from .mlmodel.detect import datreeINPUT

def analyseSocialsView(request):

    analysis = None
    
    if request.method == "POST":
        form = UsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            tweets = get_all_tweets(username)
            print(tweets)
            analysis = datreeINPUT(tweets[0][2])
    else:
        form = UsernameForm()

    return render(request, 'socialanalysis/analyse.html', {'analysis': analysis, 'form': form})