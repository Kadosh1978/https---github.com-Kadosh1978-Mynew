# encoding: utf-8
# module samba._glue
# from /usr/lib/python3/dist-packages/samba/_glue.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" Python bindings for miscellaneous Samba functions. """
# no imports

# Variables with simple values

version = '4.15.13-Ubuntu'

# functions

def check_password_quality(pass_): # real signature unknown; restored from __doc__
    """
    check_password_quality(pass) -> bool
    Check password quality against Samba's check_password_quality,the implementation of Microsoft's rules:http://msdn.microsoft.com/en-us/subscriptions/cc786468%28v=ws.10%29.aspx
    """
    return False

def fault_setup(*args, **kwargs): # real signature unknown
    """ setup the default samba panic handler """
    pass

def float2nttime(*args, **kwargs): # real signature unknown
    """ pytime2nttime(floattimestamp) -> nttime """
    pass

def generate_random_bytes(len): # real signature unknown; restored from __doc__
    """
    generate_random_bytes(len) -> bytes
    Generate random bytes with specified length.
    """
    return b""

def generate_random_machine_password(min, max): # real signature unknown; restored from __doc__
    """
    generate_random_machine_password(min, max) -> string
    Generate random password (based on random utf16 characters converted to utf8 or random ascii characters if 'unix charset' is not 'utf8')with a length >= min (at least 14) and <= max (at most 255).
    """
    return ""

def generate_random_password(min, max): # real signature unknown; restored from __doc__
    """
    generate_random_password(min, max) -> string
    Generate random password (based on printable ascii characters) with a length >= min and <= max.
    """
    return ""

def generate_random_str(len): # real signature unknown; restored from __doc__
    """
    generate_random_str(len) -> string
    Generate random string with specified length.
    """
    return ""

def get_debug_level(*args, **kwargs): # real signature unknown
    """ get debug level """
    pass

def interface_ips(lp_ctx, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    interface_ips(lp_ctx[, all_interfaces) -> list_of_ifaces
    
    get interface IP address list
    """
    pass

def is_ad_dc_built(*args, **kwargs): # real signature unknown
    """ is Samba built with AD DC? """
    pass

def is_heimdal_built(*args, **kwargs): # real signature unknown
    """ is Samba built with Heimdal Kerberbos? """
    pass

def is_ntvfs_fileserver_built(*args, **kwargs): # real signature unknown
    """ is the NTVFS file server built in this installation? """
    pass

def is_selftest_enabled(*args, **kwargs): # real signature unknown
    """ is Samba built with selftest enabled? """
    pass

def ndr_token_max_list_size(*args, **kwargs): # real signature unknown
    """ How many NDR internal tokens is too many for this build? """
    pass

def nttime2float(*args, **kwargs): # real signature unknown
    """ nttime2pytime(nttime) -> floattimestamp """
    pass

def nttime2string(nttime): # real signature unknown; restored from __doc__
    """ nttime2string(nttime) -> string """
    return ""

def nttime2unix(nttime): # real signature unknown; restored from __doc__
    """ nttime2unix(nttime) -> timestamp """
    pass

def set_debug_level(*args, **kwargs): # real signature unknown
    """ set debug level """
    pass

def strcasecmp_m(): # real signature unknown; restored from __doc__
    """ (for testing) compare two strings using Samba's strcasecmp_m() """
    pass

def strstr_m(): # real signature unknown; restored from __doc__
    """ (for testing) find one string in another with Samba's strstr_m() """
    pass

def unix2nttime(timestamp): # real signature unknown; restored from __doc__
    """ unix2nttime(timestamp) -> nttime """
    pass

# classes

class DsExtendedError(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class HRESULTError(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class NTSTATUSError(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class WERRORError(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d388e0>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba._glue', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d388e0>, origin='/usr/lib/python3/dist-packages/samba/_glue.cpython-310-x86_64-linux-gnu.so')"

