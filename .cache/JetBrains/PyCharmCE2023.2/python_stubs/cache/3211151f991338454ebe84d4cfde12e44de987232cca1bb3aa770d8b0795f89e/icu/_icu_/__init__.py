# encoding: utf-8
# module icu._icu_
# from /usr/lib/python3/dist-packages/icu/_icu_.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" PyICU extension module """

# imports
import datetime as __datetime
import icu as __icu


# Variables with simple values

FLOATING_TZNAME = 'World/Floating'

ICU_MAX_MAJOR_VERSION = '70'

ICU_VERSION = '70.1'

PY_VERSION = '3.10.3'

UNICODE_VERSION = '14.0'

UNORM_INPUT_IS_FCD = 131072

USET_ADD_CASE_MAPPINGS = 4

USET_CASE_INSENSITIVE = 2

USET_IGNORE_SPACE = 1

U_COMPARE_CODE_POINT_ORDER = 32768

U_COMPARE_IGNORE_CASE = 65536

U_EDITS_NO_RESET = 8192

U_FOLD_CASE_DEFAULT = 0

U_FOLD_CASE_EXCLUDE_SPECIAL_I = 1

U_OMIT_UNCHANGED_TEXT = 16384

U_TITLECASE_ADJUST_TO_CASED = 1024

U_TITLECASE_NO_BREAK_ADJUSTMENT = 512

U_TITLECASE_NO_LOWERCASE = 256

U_TITLECASE_SENTENCES = 64

U_TITLECASE_WHOLE_STRING = 32

VERSION = '2.8.1'

# no functions
# classes

