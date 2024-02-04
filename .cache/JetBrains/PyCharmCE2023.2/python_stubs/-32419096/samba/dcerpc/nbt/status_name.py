# encoding: utf-8
# module samba.dcerpc.nbt
# from /usr/lib/python3/dist-packages/samba/dcerpc/nbt.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" nbt DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class status_name(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    nb_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type nb_flags"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type nbt_name_type"""



