# encoding: utf-8
# module samba.dcerpc.netlogon
# from /usr/lib/python3/dist-packages/samba/dcerpc/netlogon.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" netlogon DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class netr_PacInfo(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    auth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    auth_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    expansionroom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    logon_domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    logon_server = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    pac = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    pac_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    principal_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    unknown1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    unknown2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    unknown3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    unknown4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    user_session_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type netr_UserSessionKey"""



