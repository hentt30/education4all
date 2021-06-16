"""
Urls of the blog application
"""
from blog.views import get_view_factory
from django.urls import path

post_list = get_view_factory('PostsListFactory').create()
post_detail = get_view_factory('PostsDetailFactory').create()
contact_us = get_view_factory('ContactFactory').create()

urlpatterns = [
    path('', post_list.as_view(), name='home'),
    path('contact/', contact_us.as_view(), name='contact'),
    path('<slug:slug>/', post_detail.as_view(), name='post_detail'),
]
