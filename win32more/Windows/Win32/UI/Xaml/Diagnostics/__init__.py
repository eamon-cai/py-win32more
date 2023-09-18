from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Dxgi.Common
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.UI.Xaml.Diagnostics
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
E_UNKNOWNTYPE: win32more.Windows.Win32.Foundation.HRESULT = -2144665560
@winfunctype('Windows.UI.Xaml.dll')
def InitializeXamlDiagnostic(endPointName: win32more.Windows.Win32.Foundation.PWSTR, pid: UInt32, wszDllXamlDiagnostics: win32more.Windows.Win32.Foundation.PWSTR, wszTAPDllName: win32more.Windows.Win32.Foundation.PWSTR, tapClsid: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.UI.Xaml.dll')
def InitializeXamlDiagnosticsEx(endPointName: win32more.Windows.Win32.Foundation.PWSTR, pid: UInt32, wszDllXamlDiagnostics: win32more.Windows.Win32.Foundation.PWSTR, wszTAPDllName: win32more.Windows.Win32.Foundation.PWSTR, tapClsid: Guid, wszInitializationData: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
BaseValueSource = Int32
BaseValueSource_BaseValueSourceUnknown: BaseValueSource = 0
BaseValueSource_BaseValueSourceDefault: BaseValueSource = 1
BaseValueSource_BaseValueSourceBuiltInStyle: BaseValueSource = 2
BaseValueSource_BaseValueSourceStyle: BaseValueSource = 3
BaseValueSource_BaseValueSourceLocal: BaseValueSource = 4
BaseValueSource_Inherited: BaseValueSource = 5
BaseValueSource_DefaultStyleTrigger: BaseValueSource = 6
BaseValueSource_TemplateTrigger: BaseValueSource = 7
BaseValueSource_StyleTrigger: BaseValueSource = 8
BaseValueSource_ImplicitStyleReference: BaseValueSource = 9
BaseValueSource_ParentTemplate: BaseValueSource = 10
BaseValueSource_ParentTemplateTrigger: BaseValueSource = 11
BaseValueSource_Animation: BaseValueSource = 12
BaseValueSource_Coercion: BaseValueSource = 13
BaseValueSource_BaseValueSourceVisualState: BaseValueSource = 14
class BitmapDescription(EasyCastStructure):
    Width: UInt32
    Height: UInt32
    Format: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    AlphaMode: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_ALPHA_MODE
class CollectionElementValue(EasyCastStructure):
    Index: UInt32
    ValueType: win32more.Windows.Win32.Foundation.BSTR
    Value: win32more.Windows.Win32.Foundation.BSTR
    MetadataBits: Int64
class EnumType(EasyCastStructure):
    Name: win32more.Windows.Win32.Foundation.BSTR
    ValueInts: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY_head)
    ValueStrings: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY_head)
