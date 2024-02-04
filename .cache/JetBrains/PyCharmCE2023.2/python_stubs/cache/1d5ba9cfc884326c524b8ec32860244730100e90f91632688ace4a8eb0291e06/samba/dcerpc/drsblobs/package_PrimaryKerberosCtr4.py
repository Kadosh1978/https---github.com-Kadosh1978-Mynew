# encoding: utf-8
# module samba.dcerpc.drsblobs
# from /usr/lib/python3/dist-packages/samba/dcerpc/drsblobs.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" drsblobs DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class package_PrimaryKerberosCtr4(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    default_iteration_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type package_PrimaryKerberosKey4"""

    num_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    num_older_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    num_old_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    num_service_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    older_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type package_PrimaryKerberosKey4"""

    old_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type package_PrimaryKerberosKey4"""

    salt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type package_PrimaryKerberosString"""

    service_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type package_PrimaryKerberosKey4"""



