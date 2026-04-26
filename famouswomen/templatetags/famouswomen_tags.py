from django import template
from django.db.models import Count

from famouswomen.models import Category, TagPost
from famouswomen.utils import menu

register = template.Library()

@register.inclusion_tag('famouswomen/list_categories.html')
def show_categories(cat_select=0):
    cats = Category.objects.annotate(total=Count('categories')).filter(total__gt=0)
    return {'cats': cats, 'cat_select': cat_select}


@register.inclusion_tag('famouswomen/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.annotate(total=Count('tags')).filter(total__gt=0)}