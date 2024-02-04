# encoding: utf-8
# module icu._icu_
# from /usr/lib/python3/dist-packages/icu/_icu_.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" PyICU extension module """

# imports
import datetime as __datetime
import icu as __icu


class TimeZone(__icu.UObject):
    """ TimeZone objects """
    @classmethod
    def countEquivalentIDs(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def createDefault(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def createEnumeration(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def createTimeZone(cls, *args, **kwargs): # real signature unknown
        pass

    def getDisplayName(self, *args, **kwargs): # real signature unknown
        pass

    def getDSTSavings(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def getEquivalentID(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def getGMT(cls, *args, **kwargs): # real signature unknown
        pass

    def getID(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def getIDForWindowsID(cls, *args, **kwargs): # real signature unknown
        pass

    def getOffset(self, *args, **kwargs): # real signature unknown
        pass

    def getRawOffset(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def getWindowsID(cls, *args, **kwargs): # real signature unknown
        pass

    def hasSameRules(self, *args, **kwargs): # real signature unknown
        pass

    def inDaylightTime(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def setDefault(cls, *args, **kwargs): # real signature unknown
        pass

    def setID(self, *args, **kwargs): # real signature unknown
        pass

    def setRawOffset(self, *args, **kwargs): # real signature unknown
        pass

    def useDaylightTime(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    LONG = 2
    SHORT = 1
    __hash__ = None


