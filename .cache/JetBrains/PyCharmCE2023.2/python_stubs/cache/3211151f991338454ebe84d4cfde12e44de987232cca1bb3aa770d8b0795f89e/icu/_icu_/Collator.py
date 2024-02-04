# encoding: utf-8
# module icu._icu_
# from /usr/lib/python3/dist-packages/icu/_icu_.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" PyICU extension module """

# imports
import datetime as __datetime
import icu as __icu


class Collator(__icu.UObject):
    """ Collator objects """
    def compare(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def createInstance(cls, *args, **kwargs): # real signature unknown
        pass

    def equals(self, *args, **kwargs): # real signature unknown
        pass

    def getAttribute(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def getAvailableLocales(cls, *args, **kwargs): # real signature unknown
        pass

    def getCollationKey(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def getFunctionalEquivalent(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def getKeywords(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def getKeywordValues(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def getKeywordValuesForLocale(cls, *args, **kwargs): # real signature unknown
        pass

    def getLocale(self, *args, **kwargs): # real signature unknown
        pass

    def getSortKey(self, *args, **kwargs): # real signature unknown
        pass

    def getStrength(self, *args, **kwargs): # real signature unknown
        pass

    def getTailoredSet(self, *args, **kwargs): # real signature unknown
        pass

    def getVariableTop(self, *args, **kwargs): # real signature unknown
        pass

    def greater(self, *args, **kwargs): # real signature unknown
        pass

    def greaterOrEqual(self, *args, **kwargs): # real signature unknown
        pass

    def setAttribute(self, *args, **kwargs): # real signature unknown
        pass

    def setStrength(self, *args, **kwargs): # real signature unknown
        pass

    def setVariableTop(self, *args, **kwargs): # real signature unknown
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    IDENTICAL = 15
    PRIMARY = 0
    QUATERNARY = 3
    SECONDARY = 1
    TERTIARY = 2


