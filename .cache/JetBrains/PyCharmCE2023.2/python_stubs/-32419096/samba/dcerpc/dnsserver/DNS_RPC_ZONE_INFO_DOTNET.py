# encoding: utf-8
# module samba.dcerpc.dnsserver
# from /usr/lib/python3/dist-packages/samba/dcerpc/dnsserver.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" dnsserver DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DNS_RPC_ZONE_INFO_DOTNET(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    aipLocalMasters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type IP4_ARRAY"""

    aipMasters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type IP4_ARRAY"""

    aipNotify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type IP4_ARRAY"""

    aipScavengeServers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type IP4_ARRAY"""

    aipSecondaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type IP4_ARRAY"""

    dwAvailForScavengeTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwDpFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwForwarderTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwLastSuccessfulSoaCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwLastSuccessfulXfr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwNoRefreshInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwRefreshInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwReserved0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
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

    dwRpcStructureVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dwZoneType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    fAging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    fAllowUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dns_zone_update"""

    fAutoCreated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    fForwarderSlave = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    fNotifyLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DNS_ZONE_NOTIFY_LEVEL"""

    fPaused = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    fReverse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    fSecureSecondaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DNS_ZONE_SECONDARY_SECURITY"""

    fShutdown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    fUseDatabase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    fUseNbstat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    fUseWins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    pReserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pReserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pReserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pReserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pszDataFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pszDpFqdn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pszZoneName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pwszZoneDn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""



