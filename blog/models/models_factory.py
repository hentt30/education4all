"""
Implements a factory for view classes
"""
from abc import ABC, abstractmethod
from .posts import PostModel


class ModelsFactory(ABC):
    """
    Generates models objects
    """
    @abstractmethod
    def create(self):
        """
        Create the object
        """


class PostsFactory(ModelsFactory):
    """
    Generates the object responsible for store posts in the database
    """
    def create(self):
        """
        Create the PostModel object
        """
        return PostModel


def get_model_factory(name):
    """
    Get the correspondent models factory:

        Args:
            name: name of the factory, it can be:
                  'PostsFactory'
    """
    factory_map = {'PostsFactory': PostsFactory()}

    try:
        return factory_map[name]
    except KeyError as key_error:
        raise Exception('Name parameter not in the options') from key_error
