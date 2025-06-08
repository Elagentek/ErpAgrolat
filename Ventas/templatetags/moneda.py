from django import template

register = template.Library()

@register.filter
def clp(value):
    try:
        return "${:,.0f}".format(value).replace(",", ".")
    except:
        return value

@register.filter
def multiply(value, arg):
    return value * arg
