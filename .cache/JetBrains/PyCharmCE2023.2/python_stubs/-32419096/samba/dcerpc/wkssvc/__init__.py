# encoding: utf-8
# module samba.dcerpc.wkssvc
# from /usr/lib/python3/dist-packages/samba/dcerpc/wkssvc.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" wkssvc DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

NetAllComputerNames = 2
NetAlternateComputerNames = 1
NetComputerNameTypeMax = 3
NetPrimaryComputerName = 0
NetSetupDnsMachine = 5
NetSetupDomain = 3
NetSetupMachine = 1
NetSetupNonExistentDomain = 4
NetSetupUnknown = 0
NetSetupWorkgroup = 2

NET_SETUP_DOMAIN_NAME = 3

NET_SETUP_UNJOINED = 1

NET_SETUP_UNKNOWN_STATUS = 0

NET_SETUP_WORKGROUP_NAME = 2

WKSSVC_JOIN_FLAGS_ACCOUNT_CREATE = 2
WKSSVC_JOIN_FLAGS_ACCOUNT_DELETE = 4

WKSSVC_JOIN_FLAGS_DEFER_SPN = 256

WKSSVC_JOIN_FLAGS_DOMAIN_JOIN_IF_JOINED = 32

WKSSVC_JOIN_FLAGS_IGNORE_UNSUPPORTED_FLAGS = 268435456

WKSSVC_JOIN_FLAGS_JOIN_DC_ACCOUNT = 512

WKSSVC_JOIN_FLAGS_JOIN_TYPE = 1
WKSSVC_JOIN_FLAGS_JOIN_UNSECURE = 64

WKSSVC_JOIN_FLAGS_JOIN_WITH_NEW_NAME = 1024

WKSSVC_JOIN_FLAGS_MACHINE_PWD_PASSED = 128

WKSSVC_JOIN_FLAGS_WIN9X_UPGRADE = 16

# no functions
# classes

