# encoding: utf-8
# module samba.netbios
# from /usr/lib/python3/dist-packages/samba/netbios.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" NetBIOS over TCP/IP support """
# no imports

# no functions
# classes

class Node(object):
    """
    Node()
    Create a new NetBIOS node
    """
    def name_status(self, name, dest, timeout=0, retries=0): # real signature unknown; restored from __doc__
        """
        S.name_status(name, dest, timeout=0, retries=0) -> (reply_from, name, status)
        Find the status of a name
        """
        pass

    def query_name(self, name, dest, broadcast=True, wins=False, timeout=0, retries=3): # real signature unknown; restored from __doc__
        """
        S.query_name(name, dest, broadcast=True, wins=False, timeout=0, retries=3) -> (reply_from, name, reply_addr)
        Query for a NetBIOS name
        """
        pass

    def refresh_name(self, name, address, dest, nb_flags=0, broadcast=True, ttl=0, timeout=0, retries=0): # real signature unknown; restored from __doc__
        """
        S.refresh_name(name, address, dest, nb_flags=0, broadcast=True, ttl=0, timeout=0, retries=0) -> (reply_from, name, reply_addr, rcode)
        release a previously registered name
        """
        pass

    def register_name(self, name, address, dest, register_demand=True, broadcast=True, multi_homed=True, ttl=0, timeout=0, retries=0): # real signature unknown; restored from __doc__
        """
        S.register_name(name, address, dest, register_demand=True, broadcast=True, multi_homed=True, ttl=0, timeout=0, retries=0) -> (reply_from, name, reply_addr, rcode)
        Register a new name
        """
        pass

    def release_name(self, name, address, dest, nb_flags=0, broadcast=None, timeout=0, retries=3): # real signature unknown; restored from __doc__
        """
        S.release_name(name, address, dest, nb_flags=0, broadcast=true, timeout=0, retries=3) -> (reply_from, name, reply_addr, rcode)
        release a previously registered name
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d540>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.netbios', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d540>, origin='/usr/lib/python3/dist-packages/samba/netbios.cpython-310-x86_64-linux-gnu.so')"

