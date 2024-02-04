# encoding: utf-8
# module samba.net_s3 calls itself net
# from /usr/lib/python3/dist-packages/samba/net_s3.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# no functions
# classes

class Net(object):
    # no doc
    def join_member(self, dnshostname, createupn, createcomputer, osName, osVer, osServicePack, machinepass): # real signature unknown; restored from __doc__
        """
        join_member(dnshostname, createupn, createcomputer, osName, osVer, osServicePack, machinepass) -> (domain_sid, domain_name)
        
        Join the domain with the specified name.
        """
        pass

    def leave(self, keepAccount): # real signature unknown; restored from __doc__
        """
        leave(keepAccount) -> success
        
        Leave the joined domain.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d540>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.net_s3', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d540>, origin='/usr/lib/python3/dist-packages/samba/net_s3.cpython-310-x86_64-linux-gnu.so')"

