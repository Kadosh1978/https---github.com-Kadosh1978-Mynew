# encoding: utf-8
# module samba.dcerpc.spoolss
# from /usr/lib/python3/dist-packages/samba/dcerpc/spoolss.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" spoolss DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DeviceMode(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    bitsperpel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    collate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DeviceModeCollate"""

    color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DeviceModeColor"""

    copies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    defaultsource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DeviceModeDefaultSource"""

    devicename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    displayflags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DeviceModeNUp"""

    displayfrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    dithertype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DeviceModeDitherType"""

    driverextra_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DATA_BLOB"""

    driverversion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    duplex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DeviceModeDuplex"""

    fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DeviceModeFields"""

    formname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    icmintent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DeviceModeICMIntent"""

    icmmethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DeviceModeICMMethod"""

    logpixels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    mediatype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DeviceModeMediaType"""

    orientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DeviceModeOrientation"""

    panningheight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    panningwidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    paperlength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    papersize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DeviceModePaperSize"""

    paperwidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    pelsheight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    pelswidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    printquality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DeviceModePrintQuality"""

    reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    specversion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DeviceModeSpecVersion"""

    ttoption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DeviceModeTTOption"""

    yresolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    __driverextra_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""



