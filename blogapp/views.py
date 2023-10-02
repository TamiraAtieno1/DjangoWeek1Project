from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog2
from .forms import BlogForm

# Create your views here.
def home(request):
    blogs = Blog2.objects.all()
    context = {
        "blogs" : blogs
    }
    return render(request, "list.html", context)

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("blogapp:home")

    context = {
        'form' : form
    }

    return render(request, 'create.html', context)


def detailed(request, blog_id):
    blog = get_object_or_404(Blog2, pk=blog_id)
    context = {
        "blog" : blog
    }
    return render(request, "detailed.html", context)


def update(request, blog_id):
    blog = get_object_or_404(Blog2, pk=blog_id)
    form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect("blogapp:home")

    context = {
        'form' : form
    }

    return render(request, 'create.html', context)

def delete(request, blog_id):
    blog = get_object_or_404(Blog2, pk=blog_id)
    blog.delete()
    return redirect("blogapp:home")
