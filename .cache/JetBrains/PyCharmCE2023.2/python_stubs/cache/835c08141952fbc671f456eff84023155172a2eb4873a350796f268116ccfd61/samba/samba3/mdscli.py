# encoding: utf-8
# module samba.samba3.mdscli
# from /usr/lib/python3/dist-packages/samba/samba3/mdscli.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" RPC mdssvc client """

# imports
import talloc as __talloc


# no functions
# classes

class conn(__talloc.BaseObject):
    """ conn([....]) -> mdssvc connection """
    def disconnect(self, *more): # real signature unknown; restored from __doc__
        """ mdscli.conn.disconnect(...) -> disconnect """
        pass

    def search(self, *more): # real signature unknown; restored from __doc__
        """ mdscli.conn.search(...) -> run mdssvc query """
        pass

    def sharepath(self, *more): # real signature unknown; restored from __doc__
        """ mdscli.conn.sharepath(...) -> get share basepath """
        pass

    def __init__(self, *some): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class search(__talloc.BaseObject):
    """ search([....]) -> mdssvc client search context """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def get_results(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *some): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d39660>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.samba3.mdscli', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d39660>, origin='/usr/lib/python3/dist-packages/samba/samba3/mdscli.cpython-310-x86_64-linux-gnu.so')"

