# encoding: utf-8
# module samba.dcerpc.security
# from /usr/lib/python3/dist-packages/samba/dcerpc/security.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" security DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

BUILTIN_RID_ACCOUNT_OPERATORS = 548

BUILTIN_RID_ADMINISTRATORS = 544

BUILTIN_RID_AUTH_ACCESS = 560

BUILTIN_RID_BACKUP_OPERATORS = 551

BUILTIN_RID_CERT_SERV_DCOM_ACCESS = 574

BUILTIN_RID_CRYPTO_OPERATORS = 569

BUILTIN_RID_DISTRIBUTED_COM_USERS = 562

BUILTIN_RID_EVENT_LOG_READERS = 573

BUILTIN_RID_GUESTS = 546

BUILTIN_RID_INCOMING_FOREST_TRUST = 557

BUILTIN_RID_NETWORK_CONF_OPERATORS = 556

BUILTIN_RID_PERFLOG_USERS = 559

BUILTIN_RID_PERFMON_USERS = 558

BUILTIN_RID_POWER_USERS = 547

BUILTIN_RID_PRE_2K_ACCESS = 554

BUILTIN_RID_PRINT_OPERATORS = 550

BUILTIN_RID_RAS_SERVERS = 553

BUILTIN_RID_REMOTE_DESKTOP_USERS = 555

BUILTIN_RID_REPLICATOR = 552

BUILTIN_RID_SERVER_OPERATORS = 549

BUILTIN_RID_TS_LICENSE_SERVERS = 561

BUILTIN_RID_USERS = 545

DOMAIN_RID_ADMINISTRATOR = 500
DOMAIN_RID_ADMINS = 512

DOMAIN_RID_CERT_ADMINS = 517

DOMAIN_RID_DCS = 516

DOMAIN_RID_DOMAIN_MEMBERS = 515

DOMAIN_RID_ENTERPRISE_ADMINS = 519

DOMAIN_RID_ENTERPRISE_READONLY_DCS = 498

DOMAIN_RID_GUEST = 501
DOMAIN_RID_GUESTS = 514
DOMAIN_RID_KRBTGT = 502
DOMAIN_RID_LOGON = 9

DOMAIN_RID_POLICY_ADMINS = 520

DOMAIN_RID_RAS_SERVERS = 553

DOMAIN_RID_READONLY_DCS = 521

DOMAIN_RID_RODC_ALLOW = 571
DOMAIN_RID_RODC_DENY = 572

DOMAIN_RID_SCHEMA_ADMINS = 518

DOMAIN_RID_USERS = 513

GUID_DRS_ADD_DNS_HOST_NAME = '80863791-dbe9-4eb8-837e-7f0ab55d9ac7'

GUID_DRS_ALLOCATE_RIDS = '1abd7cf8-0a99-11d1-adbb-00c04fd8d5cd'

GUID_DRS_ALLOWED_TO_AUTHENTICATE = '68b1d179-0d15-4D4F-ab71-46152e79a7bc'

GUID_DRS_BEHAVIOR_VERSION = 'd31a8757-2447-4545-8081-3bb610cacbf2'

GUID_DRS_CHANGE_DOMAIN_MASTER = '014bf69c-7b3b-11d1-85f6-08002be74fab'

GUID_DRS_CHANGE_INFR_MASTER = 'cc17b1fb-33d9-11d2-97d4-00c04fd8d5cd'

GUID_DRS_CHANGE_PDC = 'bae50096-4752-11d1-9052-00c04fc2d4cf'

GUID_DRS_CHANGE_RID_MASTER = 'd58d5f36-0a98-11d1-adbb-00c04fd8d5cd'

GUID_DRS_CHANGE_SCHEMA_MASTER = 'e12b56b6-0a95-11d1-adbb-00c04fd8d5cd'

GUID_DRS_DNS_HOST_NAME = '72e39547-7b18-11d1-adef-00c04fd8d5cd'

GUID_DRS_DS_INSTALL_REPLICA = '9923a32a-3607-11d2-b9be-0000f87a36b2'

GUID_DRS_ENABLE_PER_USER_REVERSIBLY_ENCRYPTED_PASSWORD = '05c74c5e-4deb-43b4-bd9f-86664c2a7fd5'

