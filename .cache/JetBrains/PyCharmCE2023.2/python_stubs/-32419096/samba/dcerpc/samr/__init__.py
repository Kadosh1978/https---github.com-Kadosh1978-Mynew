# encoding: utf-8
# module samba.dcerpc.samr
# from /usr/lib/python3/dist-packages/samba/dcerpc/samr.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" samr DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

ACB_AUTOLOCK = 1024
ACB_DISABLED = 1
ACB_DOMTRUST = 64

ACB_DONT_REQUIRE_PREAUTH = 65536

ACB_ENC_TXT_PWD_ALLOWED = 2048

ACB_HOMDIRREQ = 2
ACB_MNS = 32
ACB_NORMAL = 16

ACB_NOT_DELEGATED = 16384

ACB_NO_AUTH_DATA_REQD = 524288

ACB_PARTIAL_SECRETS_ACCOUNT = 1048576

ACB_PWNOEXP = 512
ACB_PWNOTREQ = 4

ACB_PW_EXPIRED = 131072

ACB_SMARTCARD_REQUIRED = 4096

ACB_SVRTRUST = 256
ACB_TEMPDUP = 8

ACB_TRUSTED_FOR_DELEGATION = 8192

ACB_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION = 262144

ACB_USE_AES_KEYS = 2097152

ACB_USE_DES_KEY_ONLY = 32768

ACB_WSTRUST = 128

ALIASINFOALL = 1
ALIASINFODESCRIPTION = 3
ALIASINFONAME = 2

DomainGeneralInformation = 2
DomainGeneralInformation2 = 11
DomainLockoutInformation = 12
DomainLogoffInformation = 3
DomainModifiedInformation = 8
DomainModifiedInformation2 = 13
DomainNameInformation = 5
DomainOemInformation = 4
DomainPasswordInformation = 1
DomainReplicationInformation = 6
DomainServerRoleInformation = 7
DomainStateInformation = 9
DomainUasInformation = 10

DOMAIN_PASSWORD_COMPLEX = 1

DOMAIN_PASSWORD_LOCKOUT_ADMINS = 8

DOMAIN_PASSWORD_NO_ANON_CHANGE = 2

DOMAIN_PASSWORD_NO_CLEAR_CHANGE = 4

DOMAIN_PASSWORD_STORE_CLEARTEXT = 16

DOMAIN_REFUSE_PASSWORD_CHANGE = 32

DOMAIN_SERVER_DISABLED = 2
DOMAIN_SERVER_ENABLED = 1

GENERIC_RIGHTS_ALIAS_ALL_ACCESS = 983071

GENERIC_RIGHTS_ALIAS_EXECUTE = 131080
GENERIC_RIGHTS_ALIAS_READ = 131076
GENERIC_RIGHTS_ALIAS_WRITE = 851987

GENERIC_RIGHTS_DOMAIN_ALL_ACCESS = 985087

GENERIC_RIGHTS_DOMAIN_EXECUTE = 131841
GENERIC_RIGHTS_DOMAIN_READ = 131204
GENERIC_RIGHTS_DOMAIN_WRITE = 853114

GENERIC_RIGHTS_GROUP_ALL_ACCESS = 983071

GENERIC_RIGHTS_GROUP_EXECUTE = 131073
GENERIC_RIGHTS_GROUP_READ = 131088
GENERIC_RIGHTS_GROUP_WRITE = 851982

GENERIC_RIGHTS_SAM_ALL_ACCESS = 983103

GENERIC_RIGHTS_SAM_EXECUTE = 131105
GENERIC_RIGHTS_SAM_READ = 131088
GENERIC_RIGHTS_SAM_WRITE = 851982

GENERIC_RIGHTS_USER_ALL_ACCESS = 985087

GENERIC_RIGHTS_USER_EXECUTE = 131137
GENERIC_RIGHTS_USER_READ = 131866
GENERIC_RIGHTS_USER_WRITE = 853220

GROUPINFOALL = 1
GROUPINFOALL2 = 5
GROUPINFOATTRIBUTES = 3
GROUPINFODESCRIPTION = 4
GROUPINFONAME = 2

