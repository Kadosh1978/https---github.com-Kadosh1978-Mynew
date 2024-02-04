# encoding: utf-8
# module samba.dcerpc.misc
# from /usr/lib/python3/dist-packages/samba/dcerpc/misc.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" misc DCE/RPC """

# imports
import talloc as __talloc


# Variables with simple values

REG_BINARY = 3
REG_DWORD = 4

REG_DWORD_BIG_ENDIAN = 5

REG_EXPAND_SZ = 2

REG_FULL_RESOURCE_DESCRIPTOR = 9

REG_LINK = 6

REG_MULTI_SZ = 7

REG_NONE = 0
REG_QWORD = 11

REG_RESOURCE_LIST = 8

REG_RESOURCE_REQUIREMENTS_LIST = 10

REG_SZ = 1

SAM_DATABASE_BUILTIN = 1
SAM_DATABASE_DOMAIN = 0
SAM_DATABASE_PRIVS = 2

SEC_CHAN_BDC = 6

SEC_CHAN_DNS_DOMAIN = 3

SEC_CHAN_DOMAIN = 4
SEC_CHAN_LANMAN = 5
SEC_CHAN_LOCAL = 1
SEC_CHAN_NULL = 0
SEC_CHAN_RODC = 7
SEC_CHAN_WKSTA = 2

SV_TYPE_AFP = 64
SV_TYPE_ALL = 4294967295

SV_TYPE_ALTERNATE_XPORT = 536870912

SV_TYPE_BACKUP_BROWSER = 131072

SV_TYPE_DFS_SERVER = 8388608

SV_TYPE_DIALIN_SERVER = 1024

SV_TYPE_DOMAIN_BAKCTRL = 16
SV_TYPE_DOMAIN_CTRL = 8
SV_TYPE_DOMAIN_ENUM = 2147483648
SV_TYPE_DOMAIN_MASTER = 524288
SV_TYPE_DOMAIN_MEMBER = 256

SV_TYPE_LOCAL_LIST_ONLY = 1073741824

SV_TYPE_MASTER_BROWSER = 262144

SV_TYPE_NOVELL = 128
SV_TYPE_NT = 4096

SV_TYPE_POTENTIAL_BROWSER = 65536

SV_TYPE_PRINTQ_SERVER = 512

SV_TYPE_SERVER = 2

SV_TYPE_SERVER_MFPN = 16384
SV_TYPE_SERVER_NT = 32768
SV_TYPE_SERVER_OSF = 1048576
SV_TYPE_SERVER_UNIX = 2048
SV_TYPE_SERVER_VMS = 2097152

SV_TYPE_SQLSERVER = 4

SV_TYPE_TIME_SOURCE = 32

SV_TYPE_WFW = 8192

SV_TYPE_WIN95_PLUS = 4194304

SV_TYPE_WORKSTATION = 1

# no functions
# classes

class GUID(__talloc.BaseObject):
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

    clock_seq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    time_hi_and_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    time_low = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    time_mid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""



class KRB5_EDATA_NTSTATUS(__talloc.BaseObject):
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

    ntstatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type NTSTATUS"""

    unknown1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    unknown2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""



class ndr_syntax_id(__talloc.BaseObject):
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

    if_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type GUID"""



class policy_handle(__talloc.BaseObject):
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

    handle_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type GUID"""



class winreg_Data(__talloc.BaseObject):
    # no doc
    @classmethod
    def __export__(cls, mem_ctx, level, in_): # real signature unknown; restored from __doc__
        """ T.__export__(mem_ctx, level, in) => ret. """
        pass

    @classmethod
    def __import__(cls, mem_ctx, level, in_): # real signature unknown; restored from __doc__
        """ T.__import__(mem_ctx, level, in) => ret. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class winreg_Data_GPO(__talloc.BaseObject):
    # no doc
    @classmethod
    def __export__(cls, mem_ctx, level, in_): # real signature unknown; restored from __doc__
        """ T.__export__(mem_ctx, level, in) => ret. """
        pass

    @classmethod
    def __import__(cls, mem_ctx, level, in_): # real signature unknown; restored from __doc__
        """ T.__import__(mem_ctx, level, in) => ret. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d399c0>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.misc', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d399c0>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/misc.cpython-310-x86_64-linux-gnu.so')"

