# encoding: utf-8
# module samba.dcerpc.drsblobs
# from /usr/lib/python3/dist-packages/samba/dcerpc/drsblobs.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" drsblobs DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


# Variables with simple values

ENCRYPTED_SECRET_MAGIC_VALUE = 3395071469

ENC_SECRET_AES_128_AEAD = 1

EXTENDED_ERROR_COMPUTER_NAME_NOT_PRESENT = 2

EXTENDED_ERROR_COMPUTER_NAME_PRESENT = 1

EXTENDED_ERROR_PARAM_TYPE_ASCII_STRING = 1

EXTENDED_ERROR_PARAM_TYPE_BLOB = 7
EXTENDED_ERROR_PARAM_TYPE_NONE = 6
EXTENDED_ERROR_PARAM_TYPE_UINT16 = 4
EXTENDED_ERROR_PARAM_TYPE_UINT32 = 3
EXTENDED_ERROR_PARAM_TYPE_UINT64 = 5

EXTENDED_ERROR_PARAM_TYPE_UNICODE_STRING = 2

FOREST_TRUST_DOMAIN_INFO = 2

FOREST_TRUST_TOP_LEVEL_NAME = 0

FOREST_TRUST_TOP_LEVEL_NAME_EX = 1

PREFIX_MAP_VERSION_DSDB = 1146307650

SUPPLEMENTAL_CREDENTIALS_PREFIX = '                                                '
SUPPLEMENTAL_CREDENTIALS_SIGNATURE = 80

# no functions
# classes

from .drsblobs_abstract_syntax import drsblobs_abstract_syntax
from .abstract_syntax import abstract_syntax
from .AuthenticationInformation import AuthenticationInformation
from .AuthenticationInformationArray import AuthenticationInformationArray
from .AuthInfo import AuthInfo
from .AuthInfoClear import AuthInfoClear
from .AuthInfoNone import AuthInfoNone
from .AuthInfoNT4Owf import AuthInfoNT4Owf
from .AuthInfoVersion import AuthInfoVersion
from .drsblobs import drsblobs
from .drsuapi_MSPrefixMap_Ctr import drsuapi_MSPrefixMap_Ctr
from .drsuapi_MSPrefixMap_Entry import drsuapi_MSPrefixMap_Entry
from .DsCompressedChunk import DsCompressedChunk
from .EncryptedSecret import EncryptedSecret
from .EncryptedSecretHeader import EncryptedSecretHeader
from .ExtendedErrorAString import ExtendedErrorAString
from .ExtendedErrorBlob import ExtendedErrorBlob
from .ExtendedErrorComputerName import ExtendedErrorComputerName
from .ExtendedErrorComputerNameU import ExtendedErrorComputerNameU
from .ExtendedErrorInfo import ExtendedErrorInfo
from .ExtendedErrorInfoPtr import ExtendedErrorInfoPtr
from .ExtendedErrorParam import ExtendedErrorParam
from .ExtendedErrorParamU import ExtendedErrorParamU
from .ExtendedErrorUString import ExtendedErrorUString
from .ForestTrustData import ForestTrustData
from .ForestTrustDataBinaryData import ForestTrustDataBinaryData
from .ForestTrustDataDomainInfo import ForestTrustDataDomainInfo
from .ForestTrustInfo import ForestTrustInfo
from .ForestTrustInfoRecord import ForestTrustInfoRecord
from .ForestTrustInfoRecordArmor import ForestTrustInfoRecordArmor
from .ForestTrustString import ForestTrustString
from .ldapControlDirSyncBlob import ldapControlDirSyncBlob
from .ldapControlDirSyncCookie import ldapControlDirSyncCookie
from .ldapControlDirSyncExtra import ldapControlDirSyncExtra
from .package_PackagesBlob import package_PackagesBlob
from .package_PrimaryCLEARTEXTBlob import package_PrimaryCLEARTEXTBlob
from .package_PrimaryKerberosBlob import package_PrimaryKerberosBlob
from .package_PrimaryKerberosCtr import package_PrimaryKerberosCtr
from .package_PrimaryKerberosCtr3 import package_PrimaryKerberosCtr3
from .package_PrimaryKerberosCtr4 import package_PrimaryKerberosCtr4
from .package_PrimaryKerberosKey3 import package_PrimaryKerberosKey3
from .package_PrimaryKerberosKey4 import package_PrimaryKerberosKey4
from .package_PrimaryKerberosString import package_PrimaryKerberosString
from .package_PrimarySambaGPGBlob import package_PrimarySambaGPGBlob
from .package_PrimaryUserPasswordBlob import package_PrimaryUserPasswordBlob
from .package_PrimaryUserPasswordValue import package_PrimaryUserPasswordValue
from .package_PrimaryWDigestBlob import package_PrimaryWDigestBlob
from .package_PrimaryWDigestHash import package_PrimaryWDigestHash
from .partialAttributeSetBlob import partialAttributeSetBlob
from .partialAttributeSetCtr import partialAttributeSetCtr
from .partialAttributeSetCtr1 import partialAttributeSetCtr1
from .PlaintextSecret import PlaintextSecret
from .prefixMapBlob import prefixMapBlob
from .prefixMapCtr import prefixMapCtr
from .replPropertyMetaData1 import replPropertyMetaData1
from .replPropertyMetaDataBlob import replPropertyMetaDataBlob
from .replPropertyMetaDataCtr import replPropertyMetaDataCtr
from .replPropertyMetaDataCtr1 import replPropertyMetaDataCtr1
from .replUpToDateVectorBlob import replUpToDateVectorBlob
from .replUpToDateVectorCtr import replUpToDateVectorCtr
from .replUpToDateVectorCtr1 import replUpToDateVectorCtr1
from .replUpToDateVectorCtr2 import replUpToDateVectorCtr2
from .repsFromTo import repsFromTo
from .repsFromTo1 import repsFromTo1
from .repsFromTo1OtherInfo import repsFromTo1OtherInfo
from .repsFromTo2 import repsFromTo2
from .repsFromTo2OtherInfo import repsFromTo2OtherInfo
from .repsFromToBlob import repsFromToBlob
from .schedule import schedule
from .scheduleHeader import scheduleHeader
from .scheduleSlots import scheduleSlots
from .schemaInfoBlob import schemaInfoBlob
from .supplementalCredentialsBlob import supplementalCredentialsBlob
from .supplementalCredentialsPackage import supplementalCredentialsPackage
from .supplementalCredentialsSubBlob import supplementalCredentialsSubBlob
from .trustAuthInOutBlob import trustAuthInOutBlob
from .trustDomainPasswords import trustDomainPasswords
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>'

__spec__ = None # (!) real value is "ModuleSpec(name='samba.dcerpc.drsblobs', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f4211d2db40>, origin='/usr/lib/python3/dist-packages/samba/dcerpc/drsblobs.cpython-310-x86_64-linux-gnu.so')"

