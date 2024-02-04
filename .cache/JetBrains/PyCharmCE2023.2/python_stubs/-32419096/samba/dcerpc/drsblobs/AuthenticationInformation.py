# encoding: utf-8
# module samba.dcerpc.drsblobs
# from /usr/lib/python3/dist-packages/samba/dcerpc/drsblobs.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" drsblobs DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class AuthenticationInformation(__talloc.BaseObject):
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

    AuthInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type AuthInfo"""

    AuthType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_TrustAuthType"""

    LastUpdateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type NTTIME"""

    _pad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DATA_BLOB"""