from .UMemory import UMemory
from .UObject import UObject
from .AlphabeticIndex import AlphabeticIndex
from .TimeZoneRule import TimeZoneRule
from .AnnualTimeZoneRule import AnnualTimeZoneRule
from .TimeZone import TimeZone
from .BasicTimeZone import BasicTimeZone
from .Bidi import Bidi
from .BidiTransform import BidiTransform
from .BreakIterator import BreakIterator
from .BytesTrie import BytesTrie
from .StringTrieBuilder import StringTrieBuilder
from .BytesTrieBuilder import BytesTrieBuilder
from .BytesTrieIterator import BytesTrieIterator
from .BytesTrieState import BytesTrieState
from .Calendar import Calendar
from .CanonicalIterator import CanonicalIterator
from .CaseMap import CaseMap
from .Char import Char
from .ForwardCharacterIterator import ForwardCharacterIterator
from .CharacterIterator import CharacterIterator
from .CharsetDetector import CharsetDetector
from .CharsetMatch import CharsetMatch
from .Format import Format
from .NumberFormat import NumberFormat
from .ChoiceFormat import ChoiceFormat
from .CollationElementIterator import CollationElementIterator
from .CollationKey import CollationKey
from .Collator import Collator
from .DecimalFormat import DecimalFormat
from .CompactDecimalFormat import CompactDecimalFormat
from .ConstrainedFieldPosition import ConstrainedFieldPosition
from .Measure import Measure
from .CurrencyAmount import CurrencyAmount
from .CurrencyPluralInfo import CurrencyPluralInfo
from .Precision import Precision
from .CurrencyPrecision import CurrencyPrecision
from .MeasureUnit import MeasureUnit
from .CurrencyUnit import CurrencyUnit
from .DateFormat import DateFormat
from .DateFormatSymbols import DateFormatSymbols
from .DateInterval import DateInterval
from .DateIntervalFormat import DateIntervalFormat
from .DateIntervalInfo import DateIntervalInfo
from .DateRuleType import DateRuleType
from .DateTimePatternGenerator import DateTimePatternGenerator
from .DateTimeRule import DateTimeRule
from .DecimalFormatSymbols import DecimalFormatSymbols
from .RuleBasedBreakIterator import RuleBasedBreakIterator
from .DictionaryBasedBreakIterator import DictionaryBasedBreakIterator
from .Edits import Edits
from .EditsIterator import EditsIterator
from .FieldPosition import FieldPosition
from .Normalizer2 import Normalizer2
from .FilteredNormalizer2 import FilteredNormalizer2
from .FloatingTZ import FloatingTZ
from .Formattable import Formattable
from .FormattedValue import FormattedValue
from .FormattedDateInterval import FormattedDateInterval
from .FormattedList import FormattedList
from .FormattedNumber import FormattedNumber
from .FormattedNumberRange import FormattedNumberRange
from .FormattedRelativeDateTime import FormattedRelativeDateTime
from .FractionPrecision import FractionPrecision
from .GenderInfo import GenderInfo
from .GregorianCalendar import GregorianCalendar
from .ICUtzinfo import ICUtzinfo
from .IDNA import IDNA
from .IDNAInfo import IDNAInfo
from .ImmutableIndex import ImmutableIndex
from .IncrementPrecision import IncrementPrecision
from .InitialTimeZoneRule import InitialTimeZoneRule
from .IntegerWidth import IntegerWidth
from .ListFormatter import ListFormatter
from .Locale import Locale
from .LocaleBuilder import LocaleBuilder
from .LocaleData import LocaleData
from .LocaleMatcher import LocaleMatcher
from .LocaleMatcherBuilder import LocaleMatcherBuilder
from .LocaleMatcherResult import LocaleMatcherResult
from .LocalizedNumberFormatter import LocalizedNumberFormatter
from .LocalizedNumberRangeFormatter import LocalizedNumberRangeFormatter
from .MeasureFormat import MeasureFormat
from .MessageFormat import MessageFormat
from .MessagePattern import MessagePattern
from .MessagePattern_Part import MessagePattern_Part
from .Normalizer import Normalizer
from .Notation import Notation
from .NoUnit import NoUnit
from .NumberFormatter import NumberFormatter
from .NumberingSystem import NumberingSystem
from .NumberRangeFormatter import NumberRangeFormatter
from .ParsePosition import ParsePosition
from .PluralFormat import PluralFormat
from .PluralRules import PluralRules
from .Replaceable import Replaceable
from .PythonReplaceable import PythonReplaceable
from .RegexMatcher import RegexMatcher
from .RegexPattern import RegexPattern
from .Region import Region
from .RelativeDateTimeFormatter import RelativeDateTimeFormatter
from .ResourceBundle import ResourceBundle
from .RuleBasedCollator import RuleBasedCollator
from .RuleBasedNumberFormat import RuleBasedNumberFormat
from .RuleBasedTimeZone import RuleBasedTimeZone
from .Scale import Scale
from .ScientificNotation import ScientificNotation
from .Script import Script
from .SearchIterator import SearchIterator
from .SelectFormat import SelectFormat
from .Shape import Shape
from .SimpleDateFormat import SimpleDateFormat
from .SimpleFormatter import SimpleFormatter
from .SimpleTimeZone import SimpleTimeZone
from .SpoofChecker import SpoofChecker
from .UCharCharacterIterator import UCharCharacterIterator
from .StringCharacterIterator import StringCharacterIterator
from .StringEnumeration import StringEnumeration
from .StringSearch import StringSearch
from .TimeArrayTimeZoneRule import TimeArrayTimeZoneRule
from .TimeRuleType import TimeRuleType
from .TimeUnit import TimeUnit
from .TimeUnitAmount import TimeUnitAmount
from .TimeUnitFormat import TimeUnitFormat
from .TimeZoneTransition import TimeZoneTransition
from .Transliterator import Transliterator
from .UAcceptResult import UAcceptResult
from .UAlphabeticIndexLabelType import UAlphabeticIndexLabelType
from .UBiDiDirection import UBiDiDirection
from .UBiDiMirroring import UBiDiMirroring
from .UBiDiOrder import UBiDiOrder
from .UBidiPairedBracketType import UBidiPairedBracketType
from .UBiDiReorderingMode import UBiDiReorderingMode
from .UBiDiReorderingOption import UBiDiReorderingOption
from .UBlockCode import UBlockCode
from .UCalendarAMPMs import UCalendarAMPMs
from .UCalendarDateFields import UCalendarDateFields
from .UCalendarDaysOfWeek import UCalendarDaysOfWeek
from .UCalendarMonths import UCalendarMonths
from .UCharCategory import UCharCategory
from .UCharDirection import UCharDirection
from .UCharNameChoice import UCharNameChoice
from .UCharsTrie import UCharsTrie
from .UCharsTrieBuilder import UCharsTrieBuilder
from .UCharsTrieIterator import UCharsTrieIterator
from .UCharsTrieState import UCharsTrieState
from .UCollationResult import UCollationResult
from .UCollAttribute import UCollAttribute
from .UCollAttributeValue import UCollAttributeValue
from .UCurrencySpacing import UCurrencySpacing
from .UCurrencyUsage import UCurrencyUsage
from .UCurrNameStyle import UCurrNameStyle
from .UDateAbsoluteUnit import UDateAbsoluteUnit
from .UDateDirection import UDateDirection
from .UDateFormatBooleanAttribute import UDateFormatBooleanAttribute
from .UDateRelativeDateTimeFormatterStyle import UDateRelativeDateTimeFormatterStyle
from .UDateRelativeUnit import UDateRelativeUnit
from .UDateTimePatternConflict import UDateTimePatternConflict
from .UDateTimePatternField import UDateTimePatternField
from .UDateTimePatternMatchOptions import UDateTimePatternMatchOptions
from .UDisplayContext import UDisplayContext
from .UDisplayContextType import UDisplayContextType
from .UFieldCategory import UFieldCategory
from .UGender import UGender
from .UGraphemeClusterBreak import UGraphemeClusterBreak
from .UHangulSyllableType import UHangulSyllableType
from .UIndicPositionalCategory import UIndicPositionalCategory
from .UIndicSyllabicCategory import UIndicSyllabicCategory
from .UJoiningGroup import UJoiningGroup
from .ULineBreak import ULineBreak
from .UListFormatterField import UListFormatterField
from .ULocaleDataDelimiterType import ULocaleDataDelimiterType
from .ULocaleDataExemplarSetType import ULocaleDataExemplarSetType
from .ULocDataLocaleType import ULocDataLocaleType
from .ULocMatchDemotion import ULocMatchDemotion
from .ULocMatchDirection import ULocMatchDirection
from .ULocMatchFavorSubtag import ULocMatchFavorSubtag
from .UMatchDegree import UMatchDegree
from .UMeasurementSystem import UMeasurementSystem
from .UMeasureUnitComplexity import UMeasureUnitComplexity
from .UMessagePatternApostropheMode import UMessagePatternApostropheMode
from .UMessagePatternArgType import UMessagePatternArgType
from .UMessagePatternPartType import UMessagePatternPartType
from .UnicodeFilter import UnicodeFilter
from .UnicodeFunctor import UnicodeFunctor
from .UnicodeMatcher import UnicodeMatcher
from .UnicodeSet import UnicodeSet
from .UnicodeSetIterator import UnicodeSetIterator
from .UnicodeString import UnicodeString
from .UnlocalizedNumberFormatter import UnlocalizedNumberFormatter
from .UnlocalizedNumberRangeFormatter import UnlocalizedNumberRangeFormatter
from .UNormalizationCheckResult import UNormalizationCheckResult
from .UNormalizationMode import UNormalizationMode
from .UNormalizationMode2 import UNormalizationMode2
from .UNumberCompactStyle import UNumberCompactStyle
from .UNumberDecimalSeparatorDisplay import UNumberDecimalSeparatorDisplay
from .UNumberFormatAttribute import UNumberFormatAttribute
from .UNumberFormatFields import UNumberFormatFields
from .UNumberFormatRoundingMode import UNumberFormatRoundingMode
from .UNumberFormatStyle import UNumberFormatStyle
from .UNumberGroupingStrategy import UNumberGroupingStrategy
from .UNumberRangeCollapse import UNumberRangeCollapse
from .UNumberRangeIdentityFallback import UNumberRangeIdentityFallback
from .UNumberRangeIdentityResult import UNumberRangeIdentityResult
from .UNumberSignDisplay import UNumberSignDisplay
from .UNumberUnitWidth import UNumberUnitWidth
from .UProperty import UProperty
from .UPropertyNameChoice import UPropertyNameChoice
from .URBNFRuleSetTag import URBNFRuleSetTag
from .URegexpFlag import URegexpFlag
from .URegionType import URegionType
from .URelativeDateTimeFormatterField import URelativeDateTimeFormatterField
from .URelativeDateTimeUnit import URelativeDateTimeUnit
from .URestrictionLevel import URestrictionLevel
from .UResType import UResType
from .UScriptCode import UScriptCode
from .UScriptUsage import UScriptUsage
from .USearchAttribute import USearchAttribute
from .USearchAttributeValue import USearchAttributeValue
from .USetSpanCondition import USetSpanCondition
from .USpoofChecks import USpoofChecks
from .UStringTrieBuildOption import UStringTrieBuildOption
from .UStringTrieResult import UStringTrieResult
from .UTimeUnitFields import UTimeUnitFields
from .UTimeUnitFormatStyle import UTimeUnitFormatStyle
from .UTimeZoneLocalOption import UTimeZoneLocalOption
from .UTransDirection import UTransDirection
from .UTransPosition import UTransPosition
from .UVerticalOrientation import UVerticalOrientation
from .UWordBreak import UWordBreak
from .UWordBreakValues import UWordBreakValues
from .VTimeZone import VTimeZone
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d6c0>'

