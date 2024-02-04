# encoding: utf-8
# module samba.dcerpc.dcerpc
# from /usr/lib/python3/dist-packages/samba/dcerpc/dcerpc.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" dcerpc DCE/RPC """

# imports
import talloc as __talloc


class ctx_list(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    abstract_syntax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type ndr_syntax_id"""

    context_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    num_transfer_syntaxes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    transfer_syntaxes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type ndr_syntax_id"""



