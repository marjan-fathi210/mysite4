from django.shortcuts import render, get_object_or_404
from blog.models import Post
from blog.models import Category
from django.utils import timezone
from django.http import HttpResponse, JsonResponse

# Create your views here.
def blog_view(request, cat_name=None):
    posts= Post.objects.filter(published_date__lte= timezone.now(), status=1)
    if cat_name:
        posts= posts.filter(category__name= cat_name)

    context={'posts': posts}
    return render(request,'blog/blog-home.html', context)

def blog_single(request, pid):
    posts= Post.objects.filter(status=1).order_by('published_date')
    post= get_object_or_404(posts, pk= pid)
    post.counted_views+=1
    post.save()
    
    post_list= list(posts)
    current_index= post_list.index(post)
    prev_post= post_list[current_index-1] if current_index> 0 else None
    next_post= post_list[current_index+1] if current_index< len(post_list) -1 else None
    context={'post': post, 'prev_post': prev_post, 'next_post':next_post}
    return render(request,'blog/blog-single.html',context)

def blog_category(request,cat_name):
    posts= Post.objects.filter(status=1)
    posts= posts.filter(category__name= cat_name)
    context={'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def test_view(request):
    return render(request,'test.html')
        