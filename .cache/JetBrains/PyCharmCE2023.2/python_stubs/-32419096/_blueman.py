# encoding: utf-8
# module _blueman
# from /usr/lib/python3/dist-packages/_blueman.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import logging as logging # /usr/lib/python3.10/logging/__init__.py

# Variables with simple values

RFCOMM_HANGUP_NOW = 2

RFCOMM_RELEASE_ONHUP = 1

RFCOMM_REUSE_DLC = 0

RFCOMM_TTY_ATTACHED = 3

# functions

def create_bridge(*args, **kwargs): # real signature unknown
    pass

def create_rfcomm_device(*args, **kwargs): # real signature unknown
    pass

def destroy_bridge(*args, **kwargs): # real signature unknown
    pass

def device_info(*args, **kwargs): # real signature unknown
    pass

def get_rfcomm_channel(*args, **kwargs): # real signature unknown
    pass

def page_timeout(*args, **kwargs): # real signature unknown
    pass

def release_rfcomm_device(*args, **kwargs): # real signature unknown
    pass

def rfcomm_list(*args, **kwargs): # real signature unknown
    pass

# classes

class BridgeException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class ConnInfoReadError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class conn_info(object):
    # no doc
    def deinit(self, *args, **kwargs): # real signature unknown
        pass

    def get_lq(self, *args, **kwargs): # real signature unknown
        pass

    def get_rssi(self, *args, **kwargs): # real signature unknown
        pass

    def get_tpl(self, *args, **kwargs): # real signature unknown
        pass

    def init(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    failed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class RFCOMMError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

ERR = {
    -15: "Can't release RFCOMM TTY",
    -14: "Can't create RFCOMM TTY",
    -13: "Can't connect RFCOMM socket",
    -12: "Can't bind RFCOMM socket",
    -11: 'ERR_READ_PAGE_TIMEOUT',
    -10: 'ERR_CANT_READ_PAGE_TIMEOUT',
    -9: 'ERR_SOCKET_FAILED',
    -8: 'Getting rfcomm list failed',
    -7: 'Read Link quality failed',
    -6: 'Read transmit power level request failed',
    -5: 'Read RSSI failed',
    -4: 'Get connection info failed',
    -3: 'Not connected',
    -2: 'HCI device open failed',
    -1: "Can't allocate memory",
}

RFCOMM_STATES = [
    'unknown',
    'connected',
    'clean',
    'bound',
    'listening',
    'connecting',
    'connecting',
    'config',
    'disconnecting',
    'closed',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2dba0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_blueman', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2dba0>, origin='/usr/lib/python3/dist-packages/_blueman.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

