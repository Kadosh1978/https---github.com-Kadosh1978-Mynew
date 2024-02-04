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


class AsyncIOEngine(__enum.Enum):
    """ An enumeration. """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initial start value or None
                count: the number of existing members
                last_value: the last value assigned or None
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    CUSTOM_IO_MANAGER = None # (!) real value is "<AsyncIOEngine.CUSTOM_IO_MANAGER: 'custom_io_manager'>"
    POLLER = None # (!) real value is "<AsyncIOEngine.POLLER: 'poller'>"
    _member_map_ = {
        'CUSTOM_IO_MANAGER': None, # (!) real value is "<AsyncIOEngine.CUSTOM_IO_MANAGER: 'custom_io_manager'>"
        'POLLER': None, # (!) real value is "<AsyncIOEngine.POLLER: 'poller'>"
    }
    _member_names_ = [
        'CUSTOM_IO_MANAGER',
        'POLLER',
    ]
    _member_type_ = object
    _value2member_map_ = {
        'custom_io_manager': None, # (!) real value is "<AsyncIOEngine.CUSTOM_IO_MANAGER: 'custom_io_manager'>"
        'poller': None, # (!) real value is "<AsyncIOEngine.POLLER: 'poller'>"
    }


