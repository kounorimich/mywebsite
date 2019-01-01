from django.shortcuts import render, get_object_or_404 #追記分
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
    #return HttpResponse('Hello World!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    posts = Post.objects.order_by('-published')
    return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request, post_id):
    #post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id) #変更分。get_object_or_404を使う場合は、クラスとキーだけ入れればいい。
    return render(request, 'posts/post_detail.html', {'post': post})

def about(request):
    return render(request, 'posts/about.html')
