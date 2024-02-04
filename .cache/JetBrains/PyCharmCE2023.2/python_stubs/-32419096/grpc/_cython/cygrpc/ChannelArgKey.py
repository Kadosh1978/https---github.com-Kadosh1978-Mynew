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

class ChannelArgKey(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    default_authority = b'grpc.default_authority'
    enable_census = b'grpc.census'
    http2_initial_sequence_number = b'grpc.http2.initial_sequence_number'
    max_concurrent_streams = b'grpc.max_concurrent_streams'
    max_receive_message_length = b'grpc.max_receive_message_length'
    max_send_message_length = b'grpc.max_send_message_length'
    primary_user_agent_string = b'grpc.primary_user_agent'
    secondary_user_agent_string = b'grpc.secondary_user_agent'
    ssl_session_cache = b'grpc.ssl_session_cache'
    ssl_target_name_override = b'grpc.ssl_target_name_override'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'grpc._cython.cygrpc', 'enable_census': b'grpc.census', 'max_concurrent_streams': b'grpc.max_concurrent_streams', 'max_receive_message_length': b'grpc.max_receive_message_length', 'max_send_message_length': b'grpc.max_send_message_length', 'http2_initial_sequence_number': b'grpc.http2.initial_sequence_number', 'default_authority': b'grpc.default_authority', 'primary_user_agent_string': b'grpc.primary_user_agent', 'secondary_user_agent_string': b'grpc.secondary_user_agent', 'ssl_session_cache': b'grpc.ssl_session_cache', 'ssl_target_name_override': b'grpc.ssl_target_name_override', '__dict__': <attribute '__dict__' of 'ChannelArgKey' objects>, '__weakref__': <attribute '__weakref__' of 'ChannelArgKey' objects>, '__doc__': None})"


