# encoding: utf-8
# module samba.samba3.libsmb_samba_cwrapper
# from /usr/lib/python3/dist-packages/samba/samba3/libsmb_samba_cwrapper.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" libsmb wrapper """
# no imports

# Variables with simple values

FILE_ATTRIBUTE_ALL_MASK = 32767

FILE_ATTRIBUTE_ARCHIVE = 32
FILE_ATTRIBUTE_COMPRESSED = 2048
FILE_ATTRIBUTE_DEVICE = 64
FILE_ATTRIBUTE_DIRECTORY = 16
FILE_ATTRIBUTE_ENCRYPTED = 16384
FILE_ATTRIBUTE_HIDDEN = 2
FILE_ATTRIBUTE_NONINDEXED = 8192
FILE_ATTRIBUTE_NORMAL = 128
FILE_ATTRIBUTE_OFFLINE = 4096
FILE_ATTRIBUTE_READONLY = 1

FILE_ATTRIBUTE_REPARSE_POINT = 1024

FILE_ATTRIBUTE_SPARSE = 512
FILE_ATTRIBUTE_SYSTEM = 4
FILE_ATTRIBUTE_TEMPORARY = 256
FILE_ATTRIBUTE_VOLUME = 8

FILE_NOTIFY_CHANGE_ALL = 4095
FILE_NOTIFY_CHANGE_ATTRIBUTES = 4
FILE_NOTIFY_CHANGE_CREATION = 64

FILE_NOTIFY_CHANGE_DIR_NAME = 2

FILE_NOTIFY_CHANGE_EA = 128

FILE_NOTIFY_CHANGE_FILE_NAME = 1

FILE_NOTIFY_CHANGE_LAST_ACCESS = 32
FILE_NOTIFY_CHANGE_LAST_WRITE = 16

FILE_NOTIFY_CHANGE_NAME = 3
FILE_NOTIFY_CHANGE_SECURITY = 256
FILE_NOTIFY_CHANGE_SIZE = 8

FILE_NOTIFY_CHANGE_STREAM_NAME = 512
FILE_NOTIFY_CHANGE_STREAM_SIZE = 1024
FILE_NOTIFY_CHANGE_STREAM_WRITE = 2048

FILE_SHARE_DELETE = 4
FILE_SHARE_READ = 1
FILE_SHARE_WRITE = 2

NOTIFY_ACTION_ADDED = 1

NOTIFY_ACTION_ADDED_STREAM = 6

NOTIFY_ACTION_MODIFIED = 3

NOTIFY_ACTION_MODIFIED_STREAM = 8

NOTIFY_ACTION_NEW_NAME = 5

NOTIFY_ACTION_OLD_NAME = 4

NOTIFY_ACTION_REMOVED = 2

NOTIFY_ACTION_REMOVED_STREAM = 7

# no functions
# classes

class LibsmbCConn(object):
    """ libsmb cwrapper connection """
    def chkpath(self, dir_path): # real signature unknown; restored from __doc__
        """
        chkpath(dir_path) -> True or False
        
        		Return true if directory exists, false otherwise.
        """
        return False

    def close(self, *args, **kwargs): # real signature unknown
        """ Close a file handle """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        """ Open a file """
        pass

    def delete_on_close(self, *args, **kwargs): # real signature unknown
        """ Set/Reset the delete on close flag """
        pass

    def echo(self, *args, **kwargs): # real signature unknown
        """ Ping the server connection """
        pass

    def get_oplock_break(self, *args, **kwargs): # real signature unknown
        """ Wait for an oplock break """
        pass

    def get_sd(self, fnum, security_info=0): # real signature unknown; restored from __doc__
        """
        get_sd(fnum[, security_info=0]) -> security_descriptor object
        
        		Get security descriptor for opened file.
        """
        pass

    def list(self, directory, mask='*', attribs=None): # real signature unknown; restored from __doc__
        """
        list(directory, mask='*', attribs=DEFAULT_ATTRS) -> directory contents as a dictionary
        		DEFAULT_ATTRS: FILE_ATTRIBUTE_SYSTEM | FILE_ATTRIBUTE_DIRECTORY | FILE_ATTRIBUTE_ARCHIVE
        
        		List contents of a directory. The keys are, 
        			name: Long name of the directory item
        			short_name: Short name of the directory item
        			size: File size in bytes
        			attrib: Attributes
        			mtime: Modification time
        """
        pass

    def loadfile(self, path): # real signature unknown; restored from __doc__
        """
        loadfile(path) -> file contents as a bytes object
        
        		Read contents of a file.
        """
        pass

    def mkdir(self, path): # real signature unknown; restored from __doc__
        """
        mkdir(path) -> None
        
         		Create a directory.
        """
        pass

    def notify(self, fnum, buffer_size, completion_filter___): # real signature unknown; restored from __doc__
        """
        Wait for change notifications: 
        notify(fnum, buffer_size, completion_filter...) -> libsmb_samba_internal.Notify request handle
        """
        pass

    def posix_whoami(self): # real signature unknown; restored from __doc__
        """ posix_whoami() -> (uid, gid, gids, sids, guest) """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """ Read from a file handle """
        pass

    def rename(self, src, dst): # real signature unknown; restored from __doc__
        """
        rename(src,dst) -> None
        
         		Rename a file.
        """
        pass

    def rmdir(self, path): # real signature unknown; restored from __doc__
        """
        rmdir(path) -> None
        
         		Delete a directory.
        """
        pass

    def savefile(self, path, bytes): # real signature unknown; restored from __doc__
        """
        savefile(path, bytes) -> None
        
        		Write bytes to file.
        """
        pass

    def settimeout(self, new_timeout_msecs): # real signature unknown; restored from __doc__
        """ settimeout(new_timeout_msecs) => return old_timeout_msecs """
        pass

    def set_sd(self, fnum, security_descriptor, security_info=0): # real signature unknown; restored from __doc__
        """
        set_sd(fnum, security_descriptor[, security_info=0]) -> None
        
        		Set security descriptor for opened file.
        """
        pass

    def truncate(self, *args, **kwargs): # real signature unknown
        """ Truncate a file """
        pass

    def unlink(self, path): # real signature unknown; restored from __doc__
        """
        unlink(path) -> None
        
         		Delete a file.
        """
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """ Write to a file handle """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d39660>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.samba3.libsmb_samba_cwrapper', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d39660>, origin='/usr/lib/python3/dist-packages/samba/samba3/libsmb_samba_cwrapper.cpython-310-x86_64-linux-gnu.so')"

