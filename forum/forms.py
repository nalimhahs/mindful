from django.forms import ModelForm
from .models import Thread, Post


class ThreadForm(ModelForm):

    class Meta:
        model = Thread
        fields = ('title', 'desc', 'tags')


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('content', )
