# encoding: utf-8
# module gevent._gevent_cqueue
# from /home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_cqueue.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
"""
Synchronized queues.

The :mod:`gevent.queue` module implements multi-producer, multi-consumer queues
that work across greenlets, with the API similar to the classes found in the
standard :mod:`Queue` and :class:`multiprocessing <multiprocessing.Queue>` modules.

The classes in this module implement the iterator protocol. Iterating
over a queue means repeatedly calling :meth:`get <Queue.get>` until
:meth:`get <Queue.get>` returns ``StopIteration`` (specifically that
class, not an instance or subclass).

    >>> import gevent.queue
    >>> queue = gevent.queue.Queue()
    >>> queue.put(1)
    >>> queue.put(2)
    >>> queue.put(StopIteration)
    >>> for item in queue:
    ...    print(item)
    1
    2

.. versionchanged:: 1.0
       ``Queue(0)`` now means queue of infinite size, not a channel. A :exc:`DeprecationWarning`
       will be issued with this argument.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import collections as collections # /usr/lib/python3.10/collections/__init__.py
import queue as __queue__ # /usr/lib/python3.10/queue.py
import gevent as gevent # /home/kadosh/.local/lib/python3.10/site-packages/gevent/__init__.py
from gevent._gevent_c_hub_local import get_hub_noargs

from gevent._gevent_c_waiter import Waiter

from greenlet._greenlet import getcurrent

from _queue import Empty

import gevent._gevent_c_waiter as __gevent__gevent_c_waiter


# functions

def greenlet_init(*args, **kwargs): # real signature unknown
    pass

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

def _init(): # real signature unknown; restored from __doc__
    """ _init() """
    pass

# classes

class Channel(object):
    """ Channel(maxsize=1) """
    def empty(self): # real signature unknown; restored from __doc__
        """ Channel.empty(self) """
        pass

    def full(self): # real signature unknown; restored from __doc__
        """ Channel.full(self) """
        pass

    def get(self, block=True, timeout=None): # real signature unknown; restored from __doc__
        """ Channel.get(self, block=True, timeout=None) """
        pass

    def get_nowait(self): # real signature unknown; restored from __doc__
        """ Channel.get_nowait(self) """
        pass

    def next(self, *args, **kwargs): # real signature unknown
        pass

    def put(self, item, block=True, timeout=None): # real signature unknown; restored from __doc__
        """ Channel.put(self, item, block=True, timeout=None) """
        pass

    def put_nowait(self, item): # real signature unknown; restored from __doc__
        """ Channel.put_nowait(self, item) """
        pass

    def qsize(self): # real signature unknown; restored from __doc__
        """ Channel.qsize(self) """
        pass

    def _format(self): # real signature unknown; restored from __doc__
        """ Channel._format(self) """
        pass

    def _unlock(self): # real signature unknown; restored from __doc__
        """ Channel._unlock(self) """
        pass

    def __init__(self, maxsize=1): # real signature unknown; restored from __doc__
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    balance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    getters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hub = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    putters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f75163bd1a0>'
    __slots__ = (
        'getters',
        'putters',
        'hub',
        '_event_unlock',
        '__weakref__',
    )


class Full(Exception):
    """ Exception raised by Queue.put(block=0)/put_nowait(). """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class ItemWaiter(__gevent__gevent_c_waiter.Waiter):
    """ ItemWaiter(item, queue) """
    def put_and_switch(self): # real signature unknown; restored from __doc__
        """ ItemWaiter.put_and_switch(self) """
        pass

    def __init__(self, item, queue): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    queue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f75163bcf90>'
    __slots__ = (
        'item',
        'queue',
    )


class Queue(object):
    """
    Queue(maxsize=None, items=(), _warn_depth=2)
    
        Create a queue object with a given maximum size.
    
        If *maxsize* is less than or equal to zero or ``None``, the queue
        size is infinite.
    
        Queues have a ``len`` equal to the number of items in them (the :meth:`qsize`),
        but in a boolean context they are always True.
    
        .. versionchanged:: 1.1b3
           Queues now support :func:`len`; it behaves the same as :meth:`qsize`.
        .. versionchanged:: 1.1b3
           Multiple greenlets that block on a call to :meth:`put` for a full queue
           will now be awakened to put their items into the queue in the order in which
           they arrived. Likewise, multiple greenlets that block on a call to :meth:`get` for
           an empty queue will now receive items in the order in which they blocked. An
           implementation quirk under CPython *usually* ensured this was roughly the case
           previously anyway, but that wasn't the case for PyPy.
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ Queue.copy(self) """
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """
        Queue.empty(self) -> bool
        Return ``True`` if the queue is empty, ``False`` otherwise.
        """
        return False

    def full(self): # real signature unknown; restored from __doc__
        """
        Queue.full(self) -> bool
        Return ``True`` if the queue is full, ``False`` otherwise.
        
                ``Queue(None)`` is never full.
        """
        return False

    def get(self, block=True, timeout=None): # real signature unknown; restored from __doc__
        """
        Queue.get(self, block=True, timeout=None)
        Remove and return an item from the queue.
        
                If optional args *block* is true and *timeout* is ``None`` (the default),
                block if necessary until an item is available. If *timeout* is a positive number,
                it blocks at most *timeout* seconds and raises the :class:`Empty` exception
                if no item was available within that time. Otherwise (*block* is false), return
                an item if one is immediately available, else raise the :class:`Empty` exception
                (*timeout* is ignored in that case).
        """
        pass

    def get_nowait(self): # real signature unknown; restored from __doc__
        """
        Queue.get_nowait(self)
        Remove and return an item from the queue without blocking.
        
                Only get an item if one is immediately available. Otherwise
                raise the :class:`Empty` exception.
        """
        pass

    def next(self, *args, **kwargs): # real signature unknown
        pass

    def peek(self, block=True, timeout=None): # real signature unknown; restored from __doc__
        """
        Queue.peek(self, block=True, timeout=None)
        Return an item from the queue without removing it.
        
                If optional args *block* is true and *timeout* is ``None`` (the default),
                block if necessary until an item is available. If *timeout* is a positive number,
                it blocks at most *timeout* seconds and raises the :class:`Empty` exception
                if no item was available within that time. Otherwise (*block* is false), return
                an item if one is immediately available, else raise the :class:`Empty` exception
                (*timeout* is ignored in that case).
        """
        pass

    def peek_nowait(self): # real signature unknown; restored from __doc__
        """
        Queue.peek_nowait(self)
        Return an item from the queue without blocking.
        
                Only return an item if one is immediately available. Otherwise
                raise the :class:`Empty` exception.
        """
        pass

    def put(self, item, block=True, timeout=None): # real signature unknown; restored from __doc__
        """
        Queue.put(self, item, block=True, timeout=None)
        Put an item into the queue.
        
                If optional arg *block* is true and *timeout* is ``None`` (the default),
                block if necessary until a free slot is available. If *timeout* is
                a positive number, it blocks at most *timeout* seconds and raises
                the :class:`Full` exception if no free slot was available within that time.
                Otherwise (*block* is false), put an item on the queue if a free slot
                is immediately available, else raise the :class:`Full` exception (*timeout*
                is ignored in that case).
        """
        pass

    def put_nowait(self, item): # real signature unknown; restored from __doc__
        """
        Queue.put_nowait(self, item)
        Put an item into the queue without blocking.
        
                Only enqueue the item if a free slot is immediately available.
                Otherwise raise the :class:`Full` exception.
        """
        pass

    def qsize(self): # real signature unknown; restored from __doc__
        """
        Queue.qsize(self) -> Py_ssize_t
        Return the size of the queue.
        """
        pass

    def _create_queue(self, items=()): # real signature unknown; restored from __doc__
        """ Queue._create_queue(self, items=()) """
        pass

    def _format(self): # real signature unknown; restored from __doc__
        """ Queue._format(self) """
        pass

    def _get(self): # real signature unknown; restored from __doc__
        """ Queue._get(self) """
        pass

    def _peek(self): # real signature unknown; restored from __doc__
        """ Queue._peek(self) """
        pass

    def _put(self, item): # real signature unknown; restored from __doc__
        """ Queue._put(self, item) """
        pass

    def _unlock(self): # real signature unknown; restored from __doc__
        """ Queue._unlock(self) """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __init__(self, maxsize=None, items=(), _warn_depth=2): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """
        Return the size of the queue. This is the same as :meth:`qsize`.
        
                .. versionadded: 1.1b3
        
                    Previously, getting len() of a queue would raise a TypeError.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    hub = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maxsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    queue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f75163bce70>'
    __slots__ = (
        '_maxsize',
        'getters',
        'putters',
        'hub',
        '_event_unlock',
        'queue',
        '__weakref__',
    )


