# encoding: utf-8
# module samba.dcerpc.smb_acl
# from /usr/lib/python3/dist-packages/samba/dcerpc/smb_acl.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" smb_acl DCE/RPC """

# imports
import talloc as __talloc


# Variables with simple values

SMB_ACL_EXECUTE = 1

SMB_ACL_FIRST_ENTRY = 0

SMB_ACL_GROUP = 3

SMB_ACL_GROUP_OBJ = 4

SMB_ACL_MASK = 6

SMB_ACL_NEXT_ENTRY = 1

SMB_ACL_OTHER = 5
SMB_ACL_READ = 4

SMB_ACL_TAG_INVALID = 0

SMB_ACL_TYPE_ACCESS = 0
SMB_ACL_TYPE_DEFAULT = 1

SMB_ACL_USER = 1

SMB_ACL_USER_OBJ = 2

SMB_ACL_WRITE = 2

# no functions
# classes

class entry(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    a_perm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    a_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type smb_acl_tag_t"""

    info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type smb_acl_entry_info"""



class entry_info(__talloc.BaseObject):
    # no doc
    @classmethod
    def __export__(cls, mem_ctx, level, in_): # real signature unknown; restored from __doc__
        """ T.__export__(mem_ctx, level, in) => ret. """
        pass

    @classmethod
    def __import__(cls, mem_ctx, level, in_): # real signature unknown; restored from __doc__
        """ T.__import__(mem_ctx, level, in) => ret. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class group(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type gid_t"""



class t(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    acl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type smb_acl_entry"""

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type int32"""

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type int32"""



class user(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uid_t"""



class wrapper(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    access_acl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type smb_acl_t"""

    default_acl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type smb_acl_t"""

    group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type gid_t"""

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uid_t"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.smb_acl', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/smb_acl.cpython-310-x86_64-linux-gnu.so')"

