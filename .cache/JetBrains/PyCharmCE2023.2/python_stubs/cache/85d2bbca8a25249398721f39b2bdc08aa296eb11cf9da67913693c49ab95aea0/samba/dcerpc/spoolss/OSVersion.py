# encoding: utf-8
# module samba.dcerpc.spoolss
# from /usr/lib/python3/dist-packages/samba/dcerpc/spoolss.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" spoolss DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class OSVersion(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    build = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    extra_string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type string"""

    major = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    minor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    platform_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    _ndr_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""



