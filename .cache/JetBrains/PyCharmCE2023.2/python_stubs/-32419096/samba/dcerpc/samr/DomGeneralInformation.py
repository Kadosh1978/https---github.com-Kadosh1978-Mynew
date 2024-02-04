# encoding: utf-8
# module samba.dcerpc.samr
# from /usr/lib/python3/dist-packages/samba/dcerpc/samr.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" samr DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DomGeneralInformation(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    domain_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    domain_server_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type samr_DomainServerState"""

    force_logoff_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type NTTIME"""

    num_aliases = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    num_groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    num_users = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    oem_information = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    primary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_String"""

    role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type samr_Role"""

    sequence_num = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type udlong"""

    unknown3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""



