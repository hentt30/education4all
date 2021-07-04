"""
about us page
"""
from django.views import generic


class AboutUs(generic.TemplateView):
    """
    Shows contact us page
    """
    template_name = 'about_us.html'
