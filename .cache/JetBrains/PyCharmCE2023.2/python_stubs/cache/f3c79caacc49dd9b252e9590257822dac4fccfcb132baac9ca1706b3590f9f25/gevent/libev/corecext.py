# encoding: utf-8
# module gevent.libev.corecext
# from /home/kadosh/.local/lib/python3.10/site-packages/gevent/libev/corecext.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import os as os # /usr/lib/python3.10/os.py
import traceback as traceback # /usr/lib/python3.10/traceback.py
import signal as signalmodule # /usr/lib/python3.10/signal.py
from sys import getswitchinterval

import greenlet as __greenlet


# Variables with simple values

ASYNC = 524288

BACKEND_DEVPOLL = 16
BACKEND_EPOLL = 4
BACKEND_IOURING = 128
BACKEND_KQUEUE = 8
BACKEND_LINUXAIO = 64
BACKEND_POLL = 2
BACKEND_PORT = 32
BACKEND_SELECT = 1

CHECK = 32768
CHILD = 2048

CLEANUP = 262144

CUSTOM = 16777216

EMBED = 65536

ERROR = -2147483648

EV_USE_4HEAP = 2

EV_USE_CLOCK_SYSCALL = 0

EV_USE_EVENTFD = 64
EV_USE_FLOOR = 1
EV_USE_INOTIFY = 64
EV_USE_MONOTONIC = 1
EV_USE_NANOSLEEP = 64
EV_USE_REALTIME = 1
EV_USE_SIGNALFD = 64

FORK = 131072
FORKCHECK = 33554432

IDLE = 8192

LIBEV_EMBED = True

MAXPRI = 2

MINPRI = -2

NOINOTIFY = 1048576
NONE = 0
NOSIGMASK = 4194304

PERIODIC = 512

PREPARE = 16384

READ = 1
READWRITE = 3

SIGNAL = 1024
SIGNALFD = 2097152

STAT = 4096

TIMER = 256

UNDEF = -1

WRITE = 2

# functions

def classImplements(cls, *interfaces): # reliably restored by inspect
    """
    Declare additional interfaces implemented for instances of a class
    
        The arguments after the class are one or more interfaces or
        interface specifications (`~zope.interface.interfaces.IDeclaration` objects).
    
        The interfaces given (including the interfaces in the specifications)
        are added to any interfaces previously declared. An effort is made to
        keep a consistent C3 resolution order, but this cannot be guaranteed.
    
        .. versionchanged:: 5.0.0
           Each individual interface in *interfaces* may be added to either the
           beginning or end of the list of interfaces declared for *cls*,
           based on inheritance, in order to try to maintain a consistent
           resolution order. Previously, all interfaces were added to the end.
        .. versionchanged:: 5.1.0
           If *cls* is already declared to implement an interface (or derived interface)
           in *interfaces* through inheritance, the interface is ignored. Previously, it
           would redundantly be made direct base of *cls*, which often produced inconsistent
           interface resolution orders. Now, the order will be consistent, but may change.
           Also, if the ``__bases__`` of the *cls* are later changed, the *cls* will no
           longer be considered to implement such an interface (changing the ``__bases__`` of *cls*
           has never been supported).
    """
    pass

def embeddable_backends(*args, **kwargs): # real signature unknown
    pass

def get_header_version(*args, **kwargs): # real signature unknown
    pass

def get_version(*args, **kwargs): # real signature unknown
    pass

def ICallback(*args, **kwargs): # real signature unknown
    """
    Represents a function that will be run some time in the future.
    
        Callback functions run in the hub, and as such they cannot use
        gevent's blocking API; any exception they raise cannot be caught.
    """
    pass

def ILoop(*args, **kwargs): # real signature unknown
    """
    The common interface expected for all event loops.
    
        .. caution::
           This is an internal, low-level interface. It may change
           between minor versions of gevent.
    
        .. rubric:: Watchers
    
        The methods that create event loop watchers are `io`, `timer`,
        `signal`, `idle`, `prepare`, `check`, `fork`, `async_`, `child`,
        `stat`. These all return various types of :class:`IWatcher`.
    
        All of those methods have one or two common arguments. *ref* is a
        boolean saying whether the event loop is allowed to exit even if
        this watcher is still started. *priority* is event loop specific.
    """
    pass

def print_exception(exc, value='<implicit>', tb='<implicit>', limit=None, file=None, chain=True): # reliably restored by inspect
    """
    Print exception up to 'limit' stack trace entries from 'tb' to 'file'.
    
        This differs from print_tb() in the following ways: (1) if
        traceback is not None, it prints a header "Traceback (most recent
        call last):"; (2) it prints the exception type and value after the
        stack trace; (3) if type is SyntaxError and value has the
        appropriate format, it prints the line where the syntax error
        occurred with a caret on the next line indicating the approximate
        position of the error.
    """
    pass

def recommended_backends(*args, **kwargs): # real signature unknown
    pass

def set_syserr_cb(*args, **kwargs): # real signature unknown
    pass

def supported_backends(*args, **kwargs): # real signature unknown
    pass

def time(*args, **kwargs): # real signature unknown
    pass

def _check_flags(*args, **kwargs): # real signature unknown
    pass

def _events_to_str(*args, **kwargs): # real signature unknown
    pass

def _flags_to_int(*args, **kwargs): # real signature unknown
    pass

def _flags_to_list(*args, **kwargs): # real signature unknown
    pass

# classes