from .wkssvc_abstract_syntax import wkssvc_abstract_syntax
from .abstract_syntax import abstract_syntax
from .ComputerNamesCtr import ComputerNamesCtr
from .NetrAddAlternateComputerName import NetrAddAlternateComputerName
from .NetrEnumerateComputerNames import NetrEnumerateComputerNames
from .NetrGetJoinableOus import NetrGetJoinableOus
from .NetrGetJoinableOus2 import NetrGetJoinableOus2
from .NetrGetJoinInformation import NetrGetJoinInformation
from .NetrJoinDomain import NetrJoinDomain
from .NetrJoinDomain2 import NetrJoinDomain2
from .NetrLogonDomainNameAdd import NetrLogonDomainNameAdd
from .NetrLogonDomainNameDel import NetrLogonDomainNameDel
from .NetrMessageBufferSend import NetrMessageBufferSend
from .NetrRemoveAlternateComputerName import NetrRemoveAlternateComputerName
from .NetrRenameMachineInDomain import NetrRenameMachineInDomain
from .NetrRenameMachineInDomain2 import NetrRenameMachineInDomain2
from .NetrSetPrimaryComputername import NetrSetPrimaryComputername
from .NetrUnjoinDomain import NetrUnjoinDomain
from .NetrUnjoinDomain2 import NetrUnjoinDomain2
from .NetrUseAdd import NetrUseAdd
from .NetrUseDel import NetrUseDel
from .NetrUseEnum import NetrUseEnum
from .NetrUseEnumCtr import NetrUseEnumCtr
from .NetrUseEnumCtr0 import NetrUseEnumCtr0
from .NetrUseEnumCtr1 import NetrUseEnumCtr1
from .NetrUseEnumCtr2 import NetrUseEnumCtr2
from .NetrUseEnumInfo import NetrUseEnumInfo
from .NetrUseGetInfo import NetrUseGetInfo
from .NetrUseGetInfoCtr import NetrUseGetInfoCtr
from .NetrUseInfo0 import NetrUseInfo0
from .NetrUseInfo1 import NetrUseInfo1
from .NetrUseInfo2 import NetrUseInfo2
from .NetrUseInfo3 import NetrUseInfo3
from .NetrValidateName import NetrValidateName
from .NetrValidateName2 import NetrValidateName2
from .NetrWkstaTransportAdd import NetrWkstaTransportAdd
from .NetrWkstaTransportDel import NetrWkstaTransportDel
from .NetrWkstaUserGetInfo import NetrWkstaUserGetInfo
from .NetrWkstaUserInfo import NetrWkstaUserInfo
from .NetrWkstaUserInfo0 import NetrWkstaUserInfo0
from .NetrWkstaUserInfo1 import NetrWkstaUserInfo1
from .NetrWkstaUserInfo1101 import NetrWkstaUserInfo1101
from .NetrWkstaUserSetInfo import NetrWkstaUserSetInfo
from .NetrWorkstationStatistics import NetrWorkstationStatistics
from .NetrWorkstationStatisticsGet import NetrWorkstationStatisticsGet
from .NetWkstaEnumUsers import NetWkstaEnumUsers
from .NetWkstaEnumUsersCtr import NetWkstaEnumUsersCtr
from .NetWkstaEnumUsersCtr0 import NetWkstaEnumUsersCtr0
from .NetWkstaEnumUsersCtr1 import NetWkstaEnumUsersCtr1
from .NetWkstaEnumUsersInfo import NetWkstaEnumUsersInfo
from .NetWkstaGetInfo import NetWkstaGetInfo
from .NetWkstaInfo import NetWkstaInfo
from .NetWkstaInfo100 import NetWkstaInfo100
from .NetWkstaInfo101 import NetWkstaInfo101
from .NetWkstaInfo1010 import NetWkstaInfo1010
from .NetWkstaInfo1011 import NetWkstaInfo1011
from .NetWkstaInfo1012 import NetWkstaInfo1012
from .NetWkstaInfo1013 import NetWkstaInfo1013
from .NetWkstaInfo1018 import NetWkstaInfo1018
from .NetWkstaInfo102 import NetWkstaInfo102
from .NetWkstaInfo1023 import NetWkstaInfo1023
from .NetWkstaInfo1027 import NetWkstaInfo1027
from .NetWkstaInfo1028 import NetWkstaInfo1028
from .NetWkstaInfo1032 import NetWkstaInfo1032
from .NetWkstaInfo1033 import NetWkstaInfo1033
from .NetWkstaInfo1041 import NetWkstaInfo1041
from .NetWkstaInfo1042 import NetWkstaInfo1042
from .NetWkstaInfo1043 import NetWkstaInfo1043
from .NetWkstaInfo1044 import NetWkstaInfo1044
from .NetWkstaInfo1045 import NetWkstaInfo1045
from .NetWkstaInfo1046 import NetWkstaInfo1046
from .NetWkstaInfo1047 import NetWkstaInfo1047
from .NetWkstaInfo1048 import NetWkstaInfo1048
from .NetWkstaInfo1049 import NetWkstaInfo1049
from .NetWkstaInfo1050 import NetWkstaInfo1050
from .NetWkstaInfo1051 import NetWkstaInfo1051
from .NetWkstaInfo1052 import NetWkstaInfo1052
from .NetWkstaInfo1053 import NetWkstaInfo1053
from .NetWkstaInfo1054 import NetWkstaInfo1054
from .NetWkstaInfo1055 import NetWkstaInfo1055
from .NetWkstaInfo1056 import NetWkstaInfo1056
from .NetWkstaInfo1057 import NetWkstaInfo1057
from .NetWkstaInfo1058 import NetWkstaInfo1058
from .NetWkstaInfo1059 import NetWkstaInfo1059
from .NetWkstaInfo1060 import NetWkstaInfo1060
from .NetWkstaInfo1061 import NetWkstaInfo1061
from .NetWkstaInfo1062 import NetWkstaInfo1062
from .NetWkstaInfo502 import NetWkstaInfo502
from .NetWkstaSetInfo import NetWkstaSetInfo
from .NetWkstaTransportCtr import NetWkstaTransportCtr
from .NetWkstaTransportCtr0 import NetWkstaTransportCtr0
from .NetWkstaTransportEnum import NetWkstaTransportEnum
from .NetWkstaTransportInfo import NetWkstaTransportInfo
from .NetWkstaTransportInfo0 import NetWkstaTransportInfo0
from .PasswordBuffer import PasswordBuffer
from .wkssvc import wkssvc
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.wkssvc', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/wkssvc.cpython-310-x86_64-linux-gnu.so')"

