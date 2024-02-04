# encoding: utf-8
# module zope.interface._zope_interface_coptimizations
# from /home/kadosh/PycharmProjects/WeatherEnglish/venv/lib/python3.10/site-packages/zope/interface/_zope_interface_coptimizations.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" C optimizations for zope.interface """

# imports
import _interface_coptimizations as ___interface_coptimizations
import _zope_interface_coptimizations as ___zope_interface_coptimizations


# functions

def getObjectSpecification(*args, **kwargs): # real signature unknown
    """ Get an object's interfaces (internal api) """
    pass

def implementedBy(*args, **kwargs): # real signature unknown
    """
    Interfaces implemented by a class or factory.
    Raises TypeError if argument is neither a class nor a callable.
    """
    pass

def providedBy(*args, **kwargs): # real signature unknown
    """ Get an object's interfaces """
    pass

# classes

class SpecificationBase(object):
    """ Base type for Specification objects """
    def implementedBy(self, *args, **kwargs): # real signature unknown
        """
        Test whether the specification is implemented by a class or factory.
        Raise TypeError if argument is neither a class nor a callable.
        """
        pass

    def isOrExtends(self, *args, **kwargs): # real signature unknown
        """ Test whether a specification is or extends another """
        pass

    def providedBy(self, *args, **kwargs): # real signature unknown
        """ Test whether an interface is implemented by the specification """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _bases = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dependents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _implied = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _v_attrs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __iro__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __sro__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ClassProvidesBase(___interface_coptimizations.SpecificationBase):
    """ C Base class for ClassProvides """
    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _cls = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defining class."""

    _implements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Result of implementedBy."""



class InterfaceBase(___interface_coptimizations.SpecificationBase):
    """ Interface base type providing __call__ and __adapt__ """
    def __adapt__(self, *args, **kwargs): # real signature unknown
        """ Adapt an object to the receiver """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __ibmodule__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'InterfaceBase'


class LookupBase(object):
    # no doc
    def adapter_hook(self, *args, **kwargs): # real signature unknown
        pass

    def changed(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def lookup1(self, *args, **kwargs): # real signature unknown
        pass

    def lookupAll(self, *args, **kwargs): # real signature unknown
        pass

    def queryAdapter(self, *args, **kwargs): # real signature unknown
        pass

    def subscriptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ObjectSpecificationDescriptor(object):
    """ Object Specification Descriptor """
    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class VerifyingBase(___zope_interface_coptimizations.LookupBase):
    # no doc
    def adapter_hook(self, *args, **kwargs): # real signature unknown
        pass

    def changed(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def lookup1(self, *args, **kwargs): # real signature unknown
        pass

    def lookupAll(self, *args, **kwargs): # real signature unknown
        pass

    def queryAdapter(self, *args, **kwargs): # real signature unknown
        pass

    def subscriptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

adapter_hooks = []

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f7516445ae0>'

__spec__ = None # (!) real value is "ModuleSpec(name='zope.interface._zope_interface_coptimizations', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f7516445ae0>, origin='/home/kadosh/.local/lib/python3.10/site-packages/zope/interface/_zope_interface_coptimizations.cpython-310-x86_64-linux-gnu.so')"

