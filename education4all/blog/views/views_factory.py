"""
Implements a factory for view classes
"""
from abc import ABC, abstractmethod
from .posts import PostDetail, PostList, PostListAlgorithms, PostListMathematics
from .contact import ContactUs


class ViewsFactory(ABC):
    """
    Generates view objects
    """
    @abstractmethod
    def create(self):
        """
        Create the object
        """


class PostsDetailFactory(ViewsFactory):
    """
    Generates the object responsible for post details creation
    """
    def create(self):
        """
        Create the PostDetail object
        """
        return PostDetail


class PostsListFactory(ViewsFactory):
    """
    Generates the object responsible for list the posts
    """
    def create(self):
        """
        Create the PostList object
        """
        return PostList


class PostListAlgorithmsFactory(ViewsFactory):
    """
    Generates the object responsible for list the posts about algorithms
    """
    def create(self):
        """
        Create the PostList object
        """
        return PostListAlgorithms


class PostListMathematicsFactory(ViewsFactory):
    """
    Generates the object responsible for list the posts about algorithms
    """
    def create(self):
        """
        Create the PostList object
        """
        return PostListMathematics


class ContactFactory(ViewsFactory):
    """
    Generates the object responsible for show contact informations
    """
    def create(self):
        """
        Create the Contact us object
        """
        return ContactUs


def get_view_factory(name):
    """
    Get the correspondent view factory:

        Args:
            name: name of the factory, it can be:
                  'ContactFactory'
                  'PostsListFactory'
                  'PostsDetailFactory'
    """
    factory_map = {
        'ContactFactory': ContactFactory(),
        'PostsListFactory': PostsListFactory(),
        'PostsDetailFactory': PostsDetailFactory(),
        'PostListAlgorithmsFactory': PostListAlgorithmsFactory(),
        'PostListMathematicsFactory': PostListMathematicsFactory(),
    }

    try:
        return factory_map[name]
    except KeyError as key_error:
        raise Exception('Name parameter not in the options') from key_error
