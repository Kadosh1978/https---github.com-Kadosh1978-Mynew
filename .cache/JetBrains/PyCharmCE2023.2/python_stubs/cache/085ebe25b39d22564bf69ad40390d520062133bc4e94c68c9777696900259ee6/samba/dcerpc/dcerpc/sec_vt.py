# encoding: utf-8
# module samba.dcerpc.dcerpc
# from /usr/lib/python3/dist-packages/samba/dcerpc/dcerpc.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" dcerpc DCE/RPC """

# imports
import talloc as __talloc


class sec_vt(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dcerpc_sec_vt_command"""

    u = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dcerpc_sec_vt_union"""



