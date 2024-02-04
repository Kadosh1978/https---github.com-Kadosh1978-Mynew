# encoding: utf-8
# module samba.dcerpc.netlogon
# from /usr/lib/python3/dist-packages/samba/dcerpc/netlogon.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" netlogon DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class netr_OsVersionInfoEx(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    BuildNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    CSDVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type string"""

    MajorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    MinorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    OSVersionInfoSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    PlatformId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    ProductType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type netr_ProductType"""

    Reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    ServicePackMajor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    ServicePackMinor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    SuiteMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type netr_SuiteMask"""



