# encoding: utf-8
# module samba.dcerpc.winspool
# from /usr/lib/python3/dist-packages/samba/dcerpc/winspool.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" winspool DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

IPDFP_COPY_ALL_FILES = 1

IPDFP_FLAG_NONE = 0

IREMOTEWINSPOOL_OBJECT_GUID = '9940CA8E-512F-4C58-88A9-61098D6896BD'

PropertyTypeByte = 4
PropertyTypeDevMode = 6
PropertyTypeInt32 = 2
PropertyTypeInt64 = 3
PropertyTypeNotificationOptions = 9
PropertyTypeNotificationReply = 8
PropertyTypeSD = 7
PropertyTypeString = 1
PropertyTypeTime = 5

UPDP_CHECK_DRIVERSTORE = 4

UPDP_FLAG_NONE = 0

UPDP_UPLOAD_ALWAYS = 2

# no functions
# classes

from .iremotewinspool_abstract_syntax import iremotewinspool_abstract_syntax
from .abstract_syntax import abstract_syntax
from .AsyncAbortPrinter import AsyncAbortPrinter
from .AsyncAddForm import AsyncAddForm
from .AsyncAddJob import AsyncAddJob
from .AsyncAddMonitor import AsyncAddMonitor
from .AsyncAddPerMachineConnection import AsyncAddPerMachineConnection
from .AsyncAddPort import AsyncAddPort
from .AsyncAddPrinter import AsyncAddPrinter
from .AsyncAddPrinterDriver import AsyncAddPrinterDriver
from .AsyncAddPrintProcessor import AsyncAddPrintProcessor
from .AsyncClosePrinter import AsyncClosePrinter
from .AsyncCorePrinterDriverInstalled import AsyncCorePrinterDriverInstalled
from .AsyncCreatePrinterIC import AsyncCreatePrinterIC
from .AsyncDeleteForm import AsyncDeleteForm
from .AsyncDeleteJobNamedProperty import AsyncDeleteJobNamedProperty
from .AsyncDeleteMonitor import AsyncDeleteMonitor
from .AsyncDeletePerMachineConnection import AsyncDeletePerMachineConnection
from .AsyncDeletePrinter import AsyncDeletePrinter
from .AsyncDeletePrinterData import AsyncDeletePrinterData
from .AsyncDeletePrinterDataEx import AsyncDeletePrinterDataEx
from .AsyncDeletePrinterDriver import AsyncDeletePrinterDriver
from .AsyncDeletePrinterDriverEx import AsyncDeletePrinterDriverEx
from .AsyncDeletePrinterDriverPackage import AsyncDeletePrinterDriverPackage
from .AsyncDeletePrinterIC import AsyncDeletePrinterIC
from .AsyncDeletePrinterKey import AsyncDeletePrinterKey
from .AsyncDeletePrintProcessor import AsyncDeletePrintProcessor
from .AsyncEndDocPrinter import AsyncEndDocPrinter
from .AsyncEndPagePrinter import AsyncEndPagePrinter
from .AsyncEnumForms import AsyncEnumForms
from .AsyncEnumJobNamedProperties import AsyncEnumJobNamedProperties
from .AsyncEnumJobs import AsyncEnumJobs
from .AsyncEnumMonitors import AsyncEnumMonitors
from .AsyncEnumPerMachineConnections import AsyncEnumPerMachineConnections
from .AsyncEnumPorts import AsyncEnumPorts
from .AsyncEnumPrinterData import AsyncEnumPrinterData
from .AsyncEnumPrinterDataEx import AsyncEnumPrinterDataEx
from .AsyncEnumPrinterDrivers import AsyncEnumPrinterDrivers
from .AsyncEnumPrinterKey import AsyncEnumPrinterKey
from .AsyncEnumPrinters import AsyncEnumPrinters
from .AsyncEnumPrintProcessorDatatypes import AsyncEnumPrintProcessorDatatypes
from .AsyncEnumPrintProcessors import AsyncEnumPrintProcessors
from .AsyncGetCorePrinterDrivers import AsyncGetCorePrinterDrivers
from .AsyncGetForm import AsyncGetForm
from .AsyncGetJob import AsyncGetJob
from .AsyncGetJobNamedPropertyValue import AsyncGetJobNamedPropertyValue
from .AsyncGetPrinter import AsyncGetPrinter
from .AsyncGetPrinterData import AsyncGetPrinterData
from .AsyncGetPrinterDataEx import AsyncGetPrinterDataEx
from .AsyncGetPrinterDriver import AsyncGetPrinterDriver
from .AsyncGetPrinterDriverDirectory import AsyncGetPrinterDriverDirectory
from .AsyncGetPrinterDriverPackagePath import AsyncGetPrinterDriverPackagePath
from .AsyncGetPrintProcessorDirectory import AsyncGetPrintProcessorDirectory
from .AsyncGetRemoteNotifications import AsyncGetRemoteNotifications
from .AsyncInstallPrinterDriverFromPackage import AsyncInstallPrinterDriverFromPackage
from .AsyncLogJobInfoForBranchOffice import AsyncLogJobInfoForBranchOffice
from .AsyncOpenPrinter import AsyncOpenPrinter
from .AsyncPlayGdiScriptOnPrinterIC import AsyncPlayGdiScriptOnPrinterIC
from .AsyncReadPrinter import AsyncReadPrinter
from .AsyncResetPrinter import AsyncResetPrinter
from .AsyncScheduleJob import AsyncScheduleJob
from .AsyncSendRecvBidiData import AsyncSendRecvBidiData
from .AsyncSetForm import AsyncSetForm
from .AsyncSetJob import AsyncSetJob
from .AsyncSetJobNamedProperty import AsyncSetJobNamedProperty
from .AsyncSetPort import AsyncSetPort
from .AsyncSetPrinter import AsyncSetPrinter
from .AsyncSetPrinterData import AsyncSetPrinterData
from .AsyncSetPrinterDataEx import AsyncSetPrinterDataEx
from .AsyncStartDocPrinter import AsyncStartDocPrinter
from .AsyncStartPagePrinter import AsyncStartPagePrinter
from .AsyncUploadPrinterDriverPackage import AsyncUploadPrinterDriverPackage
from .AsyncWritePrinter import AsyncWritePrinter
from .AsyncXcvData import AsyncXcvData
from .iremotewinspool import iremotewinspool
from .NOTIFY_OPTIONS_CONTAINER import NOTIFY_OPTIONS_CONTAINER
from .NOTIFY_REPLY_CONTAINER import NOTIFY_REPLY_CONTAINER
from .PrintNamedProperty import PrintNamedProperty
from .PrintPropertiesCollection import PrintPropertiesCollection
from .PrintPropertyValue import PrintPropertyValue
from .PrintPropertyValueUnion import PrintPropertyValueUnion
from .SyncRefreshRemoteNotifications import SyncRefreshRemoteNotifications
from .SyncRegisterForRemoteNotifications import SyncRegisterForRemoteNotifications
from .SyncUnRegisterForRemoteNotifications import SyncUnRegisterForRemoteNotifications
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.winspool', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/winspool.cpython-310-x86_64-linux-gnu.so')"

