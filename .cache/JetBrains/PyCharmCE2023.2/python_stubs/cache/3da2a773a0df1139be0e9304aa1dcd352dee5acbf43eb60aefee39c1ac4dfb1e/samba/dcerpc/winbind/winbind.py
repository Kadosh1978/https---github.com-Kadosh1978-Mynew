# encoding: utf-8
# module samba.dcerpc.winbind
# from /usr/lib/python3/dist-packages/samba/dcerpc/winbind.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" winbind DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class winbind(__dcerpc.ClientConnection):
    """
    winbind(binding, lp_ctx=None, credentials=None) -> connection
    
    binding should be a DCE/RPC binding string (for example: ncacn_ip_tcp:127.0.0.1)
    lp_ctx should be a path to a smb.conf file or a param.LoadParm object
    credentials should be a credentials.Credentials object.
    
    winbind parent-child protocol
    """
    def DsrUpdateReadOnlyServerDnsRecords(self, site_name, dns_ttl, dns_names): # real signature unknown; restored from __doc__
        """ S.DsrUpdateReadOnlyServerDnsRecords(site_name, dns_ttl, dns_names) -> dns_names """
        pass

    def GetForestTrustInformation(self, trusted_domain_name, flags): # real signature unknown; restored from __doc__
        """ S.GetForestTrustInformation(trusted_domain_name, flags) -> forest_trust_info """
        pass

    def LogonControl(self, function_code, level, data): # real signature unknown; restored from __doc__
        """ S.LogonControl(function_code, level, data) -> query """
        pass

    def SamLogon(self, logon_level, logon, validation_level): # real signature unknown; restored from __doc__
        """ S.SamLogon(logon_level, logon, validation_level) -> (validation, authoritative) """
        pass

    def SendToSam(self, message): # real signature unknown; restored from __doc__
        """ S.SendToSam(message) -> None """
        pass

    def wbint_AllocateGid(self): # real signature unknown; restored from __doc__
        """ S.wbint_AllocateGid() -> gid """
        pass

    def wbint_AllocateUid(self): # real signature unknown; restored from __doc__
        """ S.wbint_AllocateUid() -> uid """
        pass

    def wbint_ChangeMachineAccount(self): # real signature unknown; restored from __doc__
        """ S.wbint_ChangeMachineAccount() -> None """
        pass

    def wbint_CheckMachineAccount(self): # real signature unknown; restored from __doc__
        """ S.wbint_CheckMachineAccount() -> None """
        pass

    def wbint_DsGetDcName(self, domain_name, domain_guid, site_name, flags): # real signature unknown; restored from __doc__
        """ S.wbint_DsGetDcName(domain_name, domain_guid, site_name, flags) -> dc_info """
        pass

    def wbint_GetNssInfo(self, info): # real signature unknown; restored from __doc__
        """ S.wbint_GetNssInfo(info) -> info """
        pass

    def wbint_LookupGroupMembers(self, sid, type): # real signature unknown; restored from __doc__
        """ S.wbint_LookupGroupMembers(sid, type) -> members """
        pass

    def wbint_LookupName(self, domain, name, flags): # real signature unknown; restored from __doc__
        """ S.wbint_LookupName(domain, name, flags) -> (type, sid) """
        pass

    def wbint_LookupRids(self, domain_sid, rids): # real signature unknown; restored from __doc__
        """ S.wbint_LookupRids(domain_sid, rids) -> (domain_name, names) """
        pass

    def wbint_LookupSid(self, sid): # real signature unknown; restored from __doc__
        """ S.wbint_LookupSid(sid) -> (type, domain, name) """
        pass

    def wbint_LookupSids(self, sids): # real signature unknown; restored from __doc__
        """ S.wbint_LookupSids(sids) -> (domains, names) """
        pass

    def wbint_LookupUserAliases(self, sids): # real signature unknown; restored from __doc__
        """ S.wbint_LookupUserAliases(sids) -> rids """
        pass

    def wbint_LookupUserGroups(self, sid): # real signature unknown; restored from __doc__
        """ S.wbint_LookupUserGroups(sid) -> sids """
        pass

    def wbint_Ping(self, in_data): # real signature unknown; restored from __doc__
        """ S.wbint_Ping(in_data) -> out_data """
        pass

    def wbint_PingDc(self): # real signature unknown; restored from __doc__
        """ S.wbint_PingDc() -> dcname """
        pass

    def wbint_QueryGroupList(self): # real signature unknown; restored from __doc__
        """ S.wbint_QueryGroupList() -> groups """
        pass

    def wbint_QuerySequenceNumber(self): # real signature unknown; restored from __doc__
        """ S.wbint_QuerySequenceNumber() -> sequence """
        return ()

    def wbint_QueryUserRidList(self): # real signature unknown; restored from __doc__
        """ S.wbint_QueryUserRidList() -> rids """
        pass

    def wbint_Sids2UnixIDs(self, domains, ids): # real signature unknown; restored from __doc__
        """ S.wbint_Sids2UnixIDs(domains, ids) -> ids """
        pass

    def wbint_UnixIDs2Sids(self, domain_name, domain_sid, num_ids, xids): # real signature unknown; restored from __doc__
        """ S.wbint_UnixIDs2Sids(domain_name, domain_sid, num_ids, xids) -> (xids, sids) """
        pass

    def __init__(self, binding, lp_ctx=None, credentials=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


