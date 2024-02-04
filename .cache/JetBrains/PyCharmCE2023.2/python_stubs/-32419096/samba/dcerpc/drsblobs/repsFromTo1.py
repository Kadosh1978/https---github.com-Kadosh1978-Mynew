# encoding: utf-8
# module samba.dcerpc.drsblobs
# from /usr/lib/python3/dist-packages/samba/dcerpc/drsblobs.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" drsblobs DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class repsFromTo1(__talloc.BaseObject):
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

    blobsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    consecutive_sync_failures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    highwatermark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type drsuapi_DsReplicaHighWaterMark"""

    last_attempt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type NTTIME_1sec"""

    last_success = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type NTTIME_1sec"""

    other_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type repsFromTo1OtherInfo"""

    other_info_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    replica_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type drsuapi_DrsOptions"""

    reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    result_last_attempt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type WERROR"""

    schedule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    source_dsa_invocation_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type GUID"""

    source_dsa_obj_guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type GUID"""

    transport_guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type GUID"""



