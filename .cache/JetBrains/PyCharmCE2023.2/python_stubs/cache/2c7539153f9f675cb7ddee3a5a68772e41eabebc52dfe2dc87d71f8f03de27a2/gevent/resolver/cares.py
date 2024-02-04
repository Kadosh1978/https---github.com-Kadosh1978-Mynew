# encoding: utf-8
# module gevent.resolver.cares
# from /home/kadosh/.local/lib/python3.10/site-packages/gevent/resolver/cares.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import _socket as _socket # <module '_socket' (built-in)>

# Variables with simple values

MAC = False

# no functions
# classes

class ares_host_result(tuple):
    # no doc
    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gevent.resolver.cares', '__new__': <staticmethod(<cyfunction ares_host_result.__new__ at 0x7f75161d2190>)>, '__getnewargs__': <cyfunction ares_host_result.__getnewargs__ at 0x7f75161d2260>, '__dict__': <attribute '__dict__' of 'ares_host_result' objects>, '__doc__': None})"


class channel(object):
    # no doc
    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def getaddrinfo(self, *args, **kwargs): # real signature unknown
        pass

    def gethostbyaddr(self, *args, **kwargs): # real signature unknown
        pass

    def gethostbyname(self, *args, **kwargs): # real signature unknown
        pass

    def getnameinfo(self, *args, **kwargs): # real signature unknown
        pass

    def set_servers(self, *args, **kwargs): # real signature unknown
        pass

    def _getnameinfo(self, *args, **kwargs): # real signature unknown
        pass

    def _on_timer(self, *args, **kwargs): # real signature unknown
        pass

    def _process_fd(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f751643d1d0>'


class gaierror(OSError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class herror(OSError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class InvalidIP(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Result(object):
    # no doc
    def get(self, *args, **kwargs): # real signature unknown
        pass

    def successful(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    exception = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__all__ = [
    'channel',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f751643e290>'

__spec__ = None # (!) real value is "ModuleSpec(name='gevent.resolver.cares', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f751643e290>, origin='/home/kadosh/.local/lib/python3.10/site-packages/gevent/resolver/cares.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

