"""
Urls of the blog application
"""
<<<<<<< HEAD
from blog.views import get_view_factory
=======
from blog.views import (
    PostList,
    PostDetail,
    ContactUs,
)
>>>>>>> [feat]: Adding new pages
from django.urls import path
from django.views.generic import TemplateView

post_list = get_view_factory('PostsListFactory').create()
post_detail = get_view_factory('PostsDetailFactory').create()
contact_us = get_view_factory('ContactFactory').create()
algorithms_list = get_view_factory('PostListAlgorithmsFactory').create()
mathematics_list = get_view_factory('PostListMathematicsFactory').create()

urlpatterns = [
<<<<<<< HEAD
    path('', post_list.as_view(), name='home'),
    path('contact/', contact_us.as_view(), name='contact'),
    path('algorithms/', algorithms_list.as_view(), name='algorithms'),
    path('mathematics/', mathematics_list.as_view(), name='mathematics'),
    path('<slug:slug>/', post_detail.as_view(), name='post_detail'),
=======
    path('', PostList.as_view(), name='home'),
    path('contact/', ContactUs.as_view(), name='contact'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
>>>>>>> [feat]: Adding new pages
]
