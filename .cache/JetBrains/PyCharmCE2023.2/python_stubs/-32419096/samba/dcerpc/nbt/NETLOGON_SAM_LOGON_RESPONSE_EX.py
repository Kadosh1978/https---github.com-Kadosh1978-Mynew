# encoding: utf-8
# module samba.dcerpc.nbt
# from /usr/lib/python3/dist-packages/samba/dcerpc/nbt.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" nbt DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class NETLOGON_SAM_LOGON_RESPONSE_EX(__talloc.BaseObject):
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

    client_site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type nbt_string"""

    command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type netlogon_command"""

    dns_domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type nbt_string"""

    domain_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type nbt_string"""

    domain_uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type GUID"""

    forest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type nbt_string"""

    lm20_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    lmnt_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    next_closest_site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type nbt_string"""

    nt_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type netlogon_nt_version_flags"""

    pdc_dns_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type nbt_string"""

    pdc_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type nbt_string"""

    sbz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    server_site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type nbt_string"""

    server_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type nbt_server_type"""

    sockaddr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type nbt_sockaddr"""

    sockaddr_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    user_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type nbt_string"""



