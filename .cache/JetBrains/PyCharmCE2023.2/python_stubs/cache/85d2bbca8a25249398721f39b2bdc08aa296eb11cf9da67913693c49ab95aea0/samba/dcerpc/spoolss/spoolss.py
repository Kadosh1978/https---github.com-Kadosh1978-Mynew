# encoding: utf-8
# module samba.dcerpc.spoolss
# from /usr/lib/python3/dist-packages/samba/dcerpc/spoolss.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" spoolss DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class spoolss(__dcerpc.ClientConnection):
    """
    spoolss(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Spooler SubSystem
    """
    def AbortPrinter(self, handle): # real signature unknown; restored from __doc__
        """ S.AbortPrinter(handle) -> None """
        pass

    def AddForm(self, handle, info_ctr): # real signature unknown; restored from __doc__
        """ S.AddForm(handle, info_ctr) -> None """
        pass

    def AddJob(self, handle, level, buffer): # real signature unknown; restored from __doc__
        """ S.AddJob(handle, level, buffer) -> (buffer, needed) """
        pass

    def AddPerMachineConnection(self, server, printername, printserver, provider): # real signature unknown; restored from __doc__
        """ S.AddPerMachineConnection(server, printername, printserver, provider) -> None """
        pass

    def AddPort(self, server_name, unknown, monitor_name): # real signature unknown; restored from __doc__
        """ S.AddPort(server_name, unknown, monitor_name) -> None """
        pass

    def AddPortEx(self, servername, port_ctr, port_var_ctr, monitor_name): # real signature unknown; restored from __doc__
        """ S.AddPortEx(servername, port_ctr, port_var_ctr, monitor_name) -> None """
        pass

    def AddPrinter(self, server, info_ctr, devmode_ctr, secdesc_ctr): # real signature unknown; restored from __doc__
        """ S.AddPrinter(server, info_ctr, devmode_ctr, secdesc_ctr) -> handle """
        pass

    def AddPrinterDriver(self, servername, info_ctr): # real signature unknown; restored from __doc__
        """ S.AddPrinterDriver(servername, info_ctr) -> None """
        pass

    def AddPrinterDriverEx(self, servername, info_ctr, flags): # real signature unknown; restored from __doc__
        """ S.AddPrinterDriverEx(servername, info_ctr, flags) -> None """
        pass

    def AddPrinterEx(self, server, info_ctr, devmode_ctr, secdesc_ctr, userlevel_ctr): # real signature unknown; restored from __doc__
        """ S.AddPrinterEx(server, info_ctr, devmode_ctr, secdesc_ctr, userlevel_ctr) -> handle """
        pass

    def AddPrintProcessor(self, server, architecture, path_name, print_processor_name): # real signature unknown; restored from __doc__
        """ S.AddPrintProcessor(server, architecture, path_name, print_processor_name) -> None """
        pass

    def ClosePrinter(self, handle): # real signature unknown; restored from __doc__
        """ S.ClosePrinter(handle) -> handle """
        pass

    def CreatePrinterIC(self, handle, devmode_ctr): # real signature unknown; restored from __doc__
        """ S.CreatePrinterIC(handle, devmode_ctr) -> gdi_handle """
        pass

    def DeleteForm(self, handle, form_name): # real signature unknown; restored from __doc__
        """ S.DeleteForm(handle, form_name) -> None """
        pass

    def DeleteJobNamedProperty(self, hPrinter, JobId, pszName): # real signature unknown; restored from __doc__
        """ S.DeleteJobNamedProperty(hPrinter, JobId, pszName) -> None """
        pass

    def DeletePerMachineConnection(self, server, printername): # real signature unknown; restored from __doc__
        """ S.DeletePerMachineConnection(server, printername) -> None """
        pass

    def DeletePort(self, server_name, ptr, port_name): # real signature unknown; restored from __doc__
        """ S.DeletePort(server_name, ptr, port_name) -> None """
        pass

    def DeletePrinter(self, handle): # real signature unknown; restored from __doc__
        """ S.DeletePrinter(handle) -> None """
        pass

    def DeletePrinterData(self, handle, value_name): # real signature unknown; restored from __doc__
        """ S.DeletePrinterData(handle, value_name) -> None """
        pass

    def DeletePrinterDataEx(self, handle, key_name, value_name): # real signature unknown; restored from __doc__
        """ S.DeletePrinterDataEx(handle, key_name, value_name) -> None """
        pass

    def DeletePrinterDriver(self, server, architecture, driver): # real signature unknown; restored from __doc__
        """ S.DeletePrinterDriver(server, architecture, driver) -> None """
        pass

    def DeletePrinterDriverEx(self, server, architecture, driver, delete_flags, version): # real signature unknown; restored from __doc__
        """ S.DeletePrinterDriverEx(server, architecture, driver, delete_flags, version) -> None """
        pass

    def DeletePrinterIC(self, gdi_handle): # real signature unknown; restored from __doc__
        """ S.DeletePrinterIC(gdi_handle) -> gdi_handle """
        pass

    def DeletePrinterKey(self, handle, key_name): # real signature unknown; restored from __doc__
        """ S.DeletePrinterKey(handle, key_name) -> None """
        pass

    def DeletePrintProcessor(self, server, architecture, print_processor_name): # real signature unknown; restored from __doc__
        """ S.DeletePrintProcessor(server, architecture, print_processor_name) -> None """
        pass

    def EndDocPrinter(self, handle): # real signature unknown; restored from __doc__
        """ S.EndDocPrinter(handle) -> None """
        pass

    def EndPagePrinter(self, handle): # real signature unknown; restored from __doc__
        """ S.EndPagePrinter(handle) -> None """
        pass

    def EnumForms(self, handle, level, buffer, offered): # real signature unknown; restored from __doc__
        """ S.EnumForms(handle, level, buffer, offered) -> (count, info, needed) """
        pass

    def EnumJobNamedProperties(self, hPrinter, JobId): # real signature unknown; restored from __doc__
        """ S.EnumJobNamedProperties(hPrinter, JobId) -> (pcProperties, ppProperties) """
        pass

    def EnumJobs(self, handle, firstjob, numjobs, level, buffer, offered): # real signature unknown; restored from __doc__
        """ S.EnumJobs(handle, firstjob, numjobs, level, buffer, offered) -> (count, info, needed) """
        pass

    def EnumMonitors(self, servername, level, buffer, offered): # real signature unknown; restored from __doc__
        """ S.EnumMonitors(servername, level, buffer, offered) -> (count, info, needed) """
        pass

    def EnumPerMachineConnections(self, server, buffer, offered): # real signature unknown; restored from __doc__
        """ S.EnumPerMachineConnections(server, buffer, offered) -> (count, info, needed) """
        pass

    def EnumPorts(self, servername, level, buffer, offered): # real signature unknown; restored from __doc__
        """ S.EnumPorts(servername, level, buffer, offered) -> (count, info, needed) """
        pass

    def EnumPrinterData(self, handle, enum_index, value_offered, data_offered): # real signature unknown; restored from __doc__
        """ S.EnumPrinterData(handle, enum_index, value_offered, data_offered) -> (value_name, value_needed, type, data, data_needed) """
        pass

    def EnumPrinterDataEx(self, handle, key_name, offered): # real signature unknown; restored from __doc__
        """ S.EnumPrinterDataEx(handle, key_name, offered) -> (count, info, needed) """
        pass

    def EnumPrinterDrivers(self, server, environment, level, buffer, offered): # real signature unknown; restored from __doc__
        """ S.EnumPrinterDrivers(server, environment, level, buffer, offered) -> (count, info, needed) """
        pass

    def EnumPrinterKey(self, handle, key_name, offered): # real signature unknown; restored from __doc__
        """ S.EnumPrinterKey(handle, key_name, offered) -> (_ndr_size, key_buffer, needed) """
        pass

    def EnumPrinters(self, flags, server, level, buffer, offered): # real signature unknown; restored from __doc__
        """ S.EnumPrinters(flags, server, level, buffer, offered) -> (count, info, needed) """
        pass

    def EnumPrintProcessorDataTypes(self, servername, print_processor_name, level, buffer, offered): # real signature unknown; restored from __doc__
        """ S.EnumPrintProcessorDataTypes(servername, print_processor_name, level, buffer, offered) -> (count, info, needed) """
        pass

    def EnumPrintProcessors(self, servername, environment, level, buffer, offered): # real signature unknown; restored from __doc__
        """ S.EnumPrintProcessors(servername, environment, level, buffer, offered) -> (count, info, needed) """
        pass

    def FindClosePrinterNotify(self, handle): # real signature unknown; restored from __doc__
        """ S.FindClosePrinterNotify(handle) -> None """
        pass

    def GetCorePrinterDrivers(self, servername, architecture, core_driver_dependencies, core_printer_driver_count): # real signature unknown; restored from __doc__
        """ S.GetCorePrinterDrivers(servername, architecture, core_driver_dependencies, core_printer_driver_count) -> (core_printer_drivers, result) """
        pass

    def GetForm(self, handle, form_name, level, buffer, offered): # real signature unknown; restored from __doc__
        """ S.GetForm(handle, form_name, level, buffer, offered) -> (info, needed) """
        pass

    def GetJob(self, handle, job_id, level, buffer, offered): # real signature unknown; restored from __doc__
        """ S.GetJob(handle, job_id, level, buffer, offered) -> (info, needed) """
        pass

    def GetJobNamedPropertyValue(self, hPrinter, JobId, pszName): # real signature unknown; restored from __doc__
        """ S.GetJobNamedPropertyValue(hPrinter, JobId, pszName) -> pValue """
        pass

    def GetPrinter(self, handle, level, buffer, offered): # real signature unknown; restored from __doc__
        """ S.GetPrinter(handle, level, buffer, offered) -> (info, needed) """
        pass

    def GetPrinterData(self, handle, value_name, offered): # real signature unknown; restored from __doc__
        """ S.GetPrinterData(handle, value_name, offered) -> (type, data, needed) """
        pass

    def GetPrinterDataEx(self, handle, key_name, value_name, offered): # real signature unknown; restored from __doc__
        """ S.GetPrinterDataEx(handle, key_name, value_name, offered) -> (type, data, needed) """
        pass

    def GetPrinterDriver(self, handle, architecture, level, buffer, offered): # real signature unknown; restored from __doc__
        """ S.GetPrinterDriver(handle, architecture, level, buffer, offered) -> (info, needed) """
        pass

    def GetPrinterDriver2(self, handle, architecture, level, buffer, offered, client_major_version, client_minor_version): # real signature unknown; restored from __doc__
        """ S.GetPrinterDriver2(handle, architecture, level, buffer, offered, client_major_version, client_minor_version) -> (info, needed, server_major_version, server_minor_version) """
        pass

    def GetPrinterDriverDirectory(self, server, environment, level, buffer, offered): # real signature unknown; restored from __doc__
        """ S.GetPrinterDriverDirectory(server, environment, level, buffer, offered) -> (info, needed) """
        pass

    def GetPrinterDriverPackagePath(self, servername, architecture, language, package_id, driver_package_cab): # real signature unknown; restored from __doc__
        """ S.GetPrinterDriverPackagePath(servername, architecture, language, package_id, driver_package_cab) -> (driver_package_cab, required, result) """
        pass

    def GetPrintProcessorDirectory(self, server, environment, level, buffer, offered): # real signature unknown; restored from __doc__
        """ S.GetPrintProcessorDirectory(server, environment, level, buffer, offered) -> (info, needed) """
        pass

    def LogJobInfoForBranchOffice(self, hPrinter, pBranchOfficeJobDataContainer): # real signature unknown; restored from __doc__
        """ S.LogJobInfoForBranchOffice(hPrinter, pBranchOfficeJobDataContainer) -> None """
        pass

    def OpenPrinter(self, printername, datatype, devmode_ctr, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenPrinter(printername, datatype, devmode_ctr, access_mask) -> handle """
        pass

    def OpenPrinterEx(self, printername, datatype, devmode_ctr, access_mask, userlevel_ctr): # real signature unknown; restored from __doc__
        """ S.OpenPrinterEx(printername, datatype, devmode_ctr, access_mask, userlevel_ctr) -> handle """
        pass

    def PlayGDIScriptOnPrinterIC(self, gdi_handle, pIn, cOut, ul): # real signature unknown; restored from __doc__
        """ S.PlayGDIScriptOnPrinterIC(gdi_handle, pIn, cOut, ul) -> pOut """
        pass

    def ReadPrinter(self, handle, data_size): # real signature unknown; restored from __doc__
        """ S.ReadPrinter(handle, data_size) -> (data, _data_size) """
        pass

    def RemoteFindFirstPrinterChangeNotifyEx(self, handle, flags, options, local_machine, printer_local, notify_options): # real signature unknown; restored from __doc__
        """ S.RemoteFindFirstPrinterChangeNotifyEx(handle, flags, options, local_machine, printer_local, notify_options) -> None """
        pass

    def ReplyClosePrinter(self, handle): # real signature unknown; restored from __doc__
        """ S.ReplyClosePrinter(handle) -> handle """
        pass

    def ReplyOpenPrinter(self, server_name, printer_local, type, buffer): # real signature unknown; restored from __doc__
        """ S.ReplyOpenPrinter(server_name, printer_local, type, buffer) -> handle """
        pass

    def ResetPrinter(self, handle, data_type, devmode_ctr): # real signature unknown; restored from __doc__
        """ S.ResetPrinter(handle, data_type, devmode_ctr) -> None """
        pass

    def RouterRefreshPrinterChangeNotify(self, handle, change_low, options): # real signature unknown; restored from __doc__
        """ S.RouterRefreshPrinterChangeNotify(handle, change_low, options) -> info """
        pass

    def RouterReplyPrinter(self, handle, flags, buffer): # real signature unknown; restored from __doc__
        """ S.RouterReplyPrinter(handle, flags, buffer) -> None """
        pass

    def RouterReplyPrinterEx(self, handle, color, flags, reply_type, info): # real signature unknown; restored from __doc__
        """ S.RouterReplyPrinterEx(handle, color, flags, reply_type, info) -> reply_result """
        pass

    def ScheduleJob(self, handle, jobid): # real signature unknown; restored from __doc__
        """ S.ScheduleJob(handle, jobid) -> None """
        pass

    def SendRecvBidiData(self, hPrinter, pAction, pReqData): # real signature unknown; restored from __doc__
        """ S.SendRecvBidiData(hPrinter, pAction, pReqData) -> ppRespData """
        pass

    def SetForm(self, handle, form_name, info_ctr): # real signature unknown; restored from __doc__
        """ S.SetForm(handle, form_name, info_ctr) -> None """
        pass

    def SetJob(self, handle, job_id, ctr, command): # real signature unknown; restored from __doc__
        """ S.SetJob(handle, job_id, ctr, command) -> None """
        pass

    def SetJobNamedProperty(self, hPrinter, JobId, pProperty): # real signature unknown; restored from __doc__
        """ S.SetJobNamedProperty(hPrinter, JobId, pProperty) -> None """
        pass

    def SetPort(self, servername, port_name, port_ctr): # real signature unknown; restored from __doc__
        """ S.SetPort(servername, port_name, port_ctr) -> None """
        pass

    def SetPrinter(self, handle, info_ctr, devmode_ctr, secdesc_ctr, command): # real signature unknown; restored from __doc__
        """ S.SetPrinter(handle, info_ctr, devmode_ctr, secdesc_ctr, command) -> None """
        pass

    def SetPrinterData(self, handle, value_name, type, data): # real signature unknown; restored from __doc__
        """ S.SetPrinterData(handle, value_name, type, data) -> None """
        pass

    def SetPrinterDataEx(self, handle, key_name, value_name, type, data): # real signature unknown; restored from __doc__
        """ S.SetPrinterDataEx(handle, key_name, value_name, type, data) -> None """
        pass

    def StartDocPrinter(self, handle, info_ctr): # real signature unknown; restored from __doc__
        """ S.StartDocPrinter(handle, info_ctr) -> job_id """
        pass

    def StartPagePrinter(self, handle): # real signature unknown; restored from __doc__
        """ S.StartPagePrinter(handle) -> None """
        pass

    def WritePrinter(self, handle, data, _data_size): # real signature unknown; restored from __doc__
        """ S.WritePrinter(handle, data, _data_size) -> num_written """
        pass

    def XcvData(self, handle, function_name, in_data, _in_data_length, out_data_size, status_code): # real signature unknown; restored from __doc__
        """ S.XcvData(handle, function_name, in_data, _in_data_length, out_data_size, status_code) -> (out_data, needed, status_code) """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


