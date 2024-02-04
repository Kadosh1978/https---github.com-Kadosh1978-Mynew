# encoding: utf-8
# module samba.dcerpc.messaging
# from /usr/lib/python3/dist-packages/samba/dcerpc/messaging.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" messaging DCE/RPC """

# imports
import talloc as __talloc


# Variables with simple values

AUTH_EVENT_NAME = 'auth_event'

DSDB_EVENT_NAME = 'dsdb_event'

DSDB_GROUP_EVENT_NAME = 'dsdb_group_event'

DSDB_PWD_EVENT_NAME = 'dsdb_password_event'

ID_CACHE_DELETE = 15
ID_CACHE_KILL = 16

MSG_AUTH_LOG = 2048

MSG_BRL_RETRY = 1792

MSG_DAEMON_READY_FD = 53

MSG_DBWRAP_MODIFIED = 4003

MSG_DEBUG = 1
MSG_DEBUGLEVEL = 6

MSG_DREPL_ALLOCATE_RID = 1796

MSG_DSDB_LOG = 2049

MSG_DSDB_PWD_LOG = 2050

MSG_FORCE_ELECTION = 257

MSG_GROUP_LOG = 2051

MSG_IRPC = 1794

MSG_NTVFS_OPLOCK_BREAK = 1795

MSG_PING = 2
MSG_PONG = 3

MSG_POOL_USAGE = 10

MSG_PREFORK_CHILD_EVENT = 49

MSG_PREFORK_PARENT_EVENT = 50

MSG_PRINTERDATA_INIT_RESET = 516

MSG_PRINTER_DRVUPGRADE = 515
MSG_PRINTER_MOD = 518
MSG_PRINTER_NOTIFY2 = 514
MSG_PRINTER_PCAP = 519
MSG_PRINTER_UPDATE = 517

MSG_PROFILE = 4
MSG_PROFILELEVEL = 8

MSG_PVFS_NOTIFY = 784

MSG_PVFS_RETRY_OPEN = 1793

MSG_REQ_DEBUGLEVEL = 5

MSG_REQ_DMALLOC_LOG_CHANGED = 12

MSG_REQ_DMALLOC_MARK = 11

MSG_REQ_POOL_USAGE = 9

MSG_REQ_PROFILELEVEL = 7

MSG_REQ_RINGBUF_LOG = 51

MSG_RINGBUF_LOG = 52

MSG_SEND_PACKET = 259

MSG_SHUTDOWN = 13

MSG_SMBXSRV_CONNECTION_PASS = 1537
MSG_SMBXSRV_CONNECTION_PASSED = 1538

MSG_SMBXSRV_SESSION_CLOSE = 1536

MSG_SMB_BLOCKING_LOCK_CANCEL = 781

MSG_SMB_BREAK_REQUEST = 774

MSG_SMB_CLOSE_FILE = 787

MSG_SMB_CONF_UPDATED = 33

MSG_SMB_FILE_RENAME = 779

MSG_SMB_FORCE_TDIS = 770

MSG_SMB_FORCE_TDIS_DENIED = 801

MSG_SMB_INJECT_FAULT = 780

MSG_SMB_KERNEL_BREAK = 778

MSG_SMB_KILL_CLIENT_IP = 790

MSG_SMB_NOTIFY = 782

MSG_SMB_NOTIFY_CANCEL_DELETED = 793

MSG_SMB_NOTIFY_CLEANUP = 788
MSG_SMB_NOTIFY_DB = 797

MSG_SMB_NOTIFY_GET_DB = 796

MSG_SMB_NOTIFY_REC_CHANGE = 794
MSG_SMB_NOTIFY_REC_CHANGES = 798

MSG_SMB_NOTIFY_STARTED = 799
MSG_SMB_NOTIFY_TRIGGER = 795

MSG_SMB_NUM_CHILDREN = 792

MSG_SMB_SCAVENGER = 789
MSG_SMB_SLEEP = 800

MSG_SMB_STAT_CACHE_DELETE = 783

MSG_SMB_TELL_NUM_CHILDREN = 791

MSG_TMP_BASE = 61440

MSG_TYPE_MASK = 65535

MSG_WINBIND_DISCONNECT_DC = 1038

MSG_WINBIND_DOMAIN_OFFLINE = 1036
MSG_WINBIND_DOMAIN_ONLINE = 1035

MSG_WINBIND_DUMP_DOMAIN_LIST = 1033

MSG_WINBIND_FINISHED = 1025

MSG_WINBIND_FORGET_STATE = 1026

MSG_WINBIND_IP_DROPPED = 1034

MSG_WINBIND_OFFLINE = 1028
MSG_WINBIND_ONLINE = 1027
MSG_WINBIND_ONLINESTATUS = 1029

MSG_WINBIND_RELOAD_TRUSTED_DOMAINS = 1037

MSG_WINBIND_VALIDATE_CACHE = 1032

MSG_WINS_NEW_ENTRY = 258

# no functions
# classes

class rec(__talloc.BaseObject):
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

    buf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type DATA_BLOB"""

    dest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type server_id"""

    fds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dlong"""

    msg_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type messaging_type"""

    msg_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type messaging_rec"""

    num_fds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    prev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type messaging_rec"""

    src = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type server_id"""



class reclog(__talloc.BaseObject):
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

    num_recs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    recs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type messaging_rec"""

    rec_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type hyper"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.messaging', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/messaging.cpython-310-x86_64-linux-gnu.so')"

