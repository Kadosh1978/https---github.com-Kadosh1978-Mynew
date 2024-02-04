# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python3/dist-packages/samba/dcerpc/drsuapi.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DsGetMembershipsCtr1(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    group_attrs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type security_GroupAttrs"""

    info_array = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type drsuapi_DsReplicaObjectIdentifier"""

    num_memberships = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    num_sids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    sids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dom_sid28"""

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type NTSTATUS"""



