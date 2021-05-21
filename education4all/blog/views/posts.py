"""
View for posts model
"""
from django.views import generic
from blog.models import get_model_factory


class PostList(generic.ListView):
    """
    Create a list of posts ordered by most recent
    """

    model = get_model_factory('PostsFactory').create()
    queryset = model.objects.filter(status=1).order_by('-created_on')[:10]
    template_name = 'index.html'


class PostListAlgorithms(generic.ListView):
    """
    Create a list of posts ordered by most recent
    """
    model = get_model_factory('PostsFactory').create()
    queryset = model.objects.filter(status=1,
                                   
                                    section=1).order_by('-created_on')[:10]
    template_name = 'index.html'


class PostListMathematics(generic.ListView):
    """
    Create a list of posts ordered by most recent
    """
    model = get_model_factory('PostsFactory').create()
    queryset = model.objects.filter(status=1,
                                   
                                    section=0).order_by('-created_on')[:10]

    template_name = 'index.html'


class PostDetail(generic.DetailView):
    """
    Shows details for a specific post
    """
    model = get_model_factory('PostsFactory').create()
    template_name = 'post_detail.html'
