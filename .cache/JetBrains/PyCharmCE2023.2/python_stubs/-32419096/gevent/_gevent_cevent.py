# encoding: utf-8
# module gevent._gevent_cevent
# from /home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_cevent.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" Basic synchronization primitives: Event and AsyncResult """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from gevent._gevent_c_abstract_linkable import AbstractLinkable

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

class AsyncResult(__gevent__gevent_c_abstract_linkable.AbstractLinkable):
    """
    AsyncResult()
    
        A one-time event that stores a value or an exception.
    
        Like :class:`Event` it wakes up all the waiters when :meth:`set`
        or :meth:`set_exception` is called. Waiters may receive the passed
        value or exception by calling :meth:`get` instead of :meth:`wait`.
        An :class:`AsyncResult` instance cannot be reset.
    
        .. important::
           This object is for communicating among greenlets within the
           same thread *only*! Do not try to use it to communicate across threads.
    
        To pass a value call :meth:`set`. Calls to :meth:`get` (those that
        are currently blocking as well as those made in the future) will
        return the value::
    
            >>> from gevent.event import AsyncResult
            >>> result = AsyncResult()
            >>> result.set(100)
            >>> result.get()
            100
    
        To pass an exception call :meth:`set_exception`. This will cause
        :meth:`get` to raise that exception::
    
            >>> result = AsyncResult()
            >>> result.set_exception(RuntimeError('failure'))
            >>> result.get()
            Traceback (most recent call last):
             ...
            RuntimeError: failure
    
        :class:`AsyncResult` implements :meth:`__call__` and thus can be
        used as :meth:`link` target::
    
            >>> import gevent
            >>> result = AsyncResult()
            >>> gevent.spawn(lambda : 1/0).link(result)
            >>> try:
            ...     result.get()
            ... except ZeroDivisionError:
            ...     print('ZeroDivisionError')
            ZeroDivisionError
    
        .. note::
    
            The order and timing in which waiting greenlets are awakened is not determined.
            As an implementation note, in gevent 1.1 and 1.0, waiting greenlets are awakened in a
            undetermined order sometime *after* the current greenlet yields to the event loop. Other greenlets
            (those not waiting to be awakened) may run between the current greenlet yielding and
            the waiting greenlets being awakened. These details may change in the future.
    
        .. versionchanged:: 1.1
    
           The exact order in which waiting greenlets
           are awakened is not the same as in 1.0.
    
        .. versionchanged:: 1.1
    
           Callbacks :meth:`linked <rawlink>` to this object are required to
           be hashable, and duplicates are merged.
    
        .. versionchanged:: 1.5a3
    
           Waiting greenlets are now awakened in the order in which they
           waited.
    
        .. versionchanged:: 1.5a3
    
           The low-level ``rawlink`` method
           (most users won't use this) now automatically unlinks waiters
           before calling them.
    """
    def cancel(self): # real signature unknown; restored from __doc__
        """ AsyncResult.cancel(self) -> bool """
        return False

    def cancelled(self): # real signature unknown; restored from __doc__
        """ AsyncResult.cancelled(self) -> bool """
        return False

    def done(self): # real signature unknown; restored from __doc__
        """ AsyncResult.done(self) -> bool """
        return False

    def get(self, block=True, timeout=None): # real signature unknown; restored from __doc__
        """
        AsyncResult.get(self, block=True, timeout=None)
        Return the stored value or raise the exception.
        
                If this instance already holds a value or an exception, return  or raise it immediately.
                Otherwise, block until another greenlet calls :meth:`set` or :meth:`set_exception` or
                until the optional timeout occurs.
        
                When the *timeout* argument is present and not ``None``, it should be a
                floating point number specifying a timeout for the operation in seconds
                (or fractions thereof). If the *timeout* elapses, the *Timeout* exception will
                be raised.
        
                :keyword bool block: If set to ``False`` and this instance is not ready,
                    immediately raise a :class:`Timeout` exception.
        """
        pass

    def get_nowait(self): # real signature unknown; restored from __doc__
        """
        AsyncResult.get_nowait(self)
        
                Return the value or raise the exception without blocking.
        
                If this object is not yet :meth:`ready <ready>`, raise
                :class:`gevent.Timeout` immediately.
        """
        pass

    def ready(self): # real signature unknown; restored from __doc__
        """
        AsyncResult.ready(self) -> bool
        Return true if and only if it holds a value or an exception
        """
        return False

    def result(self, timeout=None): # real signature unknown; restored from __doc__
        """ AsyncResult.result(self, timeout=None) """
        pass

    def set(self, value=None): # real signature unknown; restored from __doc__
        """
        AsyncResult.set(self, value=None)
        Store the value and wake up any waiters.
        
                All greenlets blocking on :meth:`get` or :meth:`wait` are awakened.
                Subsequent calls to :meth:`wait` and :meth:`get` will not block at all.
        """
        pass

    def set_exception(self, exception, exc_info=None): # real signature unknown; restored from __doc__
        """
        AsyncResult.set_exception(self, exception, exc_info=None)
        Store the exception and wake up any waiters.
        
                All greenlets blocking on :meth:`get` or :meth:`wait` are awakened.
                Subsequent calls to :meth:`wait` and :meth:`get` will not block at all.
        
                :keyword tuple exc_info: If given, a standard three-tuple of type, value, :class:`traceback`
                    as returned by :func:`sys.exc_info`. This will be used when the exception
                    is re-raised to propagate the correct traceback.
        """
        pass

    def set_result(self, *args, **kwargs): # real signature unknown
        """
        AsyncResult.set(self, value=None)
        Store the value and wake up any waiters.
        
                All greenlets blocking on :meth:`get` or :meth:`wait` are awakened.
                Subsequent calls to :meth:`wait` and :meth:`get` will not block at all.
        """
        pass

    def successful(self): # real signature unknown; restored from __doc__
        """
        AsyncResult.successful(self) -> bool
        Return true if and only if it is ready and holds a value
        """
        return False

    def wait(self, timeout=None): # real signature unknown; restored from __doc__
        """
        AsyncResult.wait(self, timeout=None)
        Block until the instance is ready.
        
                If this instance already holds a value, it is returned immediately. If this
                instance already holds an exception, ``None`` is returned immediately.
        
                Otherwise, block until another greenlet calls :meth:`set` or :meth:`set_exception`
                (at which point either the value or ``None`` will be returned, respectively),
                or until the optional timeout expires (at which point ``None`` will also be
                returned).
        
                When the *timeout* argument is present and not ``None``, it should be a
                floating point number specifying a timeout for the operation in seconds
                (or fractions thereof).
        
                .. note:: If a timeout is given and expires, ``None`` will be returned
                    (no timeout exception will be raised).
        """
        pass

    def _raise_exception(self): # real signature unknown; restored from __doc__
        """ AsyncResult._raise_exception(self) """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    exception = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Holds the exception instance passed to :meth:`set_exception` if :meth:`set_exception` was called.
        Otherwise ``None``."""

    exc_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The three-tuple of exception information if :meth:`set_exception` was called.
        """

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Holds the value passed to :meth:`set` if :meth:`set` was called. Otherwise,
        ``None``
        """

    _exception = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _exc_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _imap_task_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_imap_task_index: 'int'"""

    _value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f75163bd590>'
    __slots__ = (
        '_value',
        '_exc_info',
        '_imap_task_index',
    )


