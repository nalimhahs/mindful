from django.urls import reverse_lazy, path
from django.views.generic import CreateView, TemplateView

from .models import Poster


class HomePageView(CreateView):
    model = Poster
    fields = ['title', 'content']
    template_name = 'base.html'

    def get_success_url(self):
        return reverse_lazy("home", args=[])  

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        self.object = post.save()
        return super().form_valid(post)


class PostListingView(TemplateView):

    template_name = 'pages/post-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Poster.objects.all()
        return context