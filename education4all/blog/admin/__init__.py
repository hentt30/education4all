"""
Admin access page settings
"""
from django.contrib import admin
from blog.models import PostModel
from .posts_admin import PostAdmin

# Register your models here.
admin.site.register(PostModel, PostAdmin)