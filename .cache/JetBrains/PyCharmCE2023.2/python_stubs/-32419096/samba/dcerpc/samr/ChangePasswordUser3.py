# encoding: utf-8
# module samba.dcerpc.samr
# from /usr/lib/python3/dist-packages/samba/dcerpc/samr.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" samr DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class ChangePasswordUser3(__talloc.BaseObject):
    # no doc
    @classmethod
    def opnum(cls): # real signature unknown; restored from __doc__
        """ samr.ChangePasswordUser3.opnum() -> 63 (0x3f) """
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

    in_account = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    in_lm_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    in_lm_password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type samr_CryptPassword"""

    in_lm_verifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type samr_Password"""

    in_nt_password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type samr_CryptPassword"""

    in_nt_verifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type samr_Password"""

    in_password3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type samr_CryptPassword"""

    in_server = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    out_dominfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type samr_DomInfo1"""

    out_reject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type userPwdChangeFailureInformation"""

    result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of type NTSTATUS"""



