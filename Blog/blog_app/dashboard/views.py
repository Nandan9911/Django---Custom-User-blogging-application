from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    
)
from .models import Post,Comments


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'home.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comments
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class CommentListView(ListView):
    model = Comments
    template_name = 'home.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


def about(request):
    return render(request, 'about.html', {'title': 'About'})
