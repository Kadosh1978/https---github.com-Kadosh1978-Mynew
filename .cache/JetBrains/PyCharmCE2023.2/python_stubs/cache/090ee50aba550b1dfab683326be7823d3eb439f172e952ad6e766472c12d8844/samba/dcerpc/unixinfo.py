# encoding: utf-8
# module samba.dcerpc.unixinfo
# from /usr/lib/python3/dist-packages/samba/dcerpc/unixinfo.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" unixinfo DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# no functions
# classes

class unixinfo_abstract_syntax(__misc.ndr_syntax_id):
    """
    unixinfo_abstract_syntax()
    Unixinfo specific stuff
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


abstract_syntax = unixinfo_abstract_syntax


class GetPWUid(__talloc.BaseObject):
    # no doc
    @classmethod
    def opnum(cls): # real signature unknown; restored from __doc__
        """ unixinfo.GetPWUid.opnum() -> 4 (0x04) """
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

    in_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    in_uids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type hyper"""

    out_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    out_infos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type unixinfo_GetPWUidInfo"""

    result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of type NTSTATUS"""



class GetPWUidInfo(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    homedir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    shell = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type NTSTATUS"""



class GidToSid(__talloc.BaseObject):
    # no doc
    @classmethod
    def opnum(cls): # real signature unknown; restored from __doc__
        """ unixinfo.GidToSid.opnum() -> 3 (0x03) """
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

    in_gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type hyper"""

    out_sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dom_sid"""

    result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of type NTSTATUS"""



class SidToGid(__talloc.BaseObject):
    # no doc
    @classmethod
    def opnum(cls): # real signature unknown; restored from __doc__
        """ unixinfo.SidToGid.opnum() -> 2 (0x02) """
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

    in_sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dom_sid"""

    out_gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type hyper"""

    result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of type NTSTATUS"""



class SidToUid(__talloc.BaseObject):
    # no doc
    @classmethod
    def opnum(cls): # real signature unknown; restored from __doc__
        """ unixinfo.SidToUid.opnum() -> 0 (0x00) """
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

    in_sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dom_sid"""

    out_uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type hyper"""

    result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of type NTSTATUS"""



class UidToSid(__talloc.BaseObject):
    # no doc
    @classmethod
    def opnum(cls): # real signature unknown; restored from __doc__
        """ unixinfo.UidToSid.opnum() -> 1 (0x01) """
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

    in_uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type hyper"""

    out_sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dom_sid"""

    result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of type NTSTATUS"""



class unixinfo(__dcerpc.ClientConnection):
    """
    unixinfo(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Unixinfo specific stuff
    """
    def GetPWUid(self, uids): # real signature unknown; restored from __doc__
        """ S.GetPWUid(uids) -> infos """
        pass

    def GidToSid(self, gid): # real signature unknown; restored from __doc__
        """ S.GidToSid(gid) -> sid """
        pass

    def SidToGid(self, sid): # real signature unknown; restored from __doc__
        """ S.SidToGid(sid) -> gid """
        pass

    def SidToUid(self, sid): # real signature unknown; restored from __doc__
        """ S.SidToUid(sid) -> uid """
        pass

    def UidToSid(self, uid): # real signature unknown; restored from __doc__
        """ S.UidToSid(uid) -> sid """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.unixinfo', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/unixinfo.cpython-310-x86_64-linux-gnu.so')"