class JoinableQueue(Queue):
    """
    JoinableQueue(maxsize=None, items=(), unfinished_tasks=None)
    
        A subclass of :class:`Queue` that additionally has
        :meth:`task_done` and :meth:`join` methods.
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ JoinableQueue.copy(self) """
        pass

    def join(self, timeout=None): # real signature unknown; restored from __doc__
        """
        JoinableQueue.join(self, timeout=None)
        
                Block until all items in the queue have been gotten and processed.
        
                The count of unfinished tasks goes up whenever an item is added to the queue.
                The count goes down whenever a consumer thread calls :meth:`task_done` to indicate
                that the item was retrieved and all work on it is complete. When the count of
                unfinished tasks drops to zero, :meth:`join` unblocks.
        
                :param float timeout: If not ``None``, then wait no more than this time in seconds
                    for all tasks to finish.
                :return: ``True`` if all tasks have finished; if ``timeout`` was given and expired before
                    all tasks finished, ``False``.
        
                .. versionchanged:: 1.1a1
                   Add the *timeout* parameter.
        """
        pass

    def task_done(self): # real signature unknown; restored from __doc__
        """
        JoinableQueue.task_done(self)
        Indicate that a formerly enqueued task is complete. Used by queue consumer threads.
                For each :meth:`get <Queue.get>` used to fetch a task, a subsequent call to :meth:`task_done` tells the queue
                that the processing on the task is complete.
        
                If a :meth:`join` is currently blocking, it will resume when all items have been processed
                (meaning that a :meth:`task_done` call was received for every item that had been
                :meth:`put <Queue.put>` into the queue).
        
                Raises a :exc:`ValueError` if called more times than there were items placed in the queue.
        """
        pass

    def _format(self): # real signature unknown; restored from __doc__
        """ JoinableQueue._format(self) """
        pass

    def _put(self, item): # real signature unknown; restored from __doc__
        """ JoinableQueue._put(self, item) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        .. versionchanged:: 1.1a1
                   If *unfinished_tasks* is not given, then all the given *items*
                   (if any) will be considered unfinished.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    unfinished_tasks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f75163be790>'
    __slots__ = (
        '_cond',
        'unfinished_tasks',
    )


class LifoQueue(Queue):
    """ A subclass of :class:`Queue` that retrieves most recently added entries first. """
    def _create_queue(self, items=()): # real signature unknown; restored from __doc__
        """ LifoQueue._create_queue(self, items=()) """
        pass

    def _get(self): # real signature unknown; restored from __doc__
        """ LifoQueue._get(self) """
        pass

    def _peek(self): # real signature unknown; restored from __doc__
        """ LifoQueue._peek(self) """
        pass

    def _put(self, item): # real signature unknown; restored from __doc__
        """ LifoQueue._put(self, item) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f75163bd110>'
    __slots__ = ()


