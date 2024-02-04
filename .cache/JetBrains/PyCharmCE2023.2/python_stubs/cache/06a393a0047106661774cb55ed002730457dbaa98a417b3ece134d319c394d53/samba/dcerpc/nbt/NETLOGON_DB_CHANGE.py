# encoding: utf-8
# module samba.dcerpc.nbt
# from /usr/lib/python3/dist-packages/samba/dcerpc/nbt.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" nbt DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class NETLOGON_DB_CHANGE(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    dbchange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type nbt_db_change_info"""

    db_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type string"""

    message_format_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    message_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    pdc_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type string"""

    pulse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    random = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    serial_lo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dom_sid0"""

    sid_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type time_t"""

    unicode_domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type string"""

    unicode_pdc_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type string"""

    _pad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DATA_BLOB"""



