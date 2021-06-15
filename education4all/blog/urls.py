"""
Urls of the blog application
"""
from blog.views import (
    PostList,
    PostDetail,
    ContactUs,
)
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('contact/', ContactUs.as_view(), name='contact'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
