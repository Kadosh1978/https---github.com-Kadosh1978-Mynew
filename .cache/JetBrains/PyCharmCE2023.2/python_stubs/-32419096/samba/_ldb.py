# encoding: utf-8
# module samba._ldb
# from /usr/lib/python3/dist-packages/samba/_ldb.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" Samba-specific LDB python bindings """

# imports
import ldb as __ldb


# Variables with simple values

SYNTAX_SAMBA_INT32 = 'LDB_SYNTAX_SAMBA_INT32'

# functions

def register_samba_handlers(): # real signature unknown; restored from __doc__
    """
    register_samba_handlers()
    Register Samba-specific LDB modules and schemas.
    """
    pass

def samba_schema_attribute_add(*args, **kwargs): # real signature unknown
    pass

def set_credentials(credentials): # real signature unknown; restored from __doc__
    """
    ldb_set_credentials(credentials)
    Set credentials to use when connecting.
    """
    pass

def set_loadparm(session_info): # real signature unknown; restored from __doc__
    """
    ldb_set_loadparm(session_info)
    Set loadparm context to use when connecting.
    """
    pass

def set_opaque_integer(*args, **kwargs): # real signature unknown
    pass

def set_session_info(session_info): # real signature unknown; restored from __doc__
    """
    set_session_info(session_info)
    Set session info to use when connecting.
    """
    pass

def set_utf8_casefold(): # real signature unknown; restored from __doc__
    """
    ldb_set_utf8_casefold()
    Set the right Samba casefolding function for UTF8 charset.
    """
    pass

# classes

class Ldb(__ldb.Ldb):
    """ Connection to a LDB database. """
    def register_samba_handlers(self): # real signature unknown; restored from __doc__
        """
        register_samba_handlers()
        Register Samba-specific LDB modules and schemas.
        """
        pass

    def samba_schema_attribute_add(self, *args, **kwargs): # real signature unknown
        pass

    def set_credentials(self, credentials): # real signature unknown; restored from __doc__
        """
        ldb_set_credentials(credentials)
        Set credentials to use when connecting.
        """
        pass

    def set_loadparm(self, session_info): # real signature unknown; restored from __doc__
        """
        ldb_set_loadparm(session_info)
        Set loadparm context to use when connecting.
        """
        pass

    def set_opaque_integer(self, *args, **kwargs): # real signature unknown
        pass

    def set_session_info(self, session_info): # real signature unknown; restored from __doc__
        """
        set_session_info(session_info)
        Set session info to use when connecting.
        """
        pass

    def set_utf8_casefold(self): # real signature unknown; restored from __doc__
        """
        ldb_set_utf8_casefold()
        Set the right Samba casefolding function for UTF8 charset.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d39030>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba._ldb', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d39030>, origin='/usr/lib/python3/dist-packages/samba/_ldb.cpython-310-x86_64-linux-gnu.so')"

