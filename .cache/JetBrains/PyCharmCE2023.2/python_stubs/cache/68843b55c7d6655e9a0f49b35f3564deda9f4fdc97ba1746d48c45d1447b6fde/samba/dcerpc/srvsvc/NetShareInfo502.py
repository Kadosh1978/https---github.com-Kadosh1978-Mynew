# encoding: utf-8
# module samba.dcerpc.srvsvc
# from /usr/lib/python3/dist-packages/samba/dcerpc/srvsvc.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" srvsvc DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class NetShareInfo502(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    current_users = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    max_users = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    permissions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    sd_buf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type sec_desc_buf"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type srvsvc_ShareType"""



