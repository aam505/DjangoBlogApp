from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # mixins have to be to the left inheritence
# Create your views here. 

# This is where you add the logic to how to handle certain routes 
 
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html', context)

 
class PostListView(ListView):
    model = Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=5
    #by default itnames the posts variable above as object_list
    #app/module_viewtype.html

class UserPostListView(ListView):
    model = Post
    template_name='blog/user_posts.html'
    context_object_name='posts'
    paginate_by=5

    #to modify the query set that this list view returns we can override this method
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
  
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if(self.request.user == post.author):
            return True 
        else:
            return False

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['title', 'content']

    #override form valid method
    def form_valid(self, form):
        form.instance.author = self.request.user # setting the author befor the parent form valid gets run
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields=['title', 'content']

    #override form valid method
    def form_valid(self, form):
        form.instance.author = self.request.user # setting the author befor the parent form valid gets run
        return super().form_valid(form)

    #used by user passes test mixin
    def test_func(self):
        post=self.get_object()
        if(self.request.user == post.author):
            return True 
        else:
            return False    

def about(request):
    return render(request,'blog/about.html',{'title':'DJANGO'})