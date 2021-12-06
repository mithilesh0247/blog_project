from blogapp.models import Post
from django import template
register=template.Library()

@register.simple_tag
def total_posts():
	return  Post.objects.count()
@register.inclusion_tag('latestpost.html')
def show_latest_posts():
    latest_posts=Post.objects.order_by('-publish')[:5]
    return{'latest_posts':latest_posts}	