GUID_DRS_FORCE_CHANGE_PASSWORD = '00299570-246d-11d0-a768-00aa006e0529'

GUID_DRS_GET_ALL_CHANGES = '1131f6ad-9c07-11d1-f79f-00c04fc2dcd2'

GUID_DRS_GET_CHANGES = '1131f6aa-9c07-11d1-f79f-00c04fc2dcd2'

GUID_DRS_GET_FILTERED_ATTRIBUTES = '89e95b76-444d-4c62-991a-0facbeda640c'

GUID_DRS_MANAGE_TOPOLOGY = '1131f6ac-9c07-11d1-f79f-00c04fc2dcd2'

GUID_DRS_MONITOR_TOPOLOGY = 'f98340fb-7c5b-4cdb-a00b-2ebdfa115a96'

GUID_DRS_REANIMATE_TOMBSTONE = '45ec5156-db7e-47bb-b53f-dbeb2d03c40f'

GUID_DRS_REPL_SYNCRONIZE = '1131f6ab-9c07-11d1-f79f-00c04fc2dcd2'

GUID_DRS_RO_REPL_SECRET_SYNC = '1131f6ae-9c07-11d1-f79f-00c04fc2dcd2'

GUID_DRS_SELF_MEMBERSHIP = 'bf9679c0-0de6-11d0-a285-00aa003049e2'

GUID_DRS_UNEXPIRE_PASSWORD = 'ccc2dc7d-a6ad-4a7a-8846-c04e3cc53501'

GUID_DRS_UPDATE_PASSWORD_NOT_REQUIRED_BIT = '280f369c-67c7-438e-ae98-1d46f3c6f541'

GUID_DRS_USER_CHANGE_PASSWORD = 'ab721a53-1e2f-11d0-9819-00aa0040529b'

GUID_DRS_VALIDATE_SPN = 'f3a64788-5306-11d1-a9c5-0000f80367c1'

KERB_ENCTYPE_AES128_CTS_HMAC_SHA1_96 = 8

KERB_ENCTYPE_AES256_CTS_HMAC_SHA1_96 = 16

KERB_ENCTYPE_AES256_CTS_HMAC_SHA1_96_SK = 32

KERB_ENCTYPE_CLAIMS_SUPPORTED = 262144

KERB_ENCTYPE_COMPOUND_IDENTITY_SUPPORTED = 131072

KERB_ENCTYPE_DES_CBC_CRC = 1
KERB_ENCTYPE_DES_CBC_MD5 = 2

KERB_ENCTYPE_FAST_SUPPORTED = 65536

KERB_ENCTYPE_RC4_HMAC_MD5 = 4

KERB_ENCTYPE_RESOURCE_SID_COMPRESSION_DISABLED = 524288

LSA_POLICY_MODE_ALL = 4087

LSA_POLICY_MODE_ALL_NT4 = 55

LSA_POLICY_MODE_BATCH = 4

LSA_POLICY_MODE_DENY_BATCH = 256
LSA_POLICY_MODE_DENY_INTERACTIVE = 64
LSA_POLICY_MODE_DENY_NETWORK = 128

LSA_POLICY_MODE_DENY_REMOTE_INTERACTIVE = 2048

LSA_POLICY_MODE_DENY_SERVICE = 512

LSA_POLICY_MODE_INTERACTIVE = 1
LSA_POLICY_MODE_NETWORK = 2
LSA_POLICY_MODE_PROXY = 32

LSA_POLICY_MODE_REMOTE_INTERACTIVE = 1024

LSA_POLICY_MODE_SERVICE = 16

NAME_BUILTIN = 'BUILTIN'

NAME_NT_AUTHORITY = 'NT AUTHORITY'
NAME_NT_SERVICE = 'NT SERVICE'

NAME_WORLD = 'WORLD'

NT4_ACL_REVISION = 2

SD_REVISION = 1

SECINFO_ATTRIBUTE = 32
SECINFO_BACKUP = 65536
SECINFO_DACL = 4
SECINFO_GROUP = 2
SECINFO_LABEL = 16
SECINFO_OWNER = 1

SECINFO_PROTECTED_DACL = 2147483648
SECINFO_PROTECTED_SACL = 1073741824

