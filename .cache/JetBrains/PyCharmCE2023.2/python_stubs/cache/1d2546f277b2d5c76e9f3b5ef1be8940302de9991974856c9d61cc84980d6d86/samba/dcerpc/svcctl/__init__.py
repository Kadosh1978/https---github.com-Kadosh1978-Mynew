# encoding: utf-8
# module samba.dcerpc.svcctl
# from /usr/lib/python3/dist-packages/samba/dcerpc/svcctl.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" svcctl DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

MAX_SERVICE_NAME_LENGTH = 256

SC_ACTION_NONE = 0
SC_ACTION_REBOOT = 2
SC_ACTION_RESTART = 1

SC_ACTION_RUN_COMMAND = 3

SC_MANAGER_ALL_ACCESS = 983103

SC_MANAGER_EXECUTE_ACCESS = 131093

SC_MANAGER_READ_ACCESS = 131093

SC_MANAGER_WRITE_ACCESS = 983103

SC_MAX_ACCOUNT_NAME_LENGTH = 2048

SC_MAX_ARGUMENTS = 1024

SC_MAX_ARGUMENT_LENGTH = 1024

SC_MAX_COMMENT_LENGTH = 128

SC_MAX_COMPUTER_NAME_LENGTH = 1024

SC_MAX_DEPEND_SIZE = 4096

SC_MAX_NAME_LENGTH = 257

SC_MAX_PATH_LENGTH = 32768

SC_MAX_PWD_SIZE = 514

SC_RIGHT_MGR_CONNECT = 1

SC_RIGHT_MGR_CREATE_SERVICE = 2

SC_RIGHT_MGR_ENUMERATE_SERVICE = 4

SC_RIGHT_MGR_LOCK = 8

SC_RIGHT_MGR_MODIFY_BOOT_CONFIG = 32

SC_RIGHT_MGR_QUERY_LOCK_STATUS = 16

SC_RIGHT_SVC_CHANGE_CONFIG = 2

SC_RIGHT_SVC_ENUMERATE_DEPENDENTS = 8

SC_RIGHT_SVC_INTERROGATE = 128

SC_RIGHT_SVC_PAUSE_CONTINUE = 64

SC_RIGHT_SVC_QUERY_CONFIG = 1
SC_RIGHT_SVC_QUERY_STATUS = 4

SC_RIGHT_SVC_START = 16
SC_RIGHT_SVC_STOP = 32

SC_RIGHT_SVC_USER_DEFINED_CONTROL = 256

SERVICE_ALL_ACCESS = 983551

SERVICE_CONFIG_DESCRIPTION = 1

SERVICE_CONFIG_FAILURE_ACTIONS = 2

SERVICE_EXECUTE_ACCESS = 131581

SERVICE_READ_ACCESS = 131469

SERVICE_STATE_ACTIVE = 1
SERVICE_STATE_ALL = 3
SERVICE_STATE_INACTIVE = 2

SERVICE_TYPE_ADAPTER = 4
SERVICE_TYPE_DRIVER = 11

SERVICE_TYPE_FS_DRIVER = 2

SERVICE_TYPE_INTERACTIVE_PROCESS = 256

SERVICE_TYPE_KERNEL_DRIVER = 1

SERVICE_TYPE_RECOGNIZER_DRIVER = 8

SERVICE_TYPE_WIN32 = 48

SERVICE_TYPE_WIN32_OWN_PROCESS = 16

SERVICE_TYPE_WIN32_SHARE_PROCESS = 32

SERVICE_WRITE_ACCESS = 983551

SVCCTL_ACCEPT_HARDWAREPROFILECHANGE = 32
SVCCTL_ACCEPT_NETBINDCHANGE = 16
SVCCTL_ACCEPT_NONE = 0
SVCCTL_ACCEPT_PARAMCHANGE = 8

SVCCTL_ACCEPT_PAUSE_CONTINUE = 2

SVCCTL_ACCEPT_POWEREVENT = 64
SVCCTL_ACCEPT_SHUTDOWN = 4
SVCCTL_ACCEPT_STOP = 1

SVCCTL_AUTO_START = 2

SVCCTL_BOOT_START = 0

SVCCTL_CONTINUE_PENDING = 5

