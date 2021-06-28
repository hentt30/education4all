"""
Admin section for posts
"""
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    """
    Customize posts section in admin dashboard
    """
    list_display = ('title', 'slug', 'section', 'status', 'created_on')
    list_filter = ("status", "section")
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  