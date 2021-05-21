"""
Admin section for posts
"""
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    """
    Customize posts section in admin dashboard
    """
<<<<<<< HEAD
    list_display = ('title', 'slug', 'section', 'status', 'created_on')
    list_filter = ("status", "section")
=======
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
>>>>>>> [feat]: Replacing standalone filer per modules
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  