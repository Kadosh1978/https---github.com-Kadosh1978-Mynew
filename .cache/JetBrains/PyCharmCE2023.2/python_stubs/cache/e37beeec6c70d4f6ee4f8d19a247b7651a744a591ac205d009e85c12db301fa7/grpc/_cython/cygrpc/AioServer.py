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


from .object import object

class AioServer(object):
    # no doc
    def add_generic_rpc_handlers(self, *args, **kwargs): # real signature unknown
        pass

    def add_insecure_port(self, *args, **kwargs): # real signature unknown
        pass

    def add_secure_port(self, *args, **kwargs): # real signature unknown
        pass

    def shutdown(self, *args, **kwargs): # real signature unknown
        """
        Gracefully shutdown the Core server.
        
                Application should only call shutdown once.
        
                Args:
                  grace: An optional float indicating the length of grace period in
                    seconds.
        """
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def wait_for_termination(self, *args, **kwargs): # real signature unknown
        pass

    def _request_call(self, *args, **kwargs): # real signature unknown
        pass

    def _server_main_loop(self, *args, **kwargs): # real signature unknown
        pass

    def _serving_task_crash_handler(self, *args, **kwargs): # real signature unknown
        """ Shutdown the server immediately if unexpectedly exited. """
        pass

    def _start_shutting_down(self, *args, **kwargs): # real signature unknown
        """
        Prepares the server to shutting down.
        
                This coroutine function is NOT coroutine-safe.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f4211a6bf00>'


