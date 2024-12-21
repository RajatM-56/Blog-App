from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms.models import BaseModelForm
from django.contrib.auth.models import User

# Create your views here.
class Home(generic.ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post_view.html'
    context_object_name = 'post'


class UserPostView(generic.ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'user_posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/createPost.html'

    def form_valid(self, form: BaseModelForm):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/createPost.html'

    def form_valid(self, form: BaseModelForm):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self) -> bool:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'
    success_url = '/'

    def test_func(self) -> bool:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
