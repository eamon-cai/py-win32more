from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Devices.WebServicesOnDevices
import Windows.Win32.Foundation
import Windows.Win32.Networking.WinSock
import Windows.Win32.Security.Cryptography
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
WSD_DEFAULT_HOSTING_ADDRESS: String = 'http://*:5357/'
WSD_DEFAULT_SECURE_HOSTING_ADDRESS: String = 'https://*:5358/'
WSD_DEFAULT_EVENTING_ADDRESS: String = 'http://*:5357/'
WSDAPI_OPTION_MAX_INBOUND_MESSAGE_SIZE: UInt32 = 1
WSDAPI_OPTION_TRACE_XML_TO_DEBUGGER: UInt32 = 2
WSDAPI_OPTION_TRACE_XML_TO_FILE: UInt32 = 3
WSDAPI_SSL_CERT_APPLY_DEFAULT_CHECKS: UInt32 = 0
WSDAPI_SSL_CERT_IGNORE_REVOCATION: UInt32 = 1
WSDAPI_SSL_CERT_IGNORE_EXPIRY: UInt32 = 2
WSDAPI_SSL_CERT_IGNORE_WRONG_USAGE: UInt32 = 4
WSDAPI_SSL_CERT_IGNORE_UNKNOWN_CA: UInt32 = 8
WSDAPI_SSL_CERT_IGNORE_INVALID_CN: UInt32 = 16
WSDAPI_COMPACTSIG_ACCEPT_ALL_MESSAGES: UInt32 = 1
WSD_SECURITY_HTTP_AUTH_SCHEME_NEGOTIATE: UInt32 = 1
WSD_SECURITY_HTTP_AUTH_SCHEME_NTLM: UInt32 = 2
WSDAPI_ADDRESSFAMILY_IPV4: UInt32 = 1
WSDAPI_ADDRESSFAMILY_IPV6: UInt32 = 2
@winfunctype('wsdapi.dll')
def WSDCreateUdpMessageParameters(ppTxParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDUdpMessageParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateUdpAddress(ppAddress: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDUdpAddress_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateHttpMessageParameters(ppTxParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDHttpMessageParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateHttpAddress(ppAddress: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDHttpAddress_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateOutboundAttachment(ppAttachment: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDOutboundAttachment_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLGetNameFromBuiltinNamespace(pszNamespace: Windows.Win32.Foundation.PWSTR, pszName: Windows.Win32.Foundation.PWSTR, ppName: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLCreateContext(ppContext: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryProvider(pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppProvider: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryProvider2(pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, pConfigParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head), dwConfigParamCount: UInt32, ppProvider: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryPublisher(pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppPublisher: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisher_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryPublisher2(pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, pConfigParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head), dwConfigParamCount: UInt32, ppPublisher: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisher_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceProxy(pszDeviceId: Windows.Win32.Foundation.PWSTR, pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppDeviceProxy: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceProxyAdvanced(pszDeviceId: Windows.Win32.Foundation.PWSTR, pDeviceAddress: Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head, pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppDeviceProxy: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceProxy2(pszDeviceId: Windows.Win32.Foundation.PWSTR, pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, pConfigParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head), dwConfigParamCount: UInt32, ppDeviceProxy: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceHost(pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppDeviceHost: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHost_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceHostAdvanced(pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppHostAddresses: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head), dwHostAddressCount: UInt32, ppDeviceHost: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHost_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceHost2(pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, pConfigParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head), dwConfigParamCount: UInt32, ppDeviceHost: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHost_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDSetConfigurationOption(dwOption: UInt32, pVoid: c_void_p, cbInBuffer: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDGetConfigurationOption(dwOption: UInt32, pVoid: c_void_p, cbOutBuffer: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDAllocateLinkedMemory(pParent: c_void_p, cbSize: UIntPtr) -> c_void_p: ...
@winfunctype('wsdapi.dll')
def WSDFreeLinkedMemory(pVoid: c_void_p) -> Void: ...
@winfunctype('wsdapi.dll')
def WSDAttachLinkedMemory(pParent: c_void_p, pChild: c_void_p) -> Void: ...
@winfunctype('wsdapi.dll')
def WSDDetachLinkedMemory(pVoid: c_void_p) -> Void: ...
@winfunctype('wsdapi.dll')
def WSDXMLBuildAnyForSingleElement(pElementName: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head), pszText: Windows.Win32.Foundation.PWSTR, ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLGetValueFromAny(pszNamespace: Windows.Win32.Foundation.PWSTR, pszName: Windows.Win32.Foundation.PWSTR, pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), ppszValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLAddSibling(pFirst: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pSecond: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLAddChild(pParent: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pChild: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLCleanupElement(pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDGenerateFault(pszCode: Windows.Win32.Foundation.PWSTR, pszSubCode: Windows.Win32.Foundation.PWSTR, pszReason: Windows.Win32.Foundation.PWSTR, pszDetail: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppFault: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDGenerateFaultEx(pCode: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head), pSubCode: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head), pReasons: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head), pszDetail: Windows.Win32.Foundation.PWSTR, ppFault: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDUriEncode(source: Windows.Win32.Foundation.PWSTR, cchSource: UInt32, destOut: POINTER(Windows.Win32.Foundation.PWSTR), cchDestOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDUriDecode(source: Windows.Win32.Foundation.PWSTR, cchSource: UInt32, destOut: POINTER(Windows.Win32.Foundation.PWSTR), cchDestOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
DeviceDiscoveryMechanism = Int32
DeviceDiscoveryMechanism_MulticastDiscovery: DeviceDiscoveryMechanism = 0
DeviceDiscoveryMechanism_DirectedDiscovery: DeviceDiscoveryMechanism = 1
DeviceDiscoveryMechanism_SecureDirectedDiscovery: DeviceDiscoveryMechanism = 2
class IWSDAddress(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b9574c6c-12a6-4f74-93-a1-33-18-ff-60-57-59')
    @commethod(3)
    def Serialize(self, pszBuffer: Windows.Win32.Foundation.PWSTR, cchLength: UInt32, fSafe: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Deserialize(self, pszBuffer: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDAsyncCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a63e109d-ce72-49e2-ba-98-e8-45-f5-ee-16-66')
    @commethod(3)
    def AsyncOperationComplete(self, pAsyncResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head, pAsyncState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDAsyncResult(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('11a9852a-8dd8-423e-b5-37-93-56-db-4f-bf-b8')
    @commethod(3)
    def SetCallback(self, pCallback: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, pAsyncState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetWaitHandle(self, hWaitHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HasCompleted(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAsyncState(self, ppAsyncState: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Abort(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetEvent(self, pEvent: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetEndpointProxy(self, ppEndpoint: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDEndpointProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDAttachment(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5d55a616-9df8-4b09-b1-56-9b-a3-51-a4-8b-76')
class IWSDDeviceHost(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('917fe891-3d13-4138-98-09-93-4c-8a-be-b1-2c')
    @commethod(3)
    def Init(self, pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppHostAddresses: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head), dwHostAddressCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Start(self, ullInstanceId: UInt64, pScopeList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pNotificationSink: Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHostNotify_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Terminate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RegisterPortType(self, pPortType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_PORT_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetMetadata(self, pThisModelMetadata: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_MODEL_METADATA_head), pThisDeviceMetadata: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_DEVICE_METADATA_head), pHostMetadata: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_HOST_METADATA_head), pCustomMetadata: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RegisterService(self, pszServiceId: Windows.Win32.Foundation.PWSTR, pService: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RetireService(self, pszServiceId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddDynamicService(self, pszServiceId: Windows.Win32.Foundation.PWSTR, pszEndpointAddress: Windows.Win32.Foundation.PWSTR, pPortType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_PORT_TYPE_head), pPortName: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pService: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveDynamicService(self, pszServiceId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetServiceDiscoverable(self, pszServiceId: Windows.Win32.Foundation.PWSTR, fDiscoverable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SignalEvent(self, pszServiceId: Windows.Win32.Foundation.PWSTR, pBody: c_void_p, pOperation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDDeviceHostNotify(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b5bee9f9-eeda-41fe-96-f7-f4-5e-14-99-0f-b0')
    @commethod(3)
    def GetService(self, pszServiceId: Windows.Win32.Foundation.PWSTR, ppService: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDDeviceProxy(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('eee0c031-c578-4c0e-9a-3b-97-3c-35-f4-09-db')
    @commethod(3)
    def Init(self, pszDeviceId: Windows.Win32.Foundation.PWSTR, pDeviceAddress: Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head, pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, pSponsor: Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginGetMetadata(self, ppResult: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndGetMetadata(self, pResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetHostMetadata(self, ppHostMetadata: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_HOST_METADATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetThisModelMetadata(self, ppManufacturerMetadata: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_MODEL_METADATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetThisDeviceMetadata(self, ppThisDeviceMetadata: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_DEVICE_METADATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAllMetadata(self, ppMetadata: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetServiceProxyById(self, pszServiceId: Windows.Win32.Foundation.PWSTR, ppServiceProxy: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetServiceProxyByType(self, pType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head), ppServiceProxy: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetEndpointProxy(self, ppProxy: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDEndpointProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDEndpointProxy(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1860d430-b24c-4975-9f-90-db-b3-9b-aa-24-ec')
    @commethod(3)
    def SendOneWayRequest(self, pBody: c_void_p, pOperation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendTwoWayRequest(self, pBody: c_void_p, pOperation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), pResponseContext: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SYNCHRONOUS_RESPONSE_CONTEXT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SendTwoWayRequestAsync(self, pBody: c_void_p, pOperation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), pAsyncState: Windows.Win32.System.Com.IUnknown_head, pCallback: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, pResult: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AbortAsyncOperation(self, pAsyncResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ProcessFault(self, pFault: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetErrorInfo(self, ppszErrorInfo: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFaultInfo(self, ppFault: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDEventingStatus(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('49b17f52-637a-407a-ae-99-fb-e8-2a-4d-38-c0')
    @commethod(3)
    def SubscriptionRenewed(self, pszSubscriptionAction: Windows.Win32.Foundation.PWSTR) -> Void: ...
    @commethod(4)
    def SubscriptionRenewalFailed(self, pszSubscriptionAction: Windows.Win32.Foundation.PWSTR, hr: Windows.Win32.Foundation.HRESULT) -> Void: ...
    @commethod(5)
    def SubscriptionEnded(self, pszSubscriptionAction: Windows.Win32.Foundation.PWSTR) -> Void: ...
class IWSDHttpAddress(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDTransportAddress
    Guid = Guid('d09ac7bd-2a3e-4b85-86-05-27-37-ff-3e-4e-a0')
    @commethod(10)
    def GetSecure(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetSecure(self, fSecure: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetPath(self, ppszPath: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetPath(self, pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDHttpAuthParameters(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0b476df0-8dac-480d-b0-5c-99-78-1a-58-84-aa')
    @commethod(3)
    def GetClientAccessToken(self, phToken: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAuthType(self, pAuthType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDHttpMessageParameters(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters
    Guid = Guid('540bd122-5c83-4dec-b3-96-ea-62-a2-69-7f-df')
    @commethod(8)
    def SetInboundHttpHeaders(self, pszHeaders: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetInboundHttpHeaders(self, ppszHeaders: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetOutboundHttpHeaders(self, pszHeaders: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOutboundHttpHeaders(self, ppszHeaders: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetID(self, pszId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetID(self, ppszId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetContext(self, pContext: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetContext(self, ppContext: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDInboundAttachment(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDAttachment
    Guid = Guid('5bd6ca65-233c-4fb8-9f-7a-26-41-61-96-55-c9')
    @commethod(3)
    def Read(self, pBuffer: POINTER(Byte), dwBytesToRead: UInt32, pdwNumberOfBytesRead: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDMessageParameters(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1fafe8a2-e6fc-4b80-b6-cf-b7-d4-5c-41-6d-7c')
    @commethod(3)
    def GetLocalAddress(self, ppAddress: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetLocalAddress(self, pAddress: Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRemoteAddress(self, ppAddress: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRemoteAddress(self, pAddress: Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLowerParameters(self, ppTxParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDMetadataExchange(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('06996d57-1d67-4928-93-07-3d-78-33-fd-b8-46')
    @commethod(3)
    def GetMetadata(self, MetadataOut: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDOutboundAttachment(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDAttachment
    Guid = Guid('aa302f8d-5a22-4ba5-b3-92-aa-84-86-f4-c1-5d')
    @commethod(3)
    def Write(self, pBuffer: POINTER(Byte), dwBytesToWrite: UInt32, pdwNumberOfBytesWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Abort(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDSSLClientCertificate(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('de105e87-a0da-418e-98-ad-27-b9-ee-d8-7b-dc')
    @commethod(3)
    def GetClientCertificate(self, ppCertContext: POINTER(POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMappedAccessToken(self, phToken: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDScopeMatchingRule(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fcafe424-fef5-481a-bd-9f-33-ce-05-74-25-6f')
    @commethod(3)
    def GetScopeRule(self, ppszScopeMatchingRule: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MatchScopes(self, pszScope1: Windows.Win32.Foundation.PWSTR, pszScope2: Windows.Win32.Foundation.PWSTR, pfMatch: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDServiceMessaging(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('94974cf4-0cab-460d-a3-f6-7a-0a-d6-23-c0-e6')
    @commethod(3)
    def SendResponse(self, pBody: c_void_p, pOperation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FaultRequest(self, pRequestHeader: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_HEADER_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head, pFault: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDServiceProxy(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDMetadataExchange
    Guid = Guid('d4c7fb9c-03ab-4175-9d-67-09-4f-af-eb-f4-87')
    @commethod(4)
    def BeginGetMetadata(self, ppResult: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndGetMetadata(self, pResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head, ppMetadata: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetServiceMetadata(self, ppServiceMetadata: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SubscribeToOperation(self, pOperation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), pUnknown: Windows.Win32.System.Com.IUnknown_head, pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UnsubscribeToOperation(self, pOperation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetEventingStatusCallback(self, pStatus: Windows.Win32.Devices.WebServicesOnDevices.IWSDEventingStatus_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetEndpointProxy(self, ppProxy: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDEndpointProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDServiceProxyEventing(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceProxy
    Guid = Guid('f9279d6d-1012-4a94-b8-cc-fd-35-d2-20-2b-fe')
    @commethod(11)
    def SubscribeToMultipleOperations(self, pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pUnknown: Windows.Win32.System.Com.IUnknown_head, pExpires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), ppExpires: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def BeginSubscribeToMultipleOperations(self, pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pUnknown: Windows.Win32.System.Com.IUnknown_head, pExpires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAsyncState: Windows.Win32.System.Com.IUnknown_head, pAsyncCallback: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, ppResult: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EndSubscribeToMultipleOperations(self, pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head, ppExpires: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UnsubscribeToMultipleOperations(self, pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def BeginUnsubscribeToMultipleOperations(self, pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAsyncState: Windows.Win32.System.Com.IUnknown_head, pAsyncCallback: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, ppResult: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EndUnsubscribeToMultipleOperations(self, pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def RenewMultipleOperations(self, pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pExpires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), ppExpires: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def BeginRenewMultipleOperations(self, pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pExpires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAsyncState: Windows.Win32.System.Com.IUnknown_head, pAsyncCallback: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, ppResult: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def EndRenewMultipleOperations(self, pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head, ppExpires: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetStatusForMultipleOperations(self, pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), ppExpires: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def BeginGetStatusForMultipleOperations(self, pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAsyncState: Windows.Win32.System.Com.IUnknown_head, pAsyncCallback: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, ppResult: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def EndGetStatusForMultipleOperations(self, pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head, ppExpires: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDSignatureProperty(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('03ce20aa-71c4-45e2-b3-2e-37-66-c6-1c-79-0f')
    @commethod(3)
    def IsMessageSigned(self, pbSigned: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsMessageSignatureTrusted(self, pbSignatureTrusted: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetKeyInfo(self, pbKeyInfo: POINTER(Byte), pdwKeyInfoSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSignature(self, pbSignature: POINTER(Byte), pdwSignatureSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSignedInfoHash(self, pbSignedInfoHash: POINTER(Byte), pdwHashSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDTransportAddress(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress
    Guid = Guid('70d23498-4ee6-4340-a3-df-d8-45-d2-23-54-67')
    @commethod(5)
    def GetPort(self, pwPort: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPort(self, wPort: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTransportAddress(self, ppszAddress: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTransportAddressEx(self, fSafe: Windows.Win32.Foundation.BOOL, ppszAddress: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetTransportAddress(self, pszAddress: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDUdpAddress(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDTransportAddress
    Guid = Guid('74d6124a-a441-4f78-a1-eb-97-a8-d1-99-68-93')
    @commethod(10)
    def SetSockaddr(self, pSockAddr: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSockaddr(self, pSockAddr: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetExclusive(self, fExclusive: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetExclusive(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetMessageType(self, messageType: Windows.Win32.Devices.WebServicesOnDevices.WSDUdpMessageType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetMessageType(self, pMessageType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDUdpMessageType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetTTL(self, dwTTL: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetTTL(self, pdwTTL: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetAlias(self, pAlias: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetAlias(self, pAlias: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDUdpMessageParameters(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters
    Guid = Guid('9934149f-8f0c-447b-aa-0b-73-12-4b-0c-a7-f0')
    @commethod(8)
    def SetRetransmitParams(self, pParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDUdpRetransmitParams_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRetransmitParams(self, pParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDUdpRetransmitParams_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDXMLContext(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('75d8f3ee-3e5a-43b4-a1-5a-bc-f6-88-74-60-c0')
    @commethod(3)
    def AddNamespace(self, pszUri: Windows.Win32.Foundation.PWSTR, pszSuggestedPrefix: Windows.Win32.Foundation.PWSTR, ppNamespace: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddNameToNamespace(self, pszUri: Windows.Win32.Foundation.PWSTR, pszName: Windows.Win32.Foundation.PWSTR, ppName: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNamespaces(self, pNamespaces: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head)), wNamespacesCount: UInt16, bLayerNumber: Byte) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTypes(self, pTypes: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE_head)), dwTypesCount: UInt32, bLayerNumber: Byte) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveredService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4bad8a3b-b374-4420-96-32-aa-c9-45-b3-74-aa')
    @commethod(3)
    def GetEndpointReference(self, ppEndpointReference: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTypes(self, ppTypesList: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetScopes(self, ppScopesList: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetXAddrs(self, ppXAddrsList: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMetadataVersion(self, pullMetadataVersion: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetExtendedDiscoXML(self, ppHeaderAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)), ppBodyAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetProbeResolveTag(self, ppszTag: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRemoteTransportAddress(self, ppszRemoteTransportAddress: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetLocalTransportAddress(self, ppszLocalTransportAddress: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLocalInterfaceGUID(self, pGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetInstanceId(self, pullInstanceId: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveryProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8ffc8e55-f0eb-480f-88-b7-b4-35-dd-28-1d-45')
    @commethod(3)
    def SetAddressFamily(self, dwAddressFamily: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Attach(self, pSink: Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryProviderNotify_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Detach(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SearchById(self, pszId: Windows.Win32.Foundation.PWSTR, pszTag: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SearchByAddress(self, pszAddress: Windows.Win32.Foundation.PWSTR, pszTag: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SearchByType(self, pTypesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pszMatchBy: Windows.Win32.Foundation.PWSTR, pszTag: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetXMLContext(self, ppContext: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveryProviderNotify(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('73ee3ced-b6e6-4329-a5-46-3e-8a-d4-65-63-d2')
    @commethod(3)
    def Add(self, pService: Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveredService_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Remove(self, pService: Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveredService_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SearchFailed(self, hr: Windows.Win32.Foundation.HRESULT, pszTag: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SearchComplete(self, pszTag: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveryPublisher(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ae01e1a8-3ff9-4148-81-16-05-7c-c6-16-fe-13')
    @commethod(3)
    def SetAddressFamily(self, dwAddressFamily: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterNotificationSink(self, pSink: Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisherNotify_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UnRegisterNotificationSink(self, pSink: Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisherNotify_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Publish(self, pszId: Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnPublish(self, pszId: Windows.Win32.Foundation.PWSTR, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: Windows.Win32.Foundation.PWSTR, pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MatchProbe(self, pProbeMessage: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head, pszId: Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def MatchResolve(self, pResolveMessage: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head, pszId: Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def PublishEx(self, pszId: Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pHeaderAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pReferenceParameterAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pPolicyAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pEndpointReferenceAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def MatchProbeEx(self, pProbeMessage: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head, pszId: Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pHeaderAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pReferenceParameterAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pPolicyAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pEndpointReferenceAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def MatchResolveEx(self, pResolveMessage: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head, pszId: Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pHeaderAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pReferenceParameterAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pPolicyAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pEndpointReferenceAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RegisterScopeMatchingRule(self, pScopeMatchingRule: Windows.Win32.Devices.WebServicesOnDevices.IWSDScopeMatchingRule_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UnRegisterScopeMatchingRule(self, pScopeMatchingRule: Windows.Win32.Devices.WebServicesOnDevices.IWSDScopeMatchingRule_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetXMLContext(self, ppContext: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveryPublisherNotify(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e67651b0-337a-4b3c-97-58-73-33-88-56-82-51')
    @commethod(3)
    def ProbeHandler(self, pSoap: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ResolveHandler(self, pSoap: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWSD_SOAP_MESSAGE_HANDLER(thisUnknown: Windows.Win32.System.Com.IUnknown_head, event: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class REQUESTBODY_GetStatus(EasyCastStructure):
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class REQUESTBODY_Renew(EasyCastStructure):
    Expires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class REQUESTBODY_Subscribe(EasyCastStructure):
    EndTo: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Delivery: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_DELIVERY_MODE_head)
    Expires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)
    Filter: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_FILTER_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class REQUESTBODY_Unsubscribe(EasyCastStructure):
    any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class RESPONSEBODY_GetMetadata(EasyCastStructure):
    Metadata: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head)
class RESPONSEBODY_GetStatus(EasyCastStructure):
    expires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)
    any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class RESPONSEBODY_Renew(EasyCastStructure):
    expires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)
    any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class RESPONSEBODY_Subscribe(EasyCastStructure):
    SubscriptionManager: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    expires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)
    any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class RESPONSEBODY_SubscriptionEnd(EasyCastStructure):
    SubscriptionManager: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Status: Windows.Win32.Foundation.PWSTR
    Reason: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
WSDEventType = Int32
WSDET_NONE: WSDEventType = 0
WSDET_INCOMING_MESSAGE: WSDEventType = 1
WSDET_INCOMING_FAULT: WSDEventType = 2
WSDET_TRANSMISSION_FAILURE: WSDEventType = 3
WSDET_RESPONSE_TIMEOUT: WSDEventType = 4
WSDUdpMessageType = Int32
ONE_WAY: WSDUdpMessageType = 0
TWO_WAY: WSDUdpMessageType = 1
class WSDUdpRetransmitParams(EasyCastStructure):
    ulSendDelay: UInt32
    ulRepeat: UInt32
    ulRepeatMinDelay: UInt32
    ulRepeatMaxDelay: UInt32
    ulRepeatUpperDelay: UInt32
class WSDXML_ATTRIBUTE(EasyCastStructure):
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ATTRIBUTE_head)
    Name: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    Value: Windows.Win32.Foundation.PWSTR
class WSDXML_ELEMENT(EasyCastStructure):
    Node: Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE
    Name: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    FirstAttribute: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ATTRIBUTE_head)
    FirstChild: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE_head)
    PrefixMappings: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_PREFIX_MAPPING_head)
class WSDXML_ELEMENT_LIST(EasyCastStructure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_LIST_head)
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSDXML_NAME(EasyCastStructure):
    Space: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head)
    LocalName: Windows.Win32.Foundation.PWSTR
class WSDXML_NAMESPACE(EasyCastStructure):
    Uri: Windows.Win32.Foundation.PWSTR
    PreferredPrefix: Windows.Win32.Foundation.PWSTR
    Names: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    NamesCount: UInt16
    Encoding: UInt16
class WSDXML_NODE(EasyCastStructure):
    ElementType = 0
    TextType = 1
    Type: Int32
    Parent: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE_head)
WSDXML_OP = Int32
WSDXML_OP_OpNone: WSDXML_OP = 0
WSDXML_OP_OpEndOfTable: WSDXML_OP = 1
WSDXML_OP_OpBeginElement_: WSDXML_OP = 2
WSDXML_OP_OpBeginAnyElement: WSDXML_OP = 3
WSDXML_OP_OpEndElement: WSDXML_OP = 4
WSDXML_OP_OpElement_: WSDXML_OP = 5
WSDXML_OP_OpAnyElement: WSDXML_OP = 6
WSDXML_OP_OpAnyElements: WSDXML_OP = 7
WSDXML_OP_OpAnyText: WSDXML_OP = 8
WSDXML_OP_OpAttribute_: WSDXML_OP = 9
WSDXML_OP_OpBeginChoice: WSDXML_OP = 10
WSDXML_OP_OpEndChoice: WSDXML_OP = 11
WSDXML_OP_OpBeginSequence: WSDXML_OP = 12
WSDXML_OP_OpEndSequence: WSDXML_OP = 13
WSDXML_OP_OpBeginAll: WSDXML_OP = 14
WSDXML_OP_OpEndAll: WSDXML_OP = 15
WSDXML_OP_OpAnything: WSDXML_OP = 16
WSDXML_OP_OpAnyNumber: WSDXML_OP = 17
WSDXML_OP_OpOneOrMore: WSDXML_OP = 18
WSDXML_OP_OpOptional: WSDXML_OP = 19
WSDXML_OP_OpFormatBool_: WSDXML_OP = 20
WSDXML_OP_OpFormatInt8_: WSDXML_OP = 21
WSDXML_OP_OpFormatInt16_: WSDXML_OP = 22
WSDXML_OP_OpFormatInt32_: WSDXML_OP = 23
WSDXML_OP_OpFormatInt64_: WSDXML_OP = 24
WSDXML_OP_OpFormatUInt8_: WSDXML_OP = 25
WSDXML_OP_OpFormatUInt16_: WSDXML_OP = 26
WSDXML_OP_OpFormatUInt32_: WSDXML_OP = 27
WSDXML_OP_OpFormatUInt64_: WSDXML_OP = 28
WSDXML_OP_OpFormatUnicodeString_: WSDXML_OP = 29
WSDXML_OP_OpFormatDom_: WSDXML_OP = 30
WSDXML_OP_OpFormatStruct_: WSDXML_OP = 31
WSDXML_OP_OpFormatUri_: WSDXML_OP = 32
WSDXML_OP_OpFormatUuidUri_: WSDXML_OP = 33
WSDXML_OP_OpFormatName_: WSDXML_OP = 34
WSDXML_OP_OpFormatListInsertTail_: WSDXML_OP = 35
WSDXML_OP_OpFormatType_: WSDXML_OP = 36
WSDXML_OP_OpFormatDynamicType_: WSDXML_OP = 37
WSDXML_OP_OpFormatLookupType_: WSDXML_OP = 38
WSDXML_OP_OpFormatDuration_: WSDXML_OP = 39
WSDXML_OP_OpFormatDateTime_: WSDXML_OP = 40
WSDXML_OP_OpFormatFloat_: WSDXML_OP = 41
WSDXML_OP_OpFormatDouble_: WSDXML_OP = 42
WSDXML_OP_OpProcess_: WSDXML_OP = 43
WSDXML_OP_OpQualifiedAttribute_: WSDXML_OP = 44
WSDXML_OP_OpFormatXMLDeclaration_: WSDXML_OP = 45
WSDXML_OP_OpFormatMax: WSDXML_OP = 46
class WSDXML_PREFIX_MAPPING(EasyCastStructure):
    Refs: UInt32
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_PREFIX_MAPPING_head)
    Space: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head)
    Prefix: Windows.Win32.Foundation.PWSTR
class WSDXML_TEXT(EasyCastStructure):
    Node: Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE
    Text: Windows.Win32.Foundation.PWSTR
class WSDXML_TYPE(EasyCastStructure):
    Uri: Windows.Win32.Foundation.PWSTR
    Table: POINTER(Byte)
class WSD_APP_SEQUENCE(EasyCastStructure):
    InstanceId: UInt64
    SequenceId: Windows.Win32.Foundation.PWSTR
    MessageNumber: UInt64
class WSD_BYE(EasyCastStructure):
    EndpointReference: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_CONFIG_ADDRESSES(EasyCastStructure):
    addresses: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head)
    dwAddressCount: UInt32
class WSD_CONFIG_PARAM(EasyCastStructure):
    configParamType: Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE
    pConfigData: c_void_p
    dwConfigDataSize: UInt32
WSD_CONFIG_PARAM_TYPE = Int32
WSD_CONFIG_MAX_INBOUND_MESSAGE_SIZE: WSD_CONFIG_PARAM_TYPE = 1
WSD_CONFIG_MAX_OUTBOUND_MESSAGE_SIZE: WSD_CONFIG_PARAM_TYPE = 2
WSD_SECURITY_SSL_CERT_FOR_CLIENT_AUTH: WSD_CONFIG_PARAM_TYPE = 3
WSD_SECURITY_SSL_SERVER_CERT_VALIDATION: WSD_CONFIG_PARAM_TYPE = 4
WSD_SECURITY_SSL_CLIENT_CERT_VALIDATION: WSD_CONFIG_PARAM_TYPE = 5
WSD_SECURITY_SSL_NEGOTIATE_CLIENT_CERT: WSD_CONFIG_PARAM_TYPE = 6
WSD_SECURITY_COMPACTSIG_SIGNING_CERT: WSD_CONFIG_PARAM_TYPE = 7
WSD_SECURITY_COMPACTSIG_VALIDATION: WSD_CONFIG_PARAM_TYPE = 8
WSD_CONFIG_HOSTING_ADDRESSES: WSD_CONFIG_PARAM_TYPE = 9
WSD_CONFIG_DEVICE_ADDRESSES: WSD_CONFIG_PARAM_TYPE = 10
WSD_SECURITY_REQUIRE_HTTP_CLIENT_AUTH: WSD_CONFIG_PARAM_TYPE = 11
WSD_SECURITY_REQUIRE_CLIENT_CERT_OR_HTTP_CLIENT_AUTH: WSD_CONFIG_PARAM_TYPE = 12
WSD_SECURITY_USE_HTTP_CLIENT_AUTH: WSD_CONFIG_PARAM_TYPE = 13
class WSD_DATETIME(EasyCastStructure):
    isPositive: Windows.Win32.Foundation.BOOL
    year: UInt32
    month: Byte
    day: Byte
    hour: Byte
    minute: Byte
    second: Byte
    millisecond: UInt32
    TZIsLocal: Windows.Win32.Foundation.BOOL
    TZIsPositive: Windows.Win32.Foundation.BOOL
    TZHour: Byte
    TZMinute: Byte
class WSD_DURATION(EasyCastStructure):
    isPositive: Windows.Win32.Foundation.BOOL
    year: UInt32
    month: UInt32
    day: UInt32
    hour: UInt32
    minute: UInt32
    second: UInt32
    millisecond: UInt32
class WSD_ENDPOINT_REFERENCE(EasyCastStructure):
    Address: Windows.Win32.Foundation.PWSTR
    ReferenceProperties: Windows.Win32.Devices.WebServicesOnDevices.WSD_REFERENCE_PROPERTIES
    ReferenceParameters: Windows.Win32.Devices.WebServicesOnDevices.WSD_REFERENCE_PARAMETERS
    PortType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    ServiceName: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_ENDPOINT_REFERENCE_LIST(EasyCastStructure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_LIST_head)
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
class WSD_EVENT(EasyCastStructure):
    Hr: Windows.Win32.Foundation.HRESULT
    EventType: UInt32
    DispatchTag: Windows.Win32.Foundation.PWSTR
    HandlerContext: Windows.Win32.Devices.WebServicesOnDevices.WSD_HANDLER_CONTEXT
    Soap: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head)
    Operation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head)
    MessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head
class WSD_EVENTING_DELIVERY_MODE(EasyCastStructure):
    Mode: Windows.Win32.Foundation.PWSTR
    Push: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_DELIVERY_MODE_PUSH_head)
    Data: c_void_p
class WSD_EVENTING_DELIVERY_MODE_PUSH(EasyCastStructure):
    NotifyTo: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
class WSD_EVENTING_EXPIRES(EasyCastStructure):
    Duration: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_DURATION_head)
    DateTime: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_DATETIME_head)
class WSD_EVENTING_FILTER(EasyCastStructure):
    Dialect: Windows.Win32.Foundation.PWSTR
    FilterAction: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_FILTER_ACTION_head)
    Data: c_void_p
class WSD_EVENTING_FILTER_ACTION(EasyCastStructure):
    Actions: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
class WSD_HANDLER_CONTEXT(EasyCastStructure):
    Handler: Windows.Win32.Devices.WebServicesOnDevices.PWSD_SOAP_MESSAGE_HANDLER
    PVoid: c_void_p
    Unknown: Windows.Win32.System.Com.IUnknown_head
class WSD_HEADER_RELATESTO(EasyCastStructure):
    RelationshipType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    MessageID: Windows.Win32.Foundation.PWSTR
class WSD_HELLO(EasyCastStructure):
    EndpointReference: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Types: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    Scopes: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES_head)
    XAddrs: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
    MetadataVersion: UInt64
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_HOST_METADATA(EasyCastStructure):
    Host: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_head)
    Hosted: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_LIST_head)
class WSD_LOCALIZED_STRING(EasyCastStructure):
    lang: Windows.Win32.Foundation.PWSTR
    String: Windows.Win32.Foundation.PWSTR
class WSD_LOCALIZED_STRING_LIST(EasyCastStructure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_head)
class WSD_METADATA_SECTION(EasyCastStructure):
    Dialect: Windows.Win32.Foundation.PWSTR
    Identifier: Windows.Win32.Foundation.PWSTR
    Data: c_void_p
    MetadataReference: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Location: Windows.Win32.Foundation.PWSTR
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_METADATA_SECTION_LIST(EasyCastStructure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head)
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_head)
class WSD_NAME_LIST(EasyCastStructure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
class WSD_OPERATION(EasyCastStructure):
    RequestType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE_head)
    ResponseType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE_head)
    RequestStubFunction: Windows.Win32.Devices.WebServicesOnDevices.WSD_STUB_FUNCTION
class WSD_PORT_TYPE(EasyCastStructure):
    EncodedName: UInt32
    OperationCount: UInt32
    Operations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head)
    ProtocolType: Windows.Win32.Devices.WebServicesOnDevices.WSD_PROTOCOL_TYPE
class WSD_PROBE(EasyCastStructure):
    Types: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    Scopes: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_PROBE_MATCH(EasyCastStructure):
    EndpointReference: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Types: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    Scopes: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES_head)
    XAddrs: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
    MetadataVersion: UInt64
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_PROBE_MATCHES(EasyCastStructure):
    ProbeMatch: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_LIST_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_PROBE_MATCH_LIST(EasyCastStructure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_LIST_head)
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_head)
WSD_PROTOCOL_TYPE = Int32
WSD_PT_NONE: WSD_PROTOCOL_TYPE = 0
WSD_PT_UDP: WSD_PROTOCOL_TYPE = 1
WSD_PT_HTTP: WSD_PROTOCOL_TYPE = 2
WSD_PT_HTTPS: WSD_PROTOCOL_TYPE = 4
WSD_PT_ALL: WSD_PROTOCOL_TYPE = 255
class WSD_REFERENCE_PARAMETERS(EasyCastStructure):
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_REFERENCE_PROPERTIES(EasyCastStructure):
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_RELATIONSHIP_METADATA(EasyCastStructure):
    Type: Windows.Win32.Foundation.PWSTR
    Data: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_HOST_METADATA_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_RESOLVE(EasyCastStructure):
    EndpointReference: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_RESOLVE_MATCH(EasyCastStructure):
    EndpointReference: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Types: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    Scopes: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES_head)
    XAddrs: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
    MetadataVersion: UInt64
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_RESOLVE_MATCHES(EasyCastStructure):
    ResolveMatch: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_RESOLVE_MATCH_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_SCOPES(EasyCastStructure):
    MatchBy: Windows.Win32.Foundation.PWSTR
    Scopes: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
class WSD_SECURITY_CERT_VALIDATION(EasyCastStructure):
    certMatchArray: POINTER(POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))
    dwCertMatchArrayCount: UInt32
    hCertMatchStore: Windows.Win32.Security.Cryptography.HCERTSTORE
    hCertIssuerStore: Windows.Win32.Security.Cryptography.HCERTSTORE
    dwCertCheckOptions: UInt32
    pszCNGHashAlgId: Windows.Win32.Foundation.PWSTR
    pbCertHash: POINTER(Byte)
    dwCertHashSize: UInt32
class WSD_SECURITY_CERT_VALIDATION_V1(EasyCastStructure):
    certMatchArray: POINTER(POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))
    dwCertMatchArrayCount: UInt32
    hCertMatchStore: Windows.Win32.Security.Cryptography.HCERTSTORE
    hCertIssuerStore: Windows.Win32.Security.Cryptography.HCERTSTORE
    dwCertCheckOptions: UInt32
class WSD_SECURITY_SIGNATURE_VALIDATION(EasyCastStructure):
    signingCertArray: POINTER(POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))
    dwSigningCertArrayCount: UInt32
    hSigningCertStore: Windows.Win32.Security.Cryptography.HCERTSTORE
    dwFlags: UInt32
class WSD_SERVICE_METADATA(EasyCastStructure):
    EndpointReference: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_LIST_head)
    Types: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    ServiceId: Windows.Win32.Foundation.PWSTR
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_SERVICE_METADATA_LIST(EasyCastStructure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_LIST_head)
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_head)
class WSD_SOAP_FAULT(EasyCastStructure):
    Code: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_CODE_head)
    Reason: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_REASON_head)
    Node: Windows.Win32.Foundation.PWSTR
    Role: Windows.Win32.Foundation.PWSTR
    Detail: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_SOAP_FAULT_CODE(EasyCastStructure):
    Value: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    Subcode: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_SUBCODE_head)
class WSD_SOAP_FAULT_REASON(EasyCastStructure):
    Text: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)
class WSD_SOAP_FAULT_SUBCODE(EasyCastStructure):
    Value: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    Subcode: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_SUBCODE_head)
class WSD_SOAP_HEADER(EasyCastStructure):
    To: Windows.Win32.Foundation.PWSTR
    Action: Windows.Win32.Foundation.PWSTR
    MessageID: Windows.Win32.Foundation.PWSTR
    RelatesTo: Windows.Win32.Devices.WebServicesOnDevices.WSD_HEADER_RELATESTO
    ReplyTo: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    From: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    FaultTo: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    AppSequence: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_APP_SEQUENCE_head)
    AnyHeaders: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_SOAP_MESSAGE(EasyCastStructure):
    Header: Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_HEADER
    Body: c_void_p
    BodyType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE_head)
@winfunctype_pointer
def WSD_STUB_FUNCTION(server: Windows.Win32.System.Com.IUnknown_head, session: Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceMessaging_head, event: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WSD_SYNCHRONOUS_RESPONSE_CONTEXT(EasyCastStructure):
    hr: Windows.Win32.Foundation.HRESULT
    eventHandle: Windows.Win32.Foundation.HANDLE
    messageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head
    results: c_void_p
class WSD_THIS_DEVICE_METADATA(EasyCastStructure):
    FriendlyName: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)
    FirmwareVersion: Windows.Win32.Foundation.PWSTR
    SerialNumber: Windows.Win32.Foundation.PWSTR
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_THIS_MODEL_METADATA(EasyCastStructure):
    Manufacturer: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)
    ManufacturerUrl: Windows.Win32.Foundation.PWSTR
    ModelName: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)
    ModelNumber: Windows.Win32.Foundation.PWSTR
    ModelUrl: Windows.Win32.Foundation.PWSTR
    PresentationUrl: Windows.Win32.Foundation.PWSTR
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_UNKNOWN_LOOKUP(EasyCastStructure):
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_URI_LIST(EasyCastStructure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
    Element: Windows.Win32.Foundation.PWSTR
make_head(_module, 'IWSDAddress')
make_head(_module, 'IWSDAsyncCallback')
make_head(_module, 'IWSDAsyncResult')
make_head(_module, 'IWSDAttachment')
make_head(_module, 'IWSDDeviceHost')
make_head(_module, 'IWSDDeviceHostNotify')
make_head(_module, 'IWSDDeviceProxy')
make_head(_module, 'IWSDEndpointProxy')
make_head(_module, 'IWSDEventingStatus')
make_head(_module, 'IWSDHttpAddress')
make_head(_module, 'IWSDHttpAuthParameters')
make_head(_module, 'IWSDHttpMessageParameters')
make_head(_module, 'IWSDInboundAttachment')
make_head(_module, 'IWSDMessageParameters')
make_head(_module, 'IWSDMetadataExchange')
make_head(_module, 'IWSDOutboundAttachment')
make_head(_module, 'IWSDSSLClientCertificate')
make_head(_module, 'IWSDScopeMatchingRule')
make_head(_module, 'IWSDServiceMessaging')
make_head(_module, 'IWSDServiceProxy')
make_head(_module, 'IWSDServiceProxyEventing')
make_head(_module, 'IWSDSignatureProperty')
make_head(_module, 'IWSDTransportAddress')
make_head(_module, 'IWSDUdpAddress')
make_head(_module, 'IWSDUdpMessageParameters')
make_head(_module, 'IWSDXMLContext')
make_head(_module, 'IWSDiscoveredService')
make_head(_module, 'IWSDiscoveryProvider')
make_head(_module, 'IWSDiscoveryProviderNotify')
make_head(_module, 'IWSDiscoveryPublisher')
make_head(_module, 'IWSDiscoveryPublisherNotify')
make_head(_module, 'PWSD_SOAP_MESSAGE_HANDLER')
make_head(_module, 'REQUESTBODY_GetStatus')
make_head(_module, 'REQUESTBODY_Renew')
make_head(_module, 'REQUESTBODY_Subscribe')
make_head(_module, 'REQUESTBODY_Unsubscribe')
make_head(_module, 'RESPONSEBODY_GetMetadata')
make_head(_module, 'RESPONSEBODY_GetStatus')
make_head(_module, 'RESPONSEBODY_Renew')
make_head(_module, 'RESPONSEBODY_Subscribe')
make_head(_module, 'RESPONSEBODY_SubscriptionEnd')
make_head(_module, 'WSDUdpRetransmitParams')
make_head(_module, 'WSDXML_ATTRIBUTE')
make_head(_module, 'WSDXML_ELEMENT')
make_head(_module, 'WSDXML_ELEMENT_LIST')
make_head(_module, 'WSDXML_NAME')
make_head(_module, 'WSDXML_NAMESPACE')
make_head(_module, 'WSDXML_NODE')
make_head(_module, 'WSDXML_PREFIX_MAPPING')
make_head(_module, 'WSDXML_TEXT')
make_head(_module, 'WSDXML_TYPE')
make_head(_module, 'WSD_APP_SEQUENCE')
make_head(_module, 'WSD_BYE')
make_head(_module, 'WSD_CONFIG_ADDRESSES')
make_head(_module, 'WSD_CONFIG_PARAM')
make_head(_module, 'WSD_DATETIME')
make_head(_module, 'WSD_DURATION')
make_head(_module, 'WSD_ENDPOINT_REFERENCE')
make_head(_module, 'WSD_ENDPOINT_REFERENCE_LIST')
make_head(_module, 'WSD_EVENT')
make_head(_module, 'WSD_EVENTING_DELIVERY_MODE')
make_head(_module, 'WSD_EVENTING_DELIVERY_MODE_PUSH')
make_head(_module, 'WSD_EVENTING_EXPIRES')
make_head(_module, 'WSD_EVENTING_FILTER')
make_head(_module, 'WSD_EVENTING_FILTER_ACTION')
make_head(_module, 'WSD_HANDLER_CONTEXT')
make_head(_module, 'WSD_HEADER_RELATESTO')
make_head(_module, 'WSD_HELLO')
make_head(_module, 'WSD_HOST_METADATA')
make_head(_module, 'WSD_LOCALIZED_STRING')
make_head(_module, 'WSD_LOCALIZED_STRING_LIST')
make_head(_module, 'WSD_METADATA_SECTION')
make_head(_module, 'WSD_METADATA_SECTION_LIST')
make_head(_module, 'WSD_NAME_LIST')
make_head(_module, 'WSD_OPERATION')
make_head(_module, 'WSD_PORT_TYPE')
make_head(_module, 'WSD_PROBE')
make_head(_module, 'WSD_PROBE_MATCH')
make_head(_module, 'WSD_PROBE_MATCHES')
make_head(_module, 'WSD_PROBE_MATCH_LIST')
make_head(_module, 'WSD_REFERENCE_PARAMETERS')
make_head(_module, 'WSD_REFERENCE_PROPERTIES')
make_head(_module, 'WSD_RELATIONSHIP_METADATA')
make_head(_module, 'WSD_RESOLVE')
make_head(_module, 'WSD_RESOLVE_MATCH')
make_head(_module, 'WSD_RESOLVE_MATCHES')
make_head(_module, 'WSD_SCOPES')
make_head(_module, 'WSD_SECURITY_CERT_VALIDATION')
make_head(_module, 'WSD_SECURITY_CERT_VALIDATION_V1')
make_head(_module, 'WSD_SECURITY_SIGNATURE_VALIDATION')
make_head(_module, 'WSD_SERVICE_METADATA')
make_head(_module, 'WSD_SERVICE_METADATA_LIST')
make_head(_module, 'WSD_SOAP_FAULT')
make_head(_module, 'WSD_SOAP_FAULT_CODE')
make_head(_module, 'WSD_SOAP_FAULT_REASON')
make_head(_module, 'WSD_SOAP_FAULT_SUBCODE')
make_head(_module, 'WSD_SOAP_HEADER')
make_head(_module, 'WSD_SOAP_MESSAGE')
make_head(_module, 'WSD_STUB_FUNCTION')
make_head(_module, 'WSD_SYNCHRONOUS_RESPONSE_CONTEXT')
make_head(_module, 'WSD_THIS_DEVICE_METADATA')
make_head(_module, 'WSD_THIS_MODEL_METADATA')
make_head(_module, 'WSD_UNKNOWN_LOOKUP')
make_head(_module, 'WSD_URI_LIST')