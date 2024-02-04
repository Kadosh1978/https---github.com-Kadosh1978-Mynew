# encoding: utf-8
# module samba.gpo
# from /usr/lib/python3/dist-packages/samba/gpo.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" libgpo python bindings """

# imports
import talloc as __talloc


# Variables with simple values

version = '4.15.13-Ubuntu'

# functions

def gpo_get_sysvol_gpt_version(*args, **kwargs): # real signature unknown
    pass

# classes

class ADS_STRUCT(object):
    """ ADS struct """
    def connect(self, *args, **kwargs): # real signature unknown
        """ Connect to the LDAP server """
        pass

    def get_gpo_list(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class GROUP_POLICY_OBJECT(__talloc.BaseObject):
    """ GROUP_POLICY_OBJECT """
    def get_unix_path(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    display_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ds_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_sys_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    link = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    machine_extensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_extensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d570>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.gpo', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d570>, origin='/usr/lib/python3/dist-packages/samba/gpo.cpython-310-x86_64-linux-gnu.so')"

