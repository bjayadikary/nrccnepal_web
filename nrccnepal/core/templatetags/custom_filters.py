from django import template

register = template.Library()

@register.filter(name='split_by_hash')
def split_by_hash(value):
    return value.split("#")