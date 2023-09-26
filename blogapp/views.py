from django.shortcuts import render
from .models import Blog2

# Create your views here.
def home(request):
    blogs = Blog2.objects.all()
    context = {
        "blogs" : blogs
    }
    return render(request, "index.html", context)

