# encoding: utf-8
# module tdb
# from /usr/lib/python3/dist-packages/tdb.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" simple key-value database that supports multiple writers. """
# no imports

# Variables with simple values

ALLOW_NESTING = 512

BIGENDIAN = 32

CLEAR_IF_FIRST = 1

CONVERT = 16

DEFAULT = 0

DISALLOW_NESTING = 1024

INCOMPATIBLE_HASH = 2048

INSERT = 2
INTERNAL = 2

MODIFY = 3

NOLOCK = 4
NOMMAP = 8
NOSYNC = 64

REPLACE = 1

SEQNUM = 128

VOLATILE = 256

__docformat__ = 'restructuredText'

__version__ = '1.4.5'

# functions

def open(name, hash_size=0, tdb_flags=None, flags=None, mode=0600): # real signature unknown; restored from __doc__
    """
    open(name, hash_size=0, tdb_flags=TDB_DEFAULT, flags=O_RDWR, mode=0600)
    Open a TDB file.
    """
    pass

# classes

class Tdb(object):
    """ A TDB file """
    def add_flags(self, flags): # real signature unknown; restored from __doc__
        """ S.add_flags(flags) -> None """
        pass

    def append(self, key, value): # real signature unknown; restored from __doc__
        """
        S.append(key, value) -> None
        Append data to an existing key.
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """
        S.clear() -> None
        Wipe the entire database.
        """
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def delete(self, key): # real signature unknown; restored from __doc__
        """
        S.delete(key) -> None
        Delete an entry.
        """
        pass

    def enable_seqnum(self): # real signature unknown; restored from __doc__
        """ S.enable_seqnum() -> None """
        pass

    def firstkey(self): # real signature unknown; restored from __doc__
        """
        S.firstkey() -> data
        Return the first key in this database.
        """
        pass

    def get(self, key): # real signature unknown; restored from __doc__
        """
        S.get(key) -> value
        Fetch a value.
        """
        pass

    def increment_seqnum_nonblock(self): # real signature unknown; restored from __doc__
        """ S.increment_seqnum_nonblock() -> None """
        pass

    def keys(self): # real signature unknown; restored from __doc__
        """ S.iterkeys() -> iterator """
        pass

    def lock_all(self, *args, **kwargs): # real signature unknown
        pass

    def nextkey(self, key): # real signature unknown; restored from __doc__
        """
        S.nextkey(key) -> data
        Return the next key in this database.
        """
        pass

    def read_lock_all(self, *args, **kwargs): # real signature unknown
        pass

    def read_unlock_all(self, *args, **kwargs): # real signature unknown
        pass

    def remove_flags(self, flags): # real signature unknown; restored from __doc__
        """ S.remove_flags(flags) -> None """
        pass

    def reopen(self, *args, **kwargs): # real signature unknown
        """ Reopen this file. """
        pass

    def repack(self): # real signature unknown; restored from __doc__
        """
        S.repack() -> None
        Repack the entire database.
        """
        pass

    def store(self, key, data, flag=None): # real signature unknown; restored from __doc__
        """ S.store(key, data, flag=REPLACE) -> NoneStore data. """
        pass

    def storev(self, key, data, flag=None): # real signature unknown; restored from __doc__
        """ S.storev(key, data, flag=REPLACE) -> NoneStore several data. """
        pass

    def transaction_cancel(self): # real signature unknown; restored from __doc__
        """
        S.transaction_cancel() -> None
        Cancel the currently active transaction.
        """
        pass

    def transaction_commit(self): # real signature unknown; restored from __doc__
        """
        S.transaction_commit() -> None
        Commit the currently active transaction.
        """
        pass

    def transaction_prepare_commit(self): # real signature unknown; restored from __doc__
        """
        S.transaction_prepare_commit() -> None
        Prepare to commit the currently active transaction
        """
        pass

    def transaction_start(self): # real signature unknown; restored from __doc__
        """
        S.transaction_start() -> None
        Start a new transaction.
        """
        pass

    def unlock_all(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The filename of this TDB file."""

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freelist_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hash_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    map_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_dead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seqnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db10>'

__spec__ = None # (!) real value is "ModuleSpec(name='tdb', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db10>, origin='/usr/lib/python3/dist-packages/tdb.cpython-310-x86_64-linux-gnu.so')"

