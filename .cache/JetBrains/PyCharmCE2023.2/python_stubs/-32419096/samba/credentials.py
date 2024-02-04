# encoding: utf-8
# module samba.credentials
# from /usr/lib/python3/dist-packages/samba/credentials.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" Credentials management. """

# imports
import talloc as __talloc


# Variables with simple values

AUTO_KRB_FORWARDABLE = 0

AUTO_USE_KERBEROS = 1

CALLBACK = 2

CALLBACK_RESULT = 5

CLI_CRED_CLEAR_AUTH = 16

CLI_CRED_LANMAN_AUTH = 4

CLI_CRED_NTLM2 = 1

CLI_CRED_NTLMv2_AUTH = 2

CLI_CRED_NTLM_AUTH = 8

DONT_USE_KERBEROS = 0

FORCE_KRB_FORWARDABLE = 2

GUESS_ENV = 3
GUESS_FILE = 4

MUST_USE_KERBEROS = 2

NO_KRB_FORWARDABLE = 1

SMB_CONF = 1

SMB_ENCRYPTION_DEFAULT = -1
SMB_ENCRYPTION_DESIRED = 2

SMB_ENCRYPTION_IF_REQUIRED = 1

SMB_ENCRYPTION_OFF = 0
SMB_ENCRYPTION_REQUIRED = 3

SMB_SIGNING_DEFAULT = -1
SMB_SIGNING_DESIRED = 2

SMB_SIGNING_IF_REQUIRED = 1

SMB_SIGNING_OFF = 0
SMB_SIGNING_REQUIRED = 3

SPECIFIED = 6

UNINITIALISED = 0

# functions

def authentication_requested(*args, **kwargs): # real signature unknown
    pass

def encrypt_netr_crypt_password(password): # real signature unknown; restored from __doc__
    """
    S.encrypt_netr_crypt_password(password) -> NTSTATUS
    Encrypt the supplied password using the session key and
    the negotiated encryption algorithm in place
    i.e. it overwrites the original data
    """
    pass

def get_bind_dn(): # real signature unknown; restored from __doc__
    """
    S.get_bind_dn() -> bind dn
    Obtain bind DN.
    """
    pass

def get_domain(): # real signature unknown; restored from __doc__
    """
    S.get_domain() -> domain
    Obtain domain name.
    """
    pass

def get_forced_sasl_mech(): # real signature unknown; restored from __doc__
    """
    S.get_forced_sasl_mech() -> SASL mechanism
    Obtain forced SASL mechanism.
    """
    pass

def get_gensec_features(*args, **kwargs): # real signature unknown
    pass

def get_kerberos_state(*args, **kwargs): # real signature unknown
    pass

def get_named_ccache(*args, **kwargs): # real signature unknown
    pass

def get_ntlm_response(flags, challenge, target_info=None): # real signature unknown; restored from __doc__
    """
    S.get_ntlm_response(flags, challenge[, target_info]) -> (flags, lm_response, nt_response, lm_session_key, nt_session_key)
    Obtain LM or NTLM response.
    """
    pass

def get_ntlm_username_domain(): # real signature unknown; restored from __doc__
    """
    S.get_ntlm_username_domain() -> (domain, username)
    Obtain NTLM username and domain, split up either as (DOMAIN, user) or ("", "user@realm").
    """
    pass

def get_nt_hash(*args, **kwargs): # real signature unknown
    pass

def get_old_password(): # real signature unknown; restored from __doc__
    """
    S.get_old_password() -> password
    Obtain old password.
    """
    pass

def get_password(): # real signature unknown; restored from __doc__
    """
    S.get_password() -> password
    Obtain password.
    """
    pass

def get_principal(): # real signature unknown; restored from __doc__
    """
    S.get_principal() -> user@realm
    Obtain user principal.
    """
    pass

def get_realm(): # real signature unknown; restored from __doc__
    """
    S.get_realm() -> realm
    Obtain realm name.
    """
    pass

def get_secure_channel_type(*args, **kwargs): # real signature unknown
    pass

