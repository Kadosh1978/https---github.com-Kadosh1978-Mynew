# encoding: utf-8
# module samba.auth
# from /usr/lib/python3/dist-packages/samba/auth.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" Authentication and authorization support. """

# imports
import talloc as __talloc


# Variables with simple values

AUTH_SESSION_INFO_AUTHENTICATED = 2

AUTH_SESSION_INFO_DEFAULT_GROUPS = 1

AUTH_SESSION_INFO_NTLM = 16

AUTH_SESSION_INFO_SIMPLE_PRIVILEGES = 4

# functions

def admin_session(*args, **kwargs): # real signature unknown
    pass

def copy_session_info(*args, **kwargs): # real signature unknown
    pass

def session_info_fill_unix(*args, **kwargs): # real signature unknown
    pass

def session_info_set_unix(*args, **kwargs): # real signature unknown
    pass

def system_session(*args, **kwargs): # real signature unknown
    pass

def user_session(*args, **kwargs): # real signature unknown
    pass

# classes

class AuthContext(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d570>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.auth', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d570>, origin='/usr/lib/python3/dist-packages/samba/auth.cpython-310-x86_64-linux-gnu.so')"

