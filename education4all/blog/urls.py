"""
Urls of the blog application
"""
from blog.views import get_view_factory
from django.urls import path

post_list = get_view_factory('PostsListFactory').create()
post_detail = get_view_factory('PostsDetailFactory').create()
contact_us = get_view_factory('ContactFactory').create()
algorithms_list = get_view_factory('PostListAlgorithmsFactory').create()
mathematics_list = get_view_factory('PostListMathematicsFactory').create()

post_list = get_view_factory('PostsListFactory').create()
post_detail = get_view_factory('PostsDetailFactory').create()
contact_us = get_view_factory('ContactFactory').create()
algorithms_list = get_view_factory('PostListAlgorithmsFactory').create()
mathematics_list = get_view_factory('PostListMathematicsFactory').create()

urlpatterns = [
    path('', post_list.as_view(), name='home'),
    path('contact/', contact_us.as_view(), name='contact'),
    path('algorithms/', algorithms_list.as_view(), name='algorithms'),
    path('mathematics/', mathematics_list.as_view(), name='mathematics'),
    path('<slug:slug>/', post_detail.as_view(), name='post_detail'),
]
