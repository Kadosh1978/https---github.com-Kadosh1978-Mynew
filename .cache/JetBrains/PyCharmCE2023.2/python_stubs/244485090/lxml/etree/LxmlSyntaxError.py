# encoding: utf-8
# module lxml.etree
# from /home/kadosh/PycharmProjects/Weather/venv/lib/python3.10/site-packages/lxml/etree.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .LxmlError import LxmlError

from .SyntaxError import SyntaxError

class LxmlSyntaxError(LxmlError, SyntaxError):
    """ Base class for all syntax errors. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



