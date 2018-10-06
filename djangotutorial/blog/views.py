from django.shortcuts import render
from django.http import HttpResponse 

from .models import Post
# Create your views here.
def home(request):
    #return HttpResponse("Hello World")

    posts = Post.objects.all()
    return render(
        request,
        'blog.html',
        {'posts': posts, 'name': 'Rama'}
    )