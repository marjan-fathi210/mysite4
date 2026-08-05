from django.shortcuts import render
from blog.models import Post

# Create your views here.
def blog_view(request):
    return render(request,'blog/blog-home.html')

def blog_single(request):
    context={'title':'bicoin crashed again!','content':'bitcoin was flying but now grounded,ok','author':'marjan fathi'}
    return render(request,'blog/blog-single.html',context)

def test_view(request):
    posts= Post.objects.all()
    context={'posts': posts}
    return render(request, 'test.html', context)