SECINFO_SACL = 8
SECINFO_SCOPE = 64

SECINFO_UNPROTECTED_DACL = 536870912
SECINFO_UNPROTECTED_SACL = 268435456

SECURITY_ACL_REVISION_ADS = 4
SECURITY_ACL_REVISION_NT4 = 2

SECURITY_DESCRIPTOR_REVISION_1 = 1

SEC_ACE_FLAG_CONTAINER_INHERIT = 2

SEC_ACE_FLAG_FAILED_ACCESS = 128

SEC_ACE_FLAG_INHERITED_ACE = 16

SEC_ACE_FLAG_INHERIT_ONLY = 8

SEC_ACE_FLAG_NO_PROPAGATE_INHERIT = 4

SEC_ACE_FLAG_OBJECT_INHERIT = 1

SEC_ACE_FLAG_SUCCESSFUL_ACCESS = 64

SEC_ACE_FLAG_VALID_INHERIT = 15

SEC_ACE_INHERITED_OBJECT_TYPE_PRESENT = 2

SEC_ACE_OBJECT_TYPE_PRESENT = 1

SEC_ACE_TYPE_ACCESS_ALLOWED = 0

SEC_ACE_TYPE_ACCESS_ALLOWED_OBJECT = 5

SEC_ACE_TYPE_ACCESS_DENIED = 1

SEC_ACE_TYPE_ACCESS_DENIED_OBJECT = 6

SEC_ACE_TYPE_ALLOWED_COMPOUND = 4

SEC_ACE_TYPE_SYSTEM_ALARM = 3

SEC_ACE_TYPE_SYSTEM_ALARM_OBJECT = 8

SEC_ACE_TYPE_SYSTEM_AUDIT = 2

SEC_ACE_TYPE_SYSTEM_AUDIT_OBJECT = 7

SEC_ADS_CONTROL_ACCESS = 256

SEC_ADS_CREATE_CHILD = 1

SEC_ADS_DELETE_CHILD = 2
SEC_ADS_DELETE_TREE = 64

SEC_ADS_GENERIC_ALL = 983551

SEC_ADS_GENERIC_ALL_DS = 852291

SEC_ADS_GENERIC_EXECUTE = 131076
SEC_ADS_GENERIC_READ = 131220
SEC_ADS_GENERIC_WRITE = 131112

SEC_ADS_LIST = 4

SEC_ADS_LIST_OBJECT = 128

SEC_ADS_READ_PROP = 16

SEC_ADS_SELF_WRITE = 8

SEC_ADS_WRITE_PROP = 32

SEC_DACL_AUTO_INHERIT = 1

SEC_DEFAULT_DESCRIPTOR = 4

SEC_DESC_DACL_AUTO_INHERITED = 1024

SEC_DESC_DACL_AUTO_INHERIT_REQ = 256

SEC_DESC_DACL_DEFAULTED = 8
SEC_DESC_DACL_PRESENT = 4
SEC_DESC_DACL_PROTECTED = 4096
SEC_DESC_DACL_TRUSTED = 64

SEC_DESC_GROUP_DEFAULTED = 2

SEC_DESC_OWNER_DEFAULTED = 1

SEC_DESC_RM_CONTROL_VALID = 16384

SEC_DESC_SACL_AUTO_INHERITED = 2048

SEC_DESC_SACL_AUTO_INHERIT_REQ = 512

SEC_DESC_SACL_DEFAULTED = 32
SEC_DESC_SACL_PRESENT = 16
SEC_DESC_SACL_PROTECTED = 8192

SEC_DESC_SELF_RELATIVE = 32768

SEC_DESC_SERVER_SECURITY = 128

SEC_DIR_ADD_FILE = 2
SEC_DIR_ADD_SUBDIR = 4

SEC_DIR_DELETE_CHILD = 64

SEC_DIR_LIST = 1

SEC_DIR_READ_ATTRIBUTE = 128
SEC_DIR_READ_EA = 8

SEC_DIR_TRAVERSE = 32

SEC_DIR_WRITE_ATTRIBUTE = 256
SEC_DIR_WRITE_EA = 16

SEC_FILE_ALL = 511

SEC_FILE_APPEND_DATA = 4

SEC_FILE_EXECUTE = 32

