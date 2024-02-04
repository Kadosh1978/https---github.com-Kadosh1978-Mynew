# encoding: utf-8
# module grpc._cython.cygrpc
# from /usr/lib/python3/dist-packages/grpc/_cython/cygrpc.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import logging as logging # /usr/lib/python3.10/logging/__init__.py
import os as os # /usr/lib/python3.10/os.py
import sys as sys # <module 'sys' (built-in)>
import threading as threading # /usr/lib/python3.10/threading.py
import time as time # <module 'time' (built-in)>
import grpc as grpc # /usr/lib/python3/dist-packages/grpc/__init__.py
import asyncio as asyncio # /usr/lib/python3.10/asyncio/__init__.py
import collections as collections # /usr/lib/python3.10/collections/__init__.py
import pkgutil as pkgutil # /usr/lib/python3.10/pkgutil.py
import errno as errno # <module 'errno' (built-in)>
import platform as platform # /usr/lib/python3.10/platform.py
import socket as native_socket # /usr/lib/python3.10/socket.py
import ipaddress as ipaddress # /usr/lib/python3.10/ipaddress.py
import socket as socket # /usr/lib/python3.10/socket.py
import enum as enum # /usr/lib/python3.10/enum.py
import inspect as inspect # /usr/lib/python3.10/inspect.py
import traceback as traceback # /usr/lib/python3.10/traceback.py
import functools as functools # /usr/lib/python3.10/functools.py
import enum as __enum


from .tuple import tuple

class _Metadatum(tuple):
    """ _Metadatum(key, value) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new _Metadatum object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new _Metadatum object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, key, value): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, key, value): # reliably restored by inspect
        """ Create new instance of _Metadatum(key, value) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    key = _tuplegetter(0, 'Alias for field number 0')
    value = _tuplegetter(1, 'Alias for field number 1')
    _fields = (
        'key',
        'value',
    )
    _field_defaults = {}
    __match_args__ = (
        'key',
        'value',
    )
    __slots__ = ()


