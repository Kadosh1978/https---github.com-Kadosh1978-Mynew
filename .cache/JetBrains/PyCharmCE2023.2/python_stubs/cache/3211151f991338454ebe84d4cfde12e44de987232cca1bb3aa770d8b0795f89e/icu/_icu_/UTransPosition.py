# encoding: utf-8
# module icu._icu_
# from /usr/lib/python3/dist-packages/icu/_icu_.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" PyICU extension module """

# imports
import datetime as __datetime
import icu as __icu


from .object import object

class UTransPosition(object):
    """ UTransPosition objects """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    contextLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ending index, exclusive, of the context to be considered for a transliteration operation."""

    contextStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Beginning index, inclusive, of the context to be considered for a transliteration operation."""

    limit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ending index, exclusive, of the text to be transliterated."""

    start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Beginning index, inclusive, of the text to be transliterated."""