SEC_FILE_READ_ATTRIBUTE = 128
SEC_FILE_READ_DATA = 1
SEC_FILE_READ_EA = 8

SEC_FILE_WRITE_ATTRIBUTE = 256
SEC_FILE_WRITE_DATA = 2
SEC_FILE_WRITE_EA = 16

SEC_FLAG_MAXIMUM_ALLOWED = 33554432

SEC_FLAG_SYSTEM_SECURITY = 16777216

SEC_GENERIC_ALL = 268435456
SEC_GENERIC_EXECUTE = 536870912
SEC_GENERIC_READ = 2147483648
SEC_GENERIC_WRITE = 1073741824

SEC_GROUP_FROM_PARENT = 16

SEC_MASK_FLAGS = 251658240
SEC_MASK_GENERIC = 4026531840
SEC_MASK_INVALID = 216071680
SEC_MASK_SPECIFIC = 65535
SEC_MASK_STANDARD = 16711680

SEC_OWNER_FROM_PARENT = 8

SEC_PRIV_ADD_USERS = 4098

SEC_PRIV_ADD_USERS_BIT = 64

SEC_PRIV_BACKUP = 17

SEC_PRIV_BACKUP_BIT = 512

SEC_PRIV_CHANGE_NOTIFY = 23

SEC_PRIV_CHANGE_NOTIFY_BIT = 8388608

SEC_PRIV_CREATE_GLOBAL = 30

SEC_PRIV_CREATE_GLOBAL_BIT = 268435456

SEC_PRIV_CREATE_PAGEFILE = 15

SEC_PRIV_CREATE_PAGEFILE_BIT = 524288

SEC_PRIV_DEBUG = 20

SEC_PRIV_DEBUG_BIT = 2097152

SEC_PRIV_DISK_OPERATOR = 4099

SEC_PRIV_DISK_OPERATOR_BIT = 128

SEC_PRIV_ENABLE_DELEGATION = 27

SEC_PRIV_ENABLE_DELEGATION_BIT = 33554432

SEC_PRIV_IMPERSONATE = 29

SEC_PRIV_IMPERSONATE_BIT = 134217728

SEC_PRIV_INCREASE_BASE_PRIORITY = 14

SEC_PRIV_INCREASE_BASE_PRIORITY_BIT = 262144

SEC_PRIV_INCREASE_QUOTA = 5

SEC_PRIV_INCREASE_QUOTA_BIT = 4096

SEC_PRIV_INVALID = 0

SEC_PRIV_LOAD_DRIVER = 10

SEC_PRIV_LOAD_DRIVER_BIT = 16384

SEC_PRIV_MACHINE_ACCOUNT = 6

SEC_PRIV_MACHINE_ACCOUNT_BIT = 16

SEC_PRIV_MANAGE_VOLUME = 28

SEC_PRIV_MANAGE_VOLUME_BIT = 67108864

SEC_PRIV_PRINT_OPERATOR = 4097

SEC_PRIV_PRINT_OPERATOR_BIT = 32

SEC_PRIV_PROFILE_SINGLE_PROCESS = 13

SEC_PRIV_PROFILE_SINGLE_PROCESS_BIT = 131072

SEC_PRIV_REMOTE_SHUTDOWN = 24

SEC_PRIV_REMOTE_SHUTDOWN_BIT = 256

SEC_PRIV_RESTORE = 18

SEC_PRIV_RESTORE_BIT = 1024

SEC_PRIV_SECURITY = 8

SEC_PRIV_SECURITY_BIT = 8192

SEC_PRIV_SHUTDOWN = 19

SEC_PRIV_SHUTDOWN_BIT = 1048576

SEC_PRIV_SYSTEMTIME = 12

SEC_PRIV_SYSTEMTIME_BIT = 65536

SEC_PRIV_SYSTEM_ENVIRONMENT = 22

SEC_PRIV_SYSTEM_ENVIRONMENT_BIT = 4194304

SEC_PRIV_SYSTEM_PROFILE = 11

SEC_PRIV_SYSTEM_PROFILE_BIT = 32768

SEC_PRIV_TAKE_OWNERSHIP = 9

SEC_PRIV_TAKE_OWNERSHIP_BIT = 2048

SEC_PRIV_UNDOCK = 25

