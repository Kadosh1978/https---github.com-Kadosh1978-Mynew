# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python3/dist-packages/samba/dcerpc/drsuapi.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DsReplicaObjectIdentifier3(__talloc.BaseObject):
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

    dn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type GUID"""

    sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dom_sid28"""

    __ndr_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    __ndr_size_dn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    __ndr_size_sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""



