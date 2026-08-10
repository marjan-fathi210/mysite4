from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.
def blog_view(request):
    posts= Post.objects.filter(published_date__lte= timezone.now())
    context={'posts': posts}
    return render(request,'blog/blog-home.html', context)

def blog_single(request, pid):
    posts= Post.objects.filter(status=1)
    post= get_object_or_404(posts, pk= pid, status=1)
    context={'post': post}
    return render(request,'blog/blog-single.html',context)

def test_view(request, pid):
    #post= Post.objects.get(id= pid)
    post= get_object_or_404(Post, pk= pid)
    context={'post': post}
    return render(request, 'test.html', context)