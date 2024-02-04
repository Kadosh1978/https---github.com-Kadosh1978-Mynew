# encoding: utf-8
# module samba.dcerpc.epmapper
# from /usr/lib/python3/dist-packages/samba/dcerpc/epmapper.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" epmapper DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class epm_Lookup(__talloc.BaseObject):
    # no doc
    @classmethod
    def opnum(cls): # real signature unknown; restored from __doc__
        """ epmapper.epm_Lookup.opnum() -> 2 (0x02) """
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

    in_entry_handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type policy_handle"""

    in_inquiry_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type epm_InquiryType"""

    in_interface_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type rpc_if_id_t"""

    in_max_ents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    in_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type GUID"""

    in_vers_option = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type epm_VersionOption"""

    out_entries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type epm_entry_t"""

    out_entry_handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type policy_handle"""

    out_num_ents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of type uint32"""



