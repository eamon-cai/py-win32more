from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.System.Com
import Windows.Win32.System.Com.Marshal
import Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('OLEAUT32.dll')
def BSTR_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Foundation.BSTR)) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def BSTR_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Foundation.BSTR)) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def BSTR_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Foundation.BSTR)) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def BSTR_UserFree(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Foundation.BSTR)) -> Void: ...
@winfunctype('OLE32.dll')
def HWND_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Foundation.HWND)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HWND_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Foundation.HWND)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HWND_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Foundation.HWND)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HWND_UserFree(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Foundation.HWND)) -> Void: ...
@winfunctype('OLEAUT32.dll')
def BSTR_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Foundation.BSTR)) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def BSTR_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Foundation.BSTR)) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def BSTR_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Foundation.BSTR)) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def BSTR_UserFree64(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Foundation.BSTR)) -> Void: ...
@winfunctype('OLE32.dll')
def HWND_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Foundation.HWND)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HWND_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Foundation.HWND)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HWND_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Foundation.HWND)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HWND_UserFree64(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Foundation.HWND)) -> Void: ...
@winfunctype('OLE32.dll')
def CLIPFORMAT_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(UInt16)) -> UInt32: ...
@winfunctype('OLE32.dll')
def CLIPFORMAT_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(UInt16)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def CLIPFORMAT_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(UInt16)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def CLIPFORMAT_UserFree(param0: POINTER(UInt32), param1: POINTER(UInt16)) -> Void: ...
@winfunctype('OLE32.dll')
def HBITMAP_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HBITMAP_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HBITMAP_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HBITMAP_UserFree(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> Void: ...
@winfunctype('OLE32.dll')
def HDC_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Graphics.Gdi.HDC)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HDC_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HDC)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HDC_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HDC)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HDC_UserFree(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Graphics.Gdi.HDC)) -> Void: ...
@winfunctype('OLE32.dll')
def HICON_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HICON_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HICON_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HICON_UserFree(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON)) -> Void: ...
@winfunctype('ole32.dll')
def SNB_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(POINTER(POINTER(UInt16)))) -> UInt32: ...
@winfunctype('ole32.dll')
def SNB_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(POINTER(POINTER(UInt16)))) -> POINTER(Byte): ...
@winfunctype('ole32.dll')
def SNB_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(POINTER(POINTER(UInt16)))) -> POINTER(Byte): ...
@winfunctype('ole32.dll')
def SNB_UserFree(param0: POINTER(UInt32), param1: POINTER(POINTER(POINTER(UInt16)))) -> Void: ...
@winfunctype('OLE32.dll')
def STGMEDIUM_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.System.Com.STGMEDIUM_head)) -> UInt32: ...
@winfunctype('OLE32.dll')
def STGMEDIUM_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.System.Com.STGMEDIUM_head)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def STGMEDIUM_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.System.Com.STGMEDIUM_head)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def STGMEDIUM_UserFree(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.System.Com.STGMEDIUM_head)) -> Void: ...
@winfunctype('OLE32.dll')
def CLIPFORMAT_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(UInt16)) -> UInt32: ...
@winfunctype('OLE32.dll')
def CLIPFORMAT_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(UInt16)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def CLIPFORMAT_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(UInt16)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def CLIPFORMAT_UserFree64(param0: POINTER(UInt32), param1: POINTER(UInt16)) -> Void: ...
@winfunctype('OLE32.dll')
def HBITMAP_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HBITMAP_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HBITMAP_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HBITMAP_UserFree64(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> Void: ...
@winfunctype('OLE32.dll')
def HDC_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Graphics.Gdi.HDC)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HDC_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HDC)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HDC_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HDC)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HDC_UserFree64(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Graphics.Gdi.HDC)) -> Void: ...
@winfunctype('OLE32.dll')
def HICON_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HICON_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HICON_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HICON_UserFree64(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON)) -> Void: ...
@winfunctype('ole32.dll')
def SNB_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(POINTER(POINTER(UInt16)))) -> UInt32: ...
@winfunctype('ole32.dll')
def SNB_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(POINTER(POINTER(UInt16)))) -> POINTER(Byte): ...
@winfunctype('ole32.dll')
def SNB_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(POINTER(POINTER(UInt16)))) -> POINTER(Byte): ...
@winfunctype('ole32.dll')
def SNB_UserFree64(param0: POINTER(UInt32), param1: POINTER(POINTER(POINTER(UInt16)))) -> Void: ...
@winfunctype('OLE32.dll')
def STGMEDIUM_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.System.Com.STGMEDIUM_head)) -> UInt32: ...
@winfunctype('OLE32.dll')
def STGMEDIUM_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.System.Com.STGMEDIUM_head)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def STGMEDIUM_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.System.Com.STGMEDIUM_head)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def STGMEDIUM_UserFree64(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.System.Com.STGMEDIUM_head)) -> Void: ...
@winfunctype('OLE32.dll')
def CoGetMarshalSizeMax(pulSize: POINTER(UInt32), riid: POINTER(Guid), pUnk: Windows.Win32.System.Com.IUnknown_head, dwDestContext: UInt32, pvDestContext: c_void_p, mshlflags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoMarshalInterface(pStm: Windows.Win32.System.Com.IStream_head, riid: POINTER(Guid), pUnk: Windows.Win32.System.Com.IUnknown_head, dwDestContext: UInt32, pvDestContext: c_void_p, mshlflags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoUnmarshalInterface(pStm: Windows.Win32.System.Com.IStream_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoMarshalHresult(pstm: Windows.Win32.System.Com.IStream_head, hresult: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoUnmarshalHresult(pstm: Windows.Win32.System.Com.IStream_head, phresult: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoReleaseMarshalData(pStm: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetStandardMarshal(riid: POINTER(Guid), pUnk: Windows.Win32.System.Com.IUnknown_head, dwDestContext: UInt32, pvDestContext: c_void_p, mshlflags: UInt32, ppMarshal: POINTER(Windows.Win32.System.Com.Marshal.IMarshal_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetStdMarshalEx(pUnkOuter: Windows.Win32.System.Com.IUnknown_head, smexflags: UInt32, ppUnkInner: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoMarshalInterThreadInterfaceInStream(riid: POINTER(Guid), pUnk: Windows.Win32.System.Com.IUnknown_head, ppStm: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def LPSAFEARRAY_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def LPSAFEARRAY_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def LPSAFEARRAY_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def LPSAFEARRAY_UserFree(param0: POINTER(UInt32), param1: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Void: ...
@winfunctype('OLEAUT32.dll')
def LPSAFEARRAY_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def LPSAFEARRAY_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def LPSAFEARRAY_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def LPSAFEARRAY_UserFree64(param0: POINTER(UInt32), param1: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Void: ...
@winfunctype('OLE32.dll')
def HACCEL_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HACCEL)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HACCEL_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HACCEL)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HACCEL_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HACCEL)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HACCEL_UserFree(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.UI.WindowsAndMessaging.HACCEL)) -> Void: ...
@winfunctype('OLE32.dll')
def HGLOBAL_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Foundation.HGLOBAL)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HGLOBAL_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Foundation.HGLOBAL)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HGLOBAL_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Foundation.HGLOBAL)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HGLOBAL_UserFree(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Foundation.HGLOBAL)) -> Void: ...
@winfunctype('OLE32.dll')
def HMENU_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HMENU_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HMENU_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HMENU_UserFree(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> Void: ...
@winfunctype('OLE32.dll')
def HACCEL_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HACCEL)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HACCEL_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HACCEL)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HACCEL_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HACCEL)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HACCEL_UserFree64(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.UI.WindowsAndMessaging.HACCEL)) -> Void: ...
@winfunctype('OLE32.dll')
def HGLOBAL_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Foundation.HGLOBAL)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HGLOBAL_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Foundation.HGLOBAL)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HGLOBAL_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Foundation.HGLOBAL)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HGLOBAL_UserFree64(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Foundation.HGLOBAL)) -> Void: ...
@winfunctype('OLE32.dll')
def HMENU_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HMENU_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HMENU_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HMENU_UserFree64(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> Void: ...
@winfunctype('OLE32.dll')
def HPALETTE_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Graphics.Gdi.HPALETTE)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HPALETTE_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HPALETTE)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HPALETTE_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HPALETTE)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HPALETTE_UserFree(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Graphics.Gdi.HPALETTE)) -> Void: ...
@winfunctype('OLE32.dll')
def HPALETTE_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Graphics.Gdi.HPALETTE)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HPALETTE_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HPALETTE)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HPALETTE_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HPALETTE)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HPALETTE_UserFree64(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Graphics.Gdi.HPALETTE)) -> Void: ...
class IMarshal(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000003-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetUnmarshalClass(self, riid: POINTER(Guid), pv: c_void_p, dwDestContext: UInt32, pvDestContext: c_void_p, mshlflags: UInt32, pCid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMarshalSizeMax(self, riid: POINTER(Guid), pv: c_void_p, dwDestContext: UInt32, pvDestContext: c_void_p, mshlflags: UInt32, pSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MarshalInterface(self, pStm: Windows.Win32.System.Com.IStream_head, riid: POINTER(Guid), pv: c_void_p, dwDestContext: UInt32, pvDestContext: c_void_p, mshlflags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UnmarshalInterface(self, pStm: Windows.Win32.System.Com.IStream_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ReleaseMarshalData(self, pStm: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DisconnectObject(self, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMarshal2(ComPtr):
    extends: Windows.Win32.System.Com.Marshal.IMarshal
    _iid_ = Guid('{000001cf-0000-0000-c000-000000000046}')
class IMarshalingStream(ComPtr):
    extends: Windows.Win32.System.Com.IStream
    _iid_ = Guid('{d8f2f5e6-6102-4863-9f26-389a4676efde}')
    @commethod(14)
    def GetMarshalingContextAttribute(self, attribute: Windows.Win32.System.Com.CO_MARSHALING_CONTEXT_ATTRIBUTES, pAttributeValue: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
STDMSHLFLAGS = Int32
SMEXF_SERVER: STDMSHLFLAGS = 1
SMEXF_HANDLER: STDMSHLFLAGS = 2
make_head(_module, 'IMarshal')
make_head(_module, 'IMarshal2')
make_head(_module, 'IMarshalingStream')
