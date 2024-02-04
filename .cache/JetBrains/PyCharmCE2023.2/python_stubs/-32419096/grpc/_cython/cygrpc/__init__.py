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


# Variables with simple values

gevent_event = None
gevent_g = None
gevent_hub = None
gevent_socket = None

GRPC_COMPRESSION_CHANNEL_DEFAULT_ALGORITHM = b'grpc.default_compression_algorithm'

GRPC_COMPRESSION_REQUEST_ALGORITHM_MD_KEY = b'grpc-internal-encoding-request'

g_event = None
g_pool = None

_AWAIT_THREADS_TIMEOUT_SECONDS = 5

_EMPTY_FLAGS = 0
_EMPTY_MASK = 0

_fork_handler_failed = False

_GRPC_ENABLE_FORK_SUPPORT = False

_INTERNAL_CALL_ERROR_MESSAGE_FORMAT = 'Internal gRPC call error %d. Please report to https://github.com/grpc/grpc/issues'

_NON_OK_CALL_REPRESENTATION = '<{} of RPC that terminated with:\n\tstatus = {}\n\tdetails = "{}"\n\tdebug_error_string = "{}"\n>'

_OK_CALL_REPRESENTATION = '<{} of RPC that terminated with:\n\tstatus = {}\n\tdetails = "{}"\n>'

_UNKNOWN_CANCELLATION_DETAILS = 'RPC cancelled for unknown reason.'

# functions

def applysockopts(*args, **kwargs): # real signature unknown
    pass

def async_callback_func(*args, **kwargs): # real signature unknown
    pass

def async_generator_to_generator(*args, **kwargs): # real signature unknown
    """ Converts an async generator into generator. """
    pass

def auth_context(*args, **kwargs): # real signature unknown
    pass

def block_if_fork_in_progress(*args, **kwargs): # real signature unknown
    pass

def build_census_context(*args, **kwargs): # real signature unknown
    pass

def channelz_get_channel(*args, **kwargs): # real signature unknown
    pass

def channelz_get_server(*args, **kwargs): # real signature unknown
    pass

def channelz_get_servers(*args, **kwargs): # real signature unknown
    pass

def channelz_get_server_sockets(*args, **kwargs): # real signature unknown
    pass

def channelz_get_socket(*args, **kwargs): # real signature unknown
    pass

def channelz_get_subchannel(*args, **kwargs): # real signature unknown
    pass

def channelz_get_top_channels(*args, **kwargs): # real signature unknown
    pass

def channel_credentials_alts(*args, **kwargs): # real signature unknown
    pass

def channel_credentials_local(*args, **kwargs): # real signature unknown
    pass

def compression_algorithm_name(*args, **kwargs): # real signature unknown
    pass

def enter_user_request_generator(*args, **kwargs): # real signature unknown
    pass

def execute_batch(*args, **kwargs): # real signature unknown
    """ The callback version of start batch operations. """
    pass

def fork_handlers_and_grpc_init(*args, **kwargs): # real signature unknown
    pass

def fork_register_channel(*args, **kwargs): # real signature unknown
    pass

def fork_unregister_channel(*args, **kwargs): # real signature unknown
    pass

def generator_to_async_generator(*args, **kwargs): # real signature unknown
    """
    Converts a generator into async generator.
    
        The generator might block, so we need to delegate the iteration to thread
        pool. Also, we can't simply delegate __next__ to the thread pool, otherwise
        we will see following error:
    
            TypeError: StopIteration interacts badly with generators and cannot be
                raised into a Future
    """
    pass

def get_deadline_from_context(*args, **kwargs): # real signature unknown
    pass

def get_fork_epoch(*args, **kwargs): # real signature unknown
    pass

def init_grpc_aio(*args, **kwargs): # real signature unknown
    """
    Initializes the gRPC AsyncIO module.
    
        Expected to be invoked on critical class constructors.
        E.g., AioChannel, AioServer.
    """
    pass

def init_grpc_gevent(*args, **kwargs): # real signature unknown
    pass

def install_asyncio_iomgr(*args, **kwargs): # real signature unknown
    pass

def install_context_from_request_call_event(*args, **kwargs): # real signature unknown
    pass

def is_fork_support_enabled(*args, **kwargs): # real signature unknown
    pass

def peer_identities(*args, **kwargs): # real signature unknown
    pass

def peer_identity_key(*args, **kwargs): # real signature unknown
    pass

def return_from_user_request_generator(*args, **kwargs): # real signature unknown
    pass

def schedule_coro_threadsafe(*args, **kwargs): # real signature unknown
    pass

def server_certificate_config_ssl(*args, **kwargs): # real signature unknown
    pass

def server_credentials_alts(*args, **kwargs): # real signature unknown
    pass

