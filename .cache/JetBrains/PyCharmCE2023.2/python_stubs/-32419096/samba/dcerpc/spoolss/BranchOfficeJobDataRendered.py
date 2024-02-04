# encoding: utf-8
# module samba.dcerpc.spoolss
# from /usr/lib/python3/dist-packages/samba/dcerpc/spoolss.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" spoolss DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class BranchOfficeJobDataRendered(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type int16"""

    Copies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type int16"""

    ICMMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    PrintQuality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type int16"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type hyper"""

    TTOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type int16"""

    YResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type int16"""



