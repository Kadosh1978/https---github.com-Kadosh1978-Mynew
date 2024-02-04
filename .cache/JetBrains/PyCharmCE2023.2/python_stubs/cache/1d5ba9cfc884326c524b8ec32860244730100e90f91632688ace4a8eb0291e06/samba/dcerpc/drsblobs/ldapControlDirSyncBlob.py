# encoding: utf-8
# module samba.dcerpc.drsblobs
# from /usr/lib/python3/dist-packages/samba/dcerpc/drsblobs.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" drsblobs DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class ldapControlDirSyncBlob(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    extra = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type ldapControlDirSyncExtra"""

    extra_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    guid1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type GUID"""

    highwatermark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type drsuapi_DsReplicaHighWaterMark"""

    time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type NTTIME"""

    u1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    u2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    u3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""



