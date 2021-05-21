"""
Admin section for posts
"""
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    """
    Customize posts section in admin dashboard
    """
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  