NetValidateAuthentication = 1
NetValidatePasswordChange = 2
NetValidatePasswordReset = 3

PASS_DONT_CHANGE_AT_NEXT_LOGON = 0

PASS_MUST_CHANGE_AT_NEXT_LOGON = 1

SAMR_ACCESS_ALL_ACCESS = 63

SAMR_ACCESS_CONNECT_TO_SERVER = 1

SAMR_ACCESS_CREATE_DOMAIN = 8

SAMR_ACCESS_ENUM_DOMAINS = 16

SAMR_ACCESS_INITIALIZE_SERVER = 4

SAMR_ACCESS_LOOKUP_DOMAIN = 32

SAMR_ACCESS_SHUTDOWN_SERVER = 2

SAMR_ALIAS_ACCESS_ADD_MEMBER = 1

SAMR_ALIAS_ACCESS_ALL_ACCESS = 31

SAMR_ALIAS_ACCESS_GET_MEMBERS = 4

SAMR_ALIAS_ACCESS_LOOKUP_INFO = 8

SAMR_ALIAS_ACCESS_REMOVE_MEMBER = 2

SAMR_ALIAS_ACCESS_SET_INFO = 16

SAMR_CONNECT_AFTER_W2K = 3

SAMR_CONNECT_PRE_W2K = 1

SAMR_CONNECT_W2K = 2

SAMR_DOMAIN_ACCESS_ALL_ACCESS = 2047

SAMR_DOMAIN_ACCESS_CREATE_ALIAS = 64
SAMR_DOMAIN_ACCESS_CREATE_GROUP = 32
SAMR_DOMAIN_ACCESS_CREATE_USER = 16

SAMR_DOMAIN_ACCESS_ENUM_ACCOUNTS = 256

SAMR_DOMAIN_ACCESS_LOOKUP_ALIAS = 128

SAMR_DOMAIN_ACCESS_LOOKUP_INFO_1 = 1
SAMR_DOMAIN_ACCESS_LOOKUP_INFO_2 = 4

SAMR_DOMAIN_ACCESS_OPEN_ACCOUNT = 512

SAMR_DOMAIN_ACCESS_SET_INFO_1 = 2
SAMR_DOMAIN_ACCESS_SET_INFO_2 = 8
SAMR_DOMAIN_ACCESS_SET_INFO_3 = 1024

SAMR_ENUM_USERS_MULTIPLIER = 54

SAMR_FIELD_ACCOUNT_NAME = 1

SAMR_FIELD_ACCT_EXPIRY = 524288
SAMR_FIELD_ACCT_FLAGS = 1048576

SAMR_FIELD_ALLOW_PWD_CHANGE = 65536

SAMR_FIELD_BAD_PWD_COUNT = 16384

SAMR_FIELD_CODE_PAGE = 8388608

SAMR_FIELD_COMMENT = 32

SAMR_FIELD_COUNTRY_CODE = 4194304

SAMR_FIELD_DESCRIPTION = 16

SAMR_FIELD_EXPIRED_FLAG = 134217728

SAMR_FIELD_FORCE_PWD_CHANGE = 131072

SAMR_FIELD_FULL_NAME = 2

SAMR_FIELD_HOME_DIRECTORY = 64
SAMR_FIELD_HOME_DRIVE = 128

SAMR_FIELD_LAST_LOGOFF = 4096
SAMR_FIELD_LAST_LOGON = 2048

SAMR_FIELD_LAST_PWD_CHANGE = 262144

SAMR_FIELD_LM_PASSWORD_PRESENT = 33554432

SAMR_FIELD_LOGON_HOURS = 8192
SAMR_FIELD_LOGON_SCRIPT = 256

SAMR_FIELD_NT_PASSWORD_PRESENT = 16777216

SAMR_FIELD_NUM_LOGONS = 32768

SAMR_FIELD_OWF_PWD = 536870912

SAMR_FIELD_PARAMETERS = 2097152

SAMR_FIELD_PRIMARY_GID = 8