class watcher(object):
    """ Abstract base class for all the watchers """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def _format(self, *args, **kwargs): # real signature unknown
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class async_(watcher):
    # no doc
    def send(self, *args, **kwargs): # real signature unknown
        pass

    def send_ignoring_arg(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



async = async_


class callback(object):
    # no doc
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def _format(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class check(watcher):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class child(watcher):
    # no doc
    def _format(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rpid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rstatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class fork(watcher):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class HubDestroyed(__greenlet.GreenletExit):
    """
    Internal exception, raised when we're trying to destroy the
        hub and we want the loop to stop running callbacks now.
    
        This must not be subclassed; the type is tested by identity.
    
        Clients outside of gevent must not raise this exception.
    
        .. versionadded:: 20.12.0
    """
    def __init__(self, destroy_loop): # reliably restored by inspect
        # no doc
        pass


class idle(watcher):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class io(watcher):
    # no doc
    def start(self, *args, **kwargs): # real signature unknown
        pass

    def _format(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    events_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class loop(object):
    # no doc
    def async_(self, *args, **kwargs): # real signature unknown
        pass

    def break_(self, *args, **kwargs): # real signature unknown
        pass

    def check(self, *args, **kwargs): # real signature unknown
        pass

    def child(self, *args, **kwargs): # real signature unknown
        pass

    def closing_fd(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        pass

    def fork(self, *args, **kwargs): # real signature unknown
        pass

    def handle_error(self, *args, **kwargs): # real signature unknown
        pass

    def idle(self, *args, **kwargs): # real signature unknown
        pass

    def install_sigchld(self, *args, **kwargs): # real signature unknown
        pass

    def io(self, *args, **kwargs): # real signature unknown
        pass

    def now(self, *args, **kwargs): # real signature unknown
        pass

    def prepare(self, *args, **kwargs): # real signature unknown
        pass

    def ref(self, *args, **kwargs): # real signature unknown
        pass

    def reinit(self, *args, **kwargs): # real signature unknown
        pass

    def reset_sigchld(self, *args, **kwargs): # real signature unknown
        pass

    def run(self, *args, **kwargs): # real signature unknown
        pass

    def run_callback(self, *args, **kwargs): # real signature unknown
        pass

    def run_callback_threadsafe(self, *args, **kwargs): # real signature unknown
        pass

    def signal(self, *args, **kwargs): # real signature unknown
        pass

    def stat(self, *args, **kwargs): # real signature unknown
        pass

    def timer(self, *args, **kwargs): # real signature unknown
        pass

    def unref(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def update_now(self, *args, **kwargs): # real signature unknown
        pass

    def verify(self, *args, **kwargs): # real signature unknown
        pass

    def _default_handle_error(self, *args, **kwargs): # real signature unknown
        pass

    def _format(self, *args, **kwargs): # real signature unknown
        pass

    def _format_details(self, *args, **kwargs): # real signature unknown
        pass

    def _handle_syserr(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    activecnt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    approx_timer_resolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    backend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    backend_int = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    error_handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iteration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MAXPRI = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MINPRI = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origflags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origflags_int = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pendingcnt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ptr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sigfd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sig_pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    WatcherType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _callbacks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f7516445bc0>'


class prepare(watcher):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class signal(watcher):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class stat(watcher):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    attr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    interval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _paths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class timer(watcher):
    # no doc
    def again(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    at = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

basestring = (
    bytes,
    str,
)

EVENTS = None # (!) real value is 'gevent.core.EVENTS'

_events = [
    (
        1,
        'READ',
    ),
    (
        2,
        'WRITE',
    ),
    (
        128,
        '_IOFDSET',
    ),
    (
        512,
        'PERIODIC',
    ),
    (
        1024,
        'SIGNAL',
    ),
    (
        2048,
        'CHILD',
    ),
    (
        4096,
        'STAT',
    ),
    (
        8192,
        'IDLE',
    ),
    (
        16384,
        'PREPARE',
    ),
    (
        32768,
        'CHECK',
    ),
    (
        65536,
        'EMBED',
    ),
    (
        131072,
        'FORK',
    ),
    (
        262144,
        'CLEANUP',
    ),
    (
        524288,
        'ASYNC',
    ),
    (
        16777216,
        'CUSTOM',
    ),
    (
        -2147483648,
        'ERROR',
    ),
]

_flags = [
    (
        32,
        'port',
    ),
    (
        8,
        'kqueue',
    ),
    (
        128,
        'linux_iouring',
    ),
    (
        64,
        'linux_aio',
    ),
    (
        4,
        'epoll',
    ),
    (
        2,
        'poll',
    ),
    (
        1,
        'select',
    ),
    (
        16777216,
        'noenv',
    ),
    (
        33554432,
        'forkcheck',
    ),
    (
        1048576,
        'noinotify',
    ),
    (
        2097152,
        'signalfd',
    ),
    (
        4194304,
        'nosigmask',
    ),
]

_flags_str2int = {
    'epoll': 4,
    'forkcheck': 33554432,
    'kqueue': 8,
    'linux_aio': 64,
    'linux_iouring': 128,
    'noenv': 16777216,
    'noinotify': 1048576,
    'nosigmask': 4194304,
    'poll': 2,
    'port': 32,
    'select': 1,
    'signalfd': 2097152,
}

__all__ = [
    'get_version',
    'get_header_version',
    'supported_backends',
    'recommended_backends',
    'embeddable_backends',
    'time',
    'loop',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f7516445db0>'

__spec__ = None # (!) real value is "ModuleSpec(name='gevent.libev.corecext', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f7516445db0>, origin='/home/kadosh/.local/lib/python3.10/site-packages/gevent/libev/corecext.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

