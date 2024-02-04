# encoding: utf-8
# module samba.dcerpc.netlogon
# from /usr/lib/python3/dist-packages/samba/dcerpc/netlogon.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" netlogon DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

DSGETDC_VALID_FLAGS = 3223322609

DS_ADDRESS_TYPE_INET = 1
DS_ADDRESS_TYPE_NETBIOS = 2

DS_AVOID_SELF = 16384

DS_BACKGROUND_ONLY = 256

DS_DIRECTORY_SERVICE_6_REQUIRED = 524288

DS_DIRECTORY_SERVICE_PREFERRED = 32
DS_DIRECTORY_SERVICE_REQUIRED = 16

DS_DNS_CONTROLLER = 536870912
DS_DNS_DOMAIN = 1073741824

DS_DNS_FOREST_ROOT = 2147483648

DS_FORCE_REDISCOVERY = 1

DS_GC_SERVER_REQUIRED = 64

DS_GFTI_UPDATE_TDO = 1

DS_GOOD_TIMESERV_PREFERRED = 8192

DS_IP_REQUIRED = 512

DS_IS_DNS_NAME = 131072

DS_IS_FLAT_NAME = 65536

DS_KDC_REQUIRED = 1024

DS_ONLY_LDAP_NEEDED = 32768

DS_PDC_REQUIRED = 128

DS_RETURN_DNS_NAME = 1073741824

DS_RETURN_FLAT_NAME = 2147483648

DS_SERVER_CLOSEST = 128
DS_SERVER_DS = 16

DS_SERVER_DS_8 = 16384

DS_SERVER_FULL_SECRET_DOMAIN_6 = 4096

DS_SERVER_GC = 4

DS_SERVER_GOOD_TIMESERV = 512

DS_SERVER_KDC = 32
DS_SERVER_LDAP = 8
DS_SERVER_NDNC = 1024
DS_SERVER_PDC = 1

DS_SERVER_SELECT_SECRET_DOMAIN_6 = 2048

DS_SERVER_TIMESERV = 64
DS_SERVER_WEBSERV = 8192
DS_SERVER_WRITABLE = 256

DS_TIMESERV_REQUIRED = 2048

DS_TRY_NEXTCLOSEST_SITE = 262144

DS_WEB_SERVICE_REQUIRED = 1048576

DS_WRITABLE_REQUIRED = 4096

MSV1_0_ALLOW_FORCE_GUEST = 8192

MSV1_0_ALLOW_MSVCHAPV2 = 65536

MSV1_0_ALLOW_SERVER_TRUST_ACCOUNT = 32

MSV1_0_ALLOW_WORKSTATION_TRUST_ACCOUNT = 2048

MSV1_0_CHECK_LOGONHOURS_FOR_S4U = 262144

MSV1_0_CLEARTEXT_PASSWORD_ALLOWED = 2
MSV1_0_CLEARTEXT_PASSWORD_SUPPLIED = 16384

MSV1_0_DISABLE_PERSONAL_FALLBACK = 4096

MSV1_0_DONT_TRY_GUEST_ACCOUNT = 16

MSV1_0_RETURN_PASSWORD_EXPIRY = 64

MSV1_0_RETURN_PROFILE_PATH = 512

MSV1_0_RETURN_USER_PARAMETERS = 8

MSV1_0_S4U2SELF = 131072

MSV1_0_SUBAUTHENTICATION_DLL_EX = 1048576

MSV1_0_TRY_GUEST_ACCOUNT_ONLY = 256

MSV1_0_TRY_SPECIFIED_DOMAIN_ONLY = 1024

MSV1_0_UPDATE_LOGON_STATISTICS = 4

MSV1_0_USE_CLIENT_CHALLENGE = 128

MSV1_0_USE_DOMAIN_FOR_ROUTING_ONLY = 32768

NetlogonGenericInformation = 4
NetlogonInteractiveInformation = 1
NetlogonInteractiveTransitiveInformation = 5
NetlogonNetworkInformation = 2
NetlogonNetworkTransitiveInformation = 6
NetlogonServiceInformation = 3
NetlogonServiceTransitiveInformation = 7
NetlogonValidationGenericInfo2 = 5
NetlogonValidationSamInfo = 2
NetlogonValidationSamInfo2 = 3
NetlogonValidationSamInfo4 = 6
NetlogonValidationUasInfo = 1

NETLOGON_CACHED_ACCOUNT = 4

NETLOGON_CONTROL_BACKUP_CHANGE_LOG = 65532

NETLOGON_CONTROL_BREAKPOINT = 65535

NETLOGON_CONTROL_CHANGE_PASSWORD = 9