def server_credentials_local(*args, **kwargs): # real signature unknown
    pass

def server_credentials_ssl(*args, **kwargs): # real signature unknown
    pass

def server_credentials_ssl_dynamic_cert_config(*args, **kwargs): # real signature unknown
    pass

def set_async_callback_func(*args, **kwargs): # real signature unknown
    pass

def set_census_context_on_call(*args, **kwargs): # real signature unknown
    pass

def shutdown_grpc_aio(*args, **kwargs): # real signature unknown
    """
    Shuts down the gRPC AsyncIO module.
    
        Expected to be invoked on critical class destructors.
        E.g., AioChannel, AioServer.
    """
    pass

def socket_accept_async(*args, **kwargs): # real signature unknown
    pass

def socket_connect_async(*args, **kwargs): # real signature unknown
    pass

def socket_read_async(*args, **kwargs): # real signature unknown
    pass

def socket_resolve_async_python(*args, **kwargs): # real signature unknown
    pass

def socket_sendmsg(*args, **kwargs): # real signature unknown
    pass

def socket_write_async(*args, **kwargs): # real signature unknown
    pass

def uninstall_context(*args, **kwargs): # real signature unknown
    pass

def _asyncio_apply_socket_options(*args, **kwargs): # real signature unknown
    pass

def _auth_plugin_callback_wrapper(*args, **kwargs): # real signature unknown
    pass

def _find_method_handler(*args, **kwargs): # real signature unknown
    pass

def _finish_handler_with_stream_responses(*args, **kwargs): # real signature unknown
    """
    Finishes server method handler with multiple responses.
    
        This function executes the application handler, and handles response
        sending, as well as errors. It is shared between unary-stream and
        stream-stream handlers.
    """
    pass

def _finish_handler_with_unary_response(*args, **kwargs): # real signature unknown
    """
    Finishes server method handler with a single response.
        
        This function executes the application handler, and handles response
        sending, as well as errors. It is shared between unary-unary and
        stream-unary handlers.
    """
    pass

def _grpc_shutdown_wrapper(*args, **kwargs): # real signature unknown
    """
    A thin Python wrapper of Core's shutdown function.
    
        Define functions are not allowed in "cdef" functions, and Cython complains
        about a simple lambda with a C function.
    """
    pass

def _handle_callback_wrapper(*args, **kwargs): # real signature unknown
    pass

def _handle_cancellation_from_core(*args, **kwargs): # real signature unknown
    pass

def _handle_exceptions(*args, **kwargs): # real signature unknown
    pass

def _handle_rpc(*args, **kwargs): # real signature unknown
    pass

def _handle_stream_stream_rpc(*args, **kwargs): # real signature unknown
    pass

def _handle_stream_unary_rpc(*args, **kwargs): # real signature unknown
    pass

def _handle_unary_stream_rpc(*args, **kwargs): # real signature unknown
    pass

def _handle_unary_unary_rpc(*args, **kwargs): # real signature unknown
    pass

def _is_async_handler(*args, **kwargs): # real signature unknown
    """ Inspect if a method handler is async or sync. """
    pass

def _receive_initial_metadata(*args, **kwargs): # real signature unknown
    pass

def _receive_message(*args, **kwargs): # real signature unknown
    """
    Retrives parsed messages from Core.
    
        The messages maybe already in Core's buffer, so there isn't a 1-to-1
        mapping between this and the underlying "socket.read()". Also, eventually,
        this function will end with an EOF, which reads empty message.
    """
    pass

def _run_interceptor(*args, **kwargs): # real signature unknown
    pass

def _schedule_rpc_coro(*args, **kwargs): # real signature unknown
    pass

def _send_error_status_from_server(*args, **kwargs): # real signature unknown
    pass

def _send_initial_metadata(*args, **kwargs): # real signature unknown
    pass

def _send_message(*args, **kwargs): # real signature unknown
    pass

def _spawn_callback_async(*args, **kwargs): # real signature unknown
    pass

def _spawn_callback_in_thread(*args, **kwargs): # real signature unknown
    pass

