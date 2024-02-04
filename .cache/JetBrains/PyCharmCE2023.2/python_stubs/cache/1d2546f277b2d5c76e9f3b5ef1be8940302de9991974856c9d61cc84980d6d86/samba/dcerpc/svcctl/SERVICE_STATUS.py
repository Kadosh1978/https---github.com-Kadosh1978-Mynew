# encoding: utf-8
# module samba.dcerpc.svcctl
# from /usr/lib/python3/dist-packages/samba/dcerpc/svcctl.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" svcctl DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class SERVICE_STATUS(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    check_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    controls_accepted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type svcctl_ControlsAccepted"""

    service_exit_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type svcctl_ServiceStatus"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    wait_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    win32_exit_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type WERROR"""