NETLOGON_CONTROL_FIND_USER = 8

NETLOGON_CONTROL_FORCE_DNS_REG = 11

NETLOGON_CONTROL_PDC_REPLICATE = 4

NETLOGON_CONTROL_QUERY = 1

NETLOGON_CONTROL_QUERY_DNS_REG = 12

NETLOGON_CONTROL_REDISCOVER = 5
NETLOGON_CONTROL_REPLICATE = 2

NETLOGON_CONTROL_SET_DBFLAG = 65534

NETLOGON_CONTROL_SYNCHRONIZE = 3

NETLOGON_CONTROL_TC_QUERY = 6
NETLOGON_CONTROL_TC_VERIFY = 10

NETLOGON_CONTROL_TRANSPORT_NOTIFY = 7

NETLOGON_CONTROL_TRUNCATE_LOG = 65533

NETLOGON_DNS_UPDATE_FAILURE = 64

NETLOGON_EXTRA_SIDS = 32

NETLOGON_FULL_SYNC_REPLICATION = 4

NETLOGON_GRACE_LOGON = 16777216

NETLOGON_GUEST = 1

NETLOGON_HAS_IP = 16
NETLOGON_HAS_TIMESERV = 32

NETLOGON_NEG_128BIT = 16384

NETLOGON_NEG_ACCOUNT_LOCKOUT = 1

NETLOGON_NEG_ARCFOUR = 4

NETLOGON_NEG_AUTHENTICATED_RPC = 1073741824

NETLOGON_NEG_AUTHENTICATED_RPC_LSASS = 536870912

NETLOGON_NEG_AVOID_ACCOUNT_DB_REPL = 4096

NETLOGON_NEG_AVOID_SECURITYAUTH_DB_REPL = 8192

NETLOGON_NEG_CHANGELOG_BDC = 16

NETLOGON_NEG_CONCURRENT_RPC = 2048

NETLOGON_NEG_CROSS_FOREST_TRUSTS = 524288

NETLOGON_NEG_DNS_DOMAIN_TRUSTS = 65536

NETLOGON_NEG_FULL_SYNC_REPL = 32

NETLOGON_NEG_GENERIC_PASSTHROUGH = 1024

NETLOGON_NEG_GETDOMAININFO = 262144

NETLOGON_NEG_MULTIPLE_SIDS = 64

NETLOGON_NEG_NEUTRALIZE_NT4_EMULATION = 1048576

NETLOGON_NEG_PASSWORD_CHANGE_REFUSAL = 256

NETLOGON_NEG_PASSWORD_SET2 = 131072

NETLOGON_NEG_PERSISTENT_SAMREPL = 2

NETLOGON_NEG_PROMOTION_COUNT = 8

NETLOGON_NEG_REDO = 128

NETLOGON_NEG_RODC_PASSTHROUGH = 2097152

NETLOGON_NEG_SCHANNEL = 1073741824

NETLOGON_NEG_SEND_PASSWORD_INFO_PDC = 512

NETLOGON_NEG_STRONG_KEYS = 16384

NETLOGON_NEG_SUPPORTS_AES = 16777216

NETLOGON_NEG_SUPPORTS_AES_SHA2 = 4194304

NETLOGON_NEG_TRANSITIVE_TRUSTS = 32768

NETLOGON_NOENCRYPTION = 2

NETLOGON_NTLMV2_ENABLED = 256

NETLOGON_PASSWORD_VERSION_NUMBER_PRESENT = 35854696

NETLOGON_PROFILE_PATH_RETURNED = 1024

NETLOGON_REDO_NEEDED = 8

NETLOGON_REPLICATION_IN_PROGRESS = 2

NETLOGON_REPLICATION_NEEDED = 1

NETLOGON_RESOURCE_GROUPS = 512

NETLOGON_SAMLOGON_FLAG_PASS_CROSS_FOREST_HOP = 2

NETLOGON_SAMLOGON_FLAG_PASS_TO_FOREST_ROOT = 1

NETLOGON_SAMLOGON_FLAG_RODC_NTLM_REQUEST = 8

NETLOGON_SAMLOGON_FLAG_RODC_TO_OTHER_DOMAIN = 4

NETLOGON_SERVER_TRUST_ACCOUNT = 128

NETLOGON_SUBAUTH_SESSION_KEY = 64

NETLOGON_USED_LM_PASSWORD = 8

NETLOGON_VERIFY_STATUS_RETURNED = 128

NETR_CHANGELOG_CHANGED_PASSWORD = 2

NETR_CHANGELOG_FIRST_PROMOTION_OBJ = 16

NETR_CHANGELOG_IMMEDIATE_REPL_REQUIRED = 1

