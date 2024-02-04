# encoding: utf-8
# module samba.messaging
# from /usr/lib/python3/dist-packages/samba/messaging.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" Internal RPC """
# no imports

# Variables with simple values

IRPC_CALL_TIMEOUT = 10

IRPC_CALL_TIMEOUT_INF = 0

# no functions
# classes

class Messaging(object):
    """
    Messaging(own_id=None)
    Create a new object that can be used to communicate with the peers in the specified messaging path.
    """
    def deregister(self, (callback, context), msg_type): # real signature unknown; restored from __doc__
        """
        S.deregister((callback, context), msg_type) -> None
        Deregister a message handler The callback and context must be supplied as the exact same two-element tuple as was used as registration time.
        """
        pass

    def irpc_add_name(self, name): # real signature unknown; restored from __doc__
        """
        S.irpc_add_name(name) -> None
        Add this context to the list of server_id values that are registered for a particular name
        """
        pass

    def irpc_all_servers(self): # real signature unknown; restored from __doc__
        """
        S.irpc_all_servers() -> list
        Get list of all registered names and the associated server_id values
        """
        return []

    def irpc_remove_name(self, name): # real signature unknown; restored from __doc__
        """
        S.irpc_remove_name(name) -> None
        Remove this context from the list of server_id values that are registered for a particular name
        """
        pass

    def irpc_servers_byname(self, name): # real signature unknown; restored from __doc__
        """
        S.irpc_servers_byname(name) -> list
        Get list of server_id values that are registered for a particular name
        """
        return []

    def loop_once(self, timeout): # real signature unknown; restored from __doc__
        """
        S.loop_once(timeout) -> None
        Loop on the internal event context until we get an event (which might be a message calling the callback), timeout after timeout seconds (if not 0)
        """
        pass

    def register(self, (callback, context), msg_type=None): # real signature unknown; restored from __doc__
        """
        S.register((callback, context), msg_type=None) -> msg_type
        Register a message handler.  The callback and context must be supplied as a two-element tuple.
        """
        pass

    def send(self, target, msg_type, data): # real signature unknown; restored from __doc__
        """
        S.send(target, msg_type, data) -> None
        Send a message
        """
        pass

    def __init__(self, own_id=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    server_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """local server id"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d570>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.messaging', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d570>, origin='/usr/lib/python3/dist-packages/samba/messaging.cpython-310-x86_64-linux-gnu.so')"

