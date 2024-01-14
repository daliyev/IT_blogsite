import markdown
from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe

from ..models import Post


register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = (
        Post.published
        .only('title', 'publish')
        .order_by('-publish')[:count])
    ctx = {
        'latest_posts': latest_posts,
    }
    return ctx


@register.simple_tag
def get_most_commented_posts(count=5):
    queryset = (
        Post.published
        .prefetch_related('comments')
        .only('title')
        .annotate(total_comments=Count('comments'))
        .order_by('-total_comments')[:count]
    )
    return queryset


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
