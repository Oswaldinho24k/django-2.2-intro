from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        "posts":posts
    }
    return render(request, 'posts/lista.html', context)




