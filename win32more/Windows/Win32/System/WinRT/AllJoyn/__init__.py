from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.System.WinRT.AllJoyn
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IWindowsDevicesAllJoynBusAttachmentFactoryInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4b8f7505-b239-4e7b-88af-f6682575d861}')
    @commethod(6)
    def CreateFromWin32Handle(self, win32handle: UInt64, enableAboutData: Byte, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWindowsDevicesAllJoynBusAttachmentInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{fd89c65b-b50e-4a19-9d0c-b42b783281cd}')
    @commethod(6)
    def get_Win32Handle(self, value: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWindowsDevicesAllJoynBusObjectFactoryInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6174e506-8b95-4e36-95c0-b88fed34938c}')
    @commethod(6)
    def CreateFromWin32Handle(self, win32handle: UInt64, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWindowsDevicesAllJoynBusObjectInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d78aa3d5-5054-428f-99f2-ec3a5de3c3bc}')
    @commethod(6)
    def AddPropertyGetHandler(self, context: VoidPtr, interfaceName: win32more.Windows.Win32.System.WinRT.HSTRING, callback: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddPropertySetHandler(self, context: VoidPtr, interfaceName: win32more.Windows.Win32.System.WinRT.HSTRING, callback: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Win32Handle(self, value: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IWindowsDevicesAllJoynBusAttachmentFactoryInterop')
make_head(_module, 'IWindowsDevicesAllJoynBusAttachmentInterop')
make_head(_module, 'IWindowsDevicesAllJoynBusObjectFactoryInterop')
make_head(_module, 'IWindowsDevicesAllJoynBusObjectInterop')