__spec__ = None # (!) real value is "ModuleSpec(name='icu._icu_', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2d6c0>, origin='/usr/lib/python3/dist-packages/icu/_icu_.cpython-310-x86_64-linux-gnu.so')"

__types__ = {
    'N6icu_707UObjectE': [
        'N6icu_7011ReplaceableE',
        '17PythonReplaceable',
        'N6icu_7013UnicodeStringE',
        'N6icu_7011FormattableE',
        'N6icu_7017StringEnumerationE',
        'N6icu_706LocaleE',
        'N6icu_7014ResourceBundleE',
        'N6icu_706RegionE',
        'N6icu_7013LocaleBuilderE',
        'N6icu_7014TransliteratorE',
        'N6icu_7024ForwardCharacterIteratorE',
        'N6icu_7017CharacterIteratorE',
        'N6icu_7022UCharCharacterIteratorE',
        'N6icu_7023StringCharacterIteratorE',
        'N6icu_7013BreakIteratorE',
        'N6icu_7022RuleBasedBreakIteratorE',
        'N6icu_7022RuleBasedBreakIteratorE',
        'N6icu_7017CanonicalIteratorE',
        'N6icu_7024CollationElementIteratorE',
        'N6icu_7013FieldPositionE',
        'N6icu_7013ParsePositionE',
        'N6icu_706FormatE',
        'N6icu_7013MeasureFormatE',
        'N6icu_7013MessageFormatE',
        'N6icu_7011PluralRulesE',
        'N6icu_7012PluralFormatE',
        'N6icu_7014TimeUnitFormatE',
        'N6icu_7012SelectFormatE',
        'N6icu_7013ListFormatterE',
        'N6icu_7017DateFormatSymbolsE',
        'N6icu_7010DateFormatE',
        'N6icu_7016SimpleDateFormatE',
        'N6icu_7024DateTimePatternGeneratorE',
        'N6icu_7012DateIntervalE',
        'N6icu_7016DateIntervalInfoE',
        'N6icu_7018DateIntervalFormatE',
        'N6icu_7025RelativeDateTimeFormatterE',
        'N6icu_7014MessagePatternE',
        'N6icu_7020DecimalFormatSymbolsE',
        'N6icu_7012NumberFormatE',
        'N6icu_7018CurrencyPluralInfoE',
        'N6icu_7015NumberingSystemE',
        'N6icu_7013DecimalFormatE',
        'N6icu_7020CompactDecimalFormatE',
        'N6icu_7021RuleBasedNumberFormatE',
        'N6icu_7012ChoiceFormatE',
        'N6icu_7012TimeZoneRuleE',
        'N6icu_7018AnnualTimeZoneRuleE',
        'N6icu_7019InitialTimeZoneRuleE',
        'N6icu_7021TimeArrayTimeZoneRuleE',
        'N6icu_7012DateTimeRuleE',
        'N6icu_7018TimeZoneTransitionE',
        'N6icu_708TimeZoneE',
        'N6icu_7013BasicTimeZoneE',
        'N6icu_7017RuleBasedTimeZoneE',
        'N6icu_7014SimpleTimeZoneE',
        'N6icu_709VTimeZoneE',
        'N6icu_708CalendarE',
        'N6icu_7017GregorianCalendarE',
        'N6icu_7012CollationKeyE',
        'N6icu_708CollatorE',
        'N6icu_7017RuleBasedCollatorE',
        'N6icu_7015AlphabeticIndexE',
        'N6icu_7015AlphabeticIndex14ImmutableIndexE',
        'N6icu_7014UnicodeFunctorE',
        'N6icu_7014UnicodeMatcherE',
        'N6icu_7013UnicodeFilterE',
        'N6icu_7010UnicodeSetE',
        'N6icu_7018UnicodeSetIteratorE',
        'N6icu_7012RegexPatternE',
        'N6icu_7012RegexMatcherE',
        'N6icu_7010NormalizerE',
        'N6icu_7011Normalizer2E',
        'N6icu_7019FilteredNormalizer2E',
        'N6icu_7014SearchIteratorE',
        'N6icu_7012StringSearchE',
        'N6icu_7011MeasureUnitE',
        'N6icu_707MeasureE',
        'N6icu_7012CurrencyUnitE',
        'N6icu_7014CurrencyAmountE',
        'N6icu_708TimeUnitE',
        'N6icu_7014TimeUnitAmountE',
        'N6icu_7017StringTrieBuilderE',
        'N6icu_7016BytesTrieBuilderE',
        'N6icu_7017UCharsTrieBuilderE',
        'N6icu_7010GenderInfoE',
    ],
    UObject: 
        'N6icu_707UObjectE'
    ,
    'N6icu_7011ReplaceableE': [
        '17PythonReplaceable',
        'N6icu_7013UnicodeStringE',
    ],
    Replaceable: 
        'N6icu_7011ReplaceableE'
    ,
    '17PythonReplaceable': [],
    PythonReplaceable: 
        '17PythonReplaceable'
    ,
    'N6icu_7013UnicodeStringE': '<value is a self-reference, replaced by this string>',
    UnicodeString: 
        'N6icu_7013UnicodeStringE'
    ,
    'N6icu_7011FormattableE': '<value is a self-reference, replaced by this string>',
    Formattable: 
        'N6icu_7011FormattableE'
    ,
    'N6icu_7017StringEnumerationE': '<value is a self-reference, replaced by this string>',
    StringEnumeration: 
        'N6icu_7017StringEnumerationE'
    ,
    'N6icu_706LocaleE': '<value is a self-reference, replaced by this string>',
    Locale: 
        'N6icu_706LocaleE'
    ,
    'N6icu_7014ResourceBundleE': '<value is a self-reference, replaced by this string>',
    ResourceBundle: 
        'N6icu_7014ResourceBundleE'
    ,
    'N6icu_706RegionE': '<value is a self-reference, replaced by this string>',
    Region: 
        'N6icu_706RegionE'
    ,
    'N6icu_7013LocaleBuilderE': '<value is a self-reference, replaced by this string>',
    LocaleBuilder: 
        'N6icu_7013LocaleBuilderE'
    ,
    'N6icu_7014TransliteratorE': '<value is a self-reference, replaced by this string>',
    Transliterator: 
        'N6icu_7014TransliteratorE'
    ,
    'N6icu_7024ForwardCharacterIteratorE': [
        'N6icu_7017CharacterIteratorE',
        'N6icu_7022UCharCharacterIteratorE',
        'N6icu_7023StringCharacterIteratorE',
    ],
    ForwardCharacterIterator: 
        'N6icu_7024ForwardCharacterIteratorE'
    ,
    'N6icu_7017CharacterIteratorE': [
        'N6icu_7022UCharCharacterIteratorE',
        'N6icu_7023StringCharacterIteratorE',
    ],
    CharacterIterator: 
        'N6icu_7017CharacterIteratorE'
    ,
    'N6icu_7022UCharCharacterIteratorE': [
        'N6icu_7023StringCharacterIteratorE',
    ],
    UCharCharacterIterator: 
        'N6icu_7022UCharCharacterIteratorE'
    ,
    'N6icu_7023StringCharacterIteratorE': '<value is a self-reference, replaced by this string>',
    StringCharacterIterator: 
        'N6icu_7023StringCharacterIteratorE'
    ,
    'N6icu_7013BreakIteratorE': [
        'N6icu_7022RuleBasedBreakIteratorE',
        'N6icu_7022RuleBasedBreakIteratorE',
    ],
    BreakIterator: 
        'N6icu_7013BreakIteratorE'
    ,
    'N6icu_7022RuleBasedBreakIteratorE': [
        'N6icu_7022RuleBasedBreakIteratorE',
    ],
    RuleBasedBreakIterator: 
        'N6icu_7022RuleBasedBreakIteratorE'
    ,
    DictionaryBasedBreakIterator: 
        'N6icu_7022RuleBasedBreakIteratorE'
    ,
    'N6icu_7017CanonicalIteratorE': '<value is a self-reference, replaced by this string>',
    CanonicalIterator: 
        'N6icu_7017CanonicalIteratorE'
    ,
    'N6icu_7024CollationElementIteratorE': '<value is a self-reference, replaced by this string>',
    CollationElementIterator: 
        'N6icu_7024CollationElementIteratorE'
    ,
    'N6icu_7013FieldPositionE': '<value is a self-reference, replaced by this string>',
    FieldPosition: 
        'N6icu_7013FieldPositionE'
    ,
    'N6icu_7013ParsePositionE': '<value is a self-reference, replaced by this string>',
    ParsePosition: 
        'N6icu_7013ParsePositionE'
    ,
    'N6icu_706FormatE': [
        'N6icu_7013MeasureFormatE',
        'N6icu_7013MessageFormatE',
        'N6icu_7012PluralFormatE',
        'N6icu_7014TimeUnitFormatE',
        'N6icu_7012SelectFormatE',
        'N6icu_7010DateFormatE',
        'N6icu_7016SimpleDateFormatE',
        'N6icu_7018DateIntervalFormatE',
        'N6icu_7012NumberFormatE',
        'N6icu_7013DecimalFormatE',
        'N6icu_7020CompactDecimalFormatE',
        'N6icu_7021RuleBasedNumberFormatE',
        'N6icu_7012ChoiceFormatE',
    ],
    Format: 
        'N6icu_706FormatE'
    ,
    'N6icu_7013MeasureFormatE': [
        'N6icu_7014TimeUnitFormatE',
    ],
    MeasureFormat: 
        'N6icu_7013MeasureFormatE'
    ,
    'N6icu_7013MessageFormatE': '<value is a self-reference, replaced by this string>',
    MessageFormat: 
        'N6icu_7013MessageFormatE'
    ,
    'N6icu_7011PluralRulesE': '<value is a self-reference, replaced by this string>',
    PluralRules: 
        'N6icu_7011PluralRulesE'
    ,
    'N6icu_7012PluralFormatE': '<value is a self-reference, replaced by this string>',
    PluralFormat: 
        'N6icu_7012PluralFormatE'
    ,
    'N6icu_7014TimeUnitFormatE': '<value is a self-reference, replaced by this string>',
    TimeUnitFormat: 
        'N6icu_7014TimeUnitFormatE'
    ,
    'N6icu_7012SelectFormatE': '<value is a self-reference, replaced by this string>',
    SelectFormat: 
        'N6icu_7012SelectFormatE'
    ,
    'N6icu_7013ListFormatterE': '<value is a self-reference, replaced by this string>',
    ListFormatter: 
        'N6icu_7013ListFormatterE'
    ,
    'N6icu_7017DateFormatSymbolsE': '<value is a self-reference, replaced by this string>',
    DateFormatSymbols: 
        'N6icu_7017DateFormatSymbolsE'
    ,
    'N6icu_7010DateFormatE': [
        'N6icu_7016SimpleDateFormatE',
    ],
    DateFormat: 
        'N6icu_7010DateFormatE'
    ,
    'N6icu_7016SimpleDateFormatE': '<value is a self-reference, replaced by this string>',
    SimpleDateFormat: 
        'N6icu_7016SimpleDateFormatE'
    ,
    'N6icu_7024DateTimePatternGeneratorE': '<value is a self-reference, replaced by this string>',
    DateTimePatternGenerator: 
        'N6icu_7024DateTimePatternGeneratorE'
    ,
    'N6icu_7012DateIntervalE': '<value is a self-reference, replaced by this string>',
    DateInterval: 
        'N6icu_7012DateIntervalE'
    ,
    'N6icu_7016DateIntervalInfoE': '<value is a self-reference, replaced by this string>',
    DateIntervalInfo: 
        'N6icu_7016DateIntervalInfoE'
    ,
    'N6icu_7018DateIntervalFormatE': '<value is a self-reference, replaced by this string>',
    DateIntervalFormat: 
        'N6icu_7018DateIntervalFormatE'
    ,
    'N6icu_7025RelativeDateTimeFormatterE': '<value is a self-reference, replaced by this string>',
    RelativeDateTimeFormatter: 
        'N6icu_7025RelativeDateTimeFormatterE'
    ,
    'N6icu_7014MessagePatternE': '<value is a self-reference, replaced by this string>',
    MessagePattern: 
        'N6icu_7014MessagePatternE'
    ,
    'N6icu_7020DecimalFormatSymbolsE': '<value is a self-reference, replaced by this string>',
    DecimalFormatSymbols: 
        'N6icu_7020DecimalFormatSymbolsE'
    ,
    'N6icu_7012NumberFormatE': [
        'N6icu_7013DecimalFormatE',
        'N6icu_7020CompactDecimalFormatE',
        'N6icu_7021RuleBasedNumberFormatE',
        'N6icu_7012ChoiceFormatE',
    ],
    NumberFormat: 
        'N6icu_7012NumberFormatE'
    ,
    'N6icu_7018CurrencyPluralInfoE': '<value is a self-reference, replaced by this string>',
    CurrencyPluralInfo: 
        'N6icu_7018CurrencyPluralInfoE'
    ,
    'N6icu_7015NumberingSystemE': '<value is a self-reference, replaced by this string>',
    NumberingSystem: 
        'N6icu_7015NumberingSystemE'
    ,
    'N6icu_7013DecimalFormatE': [
        'N6icu_7020CompactDecimalFormatE',
    ],
    DecimalFormat: 
        'N6icu_7013DecimalFormatE'
    ,
    'N6icu_7020CompactDecimalFormatE': '<value is a self-reference, replaced by this string>',
    CompactDecimalFormat: 
        'N6icu_7020CompactDecimalFormatE'
    ,
    'N6icu_7021RuleBasedNumberFormatE': '<value is a self-reference, replaced by this string>',
    RuleBasedNumberFormat: 
        'N6icu_7021RuleBasedNumberFormatE'
    ,
    'N6icu_7012ChoiceFormatE': '<value is a self-reference, replaced by this string>',
    ChoiceFormat: 
        'N6icu_7012ChoiceFormatE'
    ,
    'N6icu_7012TimeZoneRuleE': [
        'N6icu_7018AnnualTimeZoneRuleE',
        'N6icu_7019InitialTimeZoneRuleE',
        'N6icu_7021TimeArrayTimeZoneRuleE',
    ],
    TimeZoneRule: 
        'N6icu_7012TimeZoneRuleE'
    ,
    'N6icu_7018AnnualTimeZoneRuleE': '<value is a self-reference, replaced by this string>',
    AnnualTimeZoneRule: 
        'N6icu_7018AnnualTimeZoneRuleE'
    ,
    'N6icu_7019InitialTimeZoneRuleE': '<value is a self-reference, replaced by this string>',
    InitialTimeZoneRule: 
        'N6icu_7019InitialTimeZoneRuleE'
    ,
    'N6icu_7021TimeArrayTimeZoneRuleE': '<value is a self-reference, replaced by this string>',
    TimeArrayTimeZoneRule: 
        'N6icu_7021TimeArrayTimeZoneRuleE'
    ,
    'N6icu_7012DateTimeRuleE': '<value is a self-reference, replaced by this string>',
    DateTimeRule: 
        'N6icu_7012DateTimeRuleE'
    ,
    'N6icu_7018TimeZoneTransitionE': '<value is a self-reference, replaced by this string>',
    TimeZoneTransition: 
        'N6icu_7018TimeZoneTransitionE'
    ,
    'N6icu_708TimeZoneE': [
        'N6icu_7013BasicTimeZoneE',
        'N6icu_7017RuleBasedTimeZoneE',
        'N6icu_7014SimpleTimeZoneE',
        'N6icu_709VTimeZoneE',
    ],
    TimeZone: 
        'N6icu_708TimeZoneE'
    ,
    'N6icu_7013BasicTimeZoneE': [
        'N6icu_7017RuleBasedTimeZoneE',
        'N6icu_7014SimpleTimeZoneE',
        'N6icu_709VTimeZoneE',
    ],
    BasicTimeZone: 
        'N6icu_7013BasicTimeZoneE'
    ,
    'N6icu_7017RuleBasedTimeZoneE': '<value is a self-reference, replaced by this string>',
    RuleBasedTimeZone: 
        'N6icu_7017RuleBasedTimeZoneE'
    ,
    'N6icu_7014SimpleTimeZoneE': '<value is a self-reference, replaced by this string>',
    SimpleTimeZone: 
        'N6icu_7014SimpleTimeZoneE'
    ,
    'N6icu_709VTimeZoneE': '<value is a self-reference, replaced by this string>',
    VTimeZone: 
        'N6icu_709VTimeZoneE'
    ,
    'N6icu_708CalendarE': [
        'N6icu_7017GregorianCalendarE',
    ],
    Calendar: 
        'N6icu_708CalendarE'
    ,
    'N6icu_7017GregorianCalendarE': '<value is a self-reference, replaced by this string>',
    GregorianCalendar: 
        'N6icu_7017GregorianCalendarE'
    ,
    'N6icu_7012CollationKeyE': '<value is a self-reference, replaced by this string>',
    CollationKey: 
        'N6icu_7012CollationKeyE'
    ,
    'N6icu_708CollatorE': [
        'N6icu_7017RuleBasedCollatorE',
    ],
    Collator: 
        'N6icu_708CollatorE'
    ,
    'N6icu_7017RuleBasedCollatorE': '<value is a self-reference, replaced by this string>',
    RuleBasedCollator: 
        'N6icu_7017RuleBasedCollatorE'
    ,
    'N6icu_7015AlphabeticIndexE': '<value is a self-reference, replaced by this string>',
    AlphabeticIndex: 
        'N6icu_7015AlphabeticIndexE'
    ,
    'N6icu_7015AlphabeticIndex14ImmutableIndexE': '<value is a self-reference, replaced by this string>',
    ImmutableIndex: 
        'N6icu_7015AlphabeticIndex14ImmutableIndexE'
    ,
    'N6icu_7014UnicodeFunctorE': '<value is a self-reference, replaced by this string>',
    UnicodeFunctor: 
        'N6icu_7014UnicodeFunctorE'
    ,
    'N6icu_7014UnicodeMatcherE': '<value is a self-reference, replaced by this string>',
    UnicodeMatcher: 
        'N6icu_7014UnicodeMatcherE'
    ,
    'N6icu_7013UnicodeFilterE': [
        'N6icu_7010UnicodeSetE',
    ],
    UnicodeFilter: 
        'N6icu_7013UnicodeFilterE'
    ,
    'N6icu_7010UnicodeSetE': '<value is a self-reference, replaced by this string>',
    UnicodeSet: 
        'N6icu_7010UnicodeSetE'
    ,
    'N6icu_7018UnicodeSetIteratorE': '<value is a self-reference, replaced by this string>',
    UnicodeSetIterator: 
        'N6icu_7018UnicodeSetIteratorE'
    ,
    'N6icu_7012RegexPatternE': '<value is a self-reference, replaced by this string>',
    RegexPattern: 
        'N6icu_7012RegexPatternE'
    ,
    'N6icu_7012RegexMatcherE': '<value is a self-reference, replaced by this string>',
    RegexMatcher: 
        'N6icu_7012RegexMatcherE'
    ,
    'N6icu_7010NormalizerE': '<value is a self-reference, replaced by this string>',
    Normalizer: 
        'N6icu_7010NormalizerE'
    ,
    'N6icu_7011Normalizer2E': [
        'N6icu_7019FilteredNormalizer2E',
    ],
    Normalizer2: 
        'N6icu_7011Normalizer2E'
    ,
    'N6icu_7019FilteredNormalizer2E': '<value is a self-reference, replaced by this string>',
    FilteredNormalizer2: 
        'N6icu_7019FilteredNormalizer2E'
    ,
    'N6icu_7014SearchIteratorE': [
        'N6icu_7012StringSearchE',
    ],
    SearchIterator: 
        'N6icu_7014SearchIteratorE'
    ,
    'N6icu_7012StringSearchE': '<value is a self-reference, replaced by this string>',
    StringSearch: 
        'N6icu_7012StringSearchE'
    ,
    'N6icu_7011MeasureUnitE': [
        'N6icu_7012CurrencyUnitE',
        'N6icu_708TimeUnitE',
    ],
    MeasureUnit: 
        'N6icu_7011MeasureUnitE'
    ,
    'N6icu_707MeasureE': [
        'N6icu_7014CurrencyAmountE',
        'N6icu_7014TimeUnitAmountE',
    ],
    Measure: 
        'N6icu_707MeasureE'
    ,
    'N6icu_7012CurrencyUnitE': '<value is a self-reference, replaced by this string>',
    CurrencyUnit: 
        'N6icu_7012CurrencyUnitE'
    ,
    'N6icu_7014CurrencyAmountE': '<value is a self-reference, replaced by this string>',
    CurrencyAmount: 
        'N6icu_7014CurrencyAmountE'
    ,
    'N6icu_708TimeUnitE': '<value is a self-reference, replaced by this string>',
    TimeUnit: 
        'N6icu_708TimeUnitE'
    ,
    'N6icu_7014TimeUnitAmountE': '<value is a self-reference, replaced by this string>',
    TimeUnitAmount: 
        'N6icu_7014TimeUnitAmountE'
    ,
    'N6icu_7017StringTrieBuilderE': [
        'N6icu_7016BytesTrieBuilderE',
        'N6icu_7017UCharsTrieBuilderE',
    ],
    StringTrieBuilder: 
        'N6icu_7017StringTrieBuilderE'
    ,
    'N6icu_7016BytesTrieBuilderE': '<value is a self-reference, replaced by this string>',
    BytesTrieBuilder: 
        'N6icu_7016BytesTrieBuilderE'
    ,
    'N6icu_7017UCharsTrieBuilderE': '<value is a self-reference, replaced by this string>',
    UCharsTrieBuilder: 
        'N6icu_7017UCharsTrieBuilderE'
    ,
    'N6icu_7010GenderInfoE': '<value is a self-reference, replaced by this string>',
    GenderInfo: 
        'N6icu_7010GenderInfoE'
    ,
}

