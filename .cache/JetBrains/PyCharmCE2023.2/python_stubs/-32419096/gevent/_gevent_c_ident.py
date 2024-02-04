# encoding: utf-8
# module gevent._gevent_c_ident
# from /home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_c_ident.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import weakref as __weakref


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

class IdentRegistry(object):
    """
    IdentRegistry()
    
        Maintains a unique mapping of (small) non-negative integer identifiers
        to objects that can be weakly referenced.
    
        It is guaranteed that no two objects will have the the same
        identifier at the same time, as long as those objects are
        also uniquely hashable.
    """
    def get_ident(self, obj): # real signature unknown; restored from __doc__
        """
        IdentRegistry.get_ident(self, obj)
        
                Retrieve the identifier for *obj*, creating one
                if necessary.
        """
        pass

    def _return_ident(self, ValuedWeakRef_vref): # real signature unknown; restored from __doc__
        """ IdentRegistry._return_ident(self, ValuedWeakRef vref) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f75163bf9f0>'


class ValuedWeakRef(__weakref.ReferenceType):
    """ A weak ref with an associated value. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __slots__ = (
        'value',
    )


# variables with complex values

__all__ = [
    'IdentRegistry',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f75163bf9d0>'

__pyx_capi__ = {
    'WeakKeyDictionary': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75163bf8d0>'
    'heappop': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75163bf840>'
    'heappush': None, # (!) real value is '<capsule object "PyObject *" at 0x7f75163bf870>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent._gevent_c_ident', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f75163bf9d0>, origin='/home/kadosh/.local/lib/python3.10/site-packages/gevent/_gevent_c_ident.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

