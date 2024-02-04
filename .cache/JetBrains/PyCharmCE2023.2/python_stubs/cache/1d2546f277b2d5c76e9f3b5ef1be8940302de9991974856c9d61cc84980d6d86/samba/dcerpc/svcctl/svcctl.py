# encoding: utf-8
# module samba.dcerpc.svcctl
# from /usr/lib/python3/dist-packages/samba/dcerpc/svcctl.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" svcctl DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class svcctl(__dcerpc.ClientConnection):
    """
    svcctl(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Service Control
    """
    def ChangeServiceConfig2A(self, handle, info_level, info): # real signature unknown; restored from __doc__
        """ S.ChangeServiceConfig2A(handle, info_level, info) -> None """
        pass

    def ChangeServiceConfig2W(self, handle, info_level, info): # real signature unknown; restored from __doc__
        """ S.ChangeServiceConfig2W(handle, info_level, info) -> None """
        pass

    def ChangeServiceConfigA(self, handle, type, start_type, error_control, binary_path, load_order_group, dependencies, service_start_name, password, display_name): # real signature unknown; restored from __doc__
        """ S.ChangeServiceConfigA(handle, type, start_type, error_control, binary_path, load_order_group, dependencies, service_start_name, password, display_name) -> tag_id """
        pass

    def ChangeServiceConfigW(self, handle, type, start_type, error_control, binary_path, load_order_group, tag_id, dependencies, service_start_name, password, display_name): # real signature unknown; restored from __doc__
        """ S.ChangeServiceConfigW(handle, type, start_type, error_control, binary_path, load_order_group, tag_id, dependencies, service_start_name, password, display_name) -> tag_id """
        pass

    def CloseServiceHandle(self, handle): # real signature unknown; restored from __doc__
        """ S.CloseServiceHandle(handle) -> handle """
        pass

    def ControlService(self, handle, control): # real signature unknown; restored from __doc__
        """ S.ControlService(handle, control) -> service_status """
        pass

    def CreateServiceA(self, handle, ServiceName, DisplayName, desired_access, type, start_type, error_control, binary_path, LoadOrderGroupKey, dependencies, service_start_name, password): # real signature unknown; restored from __doc__
        """ S.CreateServiceA(handle, ServiceName, DisplayName, desired_access, type, start_type, error_control, binary_path, LoadOrderGroupKey, dependencies, service_start_name, password) -> TagId """
        pass

    def CreateServiceW(self, scmanager_handle, ServiceName, DisplayName, desired_access, type, start_type, error_control, binary_path, LoadOrderGroupKey, TagId, dependencies, service_start_name, password): # real signature unknown; restored from __doc__
        """ S.CreateServiceW(scmanager_handle, ServiceName, DisplayName, desired_access, type, start_type, error_control, binary_path, LoadOrderGroupKey, TagId, dependencies, service_start_name, password) -> (TagId, handle) """
        pass

    def DeleteService(self, handle): # real signature unknown; restored from __doc__
        """ S.DeleteService(handle) -> None """
        pass

    def EnumDependentServicesA(self, service, state, offered): # real signature unknown; restored from __doc__
        """ S.EnumDependentServicesA(service, state, offered) -> (service_status, needed, services_returned) """
        pass

    def EnumDependentServicesW(self, service, state, offered): # real signature unknown; restored from __doc__
        """ S.EnumDependentServicesW(service, state, offered) -> (service_status, needed, services_returned) """
        pass

    def EnumServicesStatusA(self, handle, type, state, offered, resume_handle): # real signature unknown; restored from __doc__
        """ S.EnumServicesStatusA(handle, type, state, offered, resume_handle) -> (service, needed, services_returned, resume_handle) """
        pass

    def EnumServicesStatusExA(self, scmanager, info_level, type, state, offered, resume_handle): # real signature unknown; restored from __doc__
        """ S.EnumServicesStatusExA(scmanager, info_level, type, state, offered, resume_handle) -> (services, needed, service_returned, resume_handle, group_name) """
        pass

    def EnumServicesStatusExW(self, scmanager, info_level, type, state, offered, resume_handle, group_name): # real signature unknown; restored from __doc__
        """ S.EnumServicesStatusExW(scmanager, info_level, type, state, offered, resume_handle, group_name) -> (services, needed, service_returned, resume_handle) """
        pass

    def EnumServicesStatusW(self, handle, type, state, offered, resume_handle): # real signature unknown; restored from __doc__
        """ S.EnumServicesStatusW(handle, type, state, offered, resume_handle) -> (service, needed, services_returned, resume_handle) """
        pass

    def GetServiceDisplayNameA(self, handle, service_name, display_name_length): # real signature unknown; restored from __doc__
        """ S.GetServiceDisplayNameA(handle, service_name, display_name_length) -> (display_name, display_name_length) """
        pass

    def GetServiceDisplayNameW(self, handle, service_name, display_name_length): # real signature unknown; restored from __doc__
        """ S.GetServiceDisplayNameW(handle, service_name, display_name_length) -> (display_name, display_name_length) """
        pass

    def GetServiceKeyNameA(self, handle, service_name, display_name_length): # real signature unknown; restored from __doc__
        """ S.GetServiceKeyNameA(handle, service_name, display_name_length) -> (key_name, display_name_length) """
        pass

    def GetServiceKeyNameW(self, handle, service_name, display_name_length): # real signature unknown; restored from __doc__
        """ S.GetServiceKeyNameW(handle, service_name, display_name_length) -> (key_name, display_name_length) """
        pass

    def LockServiceDatabase(self, handle): # real signature unknown; restored from __doc__
        """ S.LockServiceDatabase(handle) -> lock """
        pass

    def OpenSCManagerA(self, MachineName, DatabaseName, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenSCManagerA(MachineName, DatabaseName, access_mask) -> handle """
        pass

    def OpenSCManagerW(self, MachineName, DatabaseName, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenSCManagerW(MachineName, DatabaseName, access_mask) -> handle """
        pass

    def OpenServiceA(self, scmanager_handle, ServiceName, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenServiceA(scmanager_handle, ServiceName, access_mask) -> handle """
        pass

    def OpenServiceW(self, scmanager_handle, ServiceName, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenServiceW(scmanager_handle, ServiceName, access_mask) -> handle """
        pass

    def QueryServiceConfig2A(self, handle, info_level, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceConfig2A(handle, info_level, offered) -> (buffer, needed) """
        pass

    def QueryServiceConfig2W(self, handle, info_level, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceConfig2W(handle, info_level, offered) -> (buffer, needed) """
        pass

    def QueryServiceConfigA(self, handle, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceConfigA(handle, offered) -> (query, needed) """
        pass

    def QueryServiceConfigW(self, handle, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceConfigW(handle, offered) -> (query, needed) """
        pass

    def QueryServiceLockStatusA(self, handle, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceLockStatusA(handle, offered) -> (lock_status, needed) """
        pass

    def QueryServiceLockStatusW(self, handle, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceLockStatusW(handle, offered) -> (lock_status, needed) """
        pass

    def QueryServiceObjectSecurity(self, handle, security_flags, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceObjectSecurity(handle, security_flags, offered) -> (buffer, needed) """
        pass

    def QueryServiceStatus(self, handle): # real signature unknown; restored from __doc__
        """ S.QueryServiceStatus(handle) -> service_status """
        pass

    def QueryServiceStatusEx(self, handle, info_level, offered): # real signature unknown; restored from __doc__
        """ S.QueryServiceStatusEx(handle, info_level, offered) -> (buffer, needed) """
        pass

    def SCSetServiceBitsA(self, handle, bits, bitson, immediate): # real signature unknown; restored from __doc__
        """ S.SCSetServiceBitsA(handle, bits, bitson, immediate) -> None """
        pass

    def SCSetServiceBitsW(self, handle, bits, bitson, immediate): # real signature unknown; restored from __doc__
        """ S.SCSetServiceBitsW(handle, bits, bitson, immediate) -> None """
        pass

    def SetServiceObjectSecurity(self, handle, security_flags, buffer): # real signature unknown; restored from __doc__
        """ S.SetServiceObjectSecurity(handle, security_flags, buffer) -> None """
        pass

    def StartServiceA(self, handle, NumArgs, Arguments): # real signature unknown; restored from __doc__
        """ S.StartServiceA(handle, NumArgs, Arguments) -> None """
        pass

    def StartServiceW(self, handle, Arguments): # real signature unknown; restored from __doc__
        """ S.StartServiceW(handle, Arguments) -> None """
        pass

    def UnlockServiceDatabase(self, lock): # real signature unknown; restored from __doc__
        """ S.UnlockServiceDatabase(lock) -> lock """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


