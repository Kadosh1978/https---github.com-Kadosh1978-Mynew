# encoding: utf-8
# module lxml.etree
# from /home/kadosh/PycharmProjects/Weather/venv/lib/python3.10/site-packages/lxml/etree.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .XPath import XPath

class ETXPath(XPath):
    """
    ETXPath(self, path, extensions=None, regexp=True, smart_strings=True)
        Special XPath class that supports the ElementTree {uri} notation for namespaces.
    
        Note that this class does not accept the ``namespace`` keyword
        argument. All namespaces must be passed as part of the path
        string.  Smart strings will be returned for string results unless
        you pass ``smart_strings=False``.
    """
    def __init__(self, path, extensions=None, regexp=True, smart_strings=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f717ff5ce10>'


