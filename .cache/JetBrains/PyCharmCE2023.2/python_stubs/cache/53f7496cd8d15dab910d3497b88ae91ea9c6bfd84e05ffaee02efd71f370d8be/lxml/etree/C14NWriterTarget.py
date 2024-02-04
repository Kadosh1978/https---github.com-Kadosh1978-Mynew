# encoding: utf-8
# module lxml.etree
# from /home/kadosh/PycharmProjects/Weather/venv/lib/python3.10/site-packages/lxml/etree.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class C14NWriterTarget(object):
    """
    Canonicalization writer target for the XMLParser.
    
        Serialises parse events to XML C14N 2.0.
    
        Configuration options:
    
        - *with_comments*: set to true to include comments
        - *strip_text*: set to true to strip whitespace before and after text content
        - *rewrite_prefixes*: set to true to replace namespace prefixes by "n{number}"
        - *qname_aware_tags*: a set of qname aware tag names in which prefixes
                              should be replaced in text content
        - *qname_aware_attrs*: a set of qname aware attribute names in which prefixes
                               should be replaced in text content
        - *exclude_attrs*: a set of attribute names that should not be serialised
        - *exclude_tags*: a set of tag names that should not be serialised
    """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def comment(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def end(self, *args, **kwargs): # real signature unknown
        pass

    def pi(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def start_ns(self, *args, **kwargs): # real signature unknown
        pass

    def _iter_namespaces(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f717ff5da70>'


