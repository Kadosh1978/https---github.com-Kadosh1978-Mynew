# encoding: utf-8
# module gevent._gevent_c_semaphore
# from /home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_c_semaphore.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from gevent._gevent_c_abstract_linkable import AbstractLinkable

from gevent._gevent_c_hub_local import get_hub_if_exists, get_hub_noargs

import gevent._gevent_c_abstract_linkable as __gevent__gevent_c_abstract_linkable


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

class Semaphore(__gevent__gevent_c_abstract_linkable.AbstractLinkable):
    """
    Semaphore(value=1, hub=None)
    
        Semaphore(value=1) -> Semaphore
    
        .. seealso:: :class:`BoundedSemaphore` for a safer version that prevents
           some classes of bugs. If unsure, most users should opt for `BoundedSemaphore`.
    
        A semaphore manages a counter representing the number of `release`
        calls minus the number of `acquire` calls, plus an initial value.
        The `acquire` method blocks if necessary until it can return
        without making the counter negative. A semaphore does not track ownership
        by greenlets; any greenlet can call `release`, whether or not it has previously
        called `acquire`.
    
        If not given, ``value`` defaults to 1.
    
        The semaphore is a context manager and can be used in ``with`` statements.
    
        This Semaphore's ``__exit__`` method does not call the trace function
        on CPython, but does under PyPy.
    
        .. versionchanged:: 1.4.0
            Document that the order in which waiters are awakened is not specified. It was not
            specified previously, but due to CPython implementation quirks usually went in FIFO order.
        .. versionchanged:: 1.5a3
           Waiting greenlets are now awakened in the order in which they waited.
        .. versionchanged:: 1.5a3
           The low-level ``rawlink`` method (most users won't use this) now automatically
           unlinks waiters before calling them.
        .. versionchanged:: 20.12.0
           Improved support for multi-threaded usage. When multi-threaded usage is detected,
           instances will no longer create the thread's hub if it's not present.
    """
    def acquire(self, bool_blocking=True, timeout=None): # real signature unknown; restored from __doc__
        """
        Semaphore.acquire(self, bool blocking=True, timeout=None) -> bool
        
                acquire(blocking=True, timeout=None) -> bool
        
                Acquire the semaphore.
        
                .. note:: If this semaphore was initialized with a *value* of 0,
                   this method will block forever (unless a timeout is given or blocking is
                   set to false).
        
                :keyword bool blocking: If True (the default), this function will block
                   until the semaphore is acquired.
                :keyword float timeout: If given, and *blocking* is true,
                   specifies the maximum amount of seconds
                   this method will block.
                :return: A `bool` indicating whether the semaphore was acquired.
                   If ``blocking`` is True and ``timeout`` is None (the default), then
                   (so long as this semaphore was initialized with a size greater than 0)
                   this will always return True. If a timeout was given, and it expired before
                   the semaphore was acquired, False will be returned. (Note that this can still
                   raise a ``Timeout`` exception, if some other caller had already started a timer.)
        """
        return False

    def locked(self): # real signature unknown; restored from __doc__
        """
        Semaphore.locked(self) -> bool
        
                Return a boolean indicating whether the semaphore can be
                acquired (`False` if the semaphore *can* be acquired). Most
                useful with binary semaphores (those with an initial value of 1).
        
                :rtype: bool
        """
        return False

    def ready(self): # real signature unknown; restored from __doc__
        """
        Semaphore.ready(self) -> bool
        
                Return a boolean indicating whether the semaphore can be
                acquired (`True` if the semaphore can be acquired).
        
                :rtype: bool
        """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """
        Semaphore.release(self) -> int
        
                Release the semaphore, notifying any waiters if needed. There
                is no return value.
        
                .. note::
        
                    This can be used to over-release the semaphore.
                    (Release more times than it has been acquired or was initially
                    created with.)
        
                    This is usually a sign of a bug, but under some circumstances it can be
                    used deliberately, for example, to model the arrival of additional
                    resources.
        
                :rtype: None
        """
        return 0

    def wait(self, timeout=None): # real signature unknown; restored from __doc__
        """
        Semaphore.wait(self, timeout=None) -> int
        
                Wait until it is possible to acquire this semaphore, or until the optional
                *timeout* elapses.
        
                .. note:: If this semaphore was initialized with a *value* of 0,
                   this method will block forever if no timeout is given.
        
                :keyword float timeout: If given, specifies the maximum amount of seconds
                   this method will block.
                :return: A number indicating how many times the semaphore can be acquired
                    before blocking. *This could be 0,* if other waiters acquired
                    the semaphore.
                :rtype: int
        """
        return 0

    def _py3k_acquire(self, *args, **kwargs): # real signature unknown
        """
        Semaphore.acquire(self, bool blocking=True, timeout=None) -> bool
        
                acquire(blocking=True, timeout=None) -> bool
        
                Acquire the semaphore.
        
                .. note:: If this semaphore was initialized with a *value* of 0,
                   this method will block forever (unless a timeout is given or blocking is
                   set to false).
        
                :keyword bool blocking: If True (the default), this function will block
                   until the semaphore is acquired.
                :keyword float timeout: If given, and *blocking* is true,
                   specifies the maximum amount of seconds
                   this method will block.
                :return: A `bool` indicating whether the semaphore was acquired.
                   If ``blocking`` is True and ``timeout`` is None (the default), then
                   (so long as this semaphore was initialized with a size greater than 0)
                   this will always return True. If a timeout was given, and it expired before
                   the semaphore was acquired, False will be returned. (Note that this can still
                   raise a ``Timeout`` exception, if some other caller had already started a timer.)
        """
        pass

    def _Semaphore__acquire_from_other_thread_cb(self, *args, **kwargs): # real signature unknown
        """ Semaphore.__acquire_from_other_thread_cb(self, list results, bool blocking, timeout, thread_lock) """
        pass

    def _start_notify(self): # real signature unknown; restored from __doc__
        """ Semaphore._start_notify(self) """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ Semaphore.__enter__(self) """
        pass

    def __exit__(self, t, v, tb): # real signature unknown; restored from __doc__
        """ Semaphore.__exit__(self, t, v, tb) """
        pass

    def __init__(self, value=1, hub=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    counter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """counter: 'int'"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f75163bcf00>'
    __slots__ = (
        'counter',
        '_multithreaded',
    )


