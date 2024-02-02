from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.HumanInterfaceDevice
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class HidBooleanControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.HumanInterfaceDevice.IHidBooleanControl
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidBooleanControl'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidBooleanControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_UsagePage(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidBooleanControl) -> UInt16: ...
    @winrt_mixinmethod
    def get_UsageId(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidBooleanControl) -> UInt16: ...
    @winrt_mixinmethod
    def get_IsActive(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidBooleanControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsActive(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidBooleanControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ControlDescription(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidBooleanControl) -> win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription: ...
    ControlDescription = property(get_ControlDescription, None)
    Id = property(get_Id, None)
    IsActive = property(get_IsActive, put_IsActive)
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
class HidBooleanControlDescription(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_ReportId(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription) -> UInt16: ...
    @winrt_mixinmethod
    def get_ReportType(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription) -> win32more.Windows.Devices.HumanInterfaceDevice.HidReportType: ...
    @winrt_mixinmethod
    def get_UsagePage(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription) -> UInt16: ...
    @winrt_mixinmethod
    def get_UsageId(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription) -> UInt16: ...
    @winrt_mixinmethod
    def get_ParentCollections(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidCollection]: ...
    @winrt_mixinmethod
    def get_IsAbsolute(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription2) -> Boolean: ...
    Id = property(get_Id, None)
    IsAbsolute = property(get_IsAbsolute, None)
    ParentCollections = property(get_ParentCollections, None)
    ReportId = property(get_ReportId, None)
    ReportType = property(get_ReportType, None)
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
class HidCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.HumanInterfaceDevice.IHidCollection
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidCollection'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidCollection) -> UInt32: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidCollection) -> win32more.Windows.Devices.HumanInterfaceDevice.HidCollectionType: ...
    @winrt_mixinmethod
    def get_UsagePage(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidCollection) -> UInt32: ...
    @winrt_mixinmethod
    def get_UsageId(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidCollection) -> UInt32: ...
    Id = property(get_Id, None)
    Type = property(get_Type, None)
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
class HidCollectionType(Int32):  # enum
    Physical = 0
    Application = 1
    Logical = 2
    Report = 3
    NamedArray = 4
    UsageSwitch = 5
    UsageModifier = 6
    Other = 7
class HidDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidDevice'
    @winrt_mixinmethod
    def get_VendorId(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice) -> UInt16: ...
    @winrt_mixinmethod
    def get_ProductId(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice) -> UInt16: ...
    @winrt_mixinmethod
    def get_Version(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice) -> UInt16: ...
    @winrt_mixinmethod
    def get_UsagePage(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice) -> UInt16: ...
    @winrt_mixinmethod
    def get_UsageId(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice) -> UInt16: ...
    @winrt_mixinmethod
    def GetInputReportAsync(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.HumanInterfaceDevice.HidInputReport]: ...
    @winrt_mixinmethod
    def GetInputReportByIdAsync(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice, reportId: UInt16) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.HumanInterfaceDevice.HidInputReport]: ...
    @winrt_mixinmethod
    def GetFeatureReportAsync(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.HumanInterfaceDevice.HidFeatureReport]: ...
    @winrt_mixinmethod
    def GetFeatureReportByIdAsync(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice, reportId: UInt16) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.HumanInterfaceDevice.HidFeatureReport]: ...
    @winrt_mixinmethod
    def CreateOutputReport(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice) -> win32more.Windows.Devices.HumanInterfaceDevice.HidOutputReport: ...
    @winrt_mixinmethod
    def CreateOutputReportById(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice, reportId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidOutputReport: ...
    @winrt_mixinmethod
    def CreateFeatureReport(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice) -> win32more.Windows.Devices.HumanInterfaceDevice.HidFeatureReport: ...
    @winrt_mixinmethod
    def CreateFeatureReportById(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice, reportId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidFeatureReport: ...
    @winrt_mixinmethod
    def SendOutputReportAsync(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice, outputReport: win32more.Windows.Devices.HumanInterfaceDevice.HidOutputReport) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def SendFeatureReportAsync(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice, featureReport: win32more.Windows.Devices.HumanInterfaceDevice.HidFeatureReport) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def GetBooleanControlDescriptions(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice, reportType: win32more.Windows.Devices.HumanInterfaceDevice.HidReportType, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription]: ...
    @winrt_mixinmethod
    def GetNumericControlDescriptions(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice, reportType: win32more.Windows.Devices.HumanInterfaceDevice.HidReportType, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription]: ...
    @winrt_mixinmethod
    def add_InputReportReceived(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice, reportHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.HumanInterfaceDevice.HidDevice, win32more.Windows.Devices.HumanInterfaceDevice.HidInputReportReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InputReportReceived(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidDevice, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.HumanInterfaceDevice.IHidDeviceStatics, usagePage: UInt16, usageId: UInt16) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorVidPid(cls: win32more.Windows.Devices.HumanInterfaceDevice.IHidDeviceStatics, usagePage: UInt16, usageId: UInt16, vendorId: UInt16, productId: UInt16) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.HumanInterfaceDevice.IHidDeviceStatics, deviceId: WinRT_String, accessMode: win32more.Windows.Storage.FileAccessMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.HumanInterfaceDevice.HidDevice]: ...
    ProductId = property(get_ProductId, None)
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
    VendorId = property(get_VendorId, None)
    Version = property(get_Version, None)
class HidFeatureReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.HumanInterfaceDevice.IHidFeatureReport
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidFeatureReport'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidFeatureReport) -> UInt16: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidFeatureReport) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Data(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidFeatureReport, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def GetBooleanControl(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidFeatureReport, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_mixinmethod
    def GetBooleanControlByDescription(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidFeatureReport, controlDescription: win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription) -> win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_mixinmethod
    def GetNumericControl(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidFeatureReport, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    @winrt_mixinmethod
    def GetNumericControlByDescription(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidFeatureReport, controlDescription: win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription) -> win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    Data = property(get_Data, put_Data)
    Id = property(get_Id, None)
class HidInputReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.HumanInterfaceDevice.IHidInputReport
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidInputReport'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidInputReport) -> UInt16: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidInputReport) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_ActivatedBooleanControls(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidInputReport) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl]: ...
    @winrt_mixinmethod
    def get_TransitionedBooleanControls(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidInputReport) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl]: ...
    @winrt_mixinmethod
    def GetBooleanControl(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidInputReport, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_mixinmethod
    def GetBooleanControlByDescription(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidInputReport, controlDescription: win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription) -> win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_mixinmethod
    def GetNumericControl(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidInputReport, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    @winrt_mixinmethod
    def GetNumericControlByDescription(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidInputReport, controlDescription: win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription) -> win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    ActivatedBooleanControls = property(get_ActivatedBooleanControls, None)
    Data = property(get_Data, None)
    Id = property(get_Id, None)
    TransitionedBooleanControls = property(get_TransitionedBooleanControls, None)
class HidInputReportReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.HumanInterfaceDevice.IHidInputReportReceivedEventArgs
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidInputReportReceivedEventArgs'
    @winrt_mixinmethod
    def get_Report(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidInputReportReceivedEventArgs) -> win32more.Windows.Devices.HumanInterfaceDevice.HidInputReport: ...
    Report = property(get_Report, None)
class HidNumericControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControl
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidNumericControl'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_IsGrouped(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_UsagePage(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControl) -> UInt16: ...
    @winrt_mixinmethod
    def get_UsageId(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControl) -> UInt16: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControl) -> Int64: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControl, value: Int64) -> Void: ...
    @winrt_mixinmethod
    def get_ScaledValue(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControl) -> Int64: ...
    @winrt_mixinmethod
    def put_ScaledValue(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControl, value: Int64) -> Void: ...
    @winrt_mixinmethod
    def get_ControlDescription(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControl) -> win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription: ...
    ControlDescription = property(get_ControlDescription, None)
    Id = property(get_Id, None)
    IsGrouped = property(get_IsGrouped, None)
    ScaledValue = property(get_ScaledValue, put_ScaledValue)
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
    Value = property(get_Value, put_Value)
class HidNumericControlDescription(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_ReportId(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt16: ...
    @winrt_mixinmethod
    def get_ReportType(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> win32more.Windows.Devices.HumanInterfaceDevice.HidReportType: ...
    @winrt_mixinmethod
    def get_ReportSize(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_ReportCount(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_UsagePage(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt16: ...
    @winrt_mixinmethod
    def get_UsageId(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt16: ...
    @winrt_mixinmethod
    def get_LogicalMinimum(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> Int32: ...
    @winrt_mixinmethod
    def get_LogicalMaximum(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> Int32: ...
    @winrt_mixinmethod
    def get_PhysicalMinimum(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> Int32: ...
    @winrt_mixinmethod
    def get_PhysicalMaximum(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> Int32: ...
    @winrt_mixinmethod
    def get_UnitExponent(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_Unit(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_IsAbsolute(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasNull(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> Boolean: ...
    @winrt_mixinmethod
    def get_ParentCollections(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidCollection]: ...
    HasNull = property(get_HasNull, None)
    Id = property(get_Id, None)
    IsAbsolute = property(get_IsAbsolute, None)
    LogicalMaximum = property(get_LogicalMaximum, None)
    LogicalMinimum = property(get_LogicalMinimum, None)
    ParentCollections = property(get_ParentCollections, None)
    PhysicalMaximum = property(get_PhysicalMaximum, None)
    PhysicalMinimum = property(get_PhysicalMinimum, None)
    ReportCount = property(get_ReportCount, None)
    ReportId = property(get_ReportId, None)
    ReportSize = property(get_ReportSize, None)
    ReportType = property(get_ReportType, None)
    Unit = property(get_Unit, None)
    UnitExponent = property(get_UnitExponent, None)
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
class HidOutputReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.HumanInterfaceDevice.IHidOutputReport
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidOutputReport'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidOutputReport) -> UInt16: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidOutputReport) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Data(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidOutputReport, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def GetBooleanControl(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidOutputReport, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_mixinmethod
    def GetBooleanControlByDescription(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidOutputReport, controlDescription: win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription) -> win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_mixinmethod
    def GetNumericControl(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidOutputReport, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    @winrt_mixinmethod
    def GetNumericControlByDescription(self: win32more.Windows.Devices.HumanInterfaceDevice.IHidOutputReport, controlDescription: win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription) -> win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    Data = property(get_Data, put_Data)
    Id = property(get_Id, None)
class HidReportType(Int32):  # enum
    Input = 0
    Output = 1
    Feature = 2
class IHidBooleanControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidBooleanControl'
    _iid_ = Guid('{524df48a-3695-408c-bba2-e2eb5abfbc20}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_UsagePage(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_UsageId(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsActive(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_ControlDescription(self) -> win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription: ...
    ControlDescription = property(get_ControlDescription, None)
    Id = property(get_Id, None)
    IsActive = property(get_IsActive, put_IsActive)
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
class IHidBooleanControlDescription(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription'
    _iid_ = Guid('{6196e543-29d8-4a2a-8683-849e207bbe31}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ReportId(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_ReportType(self) -> win32more.Windows.Devices.HumanInterfaceDevice.HidReportType: ...
    @winrt_commethod(9)
    def get_UsagePage(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_UsageId(self) -> UInt16: ...
    @winrt_commethod(11)
    def get_ParentCollections(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidCollection]: ...
    Id = property(get_Id, None)
    ParentCollections = property(get_ParentCollections, None)
    ReportId = property(get_ReportId, None)
    ReportType = property(get_ReportType, None)
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
class IHidBooleanControlDescription2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription2'
    _iid_ = Guid('{c8eed2ea-8a77-4c36-aa00-5ff0449d3e73}')
    @winrt_commethod(6)
    def get_IsAbsolute(self) -> Boolean: ...
    IsAbsolute = property(get_IsAbsolute, None)
class IHidCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidCollection'
    _iid_ = Guid('{7189f5a3-32f1-46e3-befd-44d2663b7e6a}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Type(self) -> win32more.Windows.Devices.HumanInterfaceDevice.HidCollectionType: ...
    @winrt_commethod(8)
    def get_UsagePage(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_UsageId(self) -> UInt32: ...
    Id = property(get_Id, None)
    Type = property(get_Type, None)
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
class IHidDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidDevice'
    _iid_ = Guid('{5f8a14e7-2200-432e-95da-d09b87d574a8}')
    @winrt_commethod(6)
    def get_VendorId(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_ProductId(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_Version(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_UsagePage(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_UsageId(self) -> UInt16: ...
    @winrt_commethod(11)
    def GetInputReportAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.HumanInterfaceDevice.HidInputReport]: ...
    @winrt_commethod(12)
    def GetInputReportByIdAsync(self, reportId: UInt16) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.HumanInterfaceDevice.HidInputReport]: ...
    @winrt_commethod(13)
    def GetFeatureReportAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.HumanInterfaceDevice.HidFeatureReport]: ...
    @winrt_commethod(14)
    def GetFeatureReportByIdAsync(self, reportId: UInt16) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.HumanInterfaceDevice.HidFeatureReport]: ...
    @winrt_commethod(15)
    def CreateOutputReport(self) -> win32more.Windows.Devices.HumanInterfaceDevice.HidOutputReport: ...
    @winrt_commethod(16)
    def CreateOutputReportById(self, reportId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidOutputReport: ...
    @winrt_commethod(17)
    def CreateFeatureReport(self) -> win32more.Windows.Devices.HumanInterfaceDevice.HidFeatureReport: ...
    @winrt_commethod(18)
    def CreateFeatureReportById(self, reportId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidFeatureReport: ...
    @winrt_commethod(19)
    def SendOutputReportAsync(self, outputReport: win32more.Windows.Devices.HumanInterfaceDevice.HidOutputReport) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(20)
    def SendFeatureReportAsync(self, featureReport: win32more.Windows.Devices.HumanInterfaceDevice.HidFeatureReport) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(21)
    def GetBooleanControlDescriptions(self, reportType: win32more.Windows.Devices.HumanInterfaceDevice.HidReportType, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription]: ...
    @winrt_commethod(22)
    def GetNumericControlDescriptions(self, reportType: win32more.Windows.Devices.HumanInterfaceDevice.HidReportType, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription]: ...
    @winrt_commethod(23)
    def add_InputReportReceived(self, reportHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.HumanInterfaceDevice.HidDevice, win32more.Windows.Devices.HumanInterfaceDevice.HidInputReportReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_InputReportReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ProductId = property(get_ProductId, None)
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
    VendorId = property(get_VendorId, None)
    Version = property(get_Version, None)
class IHidDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidDeviceStatics'
    _iid_ = Guid('{9e5981e4-9856-418c-9f73-77de0cd85754}')
    @winrt_commethod(6)
    def GetDeviceSelector(self, usagePage: UInt16, usageId: UInt16) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorVidPid(self, usagePage: UInt16, usageId: UInt16, vendorId: UInt16, productId: UInt16) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String, accessMode: win32more.Windows.Storage.FileAccessMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.HumanInterfaceDevice.HidDevice]: ...
class IHidFeatureReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidFeatureReport'
    _iid_ = Guid('{841d9b79-5ae5-46e3-82ef-1fec5c8942f4}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Data(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def put_Data(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(9)
    def GetBooleanControl(self, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_commethod(10)
    def GetBooleanControlByDescription(self, controlDescription: win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription) -> win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_commethod(11)
    def GetNumericControl(self, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    @winrt_commethod(12)
    def GetNumericControlByDescription(self, controlDescription: win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription) -> win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    Data = property(get_Data, put_Data)
    Id = property(get_Id, None)
class IHidInputReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidInputReport'
    _iid_ = Guid('{c35d0e50-f7e7-4e8d-b23e-cabbe56b90e9}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Data(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_ActivatedBooleanControls(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl]: ...
    @winrt_commethod(9)
    def get_TransitionedBooleanControls(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl]: ...
    @winrt_commethod(10)
    def GetBooleanControl(self, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_commethod(11)
    def GetBooleanControlByDescription(self, controlDescription: win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription) -> win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_commethod(12)
    def GetNumericControl(self, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    @winrt_commethod(13)
    def GetNumericControlByDescription(self, controlDescription: win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription) -> win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    ActivatedBooleanControls = property(get_ActivatedBooleanControls, None)
    Data = property(get_Data, None)
    Id = property(get_Id, None)
    TransitionedBooleanControls = property(get_TransitionedBooleanControls, None)
class IHidInputReportReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidInputReportReceivedEventArgs'
    _iid_ = Guid('{7059c5cb-59b2-4dc2-985c-0adc6136fa2d}')
    @winrt_commethod(6)
    def get_Report(self) -> win32more.Windows.Devices.HumanInterfaceDevice.HidInputReport: ...
    Report = property(get_Report, None)
class IHidNumericControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidNumericControl'
    _iid_ = Guid('{e38a12a5-35a7-4b75-89c8-fb1f28b10823}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_IsGrouped(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_UsagePage(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_UsageId(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_Value(self) -> Int64: ...
    @winrt_commethod(11)
    def put_Value(self, value: Int64) -> Void: ...
    @winrt_commethod(12)
    def get_ScaledValue(self) -> Int64: ...
    @winrt_commethod(13)
    def put_ScaledValue(self, value: Int64) -> Void: ...
    @winrt_commethod(14)
    def get_ControlDescription(self) -> win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription: ...
    ControlDescription = property(get_ControlDescription, None)
    Id = property(get_Id, None)
    IsGrouped = property(get_IsGrouped, None)
    ScaledValue = property(get_ScaledValue, put_ScaledValue)
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
    Value = property(get_Value, put_Value)
class IHidNumericControlDescription(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription'
    _iid_ = Guid('{638d5e86-1d97-4c75-927f-5ff58ba05e32}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ReportId(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_ReportType(self) -> win32more.Windows.Devices.HumanInterfaceDevice.HidReportType: ...
    @winrt_commethod(9)
    def get_ReportSize(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_ReportCount(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_UsagePage(self) -> UInt16: ...
    @winrt_commethod(12)
    def get_UsageId(self) -> UInt16: ...
    @winrt_commethod(13)
    def get_LogicalMinimum(self) -> Int32: ...
    @winrt_commethod(14)
    def get_LogicalMaximum(self) -> Int32: ...
    @winrt_commethod(15)
    def get_PhysicalMinimum(self) -> Int32: ...
    @winrt_commethod(16)
    def get_PhysicalMaximum(self) -> Int32: ...
    @winrt_commethod(17)
    def get_UnitExponent(self) -> UInt32: ...
    @winrt_commethod(18)
    def get_Unit(self) -> UInt32: ...
    @winrt_commethod(19)
    def get_IsAbsolute(self) -> Boolean: ...
    @winrt_commethod(20)
    def get_HasNull(self) -> Boolean: ...
    @winrt_commethod(21)
    def get_ParentCollections(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidCollection]: ...
    HasNull = property(get_HasNull, None)
    Id = property(get_Id, None)
    IsAbsolute = property(get_IsAbsolute, None)
    LogicalMaximum = property(get_LogicalMaximum, None)
    LogicalMinimum = property(get_LogicalMinimum, None)
    ParentCollections = property(get_ParentCollections, None)
    PhysicalMaximum = property(get_PhysicalMaximum, None)
    PhysicalMinimum = property(get_PhysicalMinimum, None)
    ReportCount = property(get_ReportCount, None)
    ReportId = property(get_ReportId, None)
    ReportSize = property(get_ReportSize, None)
    ReportType = property(get_ReportType, None)
    Unit = property(get_Unit, None)
    UnitExponent = property(get_UnitExponent, None)
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
class IHidOutputReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidOutputReport'
    _iid_ = Guid('{62cb2544-c896-4463-93c1-df9db053c450}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Data(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def put_Data(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(9)
    def GetBooleanControl(self, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_commethod(10)
    def GetBooleanControlByDescription(self, controlDescription: win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription) -> win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_commethod(11)
    def GetNumericControl(self, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    @winrt_commethod(12)
    def GetNumericControlByDescription(self, controlDescription: win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription) -> win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    Data = property(get_Data, put_Data)
    Id = property(get_Id, None)


make_ready(__name__)
