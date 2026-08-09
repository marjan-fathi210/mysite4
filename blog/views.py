from django.shortcuts import render, get_object_or_404
from blog.models import Post
from datetime import datetime

# Create your views here.
def blog_view(request):
    posts= Post.objects.all()
    pub_date= posts.published_date
    now_date= datetime.now()
    if pub_date <= now_date:
        context={'posts': posts}
        return render(request,'blog/blog-home.html', context)

def blog_single(request):
    context={'title':'bicoin crashed again!','content':'bitcoin was flying but now grounded,ok','author':'marjan fathi'}
    return render(request,'blog/blog-single.html',context)

def test_view(request, pid):
    #post= Post.objects.get(id= pid)
    post= get_object_or_404(Post, pk= pid)
    context={'post': post}
    return render(request, 'test.html', context)