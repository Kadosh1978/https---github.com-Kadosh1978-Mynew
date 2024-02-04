# encoding: utf-8
# module samba.dcerpc.spoolss
# from /usr/lib/python3/dist-packages/samba/dcerpc/spoolss.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" spoolss DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class AddDriverInfo6(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    architecture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    config_file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    data_file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    default_datatype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    dependent_files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_StringArray"""

    driver_date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type NTTIME"""

    driver_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    driver_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    driver_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type hyper"""

    hardware_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    help_file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    manufacturer_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    manufacturer_url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    monitor_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    previous_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_StringArray"""

    provider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type spoolss_DriverOSVersion"""

    _ndr_size_dependent_files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    _ndr_size_previous_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""



