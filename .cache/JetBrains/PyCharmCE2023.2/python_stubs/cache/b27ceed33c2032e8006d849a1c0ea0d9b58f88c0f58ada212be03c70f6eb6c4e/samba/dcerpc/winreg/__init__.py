# encoding: utf-8
# module samba.dcerpc.winreg
# from /usr/lib/python3/dist-packages/samba/dcerpc/winreg.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" winreg DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

KEY_CREATE_LINK = 32

KEY_CREATE_SUB_KEY = 4

KEY_ENUMERATE_SUB_KEYS = 8

KEY_NOTIFY = 16

KEY_QUERY_VALUE = 1

KEY_SET_VALUE = 2

KEY_WOW64_32KEY = 512
KEY_WOW64_64KEY = 256

REG_ACTION_NONE = 0

REG_CREATED_NEW_KEY = 1

REG_FORCE_RESTORE = 8

REG_KEY_ALL = 983103
REG_KEY_EXECUTE = 131097
REG_KEY_READ = 131097
REG_KEY_WRITE = 851974

REG_NOTIFY_CHANGE_ATTRIBUTES = 2

REG_NOTIFY_CHANGE_LAST_SET = 4

REG_NOTIFY_CHANGE_NAME = 1
REG_NOTIFY_CHANGE_SECURITY = 8

REG_NO_LAZY_FLUSH = 4

REG_OPENED_EXISTING_KEY = 2

REG_OPTION_BACKUP_RESTORE = 4

REG_OPTION_CREATE_LINK = 2

REG_OPTION_NON_VOLATILE = 0

REG_OPTION_OPEN_LINK = 8

REG_OPTION_VOLATILE = 1

REG_REFRESH_HIVE = 2

REG_WHOLE_HIVE_VOLATILE = 1

# no functions
# classes

from .AbortSystemShutdown import AbortSystemShutdown
from .winreg_abstract_syntax import winreg_abstract_syntax
from .abstract_syntax import abstract_syntax
from .CloseKey import CloseKey
from .CreateKey import CreateKey
from .DeleteKey import DeleteKey
from .DeleteKeyEx import DeleteKeyEx
from .DeleteValue import DeleteValue
from .EnumKey import EnumKey
from .EnumValue import EnumValue
from .FlushKey import FlushKey
from .GetKeySecurity import GetKeySecurity
from .GetVersion import GetVersion
from .InitiateSystemShutdown import InitiateSystemShutdown
from .InitiateSystemShutdownEx import InitiateSystemShutdownEx
from .KeySecurityAttribute import KeySecurityAttribute
from .KeySecurityData import KeySecurityData
from .LoadKey import LoadKey
from .NotifyChangeKeyValue import NotifyChangeKeyValue
from .OpenHKCC import OpenHKCC
from .OpenHKCR import OpenHKCR
from .OpenHKCU import OpenHKCU
from .OpenHKDD import OpenHKDD
from .OpenHKLM import OpenHKLM
from .OpenHKPD import OpenHKPD
from .OpenHKPN import OpenHKPN
from .OpenHKPT import OpenHKPT
from .OpenHKU import OpenHKU
from .OpenKey import OpenKey
from .QueryInfoKey import QueryInfoKey
from .QueryMultipleValue import QueryMultipleValue
from .QueryMultipleValues import QueryMultipleValues
from .QueryMultipleValues2 import QueryMultipleValues2
from .QueryValue import QueryValue
from .ReplaceKey import ReplaceKey
from .RestoreKey import RestoreKey
from .SaveKey import SaveKey
from .SaveKeyEx import SaveKeyEx
from .SecBuf import SecBuf
from .SetKeySecurity import SetKeySecurity
from .SetValue import SetValue
from .String import String
from .StringBuf import StringBuf
from .UnLoadKey import UnLoadKey
from .ValNameBuf import ValNameBuf
from .winreg import winreg
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.winreg', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/winreg.cpython-310-x86_64-linux-gnu.so')"

