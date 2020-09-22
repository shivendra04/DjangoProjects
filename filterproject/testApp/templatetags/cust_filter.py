from django import template
register=template.Library()

@register.filter(name='truncate_file')
def truncate_file(value):
    result=value[0:5]
    return result

@register.filter(name='t_n')
def truncate_n(value,n):
    result=value[0:n]
    return result

#register.filter('t_n',truncate_n)
#register.filter('truncate_file',truncate_file)
# alternative to these to line is decorator.
