from collections import defaultdict
from django import template
from django.contrib.auth.models import User

register = template.Library()


@register.filter
def get_blog_types(user: User) -> list[tuple]:
    types = defaultdict(int)
    for blog in user.blog_set.all():
        for content_type in blog.content_type.all():
            types[content_type] += 1
    return list(types.items())
