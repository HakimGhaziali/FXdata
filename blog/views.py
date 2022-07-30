from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin






# Create your views here.
from .forms import PostForm
from .models import Post

class PostList(generic.ListView):

    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 100  # if pagination is desired
    context_object_name = 'post_list'



class PostDetail(generic.DetailView):

    model= Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin , generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('post_list')


    def form_valid(self , form):
        lost = form.save(commit=False)
        lost.user = self.request.user 
        lost.save()
        return redirect(self.success_url)




class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'blog/post_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')

    
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user