SVCCTL_CONTROL_CONTINUE = 3
SVCCTL_CONTROL_INTERROGATE = 4
SVCCTL_CONTROL_PAUSE = 2
SVCCTL_CONTROL_SHUTDOWN = 5
SVCCTL_CONTROL_STOP = 1

SVCCTL_DEMAND_START = 3

SVCCTL_DISABLED = 4
SVCCTL_PAUSED = 7

SVCCTL_PAUSE_PENDING = 6

SVCCTL_RUNNING = 4

SVCCTL_START_PENDING = 2

SVCCTL_STATE_UNKNOWN = 0

SVCCTL_STOPPED = 1

SVCCTL_STOP_PENDING = 3

SVCCTL_SVC_ERROR_CRITICAL = 2
SVCCTL_SVC_ERROR_IGNORE = 0
SVCCTL_SVC_ERROR_NORMAL = 1
SVCCTL_SVC_ERROR_SEVERE = 3

SVCCTL_SYSTEM_START = 1

SVC_STATUS_PROCESS_INFO = 0

# no functions
# classes

from .svcctl_abstract_syntax import svcctl_abstract_syntax
from .abstract_syntax import abstract_syntax
from .ArgumentString import ArgumentString
from .ChangeServiceConfig2A import ChangeServiceConfig2A
from .ChangeServiceConfig2W import ChangeServiceConfig2W
from .ChangeServiceConfigA import ChangeServiceConfigA
from .ChangeServiceConfigW import ChangeServiceConfigW
from .CloseServiceHandle import CloseServiceHandle
from .ControlService import ControlService
from .CreateServiceA import CreateServiceA
from .CreateServiceW import CreateServiceW
from .DeleteService import DeleteService
from .EnumDependentServicesA import EnumDependentServicesA
from .EnumDependentServicesW import EnumDependentServicesW
from .EnumServicesStatusA import EnumServicesStatusA
from .EnumServicesStatusExA import EnumServicesStatusExA
from .EnumServicesStatusExW import EnumServicesStatusExW
from .EnumServicesStatusW import EnumServicesStatusW
from .ENUM_SERVICE_STATUSA import ENUM_SERVICE_STATUSA
from .ENUM_SERVICE_STATUSW import ENUM_SERVICE_STATUSW
from .GetServiceDisplayNameA import GetServiceDisplayNameA
from .GetServiceDisplayNameW import GetServiceDisplayNameW
from .GetServiceKeyNameA import GetServiceKeyNameA
from .GetServiceKeyNameW import GetServiceKeyNameW
from .LockServiceDatabase import LockServiceDatabase
from .OpenSCManagerA import OpenSCManagerA
from .OpenSCManagerW import OpenSCManagerW
from .OpenServiceA import OpenServiceA
from .OpenServiceW import OpenServiceW
from .QueryServiceConfig2A import QueryServiceConfig2A
from .QueryServiceConfig2W import QueryServiceConfig2W
from .QueryServiceConfigA import QueryServiceConfigA
from .QueryServiceConfigW import QueryServiceConfigW
from .QueryServiceLockStatusA import QueryServiceLockStatusA
from .QueryServiceLockStatusW import QueryServiceLockStatusW
from .QueryServiceObjectSecurity import QueryServiceObjectSecurity
from .QueryServiceStatus import QueryServiceStatus
from .QueryServiceStatusEx import QueryServiceStatusEx
from .QUERY_SERVICE_CONFIG import QUERY_SERVICE_CONFIG
from .SCSetServiceBitsA import SCSetServiceBitsA
from .SCSetServiceBitsW import SCSetServiceBitsW
from .SC_ACTION import SC_ACTION
from .SERVICE_DESCRIPTION import SERVICE_DESCRIPTION
from .SERVICE_FAILURE_ACTIONS import SERVICE_FAILURE_ACTIONS
from .SERVICE_LOCK_STATUS import SERVICE_LOCK_STATUS
from .SERVICE_STATUS import SERVICE_STATUS
from .SERVICE_STATUS_PROCESS import SERVICE_STATUS_PROCESS
from .SetServiceObjectSecurity import SetServiceObjectSecurity
from .StartServiceA import StartServiceA
from .StartServiceW import StartServiceW
from .svcctl import svcctl
from .UnlockServiceDatabase import UnlockServiceDatabase
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.svcctl', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/svcctl.cpython-310-x86_64-linux-gnu.so')"

