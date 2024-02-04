# encoding: utf-8
# module samba.dcerpc.netlogon
# from /usr/lib/python3/dist-packages/samba/dcerpc/netlogon.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" netlogon DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class netr_DELTA_POLICY(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    auditingmode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    auditretentionperiod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type NTTIME"""

    db_create_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type NTTIME"""

    eventauditoptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    maxauditeventcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    maxlogsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    primary_domain_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    quota_limits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type netr_QUOTA_LIMITS"""

    sdbuf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type sec_desc_buf"""

    SecurityInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    sequence_num = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type udlong"""

    sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dom_sid2"""

    unknown1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    unknown2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    unknown3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    unknown4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    unknown5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    unknown6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    unknown7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    unknown8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""



