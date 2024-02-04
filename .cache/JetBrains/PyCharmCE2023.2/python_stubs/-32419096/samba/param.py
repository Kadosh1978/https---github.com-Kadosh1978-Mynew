# encoding: utf-8
# module samba.param
# from /usr/lib/python3/dist-packages/samba/param.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" Parsing and writing Samba configuration files. """

# imports
import talloc as __talloc


# functions

def bin_dir(*args, **kwargs): # real signature unknown
    """ Returns the compiled in BINDIR. """
    pass

def data_dir(*args, **kwargs): # real signature unknown
    """ Returns the compiled in location of data directory. """
    pass

def default_path(*args, **kwargs): # real signature unknown
    """ Returns the default smb.conf path. """
    pass

def modules_dir(*args, **kwargs): # real signature unknown
    """ Returns the compiled in location of modules. """
    pass

def sbin_dir(*args, **kwargs): # real signature unknown
    """ Returns the compiled in SBINDIR. """
    pass

def setup_dir(*args, **kwargs): # real signature unknown
    """ Returns the compiled in location of provision templates. """
    pass

# classes

class LoadParm(__talloc.BaseObject):
    # no doc
    def cache_path(self, name): # real signature unknown; restored from __doc__
        """
        S.cache_path(name) -> string
        Returns a path in the Samba cache directory.
        """
        return ""

    def dump(self, show_defaults=False, file_name='', mode='w'): # real signature unknown; restored from __doc__
        """ S.dump(show_defaults=False, file_name='', mode='w') """
        pass

    def dump_a_parameter(self, name, service_name, file_name='', mode='w'): # real signature unknown; restored from __doc__
        """ S.dump_a_parameter(name, service_name, file_name='', mode='w') """
        pass

    def get(self, name, service_name): # real signature unknown; restored from __doc__
        """
        S.get(name, service_name) -> value
        Find specified parameter.
        """
        pass

    def is_mydomain(self, name): # real signature unknown; restored from __doc__
        """
        S.is_mydomain(name) -> bool
        Check whether the specified name matches our domain name.
        """
        return False

    def is_myname(self, name): # real signature unknown; restored from __doc__
        """
        S.is_myname(name) -> bool
        Check whether the specified name matches one of our netbios names.
        """
        return False

    def load(self, filename): # real signature unknown; restored from __doc__
        """
        S.load(filename) -> None
        Load specified file.
        """
        pass

    def load_default(self): # real signature unknown; restored from __doc__
        """
        S.load_default() -> None
        Load default smb.conf file.
        """
        pass

    def log_level(self): # real signature unknown; restored from __doc__
        """
        S.log_level() -> int
         Get the active log level
        """
        return 0

    def private_path(self, name): # real signature unknown; restored from __doc__
        """ S.private_path(name) -> path """
        pass

    def samdb_url(self): # real signature unknown; restored from __doc__
        """
        S.samdb_url() -> string
        Returns the current URL for sam.ldb.
        """
        return ""

    def server_role(self): # real signature unknown; restored from __doc__
        """
        S.server_role() -> value
        Get the server role.
        """
        pass

    def services(self): # real signature unknown; restored from __doc__
        """ S.services() -> list """
        return []

    def set(self, name, value): # real signature unknown; restored from __doc__
        """
        S.set(name, value) -> bool
        Change a parameter.
        """
        return False

    def state_path(self, name): # real signature unknown; restored from __doc__
        """
        S.state_path(name) -> string
        Returns a path in the Samba state directory.
        """
        return ""

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    configfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of last config file that was loaded."""

    default_service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weak_crypto = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If weak crypto is allowed."""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d030>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.param', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d030>, origin='/usr/lib/python3/dist-packages/samba/param.cpython-310-x86_64-linux-gnu.so')"

