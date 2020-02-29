from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.decorators import is_doctor
from forum.models import Post, Thread


@login_required
@is_doctor
def doctorMainDashboard(request):

    active_threads = Thread.objects.filter(
        post__in=Post.objects.filter(user=request.user)).order_by('-created')

    return render(request, 'docdash/home.html', {'active_threads': active_threads})