SEC_PRIV_UNDOCK_BIT = 16777216

SEC_REG_CREATE_LINK = 32
SEC_REG_CREATE_SUBKEY = 4

SEC_REG_ENUM_SUBKEYS = 8

SEC_REG_NOTIFY = 16

SEC_REG_QUERY_VALUE = 1

SEC_REG_SET_VALUE = 2

SEC_RIGHTS_DIR_ALL = 2032127
SEC_RIGHTS_DIR_EXECUTE = 1179808
SEC_RIGHTS_DIR_READ = 1179785
SEC_RIGHTS_DIR_WRITE = 1179926

SEC_RIGHTS_FILE_ALL = 2032127
SEC_RIGHTS_FILE_EXECUTE = 1179808
SEC_RIGHTS_FILE_READ = 1179785
SEC_RIGHTS_FILE_WRITE = 1179926

SEC_RIGHTS_PRIV_BACKUP = 17957033
SEC_RIGHTS_PRIV_RESTORE = 18809110

SEC_SACL_AUTO_INHERIT = 2

SEC_STD_ALL = 2031616
SEC_STD_DELETE = 65536

SEC_STD_READ_CONTROL = 131072

SEC_STD_REQUIRED = 983040
SEC_STD_SYNCHRONIZE = 1048576

SEC_STD_WRITE_DAC = 262144
SEC_STD_WRITE_OWNER = 524288

SE_GROUP_ENABLED = 4

SE_GROUP_ENABLED_BY_DEFAULT = 2

SE_GROUP_INTEGRITY = 32

SE_GROUP_INTEGRITY_ENABLED = 64

SE_GROUP_LOGON_ID = 3221225472

SE_GROUP_MANDATORY = 1
SE_GROUP_OWNER = 8
SE_GROUP_RESOURCE = 536870912

SE_GROUP_USE_FOR_DENY_ONLY = 16

SID_AUTHENTICATION_AUTHORITY_ASSERTED_IDENTITY = 'S-1-18-1'

SID_BUILTIN = 'S-1-5-32'

SID_BUILTIN_ACCOUNT_OPERATORS = 'S-1-5-32-548'

SID_BUILTIN_ADMINISTRATORS = 'S-1-5-32-544'

SID_BUILTIN_AUTH_ACCESS = 'S-1-5-32-560'

SID_BUILTIN_BACKUP_OPERATORS = 'S-1-5-32-551'

SID_BUILTIN_CERT_SERV_DCOM_ACCESS = 'S-1-5-32-574'

SID_BUILTIN_CRYPTO_OPERATORS = 'S-1-5-32-569'

SID_BUILTIN_DISTRIBUTED_COM_USERS = 'S-1-5-32-562'

SID_BUILTIN_EVENT_LOG_READERS = 'S-1-5-32-573'

SID_BUILTIN_GUESTS = 'S-1-5-32-546'

SID_BUILTIN_INCOMING_FOREST_TRUST = 'S-1-5-32-557'

SID_BUILTIN_NETWORK_CONF_OPERATORS = 'S-1-5-32-556'

SID_BUILTIN_PERFLOG_USERS = 'S-1-5-32-559'

SID_BUILTIN_PERFMON_USERS = 'S-1-5-32-558'

SID_BUILTIN_POWER_USERS = 'S-1-5-32-547'

SID_BUILTIN_PREW2K = 'S-1-5-32-554'

SID_BUILTIN_PRINT_OPERATORS = 'S-1-5-32-550'

SID_BUILTIN_RAS_SERVERS = 'S-1-5-32-553'

SID_BUILTIN_REMOTE_DESKTOP_USERS = 'S-1-5-32-555'

SID_BUILTIN_REPLICATOR = 'S-1-5-32-552'

SID_BUILTIN_SERVER_OPERATORS = 'S-1-5-32-549'

SID_BUILTIN_TS_LICENSE_SERVERS = 'S-1-5-32-561'

SID_BUILTIN_USERS = 'S-1-5-32-545'

SID_CLAIMS_VALID = 'S-1-5-21-0-0-0-497'

SID_COMPOUNDED_AUTHENTICATION = 'S-1-5-21-0-0-0-496'

SID_CREATOR_GROUP = 'S-1-3-1'
SID_CREATOR_OWNER = 'S-1-3-0'