def get_smb_encryption(*args, **kwargs): # real signature unknown
    pass

def get_smb_ipc_signing(*args, **kwargs): # real signature unknown
    pass

def get_smb_signing(*args, **kwargs): # real signature unknown
    pass

def get_username(): # real signature unknown; restored from __doc__
    """
    S.get_username() -> username
    Obtain username.
    """
    pass

def get_workstation(*args, **kwargs): # real signature unknown
    pass

def guess(*args, **kwargs): # real signature unknown
    pass

def is_anonymous(*args, **kwargs): # real signature unknown
    pass

def new_client_authenticator(): # real signature unknown; restored from __doc__
    """
    S.new_client_authenticator() -> Authenticator
    Get a new client NETLOGON_AUTHENTICATOR
    """
    pass

def parse_file(filename, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
    """
    S.parse_file(filename[, credentials.SPECIFIED]) -> None
    Parse credentials file.
    """
    pass

def parse_string(text, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
    """
    S.parse_string(text[, credentials.SPECIFIED]) -> None
    Parse credentials string.
    """
    pass

def set_anonymous(): # real signature unknown; restored from __doc__
    """
    S.set_anonymous() -> None
    Use anonymous credentials.
    """
    pass

def set_bind_dn(bind_dn): # real signature unknown; restored from __doc__
    """
    S.set_bind_dn(bind_dn) -> None
    Change bind DN.
    """
    pass

def set_cmdline_callbacks(): # real signature unknown; restored from __doc__
    """
    S.set_cmdline_callbacks() -> bool
    Use command-line to obtain credentials not explicitly set.
    """
    return False

def set_conf(*args, **kwargs): # real signature unknown
    pass

def set_domain(domain, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
    """
    S.set_domain(domain[, credentials.SPECIFIED]) -> None
    Change domain name.
    """
    pass

def set_forced_sasl_mech(name): # real signature unknown; restored from __doc__
    """
    S.set_forced_sasl_mech(name) -> None
    Set forced SASL mechanism.
    """
    pass

def set_gensec_features(*args, **kwargs): # real signature unknown
    pass

def set_kerberos_state(*args, **kwargs): # real signature unknown
    pass

def set_krb_forwardable(*args, **kwargs): # real signature unknown
    pass

def set_machine_account(*args, **kwargs): # real signature unknown
    pass

def set_named_ccache(krb5_ccache_name, obtained, lp): # real signature unknown; restored from __doc__
    """
    S.set_named_ccache(krb5_ccache_name, obtained, lp) -> None
    Set credentials to KRB5 Credentials Cache (by name).
    """
    pass

def set_old_password(password, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
    """
    S.set_old_password(password[, credentials.SPECIFIED]) -> None
    Change old password.
    """
    pass

def set_old_utf16_password(password, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
    """
    S.set_old_utf16_password(password[, credentials.SPECIFIED]) -> None
    Change old password.
    """
    pass

def set_password(password, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
    """
    S.set_password(password[, credentials.SPECIFIED]) -> None
    Change password.
    """
    pass

def set_password_will_be_nt_hash(bool): # real signature unknown; restored from __doc__
    """
    S.set_password_will_be_nt_hash(bool) -> None
    Alters the behaviour of S.set_password() to expect the NTHASH as hexstring.
    """
    pass

def set_principal(name, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
    """
    S.set_principal(name[, credentials.SPECIFIED]) -> None
    Change principal.
    """
    pass

def set_realm(realm, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
    """
    S.set_realm(realm[, credentials.SPECIFIED]) -> None
    Change realm name.
    """
    pass

def set_secure_channel_type(*args, **kwargs): # real signature unknown
    pass

def set_smb_encryption(*args, **kwargs): # real signature unknown
    pass

def set_smb_ipc_signing(*args, **kwargs): # real signature unknown
    pass

def set_smb_signing(*args, **kwargs): # real signature unknown
    pass

def set_username(name, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
    """
    S.set_username(name[, credentials.SPECIFIED]) -> None
    Change username.
    """
    pass

def set_utf16_password(password, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
    """
    S.set_utf16_password(password[, credentials.SPECIFIED]) -> None
    Change password.
    """
    pass

def set_workstation(*args, **kwargs): # real signature unknown
    pass

def wrong_password(): # real signature unknown; restored from __doc__
    """
    S.wrong_password() -> bool
    Indicate the returned password was incorrect.
    """
    return False

# classes

class CredentialCacheContainer(__talloc.BaseObject):
    # no doc
    def get_name(self): # real signature unknown; restored from __doc__
        """
        S.get_name() -> name
        Obtain KRB5 credentials cache name.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Credentials(__talloc.BaseObject):
    # no doc
    def authentication_requested(self, *args, **kwargs): # real signature unknown
        pass

    def encrypt_netr_crypt_password(self, password): # real signature unknown; restored from __doc__
        """
        S.encrypt_netr_crypt_password(password) -> NTSTATUS
        Encrypt the supplied password using the session key and
        the negotiated encryption algorithm in place
        i.e. it overwrites the original data
        """
        pass

    def get_bind_dn(self): # real signature unknown; restored from __doc__
        """
        S.get_bind_dn() -> bind dn
        Obtain bind DN.
        """
        pass

    def get_domain(self): # real signature unknown; restored from __doc__
        """
        S.get_domain() -> domain
        Obtain domain name.
        """
        pass

    def get_forced_sasl_mech(self): # real signature unknown; restored from __doc__
        """
        S.get_forced_sasl_mech() -> SASL mechanism
        Obtain forced SASL mechanism.
        """
        pass

    def get_gensec_features(self, *args, **kwargs): # real signature unknown
        pass

    def get_kerberos_state(self, *args, **kwargs): # real signature unknown
        pass

    def get_named_ccache(self, *args, **kwargs): # real signature unknown
        pass

    def get_ntlm_response(self, flags, challenge, target_info=None): # real signature unknown; restored from __doc__
        """
        S.get_ntlm_response(flags, challenge[, target_info]) -> (flags, lm_response, nt_response, lm_session_key, nt_session_key)
        Obtain LM or NTLM response.
        """
        pass

    def get_ntlm_username_domain(self): # real signature unknown; restored from __doc__
        """
        S.get_ntlm_username_domain() -> (domain, username)
        Obtain NTLM username and domain, split up either as (DOMAIN, user) or ("", "user@realm").
        """
        pass

    def get_nt_hash(self, *args, **kwargs): # real signature unknown
        pass

    def get_old_password(self): # real signature unknown; restored from __doc__
        """
        S.get_old_password() -> password
        Obtain old password.
        """
        pass

    def get_password(self): # real signature unknown; restored from __doc__
        """
        S.get_password() -> password
        Obtain password.
        """
        pass

    def get_principal(self): # real signature unknown; restored from __doc__
        """
        S.get_principal() -> user@realm
        Obtain user principal.
        """
        pass

    def get_realm(self): # real signature unknown; restored from __doc__
        """
        S.get_realm() -> realm
        Obtain realm name.
        """
        pass

    def get_secure_channel_type(self, *args, **kwargs): # real signature unknown
        pass

    def get_smb_encryption(self, *args, **kwargs): # real signature unknown
        pass

    def get_smb_ipc_signing(self, *args, **kwargs): # real signature unknown
        pass

    def get_smb_signing(self, *args, **kwargs): # real signature unknown
        pass

    def get_username(self): # real signature unknown; restored from __doc__
        """
        S.get_username() -> username
        Obtain username.
        """
        pass

    def get_workstation(self, *args, **kwargs): # real signature unknown
        pass

    def guess(self, *args, **kwargs): # real signature unknown
        pass

    def is_anonymous(self, *args, **kwargs): # real signature unknown
        pass

    def new_client_authenticator(self): # real signature unknown; restored from __doc__
        """
        S.new_client_authenticator() -> Authenticator
        Get a new client NETLOGON_AUTHENTICATOR
        """
        pass

    def parse_file(self, filename, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
        """
        S.parse_file(filename[, credentials.SPECIFIED]) -> None
        Parse credentials file.
        """
        pass

    def parse_string(self, text, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
        """
        S.parse_string(text[, credentials.SPECIFIED]) -> None
        Parse credentials string.
        """
        pass

    def set_anonymous(self): # real signature unknown; restored from __doc__
        """
        S.set_anonymous() -> None
        Use anonymous credentials.
        """
        pass

    def set_bind_dn(self, bind_dn): # real signature unknown; restored from __doc__
        """
        S.set_bind_dn(bind_dn) -> None
        Change bind DN.
        """
        pass

    def set_cmdline_callbacks(self): # real signature unknown; restored from __doc__
        """
        S.set_cmdline_callbacks() -> bool
        Use command-line to obtain credentials not explicitly set.
        """
        return False

    def set_conf(self, *args, **kwargs): # real signature unknown
        pass

    def set_domain(self, domain, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
        """
        S.set_domain(domain[, credentials.SPECIFIED]) -> None
        Change domain name.
        """
        pass

    def set_forced_sasl_mech(self, name): # real signature unknown; restored from __doc__
        """
        S.set_forced_sasl_mech(name) -> None
        Set forced SASL mechanism.
        """
        pass

    def set_gensec_features(self, *args, **kwargs): # real signature unknown
        pass

    def set_kerberos_state(self, *args, **kwargs): # real signature unknown
        pass

    def set_krb_forwardable(self, *args, **kwargs): # real signature unknown
        pass

    def set_machine_account(self, *args, **kwargs): # real signature unknown
        pass

    def set_named_ccache(self, krb5_ccache_name, obtained, lp): # real signature unknown; restored from __doc__
        """
        S.set_named_ccache(krb5_ccache_name, obtained, lp) -> None
        Set credentials to KRB5 Credentials Cache (by name).
        """
        pass

    def set_old_password(self, password, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
        """
        S.set_old_password(password[, credentials.SPECIFIED]) -> None
        Change old password.
        """
        pass

    def set_old_utf16_password(self, password, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
        """
        S.set_old_utf16_password(password[, credentials.SPECIFIED]) -> None
        Change old password.
        """
        pass

    def set_password(self, password, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
        """
        S.set_password(password[, credentials.SPECIFIED]) -> None
        Change password.
        """
        pass

    def set_password_will_be_nt_hash(self, bool): # real signature unknown; restored from __doc__
        """
        S.set_password_will_be_nt_hash(bool) -> None
        Alters the behaviour of S.set_password() to expect the NTHASH as hexstring.
        """
        pass

    def set_principal(self, name, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
        """
        S.set_principal(name[, credentials.SPECIFIED]) -> None
        Change principal.
        """
        pass

    def set_realm(self, realm, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
        """
        S.set_realm(realm[, credentials.SPECIFIED]) -> None
        Change realm name.
        """
        pass

    def set_secure_channel_type(self, *args, **kwargs): # real signature unknown
        pass

    def set_smb_encryption(self, *args, **kwargs): # real signature unknown
        pass

    def set_smb_ipc_signing(self, *args, **kwargs): # real signature unknown
        pass

    def set_smb_signing(self, *args, **kwargs): # real signature unknown
        pass

    def set_username(self, name, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
        """
        S.set_username(name[, credentials.SPECIFIED]) -> None
        Change username.
        """
        pass

    def set_utf16_password(self, password, credentials_SPECIFIED=None): # real signature unknown; restored from __doc__
        """
        S.set_utf16_password(password[, credentials.SPECIFIED]) -> None
        Change password.
        """
        pass

    def set_workstation(self, *args, **kwargs): # real signature unknown
        pass

    def wrong_password(self): # real signature unknown; restored from __doc__
        """
        S.wrong_password() -> bool
        Indicate the returned password was incorrect.
        """
        return False

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d570>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.credentials', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d570>, origin='/usr/lib/python3/dist-packages/samba/credentials.cpython-310-x86_64-linux-gnu.so')"

