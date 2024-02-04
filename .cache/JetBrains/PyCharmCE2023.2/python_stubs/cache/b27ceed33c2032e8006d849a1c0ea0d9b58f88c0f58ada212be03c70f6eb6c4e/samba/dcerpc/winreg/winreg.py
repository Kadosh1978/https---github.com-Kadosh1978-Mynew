# encoding: utf-8
# module samba.dcerpc.winreg
# from /usr/lib/python3/dist-packages/samba/dcerpc/winreg.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" winreg DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class winreg(__dcerpc.ClientConnection):
    """
    winreg(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    Remote Registry Service
    """
    def AbortSystemShutdown(self, server): # real signature unknown; restored from __doc__
        """ S.AbortSystemShutdown(server) -> None """
        pass

    def CloseKey(self, handle): # real signature unknown; restored from __doc__
        """ S.CloseKey(handle) -> handle """
        pass

    def CreateKey(self, handle, name, keyclass, options, access_mask, secdesc, action_taken): # real signature unknown; restored from __doc__
        """ S.CreateKey(handle, name, keyclass, options, access_mask, secdesc, action_taken) -> (new_handle, action_taken) """
        pass

    def DeleteKey(self, handle, key): # real signature unknown; restored from __doc__
        """ S.DeleteKey(handle, key) -> None """
        pass

    def DeleteKeyEx(self, handle, key, access_mask, reserved): # real signature unknown; restored from __doc__
        """ S.DeleteKeyEx(handle, key, access_mask, reserved) -> None """
        pass

    def DeleteValue(self, handle, value): # real signature unknown; restored from __doc__
        """ S.DeleteValue(handle, value) -> None """
        pass

    def EnumKey(self, handle, enum_index, name, keyclass, last_changed_time): # real signature unknown; restored from __doc__
        """ S.EnumKey(handle, enum_index, name, keyclass, last_changed_time) -> (name, keyclass, last_changed_time) """
        pass

    def EnumValue(self, handle, enum_index, name, type, value, size, length): # real signature unknown; restored from __doc__
        """ S.EnumValue(handle, enum_index, name, type, value, size, length) -> (name, type, value, size, length) """
        pass

    def FlushKey(self, handle): # real signature unknown; restored from __doc__
        """ S.FlushKey(handle) -> None """
        pass

    def GetKeySecurity(self, handle, sec_info, sd): # real signature unknown; restored from __doc__
        """ S.GetKeySecurity(handle, sec_info, sd) -> sd """
        pass

    def GetVersion(self, handle): # real signature unknown; restored from __doc__
        """ S.GetVersion(handle) -> version """
        pass

    def InitiateSystemShutdown(self, hostname, message, timeout, force_apps, do_reboot): # real signature unknown; restored from __doc__
        """ S.InitiateSystemShutdown(hostname, message, timeout, force_apps, do_reboot) -> None """
        pass

    def InitiateSystemShutdownEx(self, hostname, message, timeout, force_apps, do_reboot, reason): # real signature unknown; restored from __doc__
        """ S.InitiateSystemShutdownEx(hostname, message, timeout, force_apps, do_reboot, reason) -> None """
        pass

    def LoadKey(self, handle, keyname, filename): # real signature unknown; restored from __doc__
        """ S.LoadKey(handle, keyname, filename) -> None """
        pass

    def NotifyChangeKeyValue(self, handle, watch_subtree, notify_filter, unknown, string1, string2, unknown2): # real signature unknown; restored from __doc__
        """ S.NotifyChangeKeyValue(handle, watch_subtree, notify_filter, unknown, string1, string2, unknown2) -> None """
        pass

    def OpenHKCC(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKCC(system_name, access_mask) -> handle """
        pass

    def OpenHKCR(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKCR(system_name, access_mask) -> handle """
        pass

    def OpenHKCU(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKCU(system_name, access_mask) -> handle """
        pass

    def OpenHKDD(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKDD(system_name, access_mask) -> handle """
        pass

    def OpenHKLM(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKLM(system_name, access_mask) -> handle """
        pass

    def OpenHKPD(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKPD(system_name, access_mask) -> handle """
        pass

    def OpenHKPN(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKPN(system_name, access_mask) -> handle """
        pass

    def OpenHKPT(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKPT(system_name, access_mask) -> handle """
        pass

    def OpenHKU(self, system_name, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenHKU(system_name, access_mask) -> handle """
        pass

    def OpenKey(self, parent_handle, keyname, options, access_mask): # real signature unknown; restored from __doc__
        """ S.OpenKey(parent_handle, keyname, options, access_mask) -> handle """
        pass

    def QueryInfoKey(self, handle, classname): # real signature unknown; restored from __doc__
        """ S.QueryInfoKey(handle, classname) -> (classname, num_subkeys, max_subkeylen, max_classlen, num_values, max_valnamelen, max_valbufsize, secdescsize, last_changed_time) """
        pass

    def QueryMultipleValues(self, key_handle, values_in, buffer): # real signature unknown; restored from __doc__
        """ S.QueryMultipleValues(key_handle, values_in, buffer) -> (values_out, buffer) """
        pass

    def QueryMultipleValues2(self, key_handle, values_in, buffer): # real signature unknown; restored from __doc__
        """ S.QueryMultipleValues2(key_handle, values_in, buffer) -> (values_out, buffer, needed) """
        pass

    def QueryValue(self, handle, value_name, type, data, data_size, data_length): # real signature unknown; restored from __doc__
        """ S.QueryValue(handle, value_name, type, data, data_size, data_length) -> (type, data, data_size, data_length) """
        pass

    def ReplaceKey(self, handle, subkey, new_file, old_file): # real signature unknown; restored from __doc__
        """ S.ReplaceKey(handle, subkey, new_file, old_file) -> None """
        pass

    def RestoreKey(self, handle, filename, flags): # real signature unknown; restored from __doc__
        """ S.RestoreKey(handle, filename, flags) -> None """
        pass

    def SaveKey(self, handle, filename, sec_attrib): # real signature unknown; restored from __doc__
        """ S.SaveKey(handle, filename, sec_attrib) -> None """
        pass

    def SaveKeyEx(self, handle, filename, sec_attrib, flags): # real signature unknown; restored from __doc__
        """ S.SaveKeyEx(handle, filename, sec_attrib, flags) -> None """
        pass

    def SetKeySecurity(self, handle, sec_info, sd): # real signature unknown; restored from __doc__
        """ S.SetKeySecurity(handle, sec_info, sd) -> None """
        pass

    def SetValue(self, handle, name, type, data): # real signature unknown; restored from __doc__
        """ S.SetValue(handle, name, type, data) -> None """
        pass

    def UnLoadKey(self, handle, subkey): # real signature unknown; restored from __doc__
        """ S.UnLoadKey(handle, subkey) -> None """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


