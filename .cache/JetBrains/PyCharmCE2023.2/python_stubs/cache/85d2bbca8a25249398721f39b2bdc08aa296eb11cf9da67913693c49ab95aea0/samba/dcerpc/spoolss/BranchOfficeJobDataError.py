# encoding: utf-8
# module samba.dcerpc.spoolss
# from /usr/lib/python3/dist-packages/samba/dcerpc/spoolss.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" spoolss DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class BranchOfficeJobDataError(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    LastError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type WERROR"""

    pDataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    pDocumentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    pErrorDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    pJobError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    pMachineName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    pPrinterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    PrintedPages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    PrintedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type hyper"""

    pUserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    TotalPages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    TotalSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type hyper"""



