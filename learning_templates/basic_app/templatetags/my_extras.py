# for custom filter


from django import template

register=template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """"
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')    #Replace the arg string inside the value string with ''

#REGISTERING
#register.filter('cut',cut)    #'cut' is the name of this filter
                             #cut is the function calling to cut function
