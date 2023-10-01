from django import template

register = template.Library()

@register.filter(name='mediapath')
def mediapath(value):
    return "media/" + str(value)
