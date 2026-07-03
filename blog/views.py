from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request,'blog/blog-home.html')

def blog_single(request):
    context={'title':'bicoin crashed again!','content':'bitcoin was flying but now grounded,ok','author':'marjan fathi'}
    return render(request,'blog/blog-single.html',context)