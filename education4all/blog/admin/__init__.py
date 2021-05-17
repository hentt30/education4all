"""
Admin access page settings
"""
from django.contrib import admin
from blog.models import get_model_factory
from .posts_admin import PostAdmin

# Register your models here.
admin.site.register(get_model_factory('PostsFactory').create()gir, PostAdmin)