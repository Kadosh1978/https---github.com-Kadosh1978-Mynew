# encoding: utf-8
# module gevent._gevent_c_hub_local
# from /home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_c_hub_local.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" Maintains the thread local hub. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import _thread as _thread # <module '_thread' (built-in)>
import gevent._gevent_c_hub_primitives as __gevent__gevent_c_hub_primitives
import _thread as ___thread


# functions

def get_hub(*args, **kwargs): # real signature unknown
    """
    Return the hub for the current thread.
    
        If a hub does not exist in the current thread, a new one is
        created of the type returned by :func:`get_hub_class`.
    
        .. deprecated:: 1.3b1
           The ``*args`` and ``**kwargs`` arguments are deprecated. They were
           only used when the hub was created, and so were non-deterministic---to be
           sure they were used, *all* callers had to pass them, or they were order-dependent.
           Use ``set_hub`` instead.
    
        .. versionchanged:: 1.5a3
           The *args* and *kwargs* arguments are now completely ignored.
    
        .. versionchanged:: 23.7.0
           The long-deprecated ``args`` and ``kwargs`` parameters are no
           longer accepted.
    """
    pass

def get_hub_class(*args, **kwargs): # real signature unknown
    """
    Return the type of hub to use for the current thread.
    
        If there's no type of hub for the current thread yet, 'gevent.hub.Hub' is used.
    """
    pass

def get_hub_if_exists(*args, **kwargs): # real signature unknown
    """
    Return the hub for the current thread.
    
        Return ``None`` if no hub has been created yet.
    """
    pass

def get_hub_noargs(*args, **kwargs): # real signature unknown
    pass

def get_loop(*args, **kwargs): # real signature unknown
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

def set_default_hub_class(*args, **kwargs): # real signature unknown
    pass

def set_hub(*args, **kwargs): # real signature unknown
    pass

def set_loop(*args, **kwargs): # real signature unknown
    pass

# classes

