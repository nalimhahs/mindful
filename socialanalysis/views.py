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
            # print(tweets)
            positive=0
            negative=0
            neutral=0
            point=20
            for i in range(0,20): 
                analysis = datreeINPUT(tweets[i][2])
                if analysis == "positive":
                    positive+=point
                elif analysis == "neutral":
                    neutral+=point
                else: 
                    negative+=point
                point-=1
            if positive>negative and positive>neutral:
                analysis="positive"
            elif negative>positive and negative>neutral:
                analysis="negative"
            else:
                analysis="neutral"
                
    else:
        form = UsernameForm()

    return render(request, 'socialanalysis/analyse.html', {'analysis': analysis, 'form': form})