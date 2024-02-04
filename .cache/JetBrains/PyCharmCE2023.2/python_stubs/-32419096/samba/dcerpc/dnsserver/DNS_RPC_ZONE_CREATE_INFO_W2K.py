# encoding: utf-8
# module samba.dcerpc.dnsserver
# from /usr/lib/python3/dist-packages/samba/dcerpc/dnsserver.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" dnsserver DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DNS_RPC_ZONE_CREATE_INFO_W2K(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    aipMasters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type IP4_ARRAY"""

    aipSecondaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type IP4_ARRAY"""

    dwFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwReserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwReserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwReserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwReserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwReserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwReserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwReserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwReserved8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwZoneType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    fAging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    fAllowUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dns_zone_update"""

    fDsIntegrated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    fLoadExisting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    fNotifyLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DNS_ZONE_NOTIFY_LEVEL"""

    fSecureSecondaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DNS_ZONE_SECONDARY_SECURITY"""

    pszAdmin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pszDataFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pszZoneName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pvReserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pvReserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pvReserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pvReserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pvReserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pvReserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pvReserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pvReserved8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""



