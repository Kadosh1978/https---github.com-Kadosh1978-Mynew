# encoding: utf-8
# module samba.dcerpc.nbt
# from /usr/lib/python3/dist-packages/samba/dcerpc/nbt.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" nbt DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class nbt(__dcerpc.ClientConnection):
    """
    nbt(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    NBT messages
    """
    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


