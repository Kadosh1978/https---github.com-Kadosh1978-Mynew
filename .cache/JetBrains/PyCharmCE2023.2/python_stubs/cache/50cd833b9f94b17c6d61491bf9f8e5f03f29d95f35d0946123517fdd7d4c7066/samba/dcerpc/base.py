# encoding: utf-8
# module samba.dcerpc.base
# from /usr/lib/python3/dist-packages/samba/dcerpc/base.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" DCE/RPC protocol implementation """

# imports
import misc as __misc
import talloc as __talloc


# no functions
# classes

class bind_time_features_syntax(__misc.ndr_syntax_id):
    """ bind_time_features_syntax(features) """
    def __init__(self, features): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ClientConnection(object):
    """
    ClientConnection(binding, syntax, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    syntax should be a tuple with a GUID and version number of an interface
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    """
    def request(self, opnum, data, p_object=None): # real signature unknown; restored from __doc__
        """
        S.request(opnum, data, object=None) -> data
        Make a raw request
        """
        pass

    def transport_encrypted(self, *args, **kwargs): # real signature unknown
        """ Check if the DCE transport is encrypted """
        pass

    def __init__(self, binding, syntax, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    abstract_syntax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """syntax id of the abstract syntax"""

    request_timeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """request timeout,	in seconds"""

    server_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name of the server, if connected over SMB"""

    session_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """session key (as used for blob encryption on LSA and SAMR)"""

    transfer_syntax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """syntax id of the transfer syntax"""

    user_session_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """user_session key (as used for blob encryption on DRSUAPI)"""



class ndr_pointer(__talloc.BaseObject):
    """ ndr_pointer(value) """
    def __init__(self, value): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the value store by the pointer"""



class transfer_syntax_ndr(__misc.ndr_syntax_id):
    """ transfer_syntax_ndr() """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class transfer_syntax_ndr64(__misc.ndr_syntax_id):
    """ transfer_syntax_ndr64() """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d39870>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.base', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d39870>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/base.cpython-310-x86_64-linux-gnu.so')"

