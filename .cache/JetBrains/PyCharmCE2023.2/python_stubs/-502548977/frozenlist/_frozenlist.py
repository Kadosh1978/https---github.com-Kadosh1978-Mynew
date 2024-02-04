# encoding: utf-8
# module frozenlist._frozenlist
# from /home/kadosh/PycharmProjects/BotFactory/venv/lib/python3.10/site-packages/frozenlist/_frozenlist.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import types as types # /usr/lib/python3.10/types.py
import collections.abc as __collections_abc


# functions

def __pyx_unpickle_FrozenList(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_FrozenList(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class FrozenList(object):
    """ FrozenList(items=None) """
    def append(self, item): # real signature unknown; restored from __doc__
        """ FrozenList.append(self, item) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ FrozenList.clear(self) """
        pass

    def count(self, item): # real signature unknown; restored from __doc__
        """ FrozenList.count(self, item) """
        pass

    def extend(self, items): # real signature unknown; restored from __doc__
        """ FrozenList.extend(self, items) """
        pass

    def freeze(self): # real signature unknown; restored from __doc__
        """ FrozenList.freeze(self) """
        pass

    def index(self, item): # real signature unknown; restored from __doc__
        """ FrozenList.index(self, item) """
        pass

    def insert(self, pos, item): # real signature unknown; restored from __doc__
        """ FrozenList.insert(self, pos, item) """
        pass

    def pop(self, index=-1): # real signature unknown; restored from __doc__
        """ FrozenList.pop(self, index=-1) """
        pass

    def remove(self, item): # real signature unknown; restored from __doc__
        """ FrozenList.remove(self, item) """
        pass

    def reverse(self): # real signature unknown; restored from __doc__
        """ FrozenList.reverse(self) """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """
        Represent a PEP 585 generic type
        
        E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).
        """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __init__(self, items=None): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_cython__(self): # real signature unknown; restored from __doc__
        """ FrozenList.__reduce_cython__(self) """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FrozenList.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __reversed__(self): # real signature unknown; restored from __doc__
        """ FrozenList.__reversed__(self) """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __setstate_cython__(self, __pyx_state): # real signature unknown; restored from __doc__
        """ FrozenList.__setstate_cython__(self, __pyx_state) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FrozenList.__setstate_cython__(self, __pyx_state) """
        pass

    frozen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fdd0670e6a0>'


class MutableSequence(__collections_abc.Sequence):
    """
    All the operations on a read-write sequence.
    
        Concrete subclasses must provide __new__ or __init__,
        __getitem__, __setitem__, __delitem__, __len__, and insert().
    """
    def append(self, value): # reliably restored by inspect
        """ S.append(value) -- append value to the end of the sequence """
        pass

    def clear(self): # reliably restored by inspect
        """ S.clear() -> None -- remove all items from S """
        pass

    def extend(self, values): # reliably restored by inspect
        """ S.extend(iterable) -- extend sequence by appending elements from the iterable """
        pass

    def insert(self, index, value): # reliably restored by inspect
        """ S.insert(index, value) -- insert value before index """
        pass

    def pop(self, index=-1): # reliably restored by inspect
        """
        S.pop([index]) -> item -- remove and return item at index (default last).
                   Raise IndexError if list is empty or index is out of range.
        """
        pass

    def remove(self, value): # reliably restored by inspect
        """
        S.remove(value) -- remove first occurrence of value.
                   Raise ValueError if the value is not present.
        """
        pass

    def reverse(self): # reliably restored by inspect
        """ S.reverse() -- reverse *IN PLACE* """
        pass

    def __delitem__(self, index): # reliably restored by inspect
        # no doc
        pass

    def __iadd__(self, values): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, index, value): # reliably restored by inspect
        # no doc
        pass

    _abc_impl = None # (!) real value is '<_abc._abc_data object at 0x7fdd06e72780>'
    __abstractmethods__ = frozenset({'insert', '__setitem__', '__delitem__', '__getitem__', '__len__'})
    __slots__ = ()


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fdd0670e800>'

__spec__ = None # (!) real value is "ModuleSpec(name='frozenlist._frozenlist', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fdd0670e800>, origin='/home/kadosh/PycharmProjects/BotFactory/venv/lib/python3.10/site-packages/frozenlist/_frozenlist.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

