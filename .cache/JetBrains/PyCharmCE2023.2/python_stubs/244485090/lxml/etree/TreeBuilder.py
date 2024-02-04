# encoding: utf-8
# module lxml.etree
# from /home/kadosh/PycharmProjects/Weather/venv/lib/python3.10/site-packages/lxml/etree.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from ._SaxParserTarget import _SaxParserTarget

class TreeBuilder(_SaxParserTarget):
    """
    TreeBuilder(self, element_factory=None, parser=None,
                        comment_factory=None, pi_factory=None,
                        insert_comments=True, insert_pis=True)
    
        Parser target that builds a tree from parse event callbacks.
    
        The factory arguments can be used to influence the creation of
        elements, comments and processing instructions.
    
        By default, comments and processing instructions are inserted into
        the tree, but they can be ignored by passing the respective flags.
    
        The final tree is returned by the ``close()`` method.
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        close(self)
        
                Flushes the builder buffers, and returns the toplevel document
                element.  Raises XMLSyntaxError on inconsistencies.
        """
        pass

    def comment(self, comment): # real signature unknown; restored from __doc__
        """
        comment(self, comment)
        
                Creates a comment using the factory, appends it (unless disabled)
                and returns it.
        """
        pass

    def data(self, data): # real signature unknown; restored from __doc__
        """
        data(self, data)
        
                Adds text to the current element.  The value should be either an
                8-bit string containing ASCII text, or a Unicode string.
        """
        pass

    def end(self, tag): # real signature unknown; restored from __doc__
        """
        end(self, tag)
        
                Closes the current element.
        """
        pass

    def pi(self, target, data=None): # real signature unknown; restored from __doc__
        """
        pi(self, target, data=None)
        
                Creates a processing instruction using the factory, appends it
                (unless disabled) and returns it.
        """
        pass

    def start(self, tag, attrs, nsmap=None): # real signature unknown; restored from __doc__
        """
        start(self, tag, attrs, nsmap=None)
        
                Opens a new element.
        """
        pass

    def __init__(self, element_factory=None, parser=None, comment_factory=None, pi_factory=None, insert_comments=True, insert_pis=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f717ff5dc20>'


