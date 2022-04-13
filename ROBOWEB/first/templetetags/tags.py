from django import template

register=template.Library()

@register.simple_tag()
def which_profil():
    #if return true show hiden info for register new person

    return True

