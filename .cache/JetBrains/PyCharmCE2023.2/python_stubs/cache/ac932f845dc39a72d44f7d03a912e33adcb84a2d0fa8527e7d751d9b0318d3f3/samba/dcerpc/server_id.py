# encoding: utf-8
# module samba.dcerpc.server_id
# from /usr/lib/python3/dist-packages/samba/dcerpc/server_id.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" server_id DCE/RPC """

# imports
import talloc as __talloc


# Variables with simple values

NONCLUSTER_VNN = 4294967295

SERVERID_UNIQUE_ID_NOT_TO_VERIFY = 18446744073709551615

# no functions
# classes

class server_id(__talloc.BaseObject):
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

    pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type hyper"""

    task_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    unique_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type hyper"""

    vnn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.server_id', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/server_id.cpython-310-x86_64-linux-gnu.so')"