class Hub(__gevent__gevent_c_hub_primitives.WaitOperationsGreenlet):
    """
    A greenlet that runs the event loop.
    
        It is created automatically by :func:`get_hub`.
    
        .. rubric:: Switching
    
        Every time this greenlet (i.e., the event loop) is switched *to*,
        if the current greenlet has a ``switch_out`` method, it will be
        called. This allows a greenlet to take some cleanup actions before
        yielding control. This method should not call any gevent blocking
        functions.
    """
    def destroy(self, destroy_loop=None): # reliably restored by inspect
        """
        Destroy this hub and clean up its resources.
        
                If you manually create hubs, or you use a hub or the gevent
                blocking API from multiple native threads, you *should* call this
                method before disposing of the hub object reference. Ideally,
                this should be called from the same thread running the hub, but
                it can be called from other threads after that thread has exited.
        
                Once this is done, it is impossible to continue running the
                hub. Attempts to use the blocking gevent API with pre-existing
                objects from this native thread and bound to this hub will fail.
        
                .. versionchanged:: 20.5.1
                    Attempt to ensure that Python stack frames and greenlets referenced by this
                    hub are cleaned up. This guarantees that switching to the hub again
                    is not safe after this. (It was never safe, but it's even less safe.)
        
                    Note that this only works if the hub is destroyed in the same thread it
                    is running in. If the hub is destroyed by a different thread
                    after a ``fork()``, for example, expect some garbage to leak.
        """
        pass

    def handle_error(self, context, type, value, tb): # reliably restored by inspect
        """
        Called by the event loop when an error occurs. The default
                action is to print the exception to the :attr:`exception
                stream <exception_stream>`.
        
                The arguments ``type``, ``value``, and ``tb`` are the standard
                tuple as returned by :func:`sys.exc_info`. (Note that when
                this is called, it may not be safe to call
                :func:`sys.exc_info`.)
        
                Errors that are :attr:`not errors <NOT_ERROR>` are not
                printed.
        
                Errors that are :attr:`system errors <SYSTEM_ERROR>` are
                passed to :meth:`handle_system_error` after being printed.
        
                Applications can set a property on the hub instance with this
                same signature to override the error handling provided by this
                class. This is an advanced usage and requires great care. This
                function *must not* raise any exceptions.
        
                :param context: If this is ``None``, indicates a system error
                    that should generally result in exiting the loop and being
                    thrown to the parent greenlet.
        """
        pass

    def handle_system_error(self, type, value, tb=None): # reliably restored by inspect
        """
        Called from `handle_error` when the exception type is determined
                to be a :attr:`system error <SYSTEM_ERROR>`.
        
                System errors cause the exception to be raised in the main
                greenlet (the parent of this hub).
        
                .. versionchanged:: 20.5.1
                   Allow passing the traceback to associate with the
                   exception if it is rethrown into the main greenlet.
        """
        pass

    def join(self, timeout=None): # reliably restored by inspect
        """
        Wait for the event loop to finish. Exits only when there
                are no more spawned greenlets, started servers, active
                timeouts or watchers.
        
                .. caution:: This doesn't clean up all resources associated
                   with the hub. For that, see :meth:`destroy`.
        
                :param float timeout: If *timeout* is provided, wait no longer
                    than the specified number of seconds.
        
                :return: `True` if this method returns because the loop
                         finished execution. Or `False` if the timeout
                         expired.
        """
        pass

    def print_exception(self, context, t, v, tb): # reliably restored by inspect
        # no doc
        pass

    def run(self): # reliably restored by inspect
        """
        Entry-point to running the loop. This method is called automatically
                when the hub greenlet is scheduled; do not call it directly.
        
                :raises gevent.exceptions.LoopExit: If the loop finishes running. This means
                   that there are no other scheduled greenlets, and no active
                   watchers or servers. In some situations, this indicates a
                   programming error.
        """
        pass

    def start_periodic_monitoring_thread(self): # reliably restored by inspect
        # no doc
        pass

    def _del_resolver(self): # reliably restored by inspect
        # no doc
        pass

    def _del_threadpool(self): # reliably restored by inspect
        # no doc
        pass

    def _get_resolver(self): # reliably restored by inspect
        # no doc
        pass

    def _get_threadpool(self): # reliably restored by inspect
        # no doc
        pass

    def _normalize_exception(self, t, v, tb): # reliably restored by inspect
        # no doc
        pass

    def _set_resolver(self, value): # reliably restored by inspect
        # no doc
        pass

    def _set_threadpool(self, value): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, loop=None, default=None): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    backend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    main_hub = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Is this the hub for the main thread?

        .. versionadded:: 1.3b1
        """

    resolver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
                        The DNS resolver that the socket functions will use.

                        .. seealso:: :doc:`/dns`
                        """

    resolver_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    threadpool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
                          The threadpool associated with this hub.

                          Usually this is a
                          :class:`gevent.threadpool.ThreadPool`, but
                          you :attr:`can customize that
                          <gevent._config.Config.threadpool>`.

                          Use this object to schedule blocking
                          (non-cooperative) operations in a different
                          thread to prevent them from halting the event loop.
                          """

    threadpool_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    exception_stream = None # (!) real value is '<gevent._util.readproperty object at 0x7f75163bf010>'
    ident_registry = None # (!) real value is '<gevent._util.Lazy object at 0x7f75163bf100>'
    name = ''
    NOT_ERROR = (
        None, # (!) real value is "<class 'greenlet.GreenletExit'>"
        SystemExit,
    )
    periodic_monitoring_thread = None
    SYSTEM_ERROR = (
        KeyboardInterrupt,
        SystemExit,
        SystemError,
    )
    threadpool_size = 10
    thread_ident = None
    _hub_counter = 0


class _Threadlocal(___thread._local):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gevent._gevent_c_hub_local', '__init__': <cyfunction _Threadlocal.__init__ at 0x7f7516179560>, '__dict__': <attribute '__dict__' of '_Threadlocal' objects>, '__doc__': None})"


# variables with complex values

__all__ = [
    'get_hub',
    'get_hub_noargs',
    'get_hub_if_exists',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f75169cd1b0>'

__pyx_capi__ = {
    '_threadlocal': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75169cce70>'
    'get_hub': None, # (!) real value is '<capsule object "struct __pyx_obj_6gevent_29_gevent_c_greenlet_primitives_SwitchOutGreenletWithLoop *(int __pyx_skip_dispatch)" at 0x7f75169cd260>'
    'get_hub_class': None, # (!) real value is '<capsule object "PyObject *(int __pyx_skip_dispatch)" at 0x7f75169cd170>'
    'get_hub_if_exists': None, # (!) real value is '<capsule object "struct __pyx_obj_6gevent_29_gevent_c_greenlet_primitives_SwitchOutGreenletWithLoop *(int __pyx_skip_dispatch)" at 0x7f75169cd140>'
    'get_hub_noargs': None, # (!) real value is '<capsule object "struct __pyx_obj_6gevent_29_gevent_c_greenlet_primitives_SwitchOutGreenletWithLoop *(int __pyx_skip_dispatch)" at 0x7f75169cd290>'
    'get_loop': None, # (!) real value is '<capsule object "PyObject *(int __pyx_skip_dispatch)" at 0x7f75169cd200>'
    'set_hub': None, # (!) real value is '<capsule object "PyObject *(struct __pyx_obj_6gevent_29_gevent_c_greenlet_primitives_SwitchOutGreenletWithLoop *, int __pyx_skip_dispatch)" at 0x7f75169cd1d0>'
    'set_loop': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x7f75169cd230>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent._gevent_c_hub_local', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f75169cd1b0>, origin='/home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_c_hub_local.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

