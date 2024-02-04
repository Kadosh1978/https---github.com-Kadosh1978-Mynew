# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python3/dist-packages/samba/dcerpc/drsuapi.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DsGetNCChangesRequest5(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    destination_dsa_guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type GUID"""

    extended_op = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type drsuapi_DsExtendedOperation"""

    fsmo_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type hyper"""

    highwatermark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type drsuapi_DsReplicaHighWaterMark"""

    max_ndr_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    max_object_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    naming_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type drsuapi_DsReplicaObjectIdentifier"""

    replica_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type drsuapi_DrsOptions"""

    source_dsa_invocation_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type GUID"""

    uptodateness_vector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type drsuapi_DsReplicaCursorCtrEx"""



