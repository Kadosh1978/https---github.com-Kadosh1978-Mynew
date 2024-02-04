# encoding: utf-8
# module _csv
# from (built-in)
# by generator 1.147
"""
CSV parsing and writing.

This module provides classes that assist in the reading and writing
of Comma Separated Value (CSV) files, and implements the interface
described by PEP 305.  Although many CSV files are simple to parse,
the format is not formally defined by a stable specification and
is subtle enough that parsing lines of a CSV file with something
like line.split(",") is bound to fail.  The module supports three
basic APIs: reading, writing, and registration of dialects.


DIALECT REGISTRATION:

Readers and writers support a dialect argument, which is a convenient
handle on a group of settings.  When the dialect argument is a string,
it identifies one of the dialects previously registered with the module.
If it is a class or instance, the attributes of the argument are used as
the settings for the reader or writer:

    class excel:
        delimiter = ','
        quotechar = '"'
        escapechar = None
        doublequote = True
        skipinitialspace = False
        lineterminator = '\r\n'
        quoting = QUOTE_MINIMAL

SETTINGS:

    * quotechar - specifies a one-character string to use as the
        quoting character.  It defaults to '"'.
    * delimiter - specifies a one-character string to use as the
        field separator.  It defaults to ','.
    * skipinitialspace - specifies how to interpret spaces which
        immediately follow a delimiter.  It defaults to False, which
        means that spaces immediately following a delimiter is part
        of the following field.
    * lineterminator -  specifies the character sequence which should
        terminate rows.
    * quoting - controls when quotes should be generated by the writer.
        It can take on any of the following module constants:

        csv.QUOTE_MINIMAL means only when required, for example, when a
            field contains either the quotechar or the delimiter
        csv.QUOTE_ALL means that quotes are always placed around fields.
        csv.QUOTE_NONNUMERIC means that quotes are always placed around
            fields which do not parse as integers or floating point
            numbers.
        csv.QUOTE_NONE means that quotes are never placed around fields.
    * escapechar - specifies a one-character string used to escape
        the delimiter when quoting is set to QUOTE_NONE.
    * doublequote - controls the handling of quotes inside fields.  When
        True, two consecutive quotes are interpreted as one during read,
        and when writing, each quote character embedded in the data is
        written as two quotes
"""
# no imports

# Variables with simple values

QUOTE_ALL = 1
QUOTE_MINIMAL = 0
QUOTE_NONE = 3
QUOTE_NONNUMERIC = 2

__version__ = '1.0'

# functions

def field_size_limit(limit=None): # real signature unknown; restored from __doc__
    """
    Sets an upper limit on parsed fields.
        csv.field_size_limit([limit])
    
    Returns old limit. If limit is not given, no new limit is set and
    the old limit is returned
    """
    pass

def get_dialect(name): # real signature unknown; restored from __doc__
    """
    Return the dialect instance associated with name.
        dialect = csv.get_dialect(name)
    """
    pass

def list_dialects(): # real signature unknown; restored from __doc__
    """
    Return a list of all know dialect names.
        names = csv.list_dialects()
    """
    pass

def reader(iterable, dialect='excel', *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    csv_reader = reader(iterable [, dialect='excel']
                            [optional keyword args])
        for row in csv_reader:
            process(row)
    
    The "iterable" argument can be any object that returns a line
    of input for each iteration, such as a file object or a list.  The
    optional "dialect" parameter is discussed below.  The function
    also accepts optional keyword arguments which override settings
    provided by the dialect.
    
    The returned object is an iterator.  Each iteration returns a row
    of the CSV file (which can span multiple input lines).
    """
    pass

def register_dialect(name, dialect=None, **fmtparams=None): # real signature unknown; restored from __doc__
    """
    Create a mapping from a string name to a dialect class.
        dialect = csv.register_dialect(name[, dialect[, **fmtparams]])
    """
    pass

def unregister_dialect(name): # real signature unknown; restored from __doc__
    """
    Delete the name/dialect mapping associated with a string name.
        csv.unregister_dialect(name)
    """
    pass

def writer(fileobj, dialect='excel', *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    csv_writer = csv.writer(fileobj [, dialect='excel']
                                [optional keyword args])
        for row in sequence:
            csv_writer.writerow(row)
    
        [or]
    
        csv_writer = csv.writer(fileobj [, dialect='excel']
                                [optional keyword args])
        csv_writer.writerows(rows)
    
    The "fileobj" argument can be any object that supports the file API.
    """
    pass

# classes

class Dialect(object):
    """
    CSV dialect
    
    The Dialect type records CSV parsing and generation options.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ raises an exception to avoid pickling """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ raises an exception to avoid pickling """
        pass

    delimiter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    doublequote = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    escapechar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lineterminator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quotechar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quoting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skipinitialspace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    strict = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Reader(object):
    """
    CSV reader
    
    Reader objects are responsible for reading and parsing tabular data
    in CSV format.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    dialect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    line_num = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Writer(object):
    """
    CSV writer
    
    Writer objects are responsible for generating tabular data
    in CSV format from sequence input.
    """
    def writerow(self, iterable): # real signature unknown; restored from __doc__
        """
        writerow(iterable)
        
        Construct and write a CSV record from an iterable of fields.  Non-string
        elements will be converted to string.
        """
        pass

    def writerows(self, iterable_of_iterables): # real signature unknown; restored from __doc__
        """
        writerows(iterable of iterables)
        
        Construct and write a series of iterables to a csv file.  Non-string
        elements will be converted to string.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    dialect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



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

_dialects = {}

__spec__ = None # (!) real value is "ModuleSpec(name='_csv', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

