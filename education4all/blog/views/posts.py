"""
View for posts model
"""
from django.views import generic
from blog.models import PostModel


class PostList(generic.ListView):
    """
    Create a list of posts ordered by most recent
    """
    queryset = PostModel.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    """
    Shows details for a specific post
    """
    model = PostModel
    template_name = 'post_detail.html'