SAMR_FIELD_PRIVATE_DATA = 67108864

SAMR_FIELD_PROFILE_PATH = 512

SAMR_FIELD_RID = 4

SAMR_FIELD_SEC_DESC = 268435456

SAMR_FIELD_WORKSTATIONS = 1024

SAMR_GROUP_ACCESS_ADD_MEMBER = 4

SAMR_GROUP_ACCESS_ALL_ACCESS = 31

SAMR_GROUP_ACCESS_GET_MEMBERS = 16

SAMR_GROUP_ACCESS_LOOKUP_INFO = 1

SAMR_GROUP_ACCESS_REMOVE_MEMBER = 8

SAMR_GROUP_ACCESS_SET_INFO = 2

SAMR_ROLE_DOMAIN_BDC = 2
SAMR_ROLE_DOMAIN_MEMBER = 1
SAMR_ROLE_DOMAIN_PDC = 3

SAMR_ROLE_STANDALONE = 0

SAMR_USER_ACCESS_ALL_ACCESS = 2047

SAMR_USER_ACCESS_CHANGE_GROUP_MEMBERSHIP = 1024

SAMR_USER_ACCESS_CHANGE_PASSWORD = 64

SAMR_USER_ACCESS_GET_ATTRIBUTES = 16
SAMR_USER_ACCESS_GET_GROUPS = 256

SAMR_USER_ACCESS_GET_GROUP_MEMBERSHIP = 512

SAMR_USER_ACCESS_GET_LOCALE = 2
SAMR_USER_ACCESS_GET_LOGONINFO = 8

SAMR_USER_ACCESS_GET_NAME_ETC = 1

SAMR_USER_ACCESS_SET_ATTRIBUTES = 32

SAMR_USER_ACCESS_SET_LOC_COM = 4

SAMR_USER_ACCESS_SET_PASSWORD = 128

SAMR_VALIDATE_FIELD_BAD_PASSWORD_COUNT = 8
SAMR_VALIDATE_FIELD_BAD_PASSWORD_TIME = 2

SAMR_VALIDATE_FIELD_LOCKOUT_TIME = 4

SAMR_VALIDATE_FIELD_PASSWORD_HISTORY = 32

SAMR_VALIDATE_FIELD_PASSWORD_HISTORY_LENGTH = 16

SAMR_VALIDATE_FIELD_PASSWORD_LAST_SET = 1

SAMR_VALIDATION_STATUS_ACCOUNT_LOCKED_OUT = 2

SAMR_VALIDATION_STATUS_BAD_PASSWORD = 4

SAMR_VALIDATION_STATUS_NOT_COMPLEX_ENOUGH = 8

SAMR_VALIDATION_STATUS_PASSWORD_EXPIRED = 3

SAMR_VALIDATION_STATUS_PASSWORD_FILTER_ERROR = 10

SAMR_VALIDATION_STATUS_PASSWORD_MUST_CHANGE = 1

SAMR_VALIDATION_STATUS_PASSWORD_TOO_RECENT = 9

SAMR_VALIDATION_STATUS_PWD_HISTORY_CONFLICT = 5

SAMR_VALIDATION_STATUS_PWD_TOO_LONG = 7
SAMR_VALIDATION_STATUS_PWD_TOO_SHORT = 6

SAMR_VALIDATION_STATUS_SUCCESS = 0

SAM_PWD_CHANGE_FAILED_BY_FILTER = 7

SAM_PWD_CHANGE_FULLNAME_IN_PASSWORD = 4

SAM_PWD_CHANGE_MACHINE_NOT_DEFAULT = 6

SAM_PWD_CHANGE_NOT_COMPLEX = 5

SAM_PWD_CHANGE_NO_ERROR = 0

SAM_PWD_CHANGE_PASSWORD_TOO_LONG = 8
SAM_PWD_CHANGE_PASSWORD_TOO_SHORT = 1

SAM_PWD_CHANGE_PWD_IN_HISTORY = 2

SAM_PWD_CHANGE_USERNAME_IN_PASSWORD = 3

