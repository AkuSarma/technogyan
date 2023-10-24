from .models import BlogPost
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class BlogHome(ListView):
    model = BlogPost

    template_name = 'blog/blog_list.html'


class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = 'blog/blog_create.html'
    fields = ["title", "minidescription", "maintext"]
    success_url = reverse_lazy('blogHome')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BlogPostCreate, self).form_valid(form)
    
class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/detail.html'


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "minidescription", "maintext"]
    template_name = "blog/updateBlog.html"
    success_url = reverse_lazy('blogHome')


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/deleteBlog.html"
    success_url = reverse_lazy("blogHome")