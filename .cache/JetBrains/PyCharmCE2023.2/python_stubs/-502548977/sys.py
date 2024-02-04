# encoding: utf-8
# module sys
# from (built-in)
# by generator 1.147
"""
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules

displayhook -- called to show results in an interactive session
excepthook -- called to handle any uncaught exception other than SystemExit
  To customize printing in an interactive session or to install a custom
  top-level exception handler, assign other functions to replace these.

stdin -- standard input file object; used by input()
stdout -- standard output file object; used by print()
stderr -- standard error object; used for error messages
  By assigning other file objects (or objects that behave like files)
  to these, it is possible to redirect all of the interpreter's I/O.

last_type -- type of last uncaught exception
last_value -- value of last uncaught exception
last_traceback -- traceback of last uncaught exception
  These three are only available in an interactive session after a
  traceback has been printed.

Static objects:

builtin_module_names -- tuple of module names built into this interpreter
copyright -- copyright notice pertaining to this interpreter
exec_prefix -- prefix used to find the machine-specific Python library
executable -- absolute path of the executable binary of the Python interpreter
float_info -- a named tuple with information about the float implementation.
float_repr_style -- string indicating the style of repr() output for floats
hash_info -- a named tuple with information about the hash algorithm.
hexversion -- version information encoded as a single integer
implementation -- Python implementation information.
int_info -- a named tuple with information about the int implementation.
maxsize -- the largest supported length of containers.
maxunicode -- the value of the largest Unicode code point
platform -- platform identifier
prefix -- prefix used to find the Python library
thread_info -- a named tuple with information about the thread implementation.
version -- the version of this interpreter as a string
version_info -- version information as a named tuple
__stdin__ -- the original stdin; don't touch!
__stdout__ -- the original stdout; don't touch!
__stderr__ -- the original stderr; don't touch!
__displayhook__ -- the original displayhook; don't touch!
__excepthook__ -- the original excepthook; don't touch!

Functions:

displayhook() -- print an object to the screen, and save it in builtins._
excepthook() -- print an exception and its traceback to sys.stderr
exc_info() -- return thread-safe information about the current exception
exit() -- exit the interpreter by raising SystemExit
getdlopenflags() -- returns flags to be used for dlopen() calls
getprofile() -- get the global profiling function
getrefcount() -- return the reference count for an object (plus one :-)
getrecursionlimit() -- return the max recursion depth for the interpreter
getsizeof() -- return the size of an object in bytes
gettrace() -- get the global debug tracing function
setdlopenflags() -- set the flags to be used for dlopen() calls
setprofile() -- set the global profiling function
setrecursionlimit() -- set the max recursion depth for the interpreter
settrace() -- set the global debug tracing function
"""
# no imports

# Variables with simple values

abiflags = ''

api_version = 1013

base_exec_prefix = '/usr'

base_prefix = '/usr'

byteorder = 'little'

copyright = 'Copyright (c) 2001-2023 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'

dont_write_bytecode = True

executable = '/home/kadosh/PycharmProjects/BotFactory/venv/bin/python'

exec_prefix = '/home/kadosh/PycharmProjects/BotFactory/venv'

float_repr_style = 'short'

hexversion = 50990320

maxsize = 9223372036854775807
maxunicode = 1114111

platform = 'linux'
platlibdir = 'lib'

prefix = '/home/kadosh/PycharmProjects/BotFactory/venv'

pycache_prefix = None

version = '3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]'

_base_executable = '/home/kadosh/PycharmProjects/BotFactory/venv/bin/python'

_framework = ''

_home = '/usr/bin'

# functions

def addaudithook(*args, **kwargs): # real signature unknown
    """ Adds a new audit hook callback. """
    pass

def audit(event, *args): # real signature unknown; restored from __doc__
    """
    audit(event, *args)
    
    Passes the event to any audit hooks that are attached.
    """
    pass

def breakpointhook(*args, **kws): # real signature unknown; restored from __doc__
    """
    breakpointhook(*args, **kws)
    
    This hook function is called by built-in breakpoint().
    """
    pass

def call_tracing(*args, **kwargs): # real signature unknown
    """
    Call func(*args), while tracing is enabled.
    
    The tracing state is saved, and restored afterwards.  This is intended
    to be called from a debugger from a checkpoint, to recursively debug
    some other code.
    """
    pass

def displayhook(*args, **kwargs): # real signature unknown
    """ Print an object to sys.stdout and also save it in builtins._ """
    pass

