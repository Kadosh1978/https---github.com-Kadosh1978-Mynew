# encoding: utf-8
# module gevent._gevent_c_greenlet_primitives
# from /home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_c_greenlet_primitives.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
"""
A collection of primitives used by the hub, and suitable for
compilation with Cython because of their frequency of use.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from greenlet._greenlet import getcurrent

import greenlet as __greenlet


# functions

def get_memory(data): # real signature unknown; restored from __doc__
    """ get_memory(data) """
    pass

def get_reachable_greenlets(): # real signature unknown; restored from __doc__
    """ get_reachable_greenlets() -> list """
    return []

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

def _greenlet_switch(*args, **kwargs): # real signature unknown
    """
    switch(*args, **kwargs)
    
    Switch execution to this greenlet.
    
    If this greenlet has never been run, then this greenlet
    will be switched to using the body of ``self.run(*args, **kwargs)``.
    
    If the greenlet is active (has been run, but was switch()'ed
    out before leaving its run function), then this greenlet will
    be resumed and the return value to its switch call will be
    None if no arguments are given, the given argument if one
    argument is given, or the args tuple and keyword args dict if
    multiple arguments are given.
    
    If the greenlet is dead, or is the current greenlet then this
    function will simply return the arguments using the same rules as
    above.
    """
    pass

def _init(): # real signature unknown; restored from __doc__
    """ _init() """
    pass

# classes

class TrackedRawGreenlet(__greenlet.greenlet):
    """ TrackedRawGreenlet(function, parent) """
    def __init__(self, function, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class SwitchOutGreenletWithLoop(TrackedRawGreenlet):
    # no doc
    def switch(self): # real signature unknown; restored from __doc__
        """ SwitchOutGreenletWithLoop.switch(self) """
        pass

    def switch_out(self): # real signature unknown; restored from __doc__
        """ SwitchOutGreenletWithLoop.switch_out(self) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """loop: object"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f75169cd6e0>'


# variables with complex values

__all__ = [
    'TrackedRawGreenlet',
    'SwitchOutGreenletWithLoop',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f75169cd570>'

__pyx_capi__ = {
    'BlockingSwitchOutError': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75169cd500>'
    '_buffer': None, # (!) real value is '<capsule object "PyTypeObject *" at 0x7f75169cd5f0>'
    '_greenlet_imported': None, # (!) real value is '<capsule object "int" at 0x7f75169cd590>'
    '_memoryview': None, # (!) real value is '<capsule object "PyTypeObject *" at 0x7f75169cd5c0>'
    'get_memory': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x7f75169cd650>'
    'get_objects': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75169cd440>'
    'get_reachable_greenlets': None, # (!) real value is '<capsule object "PyObject *(int __pyx_skip_dispatch)" at 0x7f75169cd620>'
    'wref': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75169cd530>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent._gevent_c_greenlet_primitives', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f75169cd570>, origin='/home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_c_greenlet_primitives.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

