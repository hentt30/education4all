"""
contact us page
"""
from django.views import generic


class ContactUs(generic.TemplateView):
    """
    Shows contact us page
    """
    template_name = 'contact.html'
