# encoding: utf-8
# module samba.dcerpc.krb5ccache
# from /usr/lib/python3/dist-packages/samba/dcerpc/krb5ccache.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" krb5ccache DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# no functions
# classes

class krb5ccache_abstract_syntax(__misc.ndr_syntax_id):
    """
    krb5ccache_abstract_syntax()
    KRB5 credentials cache
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


abstract_syntax = krb5ccache_abstract_syntax


class ADDRESS(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    addrtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DATA_BLOB"""



class ADDRESSES(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type ADDRESS"""



class AUTHDATA(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type AUTHDATUM"""



class AUTHDATUM(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    ad_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DATA_BLOB"""



class CCACHE(__talloc.BaseObject):
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

    cred = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type CREDENTIAL"""

    further_creds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DATA_BLOB"""

    optional_header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type OPTIONAL_HEADER"""

    principal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type PRINCIPAL"""

    pvno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""



class CREDENTIAL(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    addresses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type ADDRESSES"""

    authdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type AUTHDATA"""

    authtime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    client = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type PRINCIPAL"""

    endtime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    is_skey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    keyblock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type KEYBLOCK"""

    renew_till = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    second_ticket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DATA_BLOB"""

    server = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type PRINCIPAL"""

    starttime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    ticket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DATA_BLOB"""

    ticket_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""



class DELTATIME_TAG(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    kdc_sec_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type int32"""

    kdc_usec_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type int32"""



class FIELD(__talloc.BaseObject):
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


class KEYBLOCK(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DATA_BLOB"""

    enctype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""



class krb5ccache(__dcerpc.ClientConnection):
    """
    krb5ccache(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    KRB5 credentials cache
    """
    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class MULTIPLE_CREDENTIALS(__talloc.BaseObject):
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

    cred = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type CREDENTIAL"""

    further_creds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DATA_BLOB"""



class OPTIONAL_HEADER(__talloc.BaseObject):
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


class PRINCIPAL(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type string"""

    component_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    name_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    realm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type string"""



class V4HEADER(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    v4tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type V4TAGS"""



class V4TAG(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    field = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type FIELD"""

    tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""



class V4TAGS(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    further_tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DATA_BLOB"""

    tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type V4TAG"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.krb5ccache', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/krb5ccache.cpython-310-x86_64-linux-gnu.so')"

