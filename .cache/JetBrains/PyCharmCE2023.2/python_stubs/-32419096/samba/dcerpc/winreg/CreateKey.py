# encoding: utf-8
# module samba.dcerpc.winreg
# from /usr/lib/python3/dist-packages/samba/dcerpc/winreg.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" winreg DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class CreateKey(__talloc.BaseObject):
    # no doc
    @classmethod
    def opnum(cls): # real signature unknown; restored from __doc__
        """ winreg.CreateKey.opnum() -> 6 (0x06) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack_in__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack_in(object, bigendian=False, ndr64=False) -> blob
        NDR pack input
        """
        pass

    def __ndr_pack_out__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack_out(object, bigendian=False, ndr64=False) -> blob
        NDR pack output
        """
        pass

    def __ndr_print_in__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print_in(object) -> None
        NDR print input
        """
        pass

    def __ndr_print_out__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print_out(object) -> None
        NDR print output
        """
        pass

    def __ndr_unpack_in__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack_in(class, blob, bigendian=False, ndr64=False, allow_remaining=False) -> None
        NDR unpack input
        """
        pass

    def __ndr_unpack_out__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack_out(class, blob, bigendian=False, ndr64=False, allow_remaining=False) -> None
        NDR unpack output
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    in_access_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type winreg_AccessMask"""

    in_action_taken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type winreg_CreateAction"""

    in_handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type policy_handle"""

    in_keyclass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type winreg_String"""

    in_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type winreg_String"""

    in_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type winreg_KeyOptions"""

    in_secdesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type winreg_SecBuf"""

    out_action_taken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type winreg_CreateAction"""

    out_new_handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type policy_handle"""

    result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of type WERROR"""



