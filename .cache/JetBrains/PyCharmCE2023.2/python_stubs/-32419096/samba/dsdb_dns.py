# encoding: utf-8
# module samba.dsdb_dns
# from /usr/lib/python3/dist-packages/samba/dsdb_dns.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" Python bindings for the DNS objects in the directory service databases. """
# no imports

# functions

def dns_timestamp_to_nt_time(*args, **kwargs): # real signature unknown
    """ Convert a dns timestamp to an NTTIME value """
    pass

def extract(*args, **kwargs): # real signature unknown
    """ Return the DNS database entry as a python structure from an Ldb.MessageElement of type dnsRecord """
    pass

def lookup(*args, **kwargs): # real signature unknown
    """ Get the DNS database entries for a DNS name """
    pass

def records_match(*args, **kwargs): # real signature unknown
    """ Decide whether two records match, according to dns update rules """
    pass

def replace(*args, **kwargs): # real signature unknown
    """ Replace the DNS database entries for a DNS name """
    pass

def replace_by_dn(*args, **kwargs): # real signature unknown
    """ Replace the DNS database entries for a LDB DN """
    pass

def unix_to_dns_timestamp(*args, **kwargs): # real signature unknown
    """ Convert a time.time() value to a dns timestamp (hours since 1601) """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d570>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dsdb_dns', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d570>, origin='/usr/lib/python3/dist-packages/samba/dsdb_dns.cpython-310-x86_64-linux-gnu.so')"

