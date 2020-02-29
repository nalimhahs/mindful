from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Thread, Post


class ListAllThreadsView(TemplateView):

    template_name = 'forum/list-all-threads.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['threads'] = Thread.objects.all().order_by('-created')
        return context


class CreateNewThreadView(LoginRequiredMixin, CreateView):

    model = Thread
    template_name = 'forum/create-new-thread.html'
    fields = ('title', 'desc', 'tags')
    pk = None

    def form_valid(self, form):
        thread = form.save(commit=False)
        thread.user = self.request.user
        thread.save()
        self.pk = thread.id
        return super().form_valid(thread)

    def get_success_url(self):
        return reverse_lazy("show-thread", args=(self.pk, ))


class ShowThreadView(DetailView):

    model = Thread
    template_name = 'forum/show-thread.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(thread=self.get_object().pk).order_by('created')
        return context


class CreateNewPostView(LoginRequiredMixin, CreateView):

    model = Post
    template_name = 'forum/create-new-post.html'
    fields = ('content',)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.thread = Thread.objects.get(pk=self.kwargs.get('pk'))
        post.save()
        return super().form_valid(post)

    def get_success_url(self):
        return reverse_lazy("show-thread", args=(self.kwargs.get('pk'), ))
