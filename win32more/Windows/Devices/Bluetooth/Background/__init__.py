from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Bluetooth
import win32more.Windows.Devices.Bluetooth.Advertisement
import win32more.Windows.Devices.Bluetooth.Background
import win32more.Windows.Devices.Bluetooth.GenericAttributeProfile
import win32more.Windows.Devices.Bluetooth.Rfcomm
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking.Sockets
import win32more.Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
BluetoothEventTriggeringMode = Int32
BluetoothEventTriggeringMode_Serial: BluetoothEventTriggeringMode = 0
BluetoothEventTriggeringMode_Batch: BluetoothEventTriggeringMode = 1
BluetoothEventTriggeringMode_KeepLatest: BluetoothEventTriggeringMode = 2
class BluetoothLEAdvertisementPublisherTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementPublisherTriggerDetails
    _classid_ = 'Windows.Devices.Bluetooth.Background.BluetoothLEAdvertisementPublisherTriggerDetails'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementPublisherTriggerDetails) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatus: ...
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementPublisherTriggerDetails) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_SelectedTransmitPowerLevelInDBm(self: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementPublisherTriggerDetails2) -> win32more.Windows.Foundation.IReference[Int16]: ...
    Status = property(get_Status, None)
    Error = property(get_Error, None)
    SelectedTransmitPowerLevelInDBm = property(get_SelectedTransmitPowerLevelInDBm, None)
class BluetoothLEAdvertisementWatcherTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementWatcherTriggerDetails
    _classid_ = 'Windows.Devices.Bluetooth.Background.BluetoothLEAdvertisementWatcherTriggerDetails'
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementWatcherTriggerDetails) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_Advertisements(self: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementWatcherTriggerDetails) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementReceivedEventArgs]: ...
    @winrt_mixinmethod
    def get_SignalStrengthFilter(self: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementWatcherTriggerDetails) -> win32more.Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter: ...
    Error = property(get_Error, None)
    Advertisements = property(get_Advertisements, None)
    SignalStrengthFilter = property(get_SignalStrengthFilter, None)
class GattCharacteristicNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails
    _classid_ = 'Windows.Devices.Bluetooth.Background.GattCharacteristicNotificationTriggerDetails'
    @winrt_mixinmethod
    def get_Characteristic(self: win32more.Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails2) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_EventTriggeringMode(self: win32more.Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails2) -> win32more.Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode: ...
    @winrt_mixinmethod
    def get_ValueChangedEvents(self: win32more.Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattValueChangedEventArgs]: ...
    Characteristic = property(get_Characteristic, None)
    Value = property(get_Value, None)
    Error = property(get_Error, None)
    EventTriggeringMode = property(get_EventTriggeringMode, None)
    ValueChangedEvents = property(get_ValueChangedEvents, None)
class _GattServiceProviderConnection_Meta_(ComPtr.__class__):
    pass
class GattServiceProviderConnection(ComPtr, metaclass=_GattServiceProviderConnection_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IGattServiceProviderConnection
    _classid_ = 'Windows.Devices.Bluetooth.Background.GattServiceProviderConnection'
    @winrt_mixinmethod
    def get_TriggerId(self: win32more.Windows.Devices.Bluetooth.Background.IGattServiceProviderConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Service(self: win32more.Windows.Devices.Bluetooth.Background.IGattServiceProviderConnection) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalService: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Bluetooth.Background.IGattServiceProviderConnection) -> Void: ...
    @winrt_classmethod
    def get_AllServices(cls: win32more.Windows.Devices.Bluetooth.Background.IGattServiceProviderConnectionStatics) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Devices.Bluetooth.Background.GattServiceProviderConnection]: ...
    TriggerId = property(get_TriggerId, None)
    Service = property(get_Service, None)
    _GattServiceProviderConnection_Meta_.AllServices = property(get_AllServices.__wrapped__, None)
class GattServiceProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IGattServiceProviderTriggerDetails
    _classid_ = 'Windows.Devices.Bluetooth.Background.GattServiceProviderTriggerDetails'
    @winrt_mixinmethod
    def get_Connection(self: win32more.Windows.Devices.Bluetooth.Background.IGattServiceProviderTriggerDetails) -> win32more.Windows.Devices.Bluetooth.Background.GattServiceProviderConnection: ...
    Connection = property(get_Connection, None)
class IBluetoothLEAdvertisementPublisherTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementPublisherTriggerDetails'
    _iid_ = Guid('{610eca86-3480-41c9-a918-7ddadf207e00}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatus: ...
    @winrt_commethod(7)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    Status = property(get_Status, None)
    Error = property(get_Error, None)
class IBluetoothLEAdvertisementPublisherTriggerDetails2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementPublisherTriggerDetails2'
    _iid_ = Guid('{d4a3d025-c601-42d6-9829-4ccb3f5cd77f}')
    @winrt_commethod(6)
    def get_SelectedTransmitPowerLevelInDBm(self) -> win32more.Windows.Foundation.IReference[Int16]: ...
    SelectedTransmitPowerLevelInDBm = property(get_SelectedTransmitPowerLevelInDBm, None)
class IBluetoothLEAdvertisementWatcherTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementWatcherTriggerDetails'
    _iid_ = Guid('{a7db5ad7-2257-4e69-9784-fee645c1dce0}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_commethod(7)
    def get_Advertisements(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementReceivedEventArgs]: ...
    @winrt_commethod(8)
    def get_SignalStrengthFilter(self) -> win32more.Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter: ...
    Error = property(get_Error, None)
    Advertisements = property(get_Advertisements, None)
    SignalStrengthFilter = property(get_SignalStrengthFilter, None)
class IGattCharacteristicNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails'
    _iid_ = Guid('{9ba03b18-0fec-436a-93b1-f46c697532a2}')
    @winrt_commethod(6)
    def get_Characteristic(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic: ...
    @winrt_commethod(7)
    def get_Value(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Characteristic = property(get_Characteristic, None)
    Value = property(get_Value, None)
class IGattCharacteristicNotificationTriggerDetails2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails2'
    _iid_ = Guid('{727a50dc-949d-454a-b192-983467e3d50f}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_commethod(7)
    def get_EventTriggeringMode(self) -> win32more.Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode: ...
    @winrt_commethod(8)
    def get_ValueChangedEvents(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattValueChangedEventArgs]: ...
    Error = property(get_Error, None)
    EventTriggeringMode = property(get_EventTriggeringMode, None)
    ValueChangedEvents = property(get_ValueChangedEvents, None)
class IGattServiceProviderConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IGattServiceProviderConnection'
    _iid_ = Guid('{7fa1b9b9-2f13-40b5-9582-8eb78e98ef13}')
    @winrt_commethod(6)
    def get_TriggerId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Service(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalService: ...
    @winrt_commethod(8)
    def Start(self) -> Void: ...
    TriggerId = property(get_TriggerId, None)
    Service = property(get_Service, None)
class IGattServiceProviderConnectionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IGattServiceProviderConnectionStatics'
    _iid_ = Guid('{3d509f4b-0b0e-4466-b8cd-6ebdda1fa17d}')
    @winrt_commethod(6)
    def get_AllServices(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Devices.Bluetooth.Background.GattServiceProviderConnection]: ...
    AllServices = property(get_AllServices, None)
class IGattServiceProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IGattServiceProviderTriggerDetails'
    _iid_ = Guid('{ae8c0625-05ff-4afb-b16a-de95f3cf0158}')
    @winrt_commethod(6)
    def get_Connection(self) -> win32more.Windows.Devices.Bluetooth.Background.GattServiceProviderConnection: ...
    Connection = property(get_Connection, None)
class IRfcommConnectionTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IRfcommConnectionTriggerDetails'
    _iid_ = Guid('{f922734d-2e3c-4efc-ab59-fc5cf96f97e3}')
    @winrt_commethod(6)
    def get_Socket(self) -> win32more.Windows.Networking.Sockets.StreamSocket: ...
    @winrt_commethod(7)
    def get_Incoming(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_RemoteDevice(self) -> win32more.Windows.Devices.Bluetooth.BluetoothDevice: ...
    Socket = property(get_Socket, None)
    Incoming = property(get_Incoming, None)
    RemoteDevice = property(get_RemoteDevice, None)
class IRfcommInboundConnectionInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation'
    _iid_ = Guid('{6d3e75a8-5429-4059-92e3-1e8b65528707}')
    @winrt_commethod(6)
    def get_SdpRecord(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def put_SdpRecord(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(8)
    def get_LocalServiceId(self) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(9)
    def put_LocalServiceId(self, value: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> Void: ...
    @winrt_commethod(10)
    def get_ServiceCapabilities(self) -> win32more.Windows.Devices.Bluetooth.BluetoothServiceCapabilities: ...
    @winrt_commethod(11)
    def put_ServiceCapabilities(self, value: win32more.Windows.Devices.Bluetooth.BluetoothServiceCapabilities) -> Void: ...
    SdpRecord = property(get_SdpRecord, put_SdpRecord)
    LocalServiceId = property(get_LocalServiceId, put_LocalServiceId)
    ServiceCapabilities = property(get_ServiceCapabilities, put_ServiceCapabilities)
class IRfcommOutboundConnectionInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IRfcommOutboundConnectionInformation'
    _iid_ = Guid('{b091227b-f434-4cb0-99b1-4ab8cedaedd7}')
    @winrt_commethod(6)
    def get_RemoteServiceId(self) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(7)
    def put_RemoteServiceId(self, value: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> Void: ...
    RemoteServiceId = property(get_RemoteServiceId, put_RemoteServiceId)
class RfcommConnectionTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IRfcommConnectionTriggerDetails
    _classid_ = 'Windows.Devices.Bluetooth.Background.RfcommConnectionTriggerDetails'
    @winrt_mixinmethod
    def get_Socket(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommConnectionTriggerDetails) -> win32more.Windows.Networking.Sockets.StreamSocket: ...
    @winrt_mixinmethod
    def get_Incoming(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommConnectionTriggerDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_RemoteDevice(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommConnectionTriggerDetails) -> win32more.Windows.Devices.Bluetooth.BluetoothDevice: ...
    Socket = property(get_Socket, None)
    Incoming = property(get_Incoming, None)
    RemoteDevice = property(get_RemoteDevice, None)
class RfcommInboundConnectionInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation
    _classid_ = 'Windows.Devices.Bluetooth.Background.RfcommInboundConnectionInformation'
    @winrt_mixinmethod
    def get_SdpRecord(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_SdpRecord(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_LocalServiceId(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_mixinmethod
    def put_LocalServiceId(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation, value: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> Void: ...
    @winrt_mixinmethod
    def get_ServiceCapabilities(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation) -> win32more.Windows.Devices.Bluetooth.BluetoothServiceCapabilities: ...
    @winrt_mixinmethod
    def put_ServiceCapabilities(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation, value: win32more.Windows.Devices.Bluetooth.BluetoothServiceCapabilities) -> Void: ...
    SdpRecord = property(get_SdpRecord, put_SdpRecord)
    LocalServiceId = property(get_LocalServiceId, put_LocalServiceId)
    ServiceCapabilities = property(get_ServiceCapabilities, put_ServiceCapabilities)
class RfcommOutboundConnectionInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IRfcommOutboundConnectionInformation
    _classid_ = 'Windows.Devices.Bluetooth.Background.RfcommOutboundConnectionInformation'
    @winrt_mixinmethod
    def get_RemoteServiceId(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommOutboundConnectionInformation) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_mixinmethod
    def put_RemoteServiceId(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommOutboundConnectionInformation, value: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> Void: ...
    RemoteServiceId = property(get_RemoteServiceId, put_RemoteServiceId)
make_head(_module, 'BluetoothLEAdvertisementPublisherTriggerDetails')
make_head(_module, 'BluetoothLEAdvertisementWatcherTriggerDetails')
make_head(_module, 'GattCharacteristicNotificationTriggerDetails')
make_head(_module, 'GattServiceProviderConnection')
make_head(_module, 'GattServiceProviderTriggerDetails')
make_head(_module, 'IBluetoothLEAdvertisementPublisherTriggerDetails')
make_head(_module, 'IBluetoothLEAdvertisementPublisherTriggerDetails2')
make_head(_module, 'IBluetoothLEAdvertisementWatcherTriggerDetails')
make_head(_module, 'IGattCharacteristicNotificationTriggerDetails')
make_head(_module, 'IGattCharacteristicNotificationTriggerDetails2')
make_head(_module, 'IGattServiceProviderConnection')
make_head(_module, 'IGattServiceProviderConnectionStatics')
make_head(_module, 'IGattServiceProviderTriggerDetails')
make_head(_module, 'IRfcommConnectionTriggerDetails')
make_head(_module, 'IRfcommInboundConnectionInformation')
make_head(_module, 'IRfcommOutboundConnectionInformation')
make_head(_module, 'RfcommConnectionTriggerDetails')
make_head(_module, 'RfcommInboundConnectionInformation')
make_head(_module, 'RfcommOutboundConnectionInformation')