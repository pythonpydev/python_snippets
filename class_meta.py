class Meta(type):
    """
    Flexible metaclass for defining useful decorator functions.
    """
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        return clsobj


class Base(object, metaclass=Meta):
    """
    Base class.

    Args:
        *args (list): list of arguments
        **kwargs (dict): dict of keyword arguments

    Attributes:
        self
    """

    def __init__(self, *args, **kwargs):
        allowed_keys = set([])
        self.__dict__.update((k, False) for k in allowed_keys)
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys)

    def foo(self):
        """
        Function.
        """
        pass


class Derived(Base):
    """
    Derived class.

    Args:
        *args (list): list of arguments
        **kwargs (dict): dict of keyword arguments

    Attributes:
        self
    """

    def __init__(self, *args, **kwargs):
        allowed_keys = set([])
        self.__dict__.update((k, False) for k in allowed_keys)
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys) 

    
