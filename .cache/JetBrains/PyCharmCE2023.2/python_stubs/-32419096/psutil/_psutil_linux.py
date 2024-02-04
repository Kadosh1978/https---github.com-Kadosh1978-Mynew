# encoding: utf-8
# module psutil._psutil_linux
# from /usr/lib/python3/dist-packages/psutil/_psutil_linux.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# Variables with simple values

DUPLEX_FULL = 1
DUPLEX_HALF = 0
DUPLEX_UNKNOWN = 255

version = 590

# functions

def disk_partitions(*args, **kwargs): # real signature unknown
    """ Return disk mounted partitions as a list of tuples including device, mount point and filesystem type """
    pass

def linux_sysinfo(*args, **kwargs): # real signature unknown
    """ A wrapper around sysinfo(), return system memory usage statistics """
    pass

def net_if_duplex_speed(*args, **kwargs): # real signature unknown
    """ Return duplex and speed info about a NIC """
    pass

def proc_cpu_affinity_get(*args, **kwargs): # real signature unknown
    """ Return process CPU affinity as a Python long (the bitmask). """
    pass

def proc_cpu_affinity_set(*args, **kwargs): # real signature unknown
    """ Set process CPU affinity; expects a bitmask. """
    pass

def proc_ioprio_get(*args, **kwargs): # real signature unknown
    """ Get process I/O priority """
    pass

def proc_ioprio_set(*args, **kwargs): # real signature unknown
    """ Set process I/O priority """
    pass

def set_debug(*args, **kwargs): # real signature unknown
    """ Enable or disable PSUTIL_DEBUG messages """
    pass

def users(*args, **kwargs): # real signature unknown
    """ Return currently connected users as a list of tuples """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211ca7310>'

__spec__ = None # (!) real value is "ModuleSpec(name='psutil._psutil_linux', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211ca7310>, origin='/usr/lib/python3/dist-packages/psutil/_psutil_linux.cpython-310-x86_64-linux-gnu.so')"