SID_CREATOR_OWNER_DOMAIN = 'S-1-3'

SID_NT_ANONYMOUS = 'S-1-5-7'

SID_NT_AUTHENTICATED_USERS = 'S-1-5-11'

SID_NT_AUTHORITY = 'S-1-5'
SID_NT_BATCH = 'S-1-5-3'
SID_NT_DIALUP = 'S-1-5-1'

SID_NT_DIGEST_AUTHENTICATION = 'S-1-5-64-21'

SID_NT_ENTERPRISE_DCS = 'S-1-5-9'

SID_NT_INTERACTIVE = 'S-1-5-4'
SID_NT_IUSR = 'S-1-5-17'

SID_NT_LOCAL_SERVICE = 'S-1-5-19'

SID_NT_NETWORK = 'S-1-5-2'

SID_NT_NETWORK_SERVICE = 'S-1-5-20'

SID_NT_NFS_GROUP = 'S-1-5-88-2'
SID_NT_NFS_MASK = 'S-1-5-88-3'
SID_NT_NFS_OTHERS = 'S-1-5-88-4'
SID_NT_NFS_SUBSYSTEM = 'S-1-5-88'
SID_NT_NFS_USER = 'S-1-5-88-1'

SID_NT_NTLM_AUTHENTICATION = 'S-1-5-64-10'

SID_NT_NT_SERVICE = 'S-1-5-80'

SID_NT_OTHER_ORGANISATION = 'S-1-5-1000'

SID_NT_PROXY = 'S-1-5-8'

SID_NT_REMOTE_INTERACTIVE = 'S-1-5-14'

SID_NT_RESTRICTED = 'S-1-5-12'

SID_NT_SCHANNEL_AUTHENTICATION = 'S-1-5-64-14'

SID_NT_SELF = 'S-1-5-10'
SID_NT_SERVICE = 'S-1-5-6'
SID_NT_SYSTEM = 'S-1-5-18'

SID_NT_TERMINAL_SERVER_USERS = 'S-1-5-13'

SID_NT_THIS_ORGANISATION = 'S-1-5-15'

SID_NT_TRUSTED_INSTALLER = 'S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464'

SID_NULL = 'S-1-0-0'

SID_OWNER_RIGHTS = 'S-1-3-4'

SID_SAMBA_SMB3 = 'S-1-22-1397571891'

SID_SAMBA_UNIX_GROUP_OWNER = 'S-1-22-2'

SID_SAMBA_UNIX_USER_OWNER = 'S-1-22-1'

SID_SERVICE_ASSERTED_IDENTITY = 'S-1-18-2'

SID_WORLD = 'S-1-1-0'

SID_WORLD_DOMAIN = 'S-1-1'

SMB_SUPPORTED_SECINFO_FLAGS = 65663

STANDARD_RIGHTS_ALL_ACCESS = 2031616

STANDARD_RIGHTS_EXECUTE_ACCESS = 131072

STANDARD_RIGHTS_MODIFY_ACCESS = 131072

STANDARD_RIGHTS_READ_ACCESS = 131072

STANDARD_RIGHTS_REQUIRED_ACCESS = 983040

STANDARD_RIGHTS_WRITE_ACCESS = 851968

# functions

def privilege_id(*args, **kwargs): # real signature unknown
    pass

def privilege_name(*args, **kwargs): # real signature unknown
    pass

def random_sid(*args, **kwargs): # real signature unknown
    pass

# classes

class security_abstract_syntax(__misc.ndr_syntax_id):
    """ security_abstract_syntax() """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


abstract_syntax = security_abstract_syntax


class ace(__talloc.BaseObject):
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

    access_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type security_ace_flags"""

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type security_ace_object_ctr"""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""

    trustee = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dom_sid"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type security_ace_type"""



