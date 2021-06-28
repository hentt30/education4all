from django import template
from django.template.defaultfilters import stringfilter

import markdown as md

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
<<<<<<< HEAD
    return md.markdown(value, extensions=['extra', 'smarty'])

=======
    return md.markdown(value, extensions=['extra', 'smarty'])
>>>>>>> origin/develop