class IBitmapData(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d1a34ef2-cad8-4635-a3d2-fcda8d3f3caf}')
    @commethod(3)
    def CopyBytesTo(self, sourceOffsetInBytes: UInt32, maxBytesToCopy: UInt32, pvBytes: POINTER(Byte), numberOfBytesCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStride(self, pStride: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetBitmapDescription(self, pBitmapDescription: POINTER(win32more.Windows.Win32.UI.Xaml.Diagnostics.BitmapDescription_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSourceBitmapDescription(self, pBitmapDescription: POINTER(win32more.Windows.Win32.UI.Xaml.Diagnostics.BitmapDescription_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVisualTreeService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a593b11a-d17f-48bb-8f66-83910731c8a5}')
    @commethod(3)
    def AdviseVisualTreeChange(self, pCallback: win32more.Windows.Win32.UI.Xaml.Diagnostics.IVisualTreeServiceCallback_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseVisualTreeChange(self, pCallback: win32more.Windows.Win32.UI.Xaml.Diagnostics.IVisualTreeServiceCallback_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEnums(self, pCount: POINTER(UInt32), ppEnums: POINTER(POINTER(win32more.Windows.Win32.UI.Xaml.Diagnostics.EnumType_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateInstance(self, typeName: win32more.Windows.Win32.Foundation.BSTR, value: win32more.Windows.Win32.Foundation.BSTR, pInstanceHandle: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPropertyValuesChain(self, instanceHandle: UInt64, pSourceCount: POINTER(UInt32), ppPropertySources: POINTER(POINTER(win32more.Windows.Win32.UI.Xaml.Diagnostics.PropertyChainSource_head)), pPropertyCount: POINTER(UInt32), ppPropertyValues: POINTER(POINTER(win32more.Windows.Win32.UI.Xaml.Diagnostics.PropertyChainValue_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetProperty(self, instanceHandle: UInt64, value: UInt64, propertyIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ClearProperty(self, instanceHandle: UInt64, propertyIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCollectionCount(self, instanceHandle: UInt64, pCollectionSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCollectionElements(self, instanceHandle: UInt64, startIndex: UInt32, pElementCount: POINTER(UInt32), ppElementValues: POINTER(POINTER(win32more.Windows.Win32.UI.Xaml.Diagnostics.CollectionElementValue_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddChild(self, parent: UInt64, child: UInt64, index: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RemoveChild(self, parent: UInt64, index: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ClearChildren(self, parent: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVisualTreeService2(ComPtr):
    extends: win32more.Windows.Win32.UI.Xaml.Diagnostics.IVisualTreeService
    _iid_ = Guid('{130f5136-ec43-4f61-89c7-9801a36d2e95}')
    @commethod(15)
    def GetPropertyIndex(self, object: UInt64, propertyName: win32more.Windows.Win32.Foundation.PWSTR, pPropertyIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetProperty(self, object: UInt64, propertyIndex: UInt32, pValue: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ReplaceResource(self, resourceDictionary: UInt64, key: UInt64, newValue: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RenderTargetBitmap(self, handle: UInt64, options: win32more.Windows.Win32.UI.Xaml.Diagnostics.RenderTargetBitmapOptions, maxPixelWidth: UInt32, maxPixelHeight: UInt32, ppBitmapData: POINTER(win32more.Windows.Win32.UI.Xaml.Diagnostics.IBitmapData_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVisualTreeService3(ComPtr):
    extends: win32more.Windows.Win32.UI.Xaml.Diagnostics.IVisualTreeService2
    _iid_ = Guid('{0e79c6e0-85a0-4be8-b41a-655cf1fd19bd}')
    @commethod(19)
    def ResolveResource(self, resourceContext: UInt64, resourceName: win32more.Windows.Win32.Foundation.PWSTR, resourceType: win32more.Windows.Win32.UI.Xaml.Diagnostics.ResourceType, propertyIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDictionaryItem(self, dictionaryHandle: UInt64, resourceName: win32more.Windows.Win32.Foundation.PWSTR, resourceIsImplicitStyle: win32more.Windows.Win32.Foundation.BOOL, resourceHandle: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def AddDictionaryItem(self, dictionaryHandle: UInt64, resourceKey: UInt64, resourceHandle: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def RemoveDictionaryItem(self, dictionaryHandle: UInt64, resourceKey: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVisualTreeServiceCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa7a8931-80e4-4fec-8f3b-553f87b4966e}')
    @commethod(3)
    def OnVisualTreeChange(self, relation: win32more.Windows.Win32.UI.Xaml.Diagnostics.ParentChildRelation, element: win32more.Windows.Win32.UI.Xaml.Diagnostics.VisualElement, mutationType: win32more.Windows.Win32.UI.Xaml.Diagnostics.VisualMutationType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVisualTreeServiceCallback2(ComPtr):
    extends: win32more.Windows.Win32.UI.Xaml.Diagnostics.IVisualTreeServiceCallback
    _iid_ = Guid('{bad9eb88-ae77-4397-b948-5fa2db0a19ea}')
    @commethod(4)
    def OnElementStateChanged(self, element: UInt64, elementState: win32more.Windows.Win32.UI.Xaml.Diagnostics.VisualElementState, context: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXamlDiagnostics(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{18c9e2b6-3f43-4116-9f2b-ff935d7770d2}')
    @commethod(3)
    def GetDispatcher(self, ppDispatcher: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUiLayer(self, ppLayer: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetApplication(self, ppApplication: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIInspectableFromHandle(self, instanceHandle: UInt64, ppInstance: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetHandleFromIInspectable(self, pInstance: win32more.Windows.Win32.System.WinRT.IInspectable_head, pHandle: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def HitTest(self, rect: win32more.Windows.Win32.Foundation.RECT, pCount: POINTER(UInt32), ppInstanceHandles: POINTER(POINTER(UInt64))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RegisterInstance(self, pInstance: win32more.Windows.Win32.System.WinRT.IInspectable_head, pInstanceHandle: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetInitializationData(self, pInitializationData: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
MetadataBit = Int32
MetadataBit_None: MetadataBit = 0
MetadataBit_IsValueHandle: MetadataBit = 1
MetadataBit_IsPropertyReadOnly: MetadataBit = 2
MetadataBit_IsValueCollection: MetadataBit = 4
MetadataBit_IsValueCollectionReadOnly: MetadataBit = 8
MetadataBit_IsValueBindingExpression: MetadataBit = 16
MetadataBit_IsValueNull: MetadataBit = 32
MetadataBit_IsValueHandleAndEvaluatedValue: MetadataBit = 64
class ParentChildRelation(EasyCastStructure):
    Parent: UInt64
    Child: UInt64
    ChildIndex: UInt32
class PropertyChainSource(EasyCastStructure):
    Handle: UInt64
    TargetType: win32more.Windows.Win32.Foundation.BSTR
    Name: win32more.Windows.Win32.Foundation.BSTR
    Source: win32more.Windows.Win32.UI.Xaml.Diagnostics.BaseValueSource
    SrcInfo: win32more.Windows.Win32.UI.Xaml.Diagnostics.SourceInfo
class PropertyChainValue(EasyCastStructure):
    Index: UInt32
    Type: win32more.Windows.Win32.Foundation.BSTR
    DeclaringType: win32more.Windows.Win32.Foundation.BSTR
    ValueType: win32more.Windows.Win32.Foundation.BSTR
    ItemType: win32more.Windows.Win32.Foundation.BSTR
    Value: win32more.Windows.Win32.Foundation.BSTR
    Overridden: win32more.Windows.Win32.Foundation.BOOL
    MetadataBits: Int64
    PropertyName: win32more.Windows.Win32.Foundation.BSTR
    PropertyChainIndex: UInt32
RenderTargetBitmapOptions = Int32
RenderTargetBitmapOptions_RenderTarget: RenderTargetBitmapOptions = 0
RenderTargetBitmapOptions_RenderTargetAndChildren: RenderTargetBitmapOptions = 1
ResourceType = Int32
ResourceType_ResourceTypeStatic: ResourceType = 0
ResourceType_ResourceTypeTheme: ResourceType = 1
class SourceInfo(EasyCastStructure):
    FileName: win32more.Windows.Win32.Foundation.BSTR
    LineNumber: UInt32
    ColumnNumber: UInt32
    CharPosition: UInt32
    Hash: win32more.Windows.Win32.Foundation.BSTR
class VisualElement(EasyCastStructure):
    Handle: UInt64
    SrcInfo: win32more.Windows.Win32.UI.Xaml.Diagnostics.SourceInfo
    Type: win32more.Windows.Win32.Foundation.BSTR
    Name: win32more.Windows.Win32.Foundation.BSTR
    NumChildren: UInt32
VisualElementState = Int32
VisualElementState_ErrorResolved: VisualElementState = 0
VisualElementState_ErrorResourceNotFound: VisualElementState = 1
VisualElementState_ErrorInvalidResource: VisualElementState = 2
VisualMutationType = Int32
VisualMutationType_Add: VisualMutationType = 0
VisualMutationType_Remove: VisualMutationType = 1
make_head(_module, 'BitmapDescription')
make_head(_module, 'CollectionElementValue')
make_head(_module, 'EnumType')
make_head(_module, 'IBitmapData')
make_head(_module, 'IVisualTreeService')
make_head(_module, 'IVisualTreeService2')
make_head(_module, 'IVisualTreeService3')
make_head(_module, 'IVisualTreeServiceCallback')
make_head(_module, 'IVisualTreeServiceCallback2')
make_head(_module, 'IXamlDiagnostics')
make_head(_module, 'ParentChildRelation')
make_head(_module, 'PropertyChainSource')
make_head(_module, 'PropertyChainValue')
make_head(_module, 'SourceInfo')
make_head(_module, 'VisualElement')