UserAccountInformation = 5
UserAccountNameInformation = 7
UserAdminCommentInformation = 13
UserAllInformation = 21
UserControlInformation = 16
UserExpiresInformation = 17
UserFullNameInformation = 8
UserGeneralInformation = 1
UserHomeInformation = 10
UserInternal1Information = 18
UserInternal4Information = 23
UserInternal4InformationNew = 25
UserInternal5Information = 24
UserInternal5InformationNew = 26
UserLogonHoursInformation = 4
UserLogonInformation = 3
UserNameInformation = 6
UserParametersInformation = 20
UserPreferencesInformation = 2
UserPrimaryGroupInformation = 9
UserProfileInformation = 12
UserScriptInformation = 11
UserWorkStationsInformation = 14

# no functions
# classes

from .samr_abstract_syntax import samr_abstract_syntax
from .abstract_syntax import abstract_syntax
from .AddAliasMember import AddAliasMember
from .AddGroupMember import AddGroupMember
from .AddMultipleMembersToAlias import AddMultipleMembersToAlias
from .AliasInfo import AliasInfo
from .AliasInfoAll import AliasInfoAll
from .ChangePasswordUser import ChangePasswordUser
from .ChangePasswordUser2 import ChangePasswordUser2
from .ChangePasswordUser3 import ChangePasswordUser3
from .Close import Close
from .Connect import Connect
from .Connect2 import Connect2
from .Connect3 import Connect3
from .Connect4 import Connect4
from .Connect5 import Connect5
from .ConnectInfo import ConnectInfo
from .ConnectInfo1 import ConnectInfo1
from .CreateDomainGroup import CreateDomainGroup
from .CreateDomAlias import CreateDomAlias
from .CreateUser import CreateUser
from .CreateUser2 import CreateUser2
from .CryptPassword import CryptPassword
from .CryptPasswordEx import CryptPasswordEx
from .DeleteAliasMember import DeleteAliasMember
from .DeleteDomainGroup import DeleteDomainGroup
from .DeleteDomAlias import DeleteDomAlias
from .DeleteGroupMember import DeleteGroupMember
from .DeleteUser import DeleteUser
from .DispEntryAscii import DispEntryAscii
from .DispEntryFull import DispEntryFull
from .DispEntryFullGroup import DispEntryFullGroup
from .DispEntryGeneral import DispEntryGeneral
from .DispInfo import DispInfo
from .DispInfoAscii import DispInfoAscii
from .DispInfoFull import DispInfoFull
from .DispInfoFullGroups import DispInfoFullGroups
from .DispInfoGeneral import DispInfoGeneral
from .DomainInfo import DomainInfo
from .DomGeneralInformation import DomGeneralInformation
from .DomGeneralInformation2 import DomGeneralInformation2
from .DomInfo1 import DomInfo1
from .DomInfo12 import DomInfo12
from .DomInfo13 import DomInfo13
from .DomInfo3 import DomInfo3
from .DomInfo5 import DomInfo5
from .DomInfo6 import DomInfo6
from .DomInfo7 import DomInfo7
from .DomInfo8 import DomInfo8
from .DomInfo9 import DomInfo9
from .DomOEMInformation import DomOEMInformation
from .EnumDomainAliases import EnumDomainAliases
from .EnumDomainGroups import EnumDomainGroups
from .EnumDomains import EnumDomains
from .EnumDomainUsers import EnumDomainUsers
from .GetAliasMembership import GetAliasMembership
from .GetBootKeyInformation import GetBootKeyInformation
from .GetDisplayEnumerationIndex import GetDisplayEnumerationIndex
from .GetDisplayEnumerationIndex2 import GetDisplayEnumerationIndex2
from .GetDomPwInfo import GetDomPwInfo
from .GetGroupsForUser import GetGroupsForUser
from .GetMembersInAlias import GetMembersInAlias
from .GetUserPwInfo import GetUserPwInfo
from .GroupInfo import GroupInfo
from .GroupInfoAll import GroupInfoAll
from .GroupInfoAttributes import GroupInfoAttributes
from .GroupInfoDescription import GroupInfoDescription
from .Ids import Ids
from .LogonHours import LogonHours
from .LookupDomain import LookupDomain
from .LookupNames import LookupNames
from .LookupRids import LookupRids
from .OemChangePasswordUser2 import OemChangePasswordUser2
from .OpenAlias import OpenAlias
from .OpenDomain import OpenDomain
from .OpenGroup import OpenGroup
from .OpenUser import OpenUser
from .Password import Password
from .PwInfo import PwInfo
from .QueryAliasInfo import QueryAliasInfo
from .QueryDisplayInfo import QueryDisplayInfo
from .QueryDisplayInfo2 import QueryDisplayInfo2
from .QueryDisplayInfo3 import QueryDisplayInfo3
from .QueryDomainInfo import QueryDomainInfo
from .QueryDomainInfo2 import QueryDomainInfo2
from .QueryGroupInfo import QueryGroupInfo
from .QueryGroupMember import QueryGroupMember
from .QuerySecurity import QuerySecurity
from .QueryUserInfo import QueryUserInfo
from .QueryUserInfo2 import QueryUserInfo2
from .RemoveMemberFromForeignDomain import RemoveMemberFromForeignDomain
from .RemoveMultipleMembersFromAlias import RemoveMultipleMembersFromAlias
from .RidAttrArray import RidAttrArray
from .RidToSid import RidToSid
from .RidWithAttribute import RidWithAttribute
from .RidWithAttributeArray import RidWithAttributeArray
from .SamArray import SamArray
from .SamEntry import SamEntry
from .samr import samr
from .SetAliasInfo import SetAliasInfo
from .SetBootKeyInformation import SetBootKeyInformation
from .SetDomainInfo import SetDomainInfo
from .SetDsrmPassword import SetDsrmPassword
from .SetGroupInfo import SetGroupInfo
from .SetMemberAttributesOfGroup import SetMemberAttributesOfGroup
from .SetSecurity import SetSecurity
from .SetUserInfo import SetUserInfo
from .SetUserInfo2 import SetUserInfo2
from .Shutdown import Shutdown
from .TestPrivateFunctionsDomain import TestPrivateFunctionsDomain
from .TestPrivateFunctionsUser import TestPrivateFunctionsUser
from .UserInfo import UserInfo
from .UserInfo1 import UserInfo1
from .UserInfo10 import UserInfo10
from .UserInfo11 import UserInfo11
from .UserInfo12 import UserInfo12
from .UserInfo13 import UserInfo13
from .UserInfo14 import UserInfo14
from .UserInfo16 import UserInfo16
from .UserInfo17 import UserInfo17
from .UserInfo18 import UserInfo18
from .UserInfo2 import UserInfo2
from .UserInfo20 import UserInfo20
from .UserInfo21 import UserInfo21
from .UserInfo23 import UserInfo23
from .UserInfo24 import UserInfo24
from .UserInfo25 import UserInfo25
from .UserInfo26 import UserInfo26
from .UserInfo3 import UserInfo3
from .UserInfo4 import UserInfo4
from .UserInfo5 import UserInfo5
from .UserInfo6 import UserInfo6
from .UserInfo7 import UserInfo7
from .UserInfo8 import UserInfo8
from .UserInfo9 import UserInfo9
from .userPwdChangeFailureInformation import userPwdChangeFailureInformation
from .ValidatePassword import ValidatePassword
from .ValidatePasswordInfo import ValidatePasswordInfo
from .ValidatePasswordRep import ValidatePasswordRep
from .ValidatePasswordRepCtr import ValidatePasswordRepCtr
from .ValidatePasswordReq import ValidatePasswordReq
from .ValidatePasswordReq1 import ValidatePasswordReq1
from .ValidatePasswordReq2 import ValidatePasswordReq2
from .ValidatePasswordReq3 import ValidatePasswordReq3
from .ValidationBlob import ValidationBlob
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.samr', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/samr.cpython-310-x86_64-linux-gnu.so')"