class ace_object(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type security_ace_object_flags"""

    inherited_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type security_ace_object_inherited_type"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type security_ace_object_type"""



class ace_object_ctr(__talloc.BaseObject):
    # no doc
    @classmethod
    def __export__(cls, mem_ctx, level, in_): # real signature unknown; restored from __doc__
        """ T.__export__(mem_ctx, level, in) => ret. """
        pass

    @classmethod
    def __import__(cls, mem_ctx, level, in_): # real signature unknown; restored from __doc__
        """ T.__import__(mem_ctx, level, in) => ret. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ace_object_inherited_type(__talloc.BaseObject):
    # no doc
    @classmethod
    def __export__(cls, mem_ctx, level, in_): # real signature unknown; restored from __doc__
        """ T.__export__(mem_ctx, level, in) => ret. """
        pass

    @classmethod
    def __import__(cls, mem_ctx, level, in_): # real signature unknown; restored from __doc__
        """ T.__import__(mem_ctx, level, in) => ret. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ace_object_type(__talloc.BaseObject):
    # no doc
    @classmethod
    def __export__(cls, mem_ctx, level, in_): # real signature unknown; restored from __doc__
        """ T.__export__(mem_ctx, level, in) => ret. """
        pass

    @classmethod
    def __import__(cls, mem_ctx, level, in_): # real signature unknown; restored from __doc__
        """ T.__import__(mem_ctx, level, in) => ret. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class acl(__talloc.BaseObject):
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

    aces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type security_ace"""

    num_aces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    revision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type security_acl_revision"""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint16"""



class descriptor(__talloc.BaseObject):
    # no doc
    def as_sddl(self, *args, **kwargs): # real signature unknown
        pass

    def dacl_add(self, *args, **kwargs): # real signature unknown
        pass

    def dacl_del(self, *args, **kwargs): # real signature unknown
        pass

    def dacl_del_ace(self, *args, **kwargs): # real signature unknown
        pass

    def from_sddl(self, *args, **kwargs): # real signature unknown
        pass

    def sacl_add(self, ace): # real signature unknown; restored from __doc__
        """
        S.sacl_add(ace) -> None
        Add a security ace to this security descriptor
        """
        pass

    def sacl_del(self, *args, **kwargs): # real signature unknown
        pass

    def sacl_del_ace(self, *args, **kwargs): # real signature unknown
        pass

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

    dacl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type security_acl"""

    group_sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dom_sid"""

    owner_sid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dom_sid"""

    revision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type security_descriptor_revision"""

    sacl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type security_acl"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type security_descriptor_type"""



class dom_sid(__talloc.BaseObject):
    # no doc
    def split(self): # real signature unknown; restored from __doc__
        """
        S.split() -> (domain_sid, rid)
        Split a domain sid
        """
        pass

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

    id_auth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    num_auths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type int8"""

    sid_rev_num = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    sub_auths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""



class generic_mapping(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    generic_all = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    generic_execute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    generic_read = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    generic_write = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""



class LSAP_TOKEN_INFO_INTEGRITY(__talloc.BaseObject):
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

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    MachineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint8"""

    TokenIL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""



class security(__dcerpc.ClientConnection):
    """
    security(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    """
    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class sec_desc_buf(__talloc.BaseObject):
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

    sd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type security_descriptor"""

    sd_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""



class standard_mapping(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    std_all = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    std_execute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    std_read = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    std_write = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""



class token(__talloc.BaseObject):
    # no doc
    def has_builtin_administrators(self, *args, **kwargs): # real signature unknown
        pass

    def has_nt_authenticated_users(self, *args, **kwargs): # real signature unknown
        pass

    def has_privilege(self, *args, **kwargs): # real signature unknown
        pass

    def has_sid(self, *args, **kwargs): # real signature unknown
        pass

    def is_anonymous(self): # real signature unknown; restored from __doc__
        """
        S.is_anonymous() -> bool
        Check whether this is an anonymous token.
        """
        return False

    def is_sid(self, sid): # real signature unknown; restored from __doc__
        """
        S.is_sid(sid) -> bool
        Check whether this token is of the specified SID.
        """
        return False

    def is_system(self, *args, **kwargs): # real signature unknown
        pass

    def set_privilege(self, *args, **kwargs): # real signature unknown
        pass

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

    num_sids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    privilege_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type se_privilege"""

    rights_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_SystemAccessModeFlags"""

    sids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type dom_sid"""



class unix_token(__talloc.BaseObject):
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

    gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type gid_t"""

    groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type gid_t"""

    ngroups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uint32"""

    uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type uid_t"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.security', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/security.cpython-310-x86_64-linux-gnu.so')"