class Event(__gevent__gevent_c_abstract_linkable.AbstractLinkable):
    """
    Event()
    
        A synchronization primitive that allows one greenlet to wake up
        one or more others. It has the same interface as
        :class:`threading.Event` but works across greenlets.
    
        .. important::
           This object is for communicating among greenlets within the
           same thread *only*! Do not try to use it to communicate across threads.
    
        An event object manages an internal flag that can be set to true
        with the :meth:`set` method and reset to false with the
        :meth:`clear` method. The :meth:`wait` method blocks until the
        flag is true; as soon as the flag is set to true, all greenlets
        that are currently blocked in a call to :meth:`wait` will be scheduled
        to awaken.
    
        Note that the flag may be cleared and set many times before
        any individual greenlet runs; all the greenlet can know for sure is that the
        flag was set *at least once* while it was waiting.
        If the greenlet cares whether the flag is still
        set, it must check with :meth:`ready` and possibly call back into
        :meth:`wait` again.
    
        .. note::
    
            The exact order and timing in which waiting greenlets are awakened is not determined.
    
            Once the event is set, other greenlets may run before any waiting greenlets
            are awakened.
    
            While the code here will awaken greenlets in the order in which they
            waited, each such greenlet that runs may in turn cause other greenlets
            to run.
    
            These details may change in the future.
    
        .. versionchanged:: 1.5a3
    
            Waiting greenlets are now awakened in
            the order in which they waited.
    
        .. versionchanged:: 1.5a3
    
            The low-level ``rawlink`` method (most users won't use this) now
            automatically unlinks waiters before calling them.
    
        .. versionchanged:: 20.5.1
    
            Callers to ``wait`` that find the event already set will now run
            after any other waiters that had to block. See :issue:`1520`.
    """
    def clear(self): # real signature unknown; restored from __doc__
        """
        Event.clear(self)
        
                Reset the internal flag to false.
        
                Subsequently, threads calling :meth:`wait` will block until
                :meth:`set` is called to set the internal flag to true again.
        """
        pass

    def isSet(self): # real signature unknown; restored from __doc__
        """ Event.isSet(self) """
        pass

    def is_set(self): # real signature unknown; restored from __doc__
        """
        Event.is_set(self)
        Return true if and only if the internal flag is true.
        """
        pass

    def ready(self): # real signature unknown; restored from __doc__
        """ Event.ready(self) -> bool """
        return False

    def set(self): # real signature unknown; restored from __doc__
        """
        Event.set(self)
        
                Set the internal flag to true.
        
                All greenlets waiting for it to become true are awakened in
                some order at some time in the future. Greenlets that call
                :meth:`wait` once the flag is true will not block at all
                (until :meth:`clear` is called).
        """
        pass

    def wait(self, timeout=None): # real signature unknown; restored from __doc__
        """
        Event.wait(self, timeout=None)
        
                Block until this object is :meth:`ready`.
        
                If the internal flag is true on entry, return immediately. Otherwise,
                block until another thread (greenlet) calls :meth:`set` to set the flag to true,
                or until the optional *timeout* expires.
        
                When the *timeout* argument is present and not ``None``, it should be a
                floating point number specifying a timeout for the operation in seconds
                (or fractions thereof).
        
                :return: This method returns true if and only if the internal flag has been set to
                    true, either before the wait call or after the wait starts, so it will
                    always return ``True`` except if a timeout is given and the operation
                    times out.
        
                .. versionchanged:: 1.1
                    The return value represents the flag during the elapsed wait, not
                    just after it elapses. This solves a race condition if one greenlet
                    sets and then clears the flag without switching, while other greenlets
                    are waiting. When the waiters wake up, this will return True; previously,
                    they would still wake up, but the return value would be False. This is most
                    noticeable when the *timeout* is present.
        """
        pass

    def _reset_internal_locks(self): # real signature unknown; restored from __doc__
        """ Event._reset_internal_locks(self) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f75163bd5f0>'
    __slots__ = (
        '_flag',
    )


# variables with complex values

_NONE = None # (!) real value is '<default value>'

__all__ = [
    'Event',
    'AsyncResult',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f751643d240>'

__pyx_capi__ = {
    'Timeout': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75163be8e0>'
    '_None': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75164461f0>'
    'dump_traceback': None, # (!) real value is '<capsule object "PyObject *" at 0x7f751643d200>'
    'load_traceback': None, # (!) real value is '<capsule object "PyObject *" at 0x7f751643e700>'
    'reraise': None, # (!) real value is '<capsule object "PyObject *" at 0x7f751643d1d0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent._gevent_cevent', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f751643d240>, origin='/home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_cevent.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

