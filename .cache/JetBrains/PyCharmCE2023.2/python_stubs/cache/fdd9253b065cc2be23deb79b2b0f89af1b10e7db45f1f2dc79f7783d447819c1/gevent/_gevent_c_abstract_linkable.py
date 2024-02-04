# encoding: utf-8
# module gevent._gevent_c_abstract_linkable
# from /home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_c_abstract_linkable.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" Internal module, support for the linkable protocol for "event" like objects. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
from gevent._gevent_c_hub_local import get_hub_if_exists, get_hub_noargs

from greenlet._greenlet import getcurrent

from _thread import _allocate_thread_lock


# Variables with simple values

thread_mod_name = '_thread'

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

# classes

class AbstractLinkable(object):
    """ AbstractLinkable(hub=None) """
    def linkcount(self): # real signature unknown; restored from __doc__
        """ AbstractLinkable.linkcount(self) """
        pass

    def rawlink(self, callback): # real signature unknown; restored from __doc__
        """
        AbstractLinkable.rawlink(self, callback)
        
                Register a callback to call when this object is ready.
        
                *callback* will be called in the :class:`Hub
                <gevent.hub.Hub>`, so it must not use blocking gevent API.
                *callback* will be passed one argument: this instance.
        """
        pass

    def ready(self): # real signature unknown; restored from __doc__
        """ AbstractLinkable.ready(self) -> bool """
        return False

    def unlink(self, callback): # real signature unknown; restored from __doc__
        """
        AbstractLinkable.unlink(self, callback)
        Remove the callback set by :meth:`rawlink`
        """
        pass

    def _acquire_lock_for_switch_in(self): # real signature unknown; restored from __doc__
        """ AbstractLinkable._acquire_lock_for_switch_in(self) """
        pass

    def _at_fork_reinit(self): # real signature unknown; restored from __doc__
        """
        AbstractLinkable._at_fork_reinit(self)
        
                This method was added in Python 3.9 and is called by logging.py
                ``_after_at_fork_child_reinit_locks`` on Lock objects.
        
                It is also called from threading.py, ``_after_fork`` in
                ``_reset_internal_locks``, and that can hit ``Event`` objects.
        
                Subclasses should reset themselves to an initial state. This
                includes unlocking/releasing, if possible. This method detaches from the
                previous hub and drops any existing notifier.
        """
        pass

    def _drop_lock_for_switch_out(self): # real signature unknown; restored from __doc__
        """ AbstractLinkable._drop_lock_for_switch_out(self) """
        pass

    def _notify_links(self, list_arrived_while_waiting): # real signature unknown; restored from __doc__
        """ AbstractLinkable._notify_links(self, list arrived_while_waiting) """
        pass

    def __init__(self, hub=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    hub = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f75163bd110>'
    __slots__ = (
        'hub',
        '_links',
        '_notifier',
        '_notify_all',
        '__weakref__',
    )


class greenlet_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class _FakeNotifier(object):
    """ _FakeNotifier() """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __slots__ = (
        'pending',
    )


# variables with complex values

__all__ = [
    'AbstractLinkable',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f751643d1e0>'

__pyx_capi__ = {
    'InvalidSwitchError': None, # (!) real value is '<capsule object "PyObject *" at 0x7f7516446250>'
    'InvalidThreadUseError': None, # (!) real value is '<capsule object "PyObject *" at 0x7f751643d170>'
    'Timeout': None, # (!) real value is '<capsule object "PyObject *" at 0x7f751643d1a0>'
    '_get_thread_ident': None, # (!) real value is '<capsule object "PyObject *" at 0x7f751643e760>'
    '_greenlet_imported': None, # (!) real value is '<capsule object "int" at 0x7f75163be5e0>'
    '_init': None, # (!) real value is '<capsule object "void (void)" at 0x7f75163bcf90>'
    'get_objects': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75163bce70>'
    'get_roots_and_hubs': None, # (!) real value is '<capsule object "PyObject *(void)" at 0x7f75163bd0b0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent._gevent_c_abstract_linkable', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f751643d1e0>, origin='/home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_c_abstract_linkable.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

