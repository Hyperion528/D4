from django import template
 
register = template.Library()
 
 
@register.filter(name='censor')  
def censor_func(value):
    if "матное слово" in value:
        raise ValueError
    else:
        return value