class PriorityQueue(Queue):
    """
    A subclass of :class:`Queue` that retrieves entries in priority order (lowest first).
    
        Entries are typically tuples of the form: ``(priority number, data)``.
    
        .. versionchanged:: 1.2a1
           Any *items* given to the constructor will now be passed through
           :func:`heapq.heapify` to ensure the invariants of this class hold.
           Previously it was just assumed that they were already a heap.
    """
    def _create_queue(self, items=()): # real signature unknown; restored from __doc__
        """ PriorityQueue._create_queue(self, items=()) """
        pass

    def _get(self): # real signature unknown; restored from __doc__
        """ PriorityQueue._get(self) """
        pass

    def _put(self, item): # real signature unknown; restored from __doc__
        """ PriorityQueue._put(self, item) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f75163bd0b0>'
    __slots__ = ()


class SimpleQueue(object):
    """
    Simple, unbounded FIFO queue.
    
        This pure Python implementation is not reentrant.
    """
    def empty(self): # reliably restored by inspect
        """ Return True if the queue is empty, False otherwise (not reliable!). """
        pass

    def get(self, block=True, timeout=None): # reliably restored by inspect
        """
        Remove and return an item from the queue.
        
                If optional args 'block' is true and 'timeout' is None (the default),
                block if necessary until an item is available. If 'timeout' is
                a non-negative number, it blocks at most 'timeout' seconds and raises
                the Empty exception if no item was available within that time.
                Otherwise ('block' is false), return an item if one is immediately
                available, else raise the Empty exception ('timeout' is ignored
                in that case).
        """
        pass

    def get_nowait(self): # reliably restored by inspect
        """
        Remove and return an item from the queue without blocking.
        
                Only get an item if one is immediately available. Otherwise
                raise the Empty exception.
        """
        pass

    def put(self, item, block=True, timeout=None): # reliably restored by inspect
        """
        Put the item on the queue.
        
                The optional 'block' and 'timeout' arguments are ignored, as this method
                never blocks.  They are provided for compatibility with the Queue class.
        """
        pass

    def put_nowait(self, item): # reliably restored by inspect
        """
        Put an item into the queue without blocking.
        
                This is exactly equivalent to `put(item, block=False)` and is only provided
                for compatibility with the Queue class.
        """
        pass

    def qsize(self): # reliably restored by inspect
        """ Return the approximate size of the queue (not reliable!). """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """
        Represent a PEP 585 generic type
        
        E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).
        """
        pass

    def __init__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'queue', '__doc__': 'Simple, unbounded FIFO queue.\\n\\n    This pure Python implementation is not reentrant.\\n    ', '__init__': <function _PySimpleQueue.__init__ at 0x7f75161bcd30>, 'put': <function _PySimpleQueue.put at 0x7f75161bca60>, 'get': <function _PySimpleQueue.get at 0x7f75161bc9d0>, 'put_nowait': <function _PySimpleQueue.put_nowait at 0x7f75161bc940>, 'get_nowait': <function _PySimpleQueue.get_nowait at 0x7f75161bc8b0>, 'empty': <function _PySimpleQueue.empty at 0x7f75161bc820>, 'qsize': <function _PySimpleQueue.qsize at 0x7f75161bc790>, '__class_getitem__': <classmethod(<class 'types.GenericAlias'>)>, '__dict__': <attribute '__dict__' of '_PySimpleQueue' objects>, '__weakref__': <attribute '__weakref__' of '_PySimpleQueue' objects>})"


class UnboundQueue(Queue):
    """ UnboundQueue(maxsize=None, items=()) """
    def put(self, item, block=True, timeout=None): # real signature unknown; restored from __doc__
        """ UnboundQueue.put(self, item, block=True, timeout=None) """
        pass

    def __init__(self, maxsize=None, items=()): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f75163bd020>'
    __slots__ = ()


# variables with complex values

__all__ = [
    'SimpleQueue',
    'Queue',
    'PriorityQueue',
    'LifoQueue',
    'JoinableQueue',
    'Channel',
    'Empty',
    'Full',
]

__extensions__ = [
    'JoinableQueue',
    'Channel',
]

__implements__ = [
    'Queue',
    'PriorityQueue',
    'LifoQueue',
]

__imports__ = [
    'Empty',
    'Full',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f751643d240>'

__pyx_capi__ = {
    'InvalidSwitchError': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75163bcd50>'
    'Timeout': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75163bd590>'
    '_Empty': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75163be8e0>'
    '_Full': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75163bd5f0>'
    '_greenlet_imported': None, # (!) real value is '<capsule object "int" at 0x7f75164461f0>'
    '_heapify': None, # (!) real value is '<capsule object "PyObject *" at 0x7f751643e700>'
    '_heappop': None, # (!) real value is '<capsule object "PyObject *" at 0x7f751643d200>'
    '_heappush': None, # (!) real value is '<capsule object "PyObject *" at 0x7f751643d1d0>'
    '_safe_remove': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *)" at 0x7f75163bcf00>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent._gevent_cqueue', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f751643d240>, origin='/home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_cqueue.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

