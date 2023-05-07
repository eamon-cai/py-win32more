from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Data.Xml.Dom
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Security.Credentials
import Windows.Storage.Streams
import Windows.Web.AtomPub
import Windows.Web.Syndication
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AtomPubClient(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.AtomPub.IAtomPubClient
    _classid_ = 'Windows.Web.AtomPub.AtomPubClient'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Web.AtomPub.AtomPubClient: ...
    @winrt_factorymethod
    def CreateAtomPubClientWithCredentials(cls: Windows.Web.AtomPub.IAtomPubClientFactory, serverCredential: Windows.Security.Credentials.PasswordCredential) -> Windows.Web.AtomPub.AtomPubClient: ...
    @winrt_mixinmethod
    def RetrieveServiceDocumentAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.AtomPub.ServiceDocument, Windows.Web.Syndication.RetrievalProgress]: ...
    @winrt_mixinmethod
    def RetrieveMediaResourceAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IInputStream, Windows.Web.Syndication.RetrievalProgress]: ...
    @winrt_mixinmethod
    def RetrieveResourceAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Syndication.SyndicationItem, Windows.Web.Syndication.RetrievalProgress]: ...
    @winrt_mixinmethod
    def CreateResourceAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri, description: WinRT_String, item: Windows.Web.Syndication.SyndicationItem) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Syndication.SyndicationItem, Windows.Web.Syndication.TransferProgress]: ...
    @winrt_mixinmethod
    def CreateMediaResourceAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri, mediaType: WinRT_String, description: WinRT_String, mediaStream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Syndication.SyndicationItem, Windows.Web.Syndication.TransferProgress]: ...
    @winrt_mixinmethod
    def UpdateMediaResourceAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri, mediaType: WinRT_String, mediaStream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncActionWithProgress[Windows.Web.Syndication.TransferProgress]: ...
    @winrt_mixinmethod
    def UpdateResourceAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri, item: Windows.Web.Syndication.SyndicationItem) -> Windows.Foundation.IAsyncActionWithProgress[Windows.Web.Syndication.TransferProgress]: ...
    @winrt_mixinmethod
    def UpdateResourceItemAsync(self: Windows.Web.AtomPub.IAtomPubClient, item: Windows.Web.Syndication.SyndicationItem) -> Windows.Foundation.IAsyncActionWithProgress[Windows.Web.Syndication.TransferProgress]: ...
    @winrt_mixinmethod
    def DeleteResourceAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncActionWithProgress[Windows.Web.Syndication.TransferProgress]: ...
    @winrt_mixinmethod
    def DeleteResourceItemAsync(self: Windows.Web.AtomPub.IAtomPubClient, item: Windows.Web.Syndication.SyndicationItem) -> Windows.Foundation.IAsyncActionWithProgress[Windows.Web.Syndication.TransferProgress]: ...
    @winrt_mixinmethod
    def CancelAsyncOperations(self: Windows.Web.AtomPub.IAtomPubClient) -> Void: ...
    @winrt_mixinmethod
    def get_ServerCredential(self: Windows.Web.Syndication.ISyndicationClient) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ServerCredential(self: Windows.Web.Syndication.ISyndicationClient, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyCredential(self: Windows.Web.Syndication.ISyndicationClient) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ProxyCredential(self: Windows.Web.Syndication.ISyndicationClient, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_MaxResponseBufferSize(self: Windows.Web.Syndication.ISyndicationClient) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxResponseBufferSize(self: Windows.Web.Syndication.ISyndicationClient, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Timeout(self: Windows.Web.Syndication.ISyndicationClient) -> UInt32: ...
    @winrt_mixinmethod
    def put_Timeout(self: Windows.Web.Syndication.ISyndicationClient, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_BypassCacheOnRetrieve(self: Windows.Web.Syndication.ISyndicationClient) -> Boolean: ...
    @winrt_mixinmethod
    def put_BypassCacheOnRetrieve(self: Windows.Web.Syndication.ISyndicationClient, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: Windows.Web.Syndication.ISyndicationClient, name: WinRT_String, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RetrieveFeedAsync(self: Windows.Web.Syndication.ISyndicationClient, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Syndication.SyndicationFeed, Windows.Web.Syndication.RetrievalProgress]: ...
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    MaxResponseBufferSize = property(get_MaxResponseBufferSize, put_MaxResponseBufferSize)
    Timeout = property(get_Timeout, put_Timeout)
    BypassCacheOnRetrieve = property(get_BypassCacheOnRetrieve, put_BypassCacheOnRetrieve)
class IAtomPubClient(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.AtomPub.IAtomPubClient'
    _iid_ = Guid('{35392c38-cded-4d4c-9637-05f15c1c9406}')
    @winrt_commethod(6)
    def RetrieveServiceDocumentAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.AtomPub.ServiceDocument, Windows.Web.Syndication.RetrievalProgress]: ...
    @winrt_commethod(7)
    def RetrieveMediaResourceAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IInputStream, Windows.Web.Syndication.RetrievalProgress]: ...
    @winrt_commethod(8)
    def RetrieveResourceAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Syndication.SyndicationItem, Windows.Web.Syndication.RetrievalProgress]: ...
    @winrt_commethod(9)
    def CreateResourceAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri, description: WinRT_String, item: Windows.Web.Syndication.SyndicationItem) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Syndication.SyndicationItem, Windows.Web.Syndication.TransferProgress]: ...
    @winrt_commethod(10)
    def CreateMediaResourceAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri, mediaType: WinRT_String, description: WinRT_String, mediaStream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Syndication.SyndicationItem, Windows.Web.Syndication.TransferProgress]: ...
    @winrt_commethod(11)
    def UpdateMediaResourceAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri, mediaType: WinRT_String, mediaStream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncActionWithProgress[Windows.Web.Syndication.TransferProgress]: ...
    @winrt_commethod(12)
    def UpdateResourceAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri, item: Windows.Web.Syndication.SyndicationItem) -> Windows.Foundation.IAsyncActionWithProgress[Windows.Web.Syndication.TransferProgress]: ...
    @winrt_commethod(13)
    def UpdateResourceItemAsync(self: Windows.Web.AtomPub.IAtomPubClient, item: Windows.Web.Syndication.SyndicationItem) -> Windows.Foundation.IAsyncActionWithProgress[Windows.Web.Syndication.TransferProgress]: ...
    @winrt_commethod(14)
    def DeleteResourceAsync(self: Windows.Web.AtomPub.IAtomPubClient, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncActionWithProgress[Windows.Web.Syndication.TransferProgress]: ...
    @winrt_commethod(15)
    def DeleteResourceItemAsync(self: Windows.Web.AtomPub.IAtomPubClient, item: Windows.Web.Syndication.SyndicationItem) -> Windows.Foundation.IAsyncActionWithProgress[Windows.Web.Syndication.TransferProgress]: ...
    @winrt_commethod(16)
    def CancelAsyncOperations(self: Windows.Web.AtomPub.IAtomPubClient) -> Void: ...
class IAtomPubClientFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.AtomPub.IAtomPubClientFactory'
    _iid_ = Guid('{49d55012-57cb-4bde-ab9f-2610b172777b}')
    @winrt_commethod(6)
    def CreateAtomPubClientWithCredentials(self: Windows.Web.AtomPub.IAtomPubClientFactory, serverCredential: Windows.Security.Credentials.PasswordCredential) -> Windows.Web.AtomPub.AtomPubClient: ...
class IResourceCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.AtomPub.IResourceCollection'
    _iid_ = Guid('{7f5fd609-bc88-41d4-88fa-3de6704d428e}')
    @winrt_commethod(6)
    def get_Title(self: Windows.Web.AtomPub.IResourceCollection) -> Windows.Web.Syndication.ISyndicationText: ...
    @winrt_commethod(7)
    def get_Uri(self: Windows.Web.AtomPub.IResourceCollection) -> Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_Categories(self: Windows.Web.AtomPub.IResourceCollection) -> Windows.Foundation.Collections.IVectorView[Windows.Web.Syndication.SyndicationCategory]: ...
    @winrt_commethod(9)
    def get_Accepts(self: Windows.Web.AtomPub.IResourceCollection) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    Title = property(get_Title, None)
    Uri = property(get_Uri, None)
    Categories = property(get_Categories, None)
    Accepts = property(get_Accepts, None)
class IServiceDocument(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.AtomPub.IServiceDocument'
    _iid_ = Guid('{8b7ec771-2ab3-4dbe-8bcc-778f92b75e51}')
    @winrt_commethod(6)
    def get_Workspaces(self: Windows.Web.AtomPub.IServiceDocument) -> Windows.Foundation.Collections.IVectorView[Windows.Web.AtomPub.Workspace]: ...
    Workspaces = property(get_Workspaces, None)
class IWorkspace(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.AtomPub.IWorkspace'
    _iid_ = Guid('{b41da63b-a4b8-4036-89c5-83c31266ba49}')
    @winrt_commethod(6)
    def get_Title(self: Windows.Web.AtomPub.IWorkspace) -> Windows.Web.Syndication.ISyndicationText: ...
    @winrt_commethod(7)
    def get_Collections(self: Windows.Web.AtomPub.IWorkspace) -> Windows.Foundation.Collections.IVectorView[Windows.Web.AtomPub.ResourceCollection]: ...
    Title = property(get_Title, None)
    Collections = property(get_Collections, None)
class ResourceCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.AtomPub.IResourceCollection
    _classid_ = 'Windows.Web.AtomPub.ResourceCollection'
    @winrt_mixinmethod
    def get_Title(self: Windows.Web.AtomPub.IResourceCollection) -> Windows.Web.Syndication.ISyndicationText: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.Web.AtomPub.IResourceCollection) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Categories(self: Windows.Web.AtomPub.IResourceCollection) -> Windows.Foundation.Collections.IVectorView[Windows.Web.Syndication.SyndicationCategory]: ...
    @winrt_mixinmethod
    def get_Accepts(self: Windows.Web.AtomPub.IResourceCollection) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_NodeName(self: Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeName(self: Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NodeNamespace(self: Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeNamespace(self: Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NodeValue(self: Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeValue(self: Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_BaseUri(self: Windows.Web.Syndication.ISyndicationNode) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_BaseUri(self: Windows.Web.Syndication.ISyndicationNode, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_AttributeExtensions(self: Windows.Web.Syndication.ISyndicationNode) -> Windows.Foundation.Collections.IVector[Windows.Web.Syndication.SyndicationAttribute]: ...
    @winrt_mixinmethod
    def get_ElementExtensions(self: Windows.Web.Syndication.ISyndicationNode) -> Windows.Foundation.Collections.IVector[Windows.Web.Syndication.ISyndicationNode]: ...
    @winrt_mixinmethod
    def GetXmlDocument(self: Windows.Web.Syndication.ISyndicationNode, format: Windows.Web.Syndication.SyndicationFormat) -> Windows.Data.Xml.Dom.XmlDocument: ...
    Title = property(get_Title, None)
    Uri = property(get_Uri, None)
    Categories = property(get_Categories, None)
    Accepts = property(get_Accepts, None)
    NodeName = property(get_NodeName, put_NodeName)
    NodeNamespace = property(get_NodeNamespace, put_NodeNamespace)
    NodeValue = property(get_NodeValue, put_NodeValue)
    Language = property(get_Language, put_Language)
    BaseUri = property(get_BaseUri, put_BaseUri)
    AttributeExtensions = property(get_AttributeExtensions, None)
    ElementExtensions = property(get_ElementExtensions, None)
class ServiceDocument(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.AtomPub.IServiceDocument
    _classid_ = 'Windows.Web.AtomPub.ServiceDocument'
    @winrt_mixinmethod
    def get_Workspaces(self: Windows.Web.AtomPub.IServiceDocument) -> Windows.Foundation.Collections.IVectorView[Windows.Web.AtomPub.Workspace]: ...
    @winrt_mixinmethod
    def get_NodeName(self: Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeName(self: Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NodeNamespace(self: Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeNamespace(self: Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NodeValue(self: Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeValue(self: Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_BaseUri(self: Windows.Web.Syndication.ISyndicationNode) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_BaseUri(self: Windows.Web.Syndication.ISyndicationNode, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_AttributeExtensions(self: Windows.Web.Syndication.ISyndicationNode) -> Windows.Foundation.Collections.IVector[Windows.Web.Syndication.SyndicationAttribute]: ...
    @winrt_mixinmethod
    def get_ElementExtensions(self: Windows.Web.Syndication.ISyndicationNode) -> Windows.Foundation.Collections.IVector[Windows.Web.Syndication.ISyndicationNode]: ...
    @winrt_mixinmethod
    def GetXmlDocument(self: Windows.Web.Syndication.ISyndicationNode, format: Windows.Web.Syndication.SyndicationFormat) -> Windows.Data.Xml.Dom.XmlDocument: ...
    Workspaces = property(get_Workspaces, None)
    NodeName = property(get_NodeName, put_NodeName)
    NodeNamespace = property(get_NodeNamespace, put_NodeNamespace)
    NodeValue = property(get_NodeValue, put_NodeValue)
    Language = property(get_Language, put_Language)
    BaseUri = property(get_BaseUri, put_BaseUri)
    AttributeExtensions = property(get_AttributeExtensions, None)
    ElementExtensions = property(get_ElementExtensions, None)
class Workspace(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.AtomPub.IWorkspace
    _classid_ = 'Windows.Web.AtomPub.Workspace'
    @winrt_mixinmethod
    def get_Title(self: Windows.Web.AtomPub.IWorkspace) -> Windows.Web.Syndication.ISyndicationText: ...
    @winrt_mixinmethod
    def get_Collections(self: Windows.Web.AtomPub.IWorkspace) -> Windows.Foundation.Collections.IVectorView[Windows.Web.AtomPub.ResourceCollection]: ...
    @winrt_mixinmethod
    def get_NodeName(self: Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeName(self: Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NodeNamespace(self: Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeNamespace(self: Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NodeValue(self: Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeValue(self: Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_BaseUri(self: Windows.Web.Syndication.ISyndicationNode) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_BaseUri(self: Windows.Web.Syndication.ISyndicationNode, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_AttributeExtensions(self: Windows.Web.Syndication.ISyndicationNode) -> Windows.Foundation.Collections.IVector[Windows.Web.Syndication.SyndicationAttribute]: ...
    @winrt_mixinmethod
    def get_ElementExtensions(self: Windows.Web.Syndication.ISyndicationNode) -> Windows.Foundation.Collections.IVector[Windows.Web.Syndication.ISyndicationNode]: ...
    @winrt_mixinmethod
    def GetXmlDocument(self: Windows.Web.Syndication.ISyndicationNode, format: Windows.Web.Syndication.SyndicationFormat) -> Windows.Data.Xml.Dom.XmlDocument: ...
    Title = property(get_Title, None)
    Collections = property(get_Collections, None)
    NodeName = property(get_NodeName, put_NodeName)
    NodeNamespace = property(get_NodeNamespace, put_NodeNamespace)
    NodeValue = property(get_NodeValue, put_NodeValue)
    Language = property(get_Language, put_Language)
    BaseUri = property(get_BaseUri, put_BaseUri)
    AttributeExtensions = property(get_AttributeExtensions, None)
    ElementExtensions = property(get_ElementExtensions, None)
make_head(_module, 'AtomPubClient')
make_head(_module, 'IAtomPubClient')
make_head(_module, 'IAtomPubClientFactory')
make_head(_module, 'IResourceCollection')
make_head(_module, 'IServiceDocument')
make_head(_module, 'IWorkspace')
make_head(_module, 'ResourceCollection')
make_head(_module, 'ServiceDocument')
make_head(_module, 'Workspace')
