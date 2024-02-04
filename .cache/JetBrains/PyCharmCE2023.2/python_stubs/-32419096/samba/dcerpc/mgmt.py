# encoding: utf-8
# module samba.dcerpc.mgmt
# from /usr/lib/python3/dist-packages/samba/dcerpc/mgmt.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" mgmt DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

MGMT_STATS_ARRAY_MAX_SIZE = 4

MGMT_STATS_CALLS_IN = 0
MGMT_STATS_CALLS_OUT = 1

MGMT_STATS_PKTS_IN = 2
MGMT_STATS_PKTS_OUT = 3

# no functions
# classes

class mgmt_abstract_syntax(__misc.ndr_syntax_id):
    """
    mgmt_abstract_syntax()
    DCE/RPC Remote Management
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


abstract_syntax = mgmt_abstract_syntax


class inq_if_ids(__talloc.BaseObject):
    # no doc
    @classmethod
    def opnum(cls): # real signature unknown; restored from __doc__
        """ mgmt.inq_if_ids.opnum() -> 0 (0x00) """
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

    out_if_id_vector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type rpc_if_id_vector_t"""

    result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of type WERROR"""



class inq_princ_name(__talloc.BaseObject):
    # no doc
    @classmethod
    def opnum(cls): # real signature unknown; restored from __doc__
        """ mgmt.inq_princ_name.opnum() -> 4 (0x04) """
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

    in_authn_proto = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    in_princ_name_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    out_princ_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of type WERROR"""



class inq_stats(__talloc.BaseObject):
    # no doc
    @classmethod
    def opnum(cls): # real signature unknown; restored from __doc__
        """ mgmt.inq_stats.opnum() -> 1 (0x01) """
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

    in_max_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    in_unknown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    out_statistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type mgmt_statistics"""

    result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of type WERROR"""



class is_server_listening(__talloc.BaseObject):
    # no doc
    @classmethod
    def opnum(cls): # real signature unknown; restored from __doc__
        """ mgmt.is_server_listening.opnum() -> 2 (0x02) """
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

    out_status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of type uint32"""



class mgmt(__dcerpc.ClientConnection):
    """
    mgmt(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    DCE/RPC Remote Management
    """
    def inq_if_ids(self): # real signature unknown; restored from __doc__
        """ S.inq_if_ids() -> if_id_vector """
        pass

    def inq_princ_name(self, authn_proto, princ_name_size): # real signature unknown; restored from __doc__
        """ S.inq_princ_name(authn_proto, princ_name_size) -> princ_name """
        pass

    def inq_stats(self, max_count, unknown): # real signature unknown; restored from __doc__
        """ S.inq_stats(max_count, unknown) -> statistics """
        return statistics

    def is_server_listening(self): # real signature unknown; restored from __doc__
        """ S.is_server_listening() -> (status, result) """
        pass

    def stop_server_listening(self): # real signature unknown; restored from __doc__
        """ S.stop_server_listening() -> None """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ndr_syntax_id_p(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type ndr_syntax_id"""



class rpc_if_id_vector_t(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    if_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type ndr_syntax_id_p"""



class statistics(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    statistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""



class stop_server_listening(__talloc.BaseObject):
    # no doc
    @classmethod
    def opnum(cls): # real signature unknown; restored from __doc__
        """ mgmt.stop_server_listening.opnum() -> 3 (0x03) """
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

    result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of type WERROR"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.mgmt', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/mgmt.cpython-310-x86_64-linux-gnu.so')"