def excepthook(*args, **kwargs): # real signature unknown
    """ Handle an exception by displaying it with a traceback on sys.stderr. """
    pass

def exc_info(*args, **kwargs): # real signature unknown
    """
    Return current exception information: (type, value, traceback).
    
    Return information about the most recent exception caught by an except
    clause in the current stack frame or in an older stack frame.
    """
    pass

def exit(*args, **kwargs): # real signature unknown
    """
    Exit the interpreter by raising SystemExit(status).
    
    If the status is omitted or None, it defaults to zero (i.e., success).
    If the status is an integer, it will be used as the system exit status.
    If it is another kind of object, it will be printed and the system
    exit status will be one (i.e., failure).
    """
    pass

def getallocatedblocks(*args, **kwargs): # real signature unknown
    """ Return the number of memory blocks currently allocated. """
    pass

def getdefaultencoding(*args, **kwargs): # real signature unknown
    """ Return the current default encoding used by the Unicode implementation. """
    pass

def getdlopenflags(*args, **kwargs): # real signature unknown
    """
    Return the current value of the flags that are used for dlopen calls.
    
    The flag constants are defined in the os module.
    """
    pass

def getfilesystemencodeerrors(*args, **kwargs): # real signature unknown
    """ Return the error mode used Unicode to OS filename conversion. """
    pass

def getfilesystemencoding(*args, **kwargs): # real signature unknown
    """ Return the encoding used to convert Unicode filenames to OS filenames. """
    pass

def getprofile(*args, **kwargs): # real signature unknown
    """
    Return the profiling function set with sys.setprofile.
    
    See the profiler chapter in the library manual.
    """
    pass

def getrecursionlimit(*args, **kwargs): # real signature unknown
    """
    Return the current value of the recursion limit.
    
    The recursion limit is the maximum depth of the Python interpreter
    stack.  This limit prevents infinite recursion from causing an overflow
    of the C stack and crashing Python.
    """
    pass

def getrefcount(): # real signature unknown; restored from __doc__
    """
    Return the reference count of object.
    
    The count returned is generally one higher than you might expect,
    because it includes the (temporary) reference as an argument to
    getrefcount().
    """
    pass

def getsizeof(p_object, default=None): # real signature unknown; restored from __doc__
    """
    getsizeof(object [, default]) -> int
    
    Return the size of object in bytes.
    """
    return 0

def getswitchinterval(*args, **kwargs): # real signature unknown
    """ Return the current thread switch interval; see sys.setswitchinterval(). """
    pass

def gettrace(*args, **kwargs): # real signature unknown
    """
    Return the global debug tracing function set with sys.settrace.
    
    See the debugger chapter in the library manual.
    """
    pass

def get_asyncgen_hooks(*args, **kwargs): # real signature unknown
    """
    Return the installed asynchronous generators hooks.
    
    This returns a namedtuple of the form (firstiter, finalizer).
    """
    pass

def get_coroutine_origin_tracking_depth(*args, **kwargs): # real signature unknown
    """ Check status of origin tracking for coroutine objects in this thread. """
    pass

def get_int_max_str_digits(*args, **kwargs): # real signature unknown
    """ Return the maximum string digits limit for non-binary int<->str conversions. """
    pass

def intern(*args, **kwargs): # real signature unknown
    """
    ``Intern'' the given string.
    
    This enters the string in the (global) table of interned strings whose
    purpose is to speed up dictionary lookups. Return the string itself or
    the previously interned string object with the same value.
    """
    pass

def is_finalizing(*args, **kwargs): # real signature unknown
    """ Return True if Python is exiting. """
    pass

