from django import template

register = template.Library()

@register.filter
def contains(palavra, substring):
    return str(substring).lower() in str(palavra).lower()



