# encoding: utf-8
# module icu._icu_
# from /usr/lib/python3/dist-packages/icu/_icu_.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" PyICU extension module """

# imports
import datetime as __datetime
import icu as __icu


from .object import object

class Bidi(object):
    """ Bidi objects """
    def countParagraphs(self, *args, **kwargs): # real signature unknown
        pass

    def countRuns(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def getBaseDirection(cls, *args, **kwargs): # real signature unknown
        pass

    def getDirection(self, *args, **kwargs): # real signature unknown
        pass

    def getLength(self, *args, **kwargs): # real signature unknown
        pass

    def getLevelAt(self, *args, **kwargs): # real signature unknown
        pass

    def getLevels(self, *args, **kwargs): # real signature unknown
        pass

    def getLogicalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def getLogicalMap(self, *args, **kwargs): # real signature unknown
        pass

    def getLogicalRun(self, *args, **kwargs): # real signature unknown
        pass

    def getParagraph(self, *args, **kwargs): # real signature unknown
        pass

    def getParagraphByIndex(self, *args, **kwargs): # real signature unknown
        pass

    def getParaLevel(self, *args, **kwargs): # real signature unknown
        pass

    def getProcessedLength(self, *args, **kwargs): # real signature unknown
        pass

    def getReorderingMode(self, *args, **kwargs): # real signature unknown
        pass

    def getReorderingOptions(self, *args, **kwargs): # real signature unknown
        pass

    def getResultLength(self, *args, **kwargs): # real signature unknown
        pass

    def getText(self, *args, **kwargs): # real signature unknown
        pass

    def getVisualIndex(self, *args, **kwargs): # real signature unknown
        pass

    def getVisualMap(self, *args, **kwargs): # real signature unknown
        pass

    def getVisualRun(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def invertMap(cls, *args, **kwargs): # real signature unknown
        pass

    def isInverse(self, *args, **kwargs): # real signature unknown
        pass

    def isOrderParagraphsLTR(self, *args, **kwargs): # real signature unknown
        pass

    def orderParagraphsLTR(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def reorderLogical(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def reorderVisual(cls, *args, **kwargs): # real signature unknown
        pass

    def setContext(self, *args, **kwargs): # real signature unknown
        pass

    def setInverse(self, *args, **kwargs): # real signature unknown
        pass

    def setLine(self, *args, **kwargs): # real signature unknown
        pass

    def setPara(self, *args, **kwargs): # real signature unknown
        pass

    def setReorderingMode(self, *args, **kwargs): # real signature unknown
        pass

    def setReorderingOptions(self, *args, **kwargs): # real signature unknown
        pass

    def writeReordered(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def writeReverse(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    epilogue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """epilogue property"""

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """parent property"""

    prologue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """prologue property"""

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """text property"""


    DEFAULT_LTR = 254
    DEFAULT_RTL = 255
    DO_MIRRORING = 2
    INSERT_LRM_FOR_NUMERIC = 4
    KEEP_BASE_COMBINING = 1
    LEVEL_OVERRIDE = 128
    MAP_NOWHERE = -1
    MAX_EXPLICIT_LEVEL = 125
    OUTPUT_REVERSE = 16
    REMOVE_BIDI_CONTROLS = 8


