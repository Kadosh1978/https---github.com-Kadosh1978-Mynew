# encoding: utf-8
# module lxml.etree
# from /home/kadosh/.local/lib/python3.10/site-packages/lxml/etree.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .LxmlSyntaxError import LxmlSyntaxError

from .XPathError import XPathError

class XPathSyntaxError(LxmlSyntaxError, XPathError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


