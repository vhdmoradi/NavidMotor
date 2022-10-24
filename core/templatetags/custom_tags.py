from django import template

register = template.Library()


@register.filter
def get_value(dic, key):
    return dic.get(key)
