"""
Database model for posts
"""
from django.db import models
from django.contrib.auth.models import User




class PostModel(models.Model):
    """
    Class representing the post model in the database
    """
    STATUS = (
    (0,"Draft"),
    (1,"Publish")
    )

<<<<<<< HEAD
    SECTION = (
        (0, "Matemática"),
        (1, "Algoritmos")
    )

=======
>>>>>>> [feat]: Replacing standalone filer per modules
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
<<<<<<< HEAD
    section = models.IntegerField(choices=SECTION, default=0)
=======
>>>>>>> [feat]: Replacing standalone filer per modules
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        Posts model metadata
        """
        ordering = ['-created_on']

    def __str__(self):
<<<<<<< HEAD
        """
        Returns a char field for the model
        """
        return str(self.title)
=======
        return self.title
>>>>>>> [feat]: Replacing standalone filer per modules
