from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog
from .forms import CommentForm
from django.views.generic import ListView, DetailView

# Create your views here.
class Home(ListView):
    model = Blog

def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect("blog-detail", pk)

    else:
        form = CommentForm()    
    
    context = {"object": blog, "form": form}
    
    return render(request, "blog/blog_detail.html", context)