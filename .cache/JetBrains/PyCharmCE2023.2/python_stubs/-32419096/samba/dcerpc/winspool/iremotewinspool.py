# encoding: utf-8
# module samba.dcerpc.winspool
# from /usr/lib/python3/dist-packages/samba/dcerpc/winspool.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" winspool DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class iremotewinspool(__dcerpc.ClientConnection):
    """
    iremotewinspool(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    IRemoteWinspool SubSystem
    """
    def AsyncAbortPrinter(self, hPrinter): # real signature unknown; restored from __doc__
        """ S.AsyncAbortPrinter(hPrinter) -> None """
        pass

    def AsyncAddForm(self, hPrinter, pFormInfoContainer): # real signature unknown; restored from __doc__
        """ S.AsyncAddForm(hPrinter, pFormInfoContainer) -> None """
        pass

    def AsyncAddJob(self, hPrinter, Level, pAddJob): # real signature unknown; restored from __doc__
        """ S.AsyncAddJob(hPrinter, Level, pAddJob) -> (pAddJob, pcbNeeded) """
        pass

    def AsyncAddMonitor(self, Name, pMonitorContainer): # real signature unknown; restored from __doc__
        """ S.AsyncAddMonitor(Name, pMonitorContainer) -> None """
        pass

    def AsyncAddPerMachineConnection(self, pServer, pPrinterName, pPrintServer, pProvider): # real signature unknown; restored from __doc__
        """ S.AsyncAddPerMachineConnection(pServer, pPrinterName, pPrintServer, pProvider) -> None """
        pass

    def AsyncAddPort(self, pName, pPortContainer, pPortVarContainer, pMonitorName): # real signature unknown; restored from __doc__
        """ S.AsyncAddPort(pName, pPortContainer, pPortVarContainer, pMonitorName) -> None """
        pass

    def AsyncAddPrinter(self, pName, pPrinterContainer, pDevModeContainer, pSecurityContainer, pClientInfo): # real signature unknown; restored from __doc__
        """ S.AsyncAddPrinter(pName, pPrinterContainer, pDevModeContainer, pSecurityContainer, pClientInfo) -> pHandle """
        pass

    def AsyncAddPrinterDriver(self, pName, pDriverContainer, dwFileCopyFlags): # real signature unknown; restored from __doc__
        """ S.AsyncAddPrinterDriver(pName, pDriverContainer, dwFileCopyFlags) -> None """
        pass

    def AsyncAddPrintProcessor(self, pName, pEnvironment, pPathName, pPrintProcessorName): # real signature unknown; restored from __doc__
        """ S.AsyncAddPrintProcessor(pName, pEnvironment, pPathName, pPrintProcessorName) -> None """
        pass

    def AsyncClosePrinter(self, phPrinter): # real signature unknown; restored from __doc__
        """ S.AsyncClosePrinter(phPrinter) -> phPrinter """
        pass

    def AsyncCorePrinterDriverInstalled(self, pszServer, pszEnvironment, CoreDriverGUID, ftDriverDate, dwlDriverVersion): # real signature unknown; restored from __doc__
        """ S.AsyncCorePrinterDriverInstalled(pszServer, pszEnvironment, CoreDriverGUID, ftDriverDate, dwlDriverVersion) -> (pbDriverInstalled, result) """
        pass

    def AsyncCreatePrinterIC(self, hPrinter, pDevModeContainer): # real signature unknown; restored from __doc__
        """ S.AsyncCreatePrinterIC(hPrinter, pDevModeContainer) -> pHandle """
        pass

    def AsyncDeleteForm(self, hPrinter, pFormName): # real signature unknown; restored from __doc__
        """ S.AsyncDeleteForm(hPrinter, pFormName) -> None """
        pass

    def AsyncDeleteJobNamedProperty(self, hPrinter, JobId, pszName): # real signature unknown; restored from __doc__
        """ S.AsyncDeleteJobNamedProperty(hPrinter, JobId, pszName) -> None """
        pass

    def AsyncDeleteMonitor(self, Name, pEnvironment, pMonitorName): # real signature unknown; restored from __doc__
        """ S.AsyncDeleteMonitor(Name, pEnvironment, pMonitorName) -> None """
        pass

    def AsyncDeletePerMachineConnection(self, pServer, pPrinterName): # real signature unknown; restored from __doc__
        """ S.AsyncDeletePerMachineConnection(pServer, pPrinterName) -> None """
        pass

    def AsyncDeletePrinter(self, hPrinter): # real signature unknown; restored from __doc__
        """ S.AsyncDeletePrinter(hPrinter) -> None """
        pass

    def AsyncDeletePrinterData(self, hPrinter, pValueName): # real signature unknown; restored from __doc__
        """ S.AsyncDeletePrinterData(hPrinter, pValueName) -> None """
        pass

    def AsyncDeletePrinterDataEx(self, hPrinter, pKeyName, pValueName): # real signature unknown; restored from __doc__
        """ S.AsyncDeletePrinterDataEx(hPrinter, pKeyName, pValueName) -> None """
        pass

    def AsyncDeletePrinterDriver(self, pName, pEnvironment, pDriverName): # real signature unknown; restored from __doc__
        """ S.AsyncDeletePrinterDriver(pName, pEnvironment, pDriverName) -> None """
        pass

    def AsyncDeletePrinterDriverEx(self, pName, pEnvironment, pDriverName, dwDeleteFlag, dwVersionNum): # real signature unknown; restored from __doc__
        """ S.AsyncDeletePrinterDriverEx(pName, pEnvironment, pDriverName, dwDeleteFlag, dwVersionNum) -> None """
        pass

    def AsyncDeletePrinterDriverPackage(self, pszServer, pszInfPath, pszEnvironment): # real signature unknown; restored from __doc__
        """ S.AsyncDeletePrinterDriverPackage(pszServer, pszInfPath, pszEnvironment) -> result """
        pass

    def AsyncDeletePrinterIC(self, phPrinterIC): # real signature unknown; restored from __doc__
        """ S.AsyncDeletePrinterIC(phPrinterIC) -> phPrinterIC """
        pass

    def AsyncDeletePrinterKey(self, hPrinter, pKeyName): # real signature unknown; restored from __doc__
        """ S.AsyncDeletePrinterKey(hPrinter, pKeyName) -> None """
        pass

    def AsyncDeletePrintProcessor(self, Name, pEnvironment, pPrintProcessorName): # real signature unknown; restored from __doc__
        """ S.AsyncDeletePrintProcessor(Name, pEnvironment, pPrintProcessorName) -> None """
        pass

    def AsyncEndDocPrinter(self, hPrinter): # real signature unknown; restored from __doc__
        """ S.AsyncEndDocPrinter(hPrinter) -> None """
        pass

    def AsyncEndPagePrinter(self, hPrinter): # real signature unknown; restored from __doc__
        """ S.AsyncEndPagePrinter(hPrinter) -> None """
        pass

    def AsyncEnumForms(self, hPrinter, Level, pForm): # real signature unknown; restored from __doc__
        """ S.AsyncEnumForms(hPrinter, Level, pForm) -> (pForm, pcbNeeded, pcReturned) """
        pass

    def AsyncEnumJobNamedProperties(self, hPrinter, JobId): # real signature unknown; restored from __doc__
        """ S.AsyncEnumJobNamedProperties(hPrinter, JobId) -> (pcProperties, ppProperties) """
        pass

    def AsyncEnumJobs(self, hPrinter, FirstJob, NoJobs, Level, pJob): # real signature unknown; restored from __doc__
        """ S.AsyncEnumJobs(hPrinter, FirstJob, NoJobs, Level, pJob) -> (pJob, pcbNeeded, pcReturned) """
        pass

    def AsyncEnumMonitors(self, pName, Level, pMonitor): # real signature unknown; restored from __doc__
        """ S.AsyncEnumMonitors(pName, Level, pMonitor) -> (pMonitor, pcbNeeded, pcReturned) """
        pass

    def AsyncEnumPerMachineConnections(self, pServer, pPrinterEnum): # real signature unknown; restored from __doc__
        """ S.AsyncEnumPerMachineConnections(pServer, pPrinterEnum) -> (pPrinterEnum, pcbNeeded, pcReturned) """
        pass

    def AsyncEnumPorts(self, pName, Level, pPort): # real signature unknown; restored from __doc__
        """ S.AsyncEnumPorts(pName, Level, pPort) -> (pPort, pcbNeeded, pcReturned) """
        pass

    def AsyncEnumPrinterData(self, hPrinter, dwIndex, cbValueName, cbData): # real signature unknown; restored from __doc__
        """ S.AsyncEnumPrinterData(hPrinter, dwIndex, cbValueName, cbData) -> (pValueName, pcbValueName, pType, pData, pcbData) """
        pass

    def AsyncEnumPrinterDataEx(self, hPrinter, pKeyName, cbEnumValues): # real signature unknown; restored from __doc__
        """ S.AsyncEnumPrinterDataEx(hPrinter, pKeyName, cbEnumValues) -> (pEnumValues, pcbEnumValues, pnEnumValues) """
        pass

    def AsyncEnumPrinterDrivers(self, pName, pEnvironment, Level, pDrivers): # real signature unknown; restored from __doc__
        """ S.AsyncEnumPrinterDrivers(pName, pEnvironment, Level, pDrivers) -> (pDrivers, pcbNeeded, pcReturned) """
        pass

    def AsyncEnumPrinterKey(self, hPrinter, pKeyName, cbSubkey): # real signature unknown; restored from __doc__
        """ S.AsyncEnumPrinterKey(hPrinter, pKeyName, cbSubkey) -> (pSubkey, pcbSubkey) """
        pass

    def AsyncEnumPrinters(self, Flags, pName, Level, pPrinterEnum): # real signature unknown; restored from __doc__
        """ S.AsyncEnumPrinters(Flags, pName, Level, pPrinterEnum) -> (pPrinterEnum, pcbNeeded, pcReturned) """
        pass

    def AsyncEnumPrintProcessorDatatypes(self, pName, pPrintProcessorName, Level, pDatatypes): # real signature unknown; restored from __doc__
        """ S.AsyncEnumPrintProcessorDatatypes(pName, pPrintProcessorName, Level, pDatatypes) -> (pDatatypes, pcbNeeded, pcReturned) """
        pass

    def AsyncEnumPrintProcessors(self, pName, pEnvironment, Level, pPrintProcessorInfo): # real signature unknown; restored from __doc__
        """ S.AsyncEnumPrintProcessors(pName, pEnvironment, Level, pPrintProcessorInfo) -> (pPrintProcessorInfo, pcbNeeded, pcReturned) """
        pass

    def AsyncGetCorePrinterDrivers(self, pszServer, pszEnvironment, pszzCoreDriverDependencies, cCorePrinterDrivers): # real signature unknown; restored from __doc__
        """ S.AsyncGetCorePrinterDrivers(pszServer, pszEnvironment, pszzCoreDriverDependencies, cCorePrinterDrivers) -> (pCorePrinterDrivers, result) """
        pass

    def AsyncGetForm(self, hPrinter, pFormName, Level, pForm): # real signature unknown; restored from __doc__
        """ S.AsyncGetForm(hPrinter, pFormName, Level, pForm) -> (pForm, pcbNeeded) """
        pass

    def AsyncGetJob(self, hPrinter, JobId, Level, pJob): # real signature unknown; restored from __doc__
        """ S.AsyncGetJob(hPrinter, JobId, Level, pJob) -> (pJob, pcbNeeded) """
        pass

    def AsyncGetJobNamedPropertyValue(self, hPrinter, JobId, pszName): # real signature unknown; restored from __doc__
        """ S.AsyncGetJobNamedPropertyValue(hPrinter, JobId, pszName) -> pValue """
        pass

    def AsyncGetPrinter(self, hPrinter, Level, pPrinter): # real signature unknown; restored from __doc__
        """ S.AsyncGetPrinter(hPrinter, Level, pPrinter) -> (pPrinter, pcbNeeded) """
        pass

    def AsyncGetPrinterData(self, hPrinter, pValueName, nSize): # real signature unknown; restored from __doc__
        """ S.AsyncGetPrinterData(hPrinter, pValueName, nSize) -> (pType, pData, pcbNeeded) """
        pass

    def AsyncGetPrinterDataEx(self, hPrinter, pKeyName, pValueName, nSize): # real signature unknown; restored from __doc__
        """ S.AsyncGetPrinterDataEx(hPrinter, pKeyName, pValueName, nSize) -> (pType, pData, pcbNeeded) """
        pass

    def AsyncGetPrinterDriver(self, hPrinter, pEnvironment, Level, pDriver, dwClientMajorVersion, dwClientMinorVersion): # real signature unknown; restored from __doc__
        """ S.AsyncGetPrinterDriver(hPrinter, pEnvironment, Level, pDriver, dwClientMajorVersion, dwClientMinorVersion) -> (pDriver, pcbNeeded, pdwServerMaxVersion, pdwServerMinVersion) """
        pass

    def AsyncGetPrinterDriverDirectory(self, pName, pEnvironment, Level, pDriverDirectory): # real signature unknown; restored from __doc__
        """ S.AsyncGetPrinterDriverDirectory(pName, pEnvironment, Level, pDriverDirectory) -> (pDriverDirectory, pcbNeeded) """
        pass

    def AsyncGetPrinterDriverPackagePath(self, pszServer, pszEnvironment, pszLanguage, pszPackageID, pszDriverPackageCab): # real signature unknown; restored from __doc__
        """ S.AsyncGetPrinterDriverPackagePath(pszServer, pszEnvironment, pszLanguage, pszPackageID, pszDriverPackageCab) -> (pszDriverPackageCab, pcchRequiredSize, result) """
        pass

    def AsyncGetPrintProcessorDirectory(self, pName, pEnvironment, Level, pPrintProcessorDirectory): # real signature unknown; restored from __doc__
        """ S.AsyncGetPrintProcessorDirectory(pName, pEnvironment, Level, pPrintProcessorDirectory) -> (pPrintProcessorDirectory, pcbNeeded) """
        pass

    def AsyncGetRemoteNotifications(self, hRpcHandle): # real signature unknown; restored from __doc__
        """ S.AsyncGetRemoteNotifications(hRpcHandle) -> (ppNotifyData, result) """
        pass

    def AsyncInstallPrinterDriverFromPackage(self, pszServer, pszInfPath, pszDriverName, pszEnvironment, dwFlags): # real signature unknown; restored from __doc__
        """ S.AsyncInstallPrinterDriverFromPackage(pszServer, pszInfPath, pszDriverName, pszEnvironment, dwFlags) -> result """
        pass

    def AsyncLogJobInfoForBranchOffice(self, hPrinter, pBranchOfficeJobDataContainer): # real signature unknown; restored from __doc__
        """ S.AsyncLogJobInfoForBranchOffice(hPrinter, pBranchOfficeJobDataContainer) -> None """
        pass

    def AsyncOpenPrinter(self, pPrinterName, pDatatype, pDevModeContainer, AccessRequired, pClientInfo): # real signature unknown; restored from __doc__
        """ S.AsyncOpenPrinter(pPrinterName, pDatatype, pDevModeContainer, AccessRequired, pClientInfo) -> pHandle """
        pass

    def AsyncPlayGdiScriptOnPrinterIC(self, hPrinterIC, pIn, cOut, ul): # real signature unknown; restored from __doc__
        """ S.AsyncPlayGdiScriptOnPrinterIC(hPrinterIC, pIn, cOut, ul) -> pOut """
        pass

    def AsyncReadPrinter(self, hPrinter, cbBuf): # real signature unknown; restored from __doc__
        """ S.AsyncReadPrinter(hPrinter, cbBuf) -> (pBuf, pcNoBytesRead) """
        pass

    def AsyncResetPrinter(self, hPrinter, pDatatype, pDevModeContainer): # real signature unknown; restored from __doc__
        """ S.AsyncResetPrinter(hPrinter, pDatatype, pDevModeContainer) -> None """
        pass

    def AsyncScheduleJob(self, hPrinter, JobId): # real signature unknown; restored from __doc__
        """ S.AsyncScheduleJob(hPrinter, JobId) -> None """
        pass

    def AsyncSendRecvBidiData(self, hPrinter, pAction, pReqData): # real signature unknown; restored from __doc__
        """ S.AsyncSendRecvBidiData(hPrinter, pAction, pReqData) -> ppRespData """
        pass

    def AsyncSetForm(self, hPrinter, pFormName, pFormInfoContainer): # real signature unknown; restored from __doc__
        """ S.AsyncSetForm(hPrinter, pFormName, pFormInfoContainer) -> None """
        pass

    def AsyncSetJob(self, hPrinter, JobId, pJobContainer, Command): # real signature unknown; restored from __doc__
        """ S.AsyncSetJob(hPrinter, JobId, pJobContainer, Command) -> None """
        pass

    def AsyncSetJobNamedProperty(self, hPrinter, JobId, pProperty): # real signature unknown; restored from __doc__
        """ S.AsyncSetJobNamedProperty(hPrinter, JobId, pProperty) -> None """
        pass

    def AsyncSetPort(self, pName, pPortName, pPortContainer): # real signature unknown; restored from __doc__
        """ S.AsyncSetPort(pName, pPortName, pPortContainer) -> None """
        pass

    def AsyncSetPrinter(self, hPrinter, pPrinterContainer, pDevModeContainer, pSecurityContainer, Command): # real signature unknown; restored from __doc__
        """ S.AsyncSetPrinter(hPrinter, pPrinterContainer, pDevModeContainer, pSecurityContainer, Command) -> None """
        pass

    def AsyncSetPrinterData(self, hPrinter, pValueName, Type, pData): # real signature unknown; restored from __doc__
        """ S.AsyncSetPrinterData(hPrinter, pValueName, Type, pData) -> None """
        pass

    def AsyncSetPrinterDataEx(self, hPrinter, pKeyName, pValueName, Type, pData): # real signature unknown; restored from __doc__
        """ S.AsyncSetPrinterDataEx(hPrinter, pKeyName, pValueName, Type, pData) -> None """
        pass

    def AsyncStartDocPrinter(self, hPrinter, pDocInfoContainer): # real signature unknown; restored from __doc__
        """ S.AsyncStartDocPrinter(hPrinter, pDocInfoContainer) -> pJobId """
        pass

    def AsyncStartPagePrinter(self, hPrinter): # real signature unknown; restored from __doc__
        """ S.AsyncStartPagePrinter(hPrinter) -> None """
        pass

    def AsyncUploadPrinterDriverPackage(self, pszServer, pszInfPath, pszEnvironment, dwFlags, pszDestInfPath): # real signature unknown; restored from __doc__
        """ S.AsyncUploadPrinterDriverPackage(pszServer, pszInfPath, pszEnvironment, dwFlags, pszDestInfPath) -> (pszDestInfPath, result) """
        pass

    def AsyncWritePrinter(self, hPrinter, pBuf): # real signature unknown; restored from __doc__
        """ S.AsyncWritePrinter(hPrinter, pBuf) -> pcWritten """
        pass

    def AsyncXcvData(self, hXcv, pszDataName, pInputData, cbOutputData, pdwStatus): # real signature unknown; restored from __doc__
        """ S.AsyncXcvData(hXcv, pszDataName, pInputData, cbOutputData, pdwStatus) -> (pOutputData, pcbOutputNeeded, pdwStatus) """
        pass

    def SyncRefreshRemoteNotifications(self, hRpcHandle, pNotifyFilter): # real signature unknown; restored from __doc__
        """ S.SyncRefreshRemoteNotifications(hRpcHandle, pNotifyFilter) -> (ppNotifyData, result) """
        pass

    def SyncRegisterForRemoteNotifications(self, hPrinter, pNotifyFilter): # real signature unknown; restored from __doc__
        """ S.SyncRegisterForRemoteNotifications(hPrinter, pNotifyFilter) -> (phRpcHandle, result) """
        pass

    def SyncUnRegisterForRemoteNotifications(self, phRpcHandle): # real signature unknown; restored from __doc__
        """ S.SyncUnRegisterForRemoteNotifications(phRpcHandle) -> (phRpcHandle, result) """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