def _spawn_greenlet(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_AioServer(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_CensusContext(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_ChannelCredentials(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle__Tag(*args, **kwargs): # real signature unknown
    pass

# classes

from .BaseError import BaseError
from .AbortError import AbortError
from .AioChannel import AioChannel
from .AioRpcStatus import AioRpcStatus
from .AioServer import AioServer
from .ChannelCredentials import ChannelCredentials
from .ALTSChannelCredentials import ALTSChannelCredentials
from .AsyncIOEngine import AsyncIOEngine
from .BaseCompletionQueue import BaseCompletionQueue
from .BatchOperationEvent import BatchOperationEvent
from .Call import Call
from .CallbackCompletionQueue import CallbackCompletionQueue
from .CallbackFailureHandler import CallbackFailureHandler
from .CallbackWrapper import CallbackWrapper
from .CallCredentials import CallCredentials
from .CallDetails import CallDetails
from .CallError import CallError
from .CensusContext import CensusContext
from .Channel import Channel
from .ChannelArgKey import ChannelArgKey
from .CompletionQueue import CompletionQueue
from .CompletionType import CompletionType
from .CompositeCallCredentials import CompositeCallCredentials
from .CompositeChannelCredentials import CompositeChannelCredentials
from .CompressionAlgorithm import CompressionAlgorithm
from .CompressionLevel import CompressionLevel
from .CompressionOptions import CompressionOptions
from .ConnectivityEvent import ConnectivityEvent
from .ConnectivityState import ConnectivityState
from .InternalError import InternalError
from .ExecuteBatchError import ExecuteBatchError
from .ForkManagedThread import ForkManagedThread
from .GrpcCallWrapper import GrpcCallWrapper
from .InitialMetadataFlags import InitialMetadataFlags
from .IntegratedCall import IntegratedCall
from .LocalChannelCredentials import LocalChannelCredentials
from .LocalConnectionType import LocalConnectionType
from .MetadataPluginCallCredentials import MetadataPluginCallCredentials
from .Operation import Operation
from .OperationType import OperationType
from .PollerCompletionQueue import PollerCompletionQueue
from .PropagationConstants import PropagationConstants
from .ReceiveCloseOnServerOperation import ReceiveCloseOnServerOperation
from .ReceiveInitialMetadataOperation import ReceiveInitialMetadataOperation
from .ReceiveMessageOperation import ReceiveMessageOperation
from .ReceiveStatusOnClientOperation import ReceiveStatusOnClientOperation
from .RequestCallEvent import RequestCallEvent
from .ResolveWrapper import ResolveWrapper
from .RPCState import RPCState
from .SegregatedCall import SegregatedCall
from .SendCloseFromClientOperation import SendCloseFromClientOperation
from .SendInitialMetadataOperation import SendInitialMetadataOperation
from .SendMessageOperation import SendMessageOperation
from .SendStatusFromServerOperation import SendStatusFromServerOperation
from .Server import Server
from .ServerCertificateConfig import ServerCertificateConfig
from .ServerCredentials import ServerCredentials
from .ServerShutdownEvent import ServerShutdownEvent
from .SocketWrapper import SocketWrapper
from .SSLChannelCredentials import SSLChannelCredentials
from .SslPemKeyCertPair import SslPemKeyCertPair
from .SSLSessionCacheLRU import SSLSessionCacheLRU
from .StatusCode import StatusCode
from .TimerWrapper import TimerWrapper
from .UsageError import UsageError
from .WriteFlag import WriteFlag
from ._ActiveThreadCount import _ActiveThreadCount
from ._AioCall import _AioCall
from ._AioState import _AioState
from ._AsyncioResolver import _AsyncioResolver
from ._AsyncioSocket import _AsyncioSocket
from ._AsyncioTimer import _AsyncioTimer
from ._Tag import _Tag
from ._BatchOperationTag import _BatchOperationTag
from ._CallState import _CallState
from ._ChannelArg import _ChannelArg
from ._ChannelArgs import _ChannelArgs
from ._ChannelState import _ChannelState
from ._ConnectivityTag import _ConnectivityTag
from ._EOF import _EOF
from ._ForkState import _ForkState
from ._GrpcArgWrapper import _GrpcArgWrapper
from ._HandlerCallDetails import _HandlerCallDetails
from ._MessageReceiver import _MessageReceiver
from ._Metadatum import _Metadatum
from ._RequestCallError import _RequestCallError
from ._RequestCallTag import _RequestCallTag
from ._ServerShutdownTag import _ServerShutdownTag
from ._ServerStoppedError import _ServerStoppedError
from ._ServicerContext import _ServicerContext
from ._SyncServicerContext import _SyncServicerContext
from ._WatchConnectivityFailed import _WatchConnectivityFailed
# variables with complex values

EOF = None # (!) real value is '<grpc.aio.EOF>'

_COMPRESSION_METADATA_STRING_MAPPING = {
    0: 'identity',
    1: 'deflate',
    2: 'gzip',
}

_fork_state = None # (!) real value is '<grpc._cython.cygrpc._ForkState object at 0x7f421129c6a0>'

_IMMUTABLE_EMPTY_METADATA = ()

_LOGGER = None # (!) real value is '<Logger grpc._cython.cygrpc (DEBUG)>'

_TRUE_VALUES = [
    'yes',
    'Yes',
    'YES',
    'true',
    'True',
    'TRUE',
    '1',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211a37be0>'

__pyx_capi__ = {
    '__postfork_child': None, # (!) real value is '<capsule object "void (void)" at 0x7f4211a6ab20>'
    '__postfork_parent': None, # (!) real value is '<capsule object "void (void)" at 0x7f4211a6aaf0>'
    '__prefork': None, # (!) real value is '<capsule object "void (void)" at 0x7f4211a6aac0>'
    '_check_and_raise_call_error_no_metadata': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x7f4211a6a6d0>'
    '_check_call_error': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *)" at 0x7f4211a6a700>'
    '_check_call_error_no_metadata': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x7f4211a6a6a0>'
    '_compare_pointer': None, # (!) real value is '<capsule object "int (void *, void *)" at 0x7f4211a6aa60>'
    '_composition': None, # (!) real value is '<capsule object "grpc_call_credentials *(PyObject *)" at 0x7f4211a6a790>'
    '_copy_pointer': None, # (!) real value is '<capsule object "void *(void *)" at 0x7f4211a6aa00>'
    '_copy_slice': None, # (!) real value is '<capsule object "grpc_slice (grpc_slice)" at 0x7f4211a6a910>'
    '_custom_op_on_c_call': None, # (!) real value is '<capsule object "PyObject *(int, grpc_call *)" at 0x7f4211a6aa90>'
    '_destroy': None, # (!) real value is '<capsule object "void (void *)" at 0x7f4211a6a760>'
    '_destroy_pointer': None, # (!) real value is '<capsule object "void (void *)" at 0x7f4211a6aa30>'
    '_get_metadata': None, # (!) real value is '<capsule object "int (void *, grpc_auth_metadata_context, grpc_credentials_plugin_metadata_cb, void *, grpc_metadata *, size_t *, grpc_status_code *, char const **)" at 0x7f4211a6a730>'
    '_interpret_event': None, # (!) real value is '<capsule object "PyObject *(grpc_event)" at 0x7f4211a6a7f0>'
    '_metadata': None, # (!) real value is '<capsule object "PyObject *(grpc_metadata_array *)" at 0x7f4211a6a8b0>'
    '_metadatum': None, # (!) real value is '<capsule object "PyObject *(grpc_slice, grpc_slice)" at 0x7f4211a6a880>'
    '_next': None, # (!) real value is '<capsule object "grpc_event (grpc_completion_queue *, PyObject *)" at 0x7f4211a6a7c0>'
    '_release_c_metadata': None, # (!) real value is '<capsule object "void (grpc_metadata *, int)" at 0x7f4211a6a850>'
    '_slice_bytes': None, # (!) real value is '<capsule object "PyObject *(grpc_slice)" at 0x7f4211a6a8e0>'
    '_slice_from_bytes': None, # (!) real value is '<capsule object "grpc_slice (PyObject *)" at 0x7f4211a6a940>'
    '_store_c_metadata': None, # (!) real value is '<capsule object "void (PyObject *, grpc_metadata **, size_t *)" at 0x7f4211a6a820>'
    '_time_from_timespec': None, # (!) real value is '<capsule object "double (gpr_timespec)" at 0x7f4211a6a9d0>'
    '_timespec_from_time': None, # (!) real value is '<capsule object "gpr_timespec (PyObject *)" at 0x7f4211a6a9a0>'
    '_unified_socket_write': None, # (!) real value is '<capsule object "void (int)" at 0x7f4211a6ab50>'
    '_unwrap_grpc_arg': None, # (!) real value is '<capsule object "grpc_arg (PyObject *)" at 0x7f4211a6a670>'
    '_wrap_grpc_arg': None, # (!) real value is '<capsule object "PyObject *(grpc_arg)" at 0x7f4211a6a640>'
    'default_vtable': None, # (!) real value is '<capsule object "grpc_arg_pointer_vtable" at 0x7f4211a6a610>'
    'global_completion_queue': None, # (!) real value is '<capsule object "grpc_completion_queue *(void)" at 0x7f4211a6ab80>'
    'init_grpc_aio': None, # (!) real value is '<capsule object "PyObject *(int __pyx_skip_dispatch)" at 0x7f4211a6abb0>'
    'shutdown_grpc_aio': None, # (!) real value is '<capsule object "PyObject *(int __pyx_skip_dispatch)" at 0x7f4211a6abe0>'
    'ssl_roots_override_callback': None, # (!) real value is '<capsule object "grpc_ssl_roots_override_result (char **)" at 0x7f4211a6a970>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='grpc._cython.cygrpc', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211a37be0>, origin='/usr/lib/python3/dist-packages/grpc/_cython/cygrpc.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

