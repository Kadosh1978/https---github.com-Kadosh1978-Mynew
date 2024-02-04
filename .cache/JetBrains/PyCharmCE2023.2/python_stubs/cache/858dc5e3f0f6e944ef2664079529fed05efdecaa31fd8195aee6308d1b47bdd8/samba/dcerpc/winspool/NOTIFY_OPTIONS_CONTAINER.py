# encoding: utf-8
# module samba.dcerpc.winspool
# from /usr/lib/python3/dist-packages/samba/dcerpc/winspool.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" winspool DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class NOTIFY_OPTIONS_CONTAINER(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    pOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_NotifyOption"""