class BoundedSemaphore(Semaphore):
    """
    BoundedSemaphore(*args, **kwargs)
    
        BoundedSemaphore(value=1) -> BoundedSemaphore
    
        A bounded semaphore checks to make sure its current value doesn't
        exceed its initial value. If it does, :class:`ValueError` is
        raised. In most situations semaphores are used to guard resources
        with limited capacity. If the semaphore is released too many times
        it's a sign of a bug.
    
        If not given, *value* defaults to 1.
    """
    def release(self): # real signature unknown; restored from __doc__
        """
        BoundedSemaphore.release(self) -> int
        
                Like :meth:`Semaphore.release`, but raises :class:`ValueError`
                if the semaphore is being over-released.
        """
        return 0

    def _at_fork_reinit(self): # real signature unknown; restored from __doc__
        """ BoundedSemaphore._at_fork_reinit(self) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _initial_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _OVER_RELEASE_ERROR = ValueError
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f75163bce70>'
    __slots__ = (
        '_initial_value',
    )


class _LockReleaseLink(object):
    """ _LockReleaseLink(lock) """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, lock): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __slots__ = (
        'lock',
    )


# variables with complex values

__all__ = [
    'Semaphore',
    'BoundedSemaphore',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f751643d240>'

__pyx_capi__ = {
    'InvalidThreadUseError': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75164461f0>'
    'LoopExit': None, # (!) real value is '<capsule object "PyObject *" at 0x7f751643d1d0>'
    'Timeout': None, # (!) real value is '<capsule object "PyObject *" at 0x7f751643d200>'
    '_MULTI': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75163bcd50>'
    '_UNSET': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75163bd590>'
    '_native_sleep': None, # (!) real value is '<capsule object "PyObject *" at 0x7f751643e700>'
    'monotonic': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75163be8e0>'
    'spawn_raw': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75163bd5f0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent._gevent_c_semaphore', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f751643d240>, origin='/home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_c_semaphore.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