def setdlopenflags(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Set the flags used by the interpreter for dlopen calls.
    
    This is used, for example, when the interpreter loads extension
    modules. Among other things, this will enable a lazy resolving of
    symbols when importing a module, if called as sys.setdlopenflags(0).
    To share symbols across extension modules, call as
    sys.setdlopenflags(os.RTLD_GLOBAL).  Symbolic names for the flag
    modules can be found in the os module (RTLD_xxx constants, e.g.
    os.RTLD_LAZY).
    """
    pass

def setprofile(function): # real signature unknown; restored from __doc__
    """
    setprofile(function)
    
    Set the profiling function.  It will be called on each function call
    and return.  See the profiler chapter in the library manual.
    """
    pass

def setrecursionlimit(*args, **kwargs): # real signature unknown
    """
    Set the maximum depth of the Python interpreter stack to n.
    
    This limit prevents infinite recursion from causing an overflow of the C
    stack and crashing Python.  The highest possible limit is platform-
    dependent.
    """
    pass

def setswitchinterval(*args, **kwargs): # real signature unknown
    """
    Set the ideal thread switching delay inside the Python interpreter.
    
    The actual frequency of switching threads can be lower if the
    interpreter executes long sequences of uninterruptible code
    (this is implementation-specific and workload-dependent).
    
    The parameter must represent the desired switching delay in seconds
    A typical value is 0.005 (5 milliseconds).
    """
    pass

def settrace(function): # real signature unknown; restored from __doc__
    """
    settrace(function)
    
    Set the global debug tracing function.  It will be called on each
    function call.  See the debugger chapter in the library manual.
    """
    pass

def set_asyncgen_hooks(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    set_asyncgen_hooks(* [, firstiter] [, finalizer])
    
    Set a finalizer for async generators objects.
    """
    pass

def set_coroutine_origin_tracking_depth(*args, **kwargs): # real signature unknown
    """
    Enable or disable origin tracking for coroutine objects in this thread.
    
    Coroutine objects will track 'depth' frames of traceback information
    about where they came from, available in their cr_origin attribute.
    
    Set a depth of 0 to disable.
    """
    pass

def set_int_max_str_digits(*args, **kwargs): # real signature unknown
    """ Set the maximum string digits limit for non-binary int<->str conversions. """
    pass

def unraisablehook(*args, **kwargs): # real signature unknown
    """
    Handle an unraisable exception.
    
    The unraisable argument has the following attributes:
    
    * exc_type: Exception type.
    * exc_value: Exception value, can be None.
    * exc_traceback: Exception traceback, can be None.
    * err_msg: Error message, can be None.
    * object: Object causing the exception, can be None.
    """
    pass

def _clear_type_cache(*args, **kwargs): # real signature unknown
    """ Clear the internal type lookup cache. """
    pass

def _current_exceptions(*args, **kwargs): # real signature unknown
    """
    Return a dict mapping each thread's identifier to its current raised exception.
    
    This function should be used for specialized purposes only.
    """
    pass

def _current_frames(*args, **kwargs): # real signature unknown
    """
    Return a dict mapping each thread's thread id to its current stack frame.
    
    This function should be used for specialized purposes only.
    """
    pass

def _deactivate_opcache(*args, **kwargs): # real signature unknown
    """ Deactivate the opcode cache permanently """
    pass

def _debugmallocstats(*args, **kwargs): # real signature unknown
    """
    Print summary info to stderr about the state of pymalloc's structures.
    
    In Py_DEBUG mode, also perform some expensive internal consistency
    checks.
    """
    pass

def _getframe(*args, **kwargs): # real signature unknown
    """
    Return a frame object from the call stack.
    
    If optional integer depth is given, return the frame object that many
    calls below the top of the stack.  If that is deeper than the call
    stack, ValueError is raised.  The default for depth is zero, returning
    the frame at the top of the call stack.
    
    This function should be used for internal and specialized purposes
    only.
    """
    pass

def __breakpointhook__(*args, **kwargs): # real signature unknown
    """
    breakpointhook(*args, **kws)
    
    This hook function is called by built-in breakpoint().
    """
    pass

def __displayhook__(*args, **kwargs): # real signature unknown
    """ Print an object to sys.stdout and also save it in builtins._ """
    pass

def __excepthook__(*args, **kwargs): # real signature unknown
    """ Handle an exception by displaying it with a traceback on sys.stderr. """
    pass

def __interactivehook__(): # reliably restored by inspect
    # no doc
    pass

def __unraisablehook__(*args, **kwargs): # real signature unknown
    """
    Handle an unraisable exception.
    
    The unraisable argument has the following attributes:
    
    * exc_type: Exception type.
    * exc_value: Exception value, can be None.
    * exc_traceback: Exception traceback, can be None.
    * err_msg: Error message, can be None.
    * object: Object causing the exception, can be None.
    """
    pass

# classes

class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod(<function BuiltinImporter.module_repr at 0x7f4ab8962290>)>, 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x7f4ab8962320>)>, 'find_module': <classmethod(<function BuiltinImporter.find_module at 0x7f4ab89623b0>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x7f4ab8962440>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x7f4ab89624d0>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x7f4ab89625f0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x7f4ab8962710>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x7f4ab8962830>)>, 'load_module': <classmethod(<function _load_module_shim at 0x7f4ab8961750>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

argv = [] # real value of type <class 'list'> skipped

builtin_module_names = () # real value of type <class 'tuple'> skipped

flags = (
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    False,
    0,
    0,
    -1,
)

float_info = (
    1.7976931348623157e+308,
    1024,
    308,
    2.2250738585072014e-308,
    -1021,
    -307,
    15,
    53,
    2.220446049250313e-16,
    2,
    1,
)

hash_info = (
    64,
    2305843009213693951,
    314159,
    0,
    1000003,
    'siphash24',
    64,
    128,
    0,
)

implementation = None # (!) real value is "namespace(name='cpython', cache_tag='cpython-310', version=sys.version_info(major=3, minor=10, micro=12, releaselevel='final', serial=0), hexversion=50990320, _multiarch='x86_64-linux-gnu')"

int_info = (
    30,
    4,
    4300,
    640,
)

meta_path = [
    None, # (!) real value is '<_distutils_hack.DistutilsMetaFinder object at 0x7f4ab883ce20>'
    None, # (!) real value is '<_virtualenv._Finder object at 0x7f4ab8802830>'
    __loader__,
    None, # (!) real value is "<class '_frozen_importlib.FrozenImporter'>"
    None, # (!) real value is "<class '_frozen_importlib_external.PathFinder'>"
    None, # (!) real value is '<six._SixMetaPathImporter object at 0x7f4ab80aa380>'
]

modules = {} # real value of type <class 'dict'> skipped

orig_argv = [
    '/home/kadosh/PycharmProjects/BotFactory/venv/bin/python',
    '/home/kadosh/Рабочий стол/pycharm-community-2023.2.3/plugins/python-ce/helpers/generator3/__main__.py',
    '-d',
    '/home/kadosh/.cache/JetBrains/PyCharmCE2023.2/python_stubs/-502548977',
    '-s',
    '/usr/lib/python3.10:/usr/lib/python3.10/lib-dynload:/home/kadosh/PycharmProjects/BotFactory/venv/lib/python3.10/site-packages',
]

path = [
    '/home/kadosh/Рабочий стол/pycharm-community-2023.2.3/plugins/python-ce/helpers',
    '/home/kadosh/Рабочий стол/pycharm-community-2023.2.3/plugins/python-ce/helpers/generator3',
    '/home/kadosh/Рабочий стол/pycharm-community-2023.2.3/plugins/python-ce/helpers',
    '/usr/lib/python310.zip',
    '/usr/lib/python3.10',
    '/usr/lib/python3.10/lib-dynload',
    '/home/kadosh/PycharmProjects/BotFactory/venv/lib/python3.10/site-packages',
]

path_hooks = [
    None, # (!) real value is "<class 'zipimport.zipimporter'>"
    None, # (!) real value is '<function FileFinder.path_hook.<locals>.path_hook_for_FileFinder at 0x7f4ab8960af0>'
]

path_importer_cache = {} # real value of type <class 'dict'> skipped

stderr = None # (!) real value is "<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>"

stdin = None # (!) real value is "<_io.TextIOWrapper name=5 mode='r' encoding='utf-8'>"

stdlib_module_names = None # (!) real value is "frozenset({'telnetlib', 'getpass', 'code', '_codecs_cn', 'cmath', '__future__', 'os', '_blake2', '_bz2', '_uuid', 'fileinput', 'pstats', 'random', 're', 'marshal', 'turtledemo', '_winapi', 'this', 'pathlib', 'msilib', 'posixpath', 'idlelib', 'optparse', '_codecs_iso2022', '_random', '_weakref', 'fnmatch', 'aifc', 'mailcap', 'winsound', '_collections_abc', 'ssl', '_functools', 'pipes', 'math', 'tabnanny', 'ctypes', '_osx_support', 'json', 'netrc', 'uuid', 'xmlrpc', 'ftplib', '_struct', '_heapq', 'contextlib', '_crypt', 'sysconfig', 'ensurepip', 'time', 'audioop', 'xdrlib', 'concurrent', '_stat', 'genericpath', 'html', 'timeit', '_symtable', 'zoneinfo', '_frozen_importlib', '_compat_pickle', 'http', 'gettext', '_sha1', 'asynchat', 'bz2', '_compression', '_threading_local', '_msi', '_zoneinfo', 'copy', 'shlex', 'pty', 'tokenize', 'reprlib', 'codeop', 'pprint', 'atexit', 'warnings', '_posixshmem', 'threading', 'dbm', 'py_compile', 'curses', '_decimal', '_tkinter', 'weakref', 'imghdr', 'profile', '_pyio', 'tempfile', 'sched', 'poplib', 'pwd', 'runpy', 'tkinter', 'datetime', 'xml', 'shelve', 'termios', 'importlib', '_sha3', 'imp', 'imaplib', 'binascii', 'nturl2path', '_lzma', 'enum', '_markupbase', 'configparser', 'traceback', 'sre_constants', 'token', '_warnings', 'rlcompleter', '_codecs_tw', '_sre', '_tracemalloc', 'glob', 'copyreg', 'colorsys', 'symtable', 'unicodedata', '_hashlib', 'getopt', 'statistics', '_py_abc', 'csv', 'fractions', 'platform', '_locale', 'zipfile', 'bisect', 'pdb', 'shutil', 'tarfile', '_curses_panel', 'fcntl', 'codecs', '_thread', '_multibytecodec', 'readline', 'functools', '_curses', 'modulefinder', '_codecs', '_aix_support', 'dis', 'hmac', 'spwd', 'filecmp', 'webbrowser', '_elementtree', 'tty', 'faulthandler', 'sqlite3', 'ntpath', '_opcode', 'array', 'mailbox', '_asyncio', 'logging', 'nntplib', '_ast', '_frozen_importlib_external', 'difflib', 'ossaudiodev', 'pyclbr', 'socketserver', 'locale', 'lib2to3', 'crypt', 'mimetypes', '_bisect', 'pkgutil', '_overlapped', '_sqlite3', 'heapq', 'plistlib', '_codecs_kr', 'pydoc_data', 'sunau', 'cProfile', 'errno', 'textwrap', '_scproxy', 'compileall', 'asyncore', '_json', 'pydoc', '_sha512', '_weakrefset', '_statistics', 'msvcrt', 'stat', 'cgi', '_bootsubprocess', '_abc', '_ssl', 'stringprep', 'unittest', 'sys', 'posix', '_csv', 'encodings', '_collections', 'quopri', 'numbers', '_string', 'collections', 'queue', 'string', 'gc', '_dbm', '_md5', 'grp', 'doctest', 'syslog', '_datetime', '_signal', 'ast', 'sndhdr', 'struct', 'winreg', 'abc', 'zlib', 'types', 'urllib', 'uu', 'pickletools', 'subprocess', '_pydecimal', 'binhex', 'smtplib', 'socket', 'cmd', 'bdb', '_socket', 'venv', 'selectors', '_io', 'zipimport', 'pyexpat', '_codecs_jp', 'site', 'distutils', 'typing', 'calendar', 'select', '_queue', '_posixsubprocess', '_ctypes', 'base64', 'trace', 'builtins', 'operator', '_contextvars', '_operator', 'io', 'argparse', 'wave', '_multiprocessing', '_pickle', '_codecs_hk', 'inspect', 'opcode', 'turtle', 'wsgiref', '_lsprof', '_sitebuiltins', 'email', '_strptime', 'decimal', 'contextvars', 'gzip', 'linecache', 'nt', 'smtpd', 'sre_compile', 'pickle', 'resource', 'cgitb', 'multiprocessing', 'chunk', 'secrets', 'asyncio', 'keyword', 'graphlib', 'sre_parse', 'antigravity', 'mmap', 'zipapp', 'hashlib', 'lzma', 'signal', 'nis', 'tracemalloc', 'itertools', '_imp', 'ipaddress', 'dataclasses', '_gdbm', '_sha256'})"

stdout = None # (!) forward: __stdout__, real value is "<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>"

thread_info = (
    'pthread',
    'semaphore',
    'NPTL 2.35',
)

version_info = (
    3,
    10,
    12,
    'final',
    0,
)

warnoptions = []

_git = (
    'CPython',
    '',
    '',
)

_xoptions = {}

__spec__ = None # (!) real value is "ModuleSpec(name='sys', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

__stderr__ = stderr

__stdin__ = None # (!) real value is "<_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>"

__stdout__ = None # (!) real value is "<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>"

# intermittent names
exc_value = Exception()
exc_traceback=None
