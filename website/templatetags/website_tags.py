from django import template
from blog.models import Post

register= template.Library()

@register.inclusion_tag('website/website-latestposts.html')
def latestposts(args=6):
    posts= Post.objects.filter(status=1).order_by('published_date')[:args]
    return {'posts':posts}