NETR_CHANGELOG_NAME_INCLUDED = 8

NETR_CHANGELOG_SID_INCLUDED = 4

NETR_DELTA_ACCOUNT = 16
NETR_DELTA_ALIAS = 9

NETR_DELTA_ALIAS_MEMBER = 12

NETR_DELTA_DELETE_ACCOUNT = 17
NETR_DELTA_DELETE_ALIAS = 10
NETR_DELTA_DELETE_GROUP = 3
NETR_DELTA_DELETE_GROUP2 = 20
NETR_DELTA_DELETE_SECRET = 19
NETR_DELTA_DELETE_TRUST = 15
NETR_DELTA_DELETE_USER = 6
NETR_DELTA_DELETE_USER2 = 21

NETR_DELTA_DOMAIN = 1
NETR_DELTA_GROUP = 2

NETR_DELTA_GROUP_MEMBER = 8

NETR_DELTA_MODIFY_COUNT = 22

NETR_DELTA_POLICY = 13

NETR_DELTA_RENAME_ALIAS = 11
NETR_DELTA_RENAME_GROUP = 4
NETR_DELTA_RENAME_USER = 7

NETR_DELTA_SECRET = 18

NETR_DELTA_TRUSTED_DOMAIN = 14

NETR_DELTA_USER = 5

NETR_TRUST_FLAG_AES = 256
NETR_TRUST_FLAG_INBOUND = 32

NETR_TRUST_FLAG_IN_FOREST = 1

NETR_TRUST_FLAG_MIT_KRB5 = 128

NETR_TRUST_FLAG_NATIVE = 16
NETR_TRUST_FLAG_OUTBOUND = 2
NETR_TRUST_FLAG_PRIMARY = 8
NETR_TRUST_FLAG_TREEROOT = 4

NETR_VER_NT_DOMAIN_CONTROLLER = 2

NETR_VER_NT_SERVER = 3
NETR_VER_NT_WORKSTATION = 1

NETR_VER_SUITE_BACKOFFICE = 4
NETR_VER_SUITE_BLADE = 1024

NETR_VER_SUITE_COMPUTE_SERVER = 16384

NETR_VER_SUITE_DATACENTER = 128
NETR_VER_SUITE_EMBEDDEDNT = 64
NETR_VER_SUITE_ENTERPRISE = 2
NETR_VER_SUITE_PERSONAL = 512
NETR_VER_SUITE_SINGLEUSERTS = 256
NETR_VER_SUITE_SMALLBUSINESS = 1

NETR_VER_SUITE_SMALLBUSINESS_RESTRICTED = 32

NETR_VER_SUITE_STORAGE_SERVER = 8192

NETR_VER_SUITE_TERMINAL = 16

NETR_VER_SUITE_WH_SERVER = 32768

NETR_WS_FLAG_HANDLES_INBOUND_TRUSTS = 1

NETR_WS_FLAG_HANDLES_SPN_UPDATE = 2

NlDnsDcAtSite = 32
NlDnsDomainName = 1
NlDnsDomainNameAlias = 2
NlDnsDsaCname = 28
NlDnsForestName = 3
NlDnsForestNameAlias = 4
NlDnsGcAtSite = 25
NlDnsGenericGcAtSite = 36
NlDnsInfoTypeNone = 0
NlDnsKdcAtSite = 30
NlDnsLdapAtSite = 22
NlDnsNdncDomainName = 5
NlDnsRecordName = 6
NlDnsRfc1510KdcAtSite = 34

SendToSamResetBadPasswordCount = 1
SendToSamResetSmartCardPassword = 4
SendToSamUpdateLastLogonTimestamp = 3
SendToSamUpdatePassword = 0
SendToSamUpdatePasswordForward = 2

SYNCSTATE_ALIAS_MEMBER_STATE = 7

SYNCSTATE_ALIAS_STATE = 6

SYNCSTATE_DOMAIN_STATE = 1

SYNCSTATE_GROUP_MEMBER_STATE = 5

SYNCSTATE_GROUP_STATE = 2

SYNCSTATE_NORMAL_STATE = 0

SYNCSTATE_SAM_DONE_STATE = 8

SYNCSTATE_UAS_BUILT_IN_GROUP_STATE = 3

SYNCSTATE_USER_STATE = 4

# no functions
# classes

