# encoding: utf-8
# module gevent._gevent_c_imap
# from /home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_c_imap.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" Iterators across greenlets or AsyncResult objects. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import gevent.lock as lock # /home/kadosh/.local/lib/python3.10/site-packages/gevent/lock.py
import gevent._gevent_cqueue as queue # /home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_cqueue.cpython-310-x86_64-linux-gnu.so
from gevent._gevent_cgreenlet import Greenlet

from gevent._gevent_cqueue import UnboundQueue

from gevent._gevent_c_semaphore import Semaphore

import gevent._gevent_cgreenlet as __gevent__gevent_cgreenlet


# functions

def import_c_accel(globs, cname): # reliably restored by inspect
    """
    Import the C-accelerator for the *cname*
        and copy its globals.
    
        The *cname* should be hardcoded to match the expected
        C accelerator module.
    
        Unless PURE_PYTHON is set (in the environment or automatically
        on PyPy), then the C-accelerator is required.
    """
    pass

# classes

class Failure(object):
    """ Failure(exc, raise_exception=None) """
    def __init__(self, exc, raise_exception=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    exc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __slots__ = (
        'exc',
        'raise_exception',
    )


class IMapUnordered(__gevent__gevent_cgreenlet.Greenlet):
    """
    IMapUnordered(func, iterable, spawn, maxsize=None, _zipped=False)
    
        At iterator of map results.
    """
    def next(self, *args, **kwargs): # real signature unknown
        pass

    def _on_result(self, greenlet): # real signature unknown; restored from __doc__
        """ IMapUnordered._on_result(self, greenlet) """
        pass

    def _run(self): # real signature unknown; restored from __doc__
        """ IMapUnordered._run(self) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        An iterator that.
        
                :param callable spawn: The function we use to create new greenlets.
                :keyword int maxsize: If given and not-None, specifies the maximum number of
                    finished results that will be allowed to accumulated awaiting the reader;
                    more than that number of results will cause map function greenlets to begin
                    to block. This is most useful is there is a great disparity in the speed of
                    the mapping code and the consumer and the results consume a great deal of resources.
                    Using a bound is more computationally expensive than not using a bound.
        
                .. versionchanged:: 1.1b3
                    Added the *maxsize* parameter.
        """
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        pass

    finished = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    queue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f751643d1d0>'


class IMap(IMapUnordered):
    """ IMap(*args, **kwargs) """
    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f751643d200>'


# variables with complex values

__all__ = [
    'IMapUnordered',
    'IMap',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f751643d240>'

__pyx_capi__ = {
    '_raise_exc': None, # (!) real value is '<capsule object "PyObject *(struct __pyx_obj_6gevent_14_gevent_c_imap_Failure *)" at 0x7f75164461f0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent._gevent_c_imap', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f751643d240>, origin='/home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_c_imap.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