from .netlogon_abstract_syntax import netlogon_abstract_syntax
from .abstract_syntax import abstract_syntax
from .DcSitesCtr import DcSitesCtr
from .netlogon import netlogon
from .netr_AccountBuffer import netr_AccountBuffer
from .netr_AccountDeltas import netr_AccountDeltas
from .netr_AccountSync import netr_AccountSync
from .netr_AcctLockStr import netr_AcctLockStr
from .netr_Authenticator import netr_Authenticator
from .netr_Blob import netr_Blob
from .netr_Capabilities import netr_Capabilities
from .netr_ChallengeResponse import netr_ChallengeResponse
from .netr_ChangeLogEntry import netr_ChangeLogEntry
from .netr_ChangeLogObject import netr_ChangeLogObject
from .netr_CIPHER_VALUE import netr_CIPHER_VALUE
from .netr_CONTROL_DATA_INFORMATION import netr_CONTROL_DATA_INFORMATION
from .netr_CONTROL_QUERY_INFORMATION import netr_CONTROL_QUERY_INFORMATION
from .netr_Credential import netr_Credential
from .netr_CryptPassword import netr_CryptPassword
from .netr_DatabaseDeltas import netr_DatabaseDeltas
from .netr_DatabaseRedo import netr_DatabaseRedo
from .netr_DatabaseSync import netr_DatabaseSync
from .netr_DatabaseSync2 import netr_DatabaseSync2
from .netr_DELTA_ACCOUNT import netr_DELTA_ACCOUNT
from .netr_DELTA_ALIAS import netr_DELTA_ALIAS
from .netr_DELTA_ALIAS_MEMBER import netr_DELTA_ALIAS_MEMBER
from .netr_DELTA_DELETE_USER import netr_DELTA_DELETE_USER
from .netr_DELTA_DOMAIN import netr_DELTA_DOMAIN
from .netr_DELTA_ENUM import netr_DELTA_ENUM
from .netr_DELTA_ENUM_ARRAY import netr_DELTA_ENUM_ARRAY
from .netr_DELTA_GROUP import netr_DELTA_GROUP
from .netr_DELTA_GROUP_MEMBER import netr_DELTA_GROUP_MEMBER
from .netr_DELTA_ID_UNION import netr_DELTA_ID_UNION
from .netr_DELTA_POLICY import netr_DELTA_POLICY
from .netr_DELTA_RENAME import netr_DELTA_RENAME
from .netr_DELTA_SECRET import netr_DELTA_SECRET
from .netr_DELTA_TRUSTED_DOMAIN import netr_DELTA_TRUSTED_DOMAIN
from .netr_DELTA_UNION import netr_DELTA_UNION
from .netr_DELTA_USER import netr_DELTA_USER
from .netr_DomainInfo import netr_DomainInfo
from .netr_DomainInformation import netr_DomainInformation
from .netr_DomainTrust import netr_DomainTrust
from .netr_DomainTrustList import netr_DomainTrustList
from .netr_DsRAddress import netr_DsRAddress
from .netr_DsRAddressToSitenamesExW import netr_DsRAddressToSitenamesExW
from .netr_DsRAddressToSitenamesExWCtr import netr_DsRAddressToSitenamesExWCtr
from .netr_DsRAddressToSitenamesW import netr_DsRAddressToSitenamesW
from .netr_DsRAddressToSitenamesWCtr import netr_DsRAddressToSitenamesWCtr
from .netr_DsrDeregisterDNSHostRecords import netr_DsrDeregisterDNSHostRecords
from .netr_DsrEnumerateDomainTrusts import netr_DsrEnumerateDomainTrusts
from .netr_DsRGetDCName import netr_DsRGetDCName
from .netr_DsRGetDCNameEx import netr_DsRGetDCNameEx
from .netr_DsRGetDCNameEx2 import netr_DsRGetDCNameEx2
from .netr_DsRGetDCNameInfo import netr_DsRGetDCNameInfo
from .netr_DsrGetDcSiteCoverageW import netr_DsrGetDcSiteCoverageW
from .netr_DsRGetForestTrustInformation import netr_DsRGetForestTrustInformation
from .netr_DsRGetSiteName import netr_DsRGetSiteName
from .netr_DsrUpdateReadOnlyServerDnsRecords import netr_DsrUpdateReadOnlyServerDnsRecords
from .netr_GenericInfo import netr_GenericInfo
from .netr_GenericInfo2 import netr_GenericInfo2
from .netr_GetAnyDCName import netr_GetAnyDCName
from .netr_GetDcName import netr_GetDcName
from .netr_GetForestTrustInformation import netr_GetForestTrustInformation
from .netr_IdentityInfo import netr_IdentityInfo
from .netr_LMSessionKey import netr_LMSessionKey
from .netr_LogonControl import netr_LogonControl
from .netr_LogonControl2 import netr_LogonControl2
from .netr_LogonControl2Ex import netr_LogonControl2Ex
from .netr_LogonGetCapabilities import netr_LogonGetCapabilities
from .netr_LogonGetDomainInfo import netr_LogonGetDomainInfo
from .netr_LogonGetTrustRid import netr_LogonGetTrustRid
from .netr_LogonLevel import netr_LogonLevel
from .netr_LogonSamLogoff import netr_LogonSamLogoff
from .netr_LogonSamLogon import netr_LogonSamLogon
from .netr_LogonSamLogonEx import netr_LogonSamLogonEx
from .netr_LogonSamLogonWithFlags import netr_LogonSamLogonWithFlags
from .netr_LogonUasLogoff import netr_LogonUasLogoff
from .netr_LogonUasLogon import netr_LogonUasLogon
from .netr_LsaPolicyInformation import netr_LsaPolicyInformation
from .netr_NETLOGON_INFO_1 import netr_NETLOGON_INFO_1
from .netr_NETLOGON_INFO_2 import netr_NETLOGON_INFO_2
from .netr_NETLOGON_INFO_3 import netr_NETLOGON_INFO_3
from .netr_NETLOGON_INFO_4 import netr_NETLOGON_INFO_4
from .netr_NetrEnumerateTrustedDomains import netr_NetrEnumerateTrustedDomains
from .netr_NetrEnumerateTrustedDomainsEx import netr_NetrEnumerateTrustedDomainsEx
from .netr_NetrLogonSendToSam import netr_NetrLogonSendToSam
from .netr_NetworkInfo import netr_NetworkInfo
from .netr_OneDomainInfo import netr_OneDomainInfo
from .netr_OsVersion import netr_OsVersion
from .netr_OsVersionContainer import netr_OsVersionContainer
from .netr_OsVersionInfoEx import netr_OsVersionInfoEx
from .netr_PacInfo import netr_PacInfo
from .netr_PasswordHistory import netr_PasswordHistory
from .netr_PasswordInfo import netr_PasswordInfo
from .netr_QUOTA_LIMITS import netr_QUOTA_LIMITS
from .netr_SamBaseInfo import netr_SamBaseInfo
from .netr_SamInfo2 import netr_SamInfo2
from .netr_SamInfo3 import netr_SamInfo3
from .netr_SamInfo6 import netr_SamInfo6
from .netr_SendToSamBase import netr_SendToSamBase
from .netr_SendToSamMessage import netr_SendToSamMessage
from .netr_SendToSamResetBadPasswordCount import netr_SendToSamResetBadPasswordCount
from .netr_ServerAuthenticate import netr_ServerAuthenticate
from .netr_ServerAuthenticate2 import netr_ServerAuthenticate2
from .netr_ServerAuthenticate3 import netr_ServerAuthenticate3
from .netr_ServerGetTrustInfo import netr_ServerGetTrustInfo
from .netr_ServerPasswordGet import netr_ServerPasswordGet
from .netr_ServerPasswordSet import netr_ServerPasswordSet
from .netr_ServerPasswordSet2 import netr_ServerPasswordSet2
from .netr_ServerReqChallenge import netr_ServerReqChallenge
from .netr_ServerTrustPasswordsGet import netr_ServerTrustPasswordsGet
from .netr_SidAttr import netr_SidAttr
from .netr_TrustInfo import netr_TrustInfo
from .netr_trust_extension import netr_trust_extension
from .netr_trust_extension_container import netr_trust_extension_container
from .netr_trust_extension_info import netr_trust_extension_info
from .netr_UasInfo import netr_UasInfo
from .netr_UasLogoffInfo import netr_UasLogoffInfo
from .netr_UAS_INFO_0 import netr_UAS_INFO_0
from .netr_Unused47 import netr_Unused47
from .netr_UserSessionKey import netr_UserSessionKey
from .netr_USER_KEY16 import netr_USER_KEY16
from .netr_USER_KEYS import netr_USER_KEYS
from .netr_USER_KEYS2 import netr_USER_KEYS2
from .netr_USER_KEY_UNION import netr_USER_KEY_UNION
from .netr_USER_PRIVATE_INFO import netr_USER_PRIVATE_INFO
from .netr_Validation import netr_Validation
from .netr_WorkstationInfo import netr_WorkstationInfo
from .netr_WorkstationInformation import netr_WorkstationInformation
from .NL_DNS_NAME_INFO import NL_DNS_NAME_INFO
from .NL_DNS_NAME_INFO_ARRAY import NL_DNS_NAME_INFO_ARRAY
from .NL_PASSWORD_VERSION import NL_PASSWORD_VERSION
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.netlogon', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/netlogon.cpython-310-x86_64-linux-gnu.so')"

