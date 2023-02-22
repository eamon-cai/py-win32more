from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.UI.Input.KeyboardAndMouse
import Windows.Win32.UI.TextServices
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
ACTIVATE_KEYBOARD_LAYOUT_FLAGS = UInt32
KLF_REORDER: ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 8
KLF_RESET: ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 1073741824
KLF_SETFORPROCESS: ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 256
KLF_SHIFTLOCK: ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 65536
KLF_ACTIVATE: ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 1
KLF_NOTELLSHELL: ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 128
KLF_REPLACELANG: ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 16
KLF_SUBSTITUTE_OK: ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 2
EXTENDED_BIT: UInt32 = 16777216
DONTCARE_BIT: UInt32 = 33554432
FAKE_KEYSTROKE: UInt32 = 33554432
KBDBASE: UInt32 = 0
KBDSHIFT: UInt32 = 1
KBDCTRL: UInt32 = 2
KBDALT: UInt32 = 4
KBDKANA: UInt32 = 8
KBDROYA: UInt32 = 16
KBDLOYA: UInt32 = 32
KBDGRPSELTAP: UInt32 = 128
GRAVE: UInt32 = 768
ACUTE: UInt32 = 769
CIRCUMFLEX: UInt32 = 770
TILDE: UInt32 = 771
MACRON: UInt32 = 772
OVERSCORE: UInt32 = 773
BREVE: UInt32 = 774
DOT_ABOVE: UInt32 = 775
UMLAUT: UInt32 = 776
DIARESIS: UInt32 = 776
HOOK_ABOVE: UInt32 = 777
RING: UInt32 = 778
DOUBLE_ACUTE: UInt32 = 779
HACEK: UInt32 = 780
CEDILLA: UInt32 = 807
OGONEK: UInt32 = 808
TONOS: UInt32 = 900
DIARESIS_TONOS: UInt32 = 901
wszGRAVE: String = '\u0300'
wszACUTE: String = '\u0301'
wszCIRCUMFLEX: String = '\u0302'
wszTILDE: String = '\u0303'
wszMACRON: String = '\u0304'
wszOVERSCORE: String = '\u0305'
wszBREVE: String = '\u0306'
wszDOT_ABOVE: String = '\u0307'
wszUMLAUT: String = '\u0308'
wszHOOK_ABOVE: String = '\u0309'
wszRING: String = '\u030a'
wszDOUBLE_ACUTE: String = '\u030b'
wszHACEK: String = '\u030c'
wszCEDILLA: String = '\u0327'
wszOGONEK: String = '\u0328'
wszTONOS: String = '\u0384'
wszDIARESIS_TONOS: String = '\u0385'
SHFT_INVALID: UInt32 = 15
WCH_NONE: UInt32 = 61440
WCH_DEAD: UInt32 = 61441
WCH_LGTR: UInt32 = 61442
CAPLOK: UInt32 = 1
SGCAPS: UInt32 = 2
CAPLOKALTGR: UInt32 = 4
KANALOK: UInt32 = 8
GRPSELTAP: UInt32 = 128
DKF_DEAD: UInt32 = 1
KBD_VERSION: UInt32 = 1
KLLF_ALTGR: UInt32 = 1
KLLF_SHIFTLOCK: UInt32 = 2
KLLF_LRM_RLM: UInt32 = 4
KLLF_GLOBAL_ATTRS: UInt32 = 2
KBDTABLE_MULTI_MAX: UInt32 = 8
KEYBOARD_TYPE_GENERIC_101: UInt32 = 4
KEYBOARD_TYPE_JAPAN: UInt32 = 7
KEYBOARD_TYPE_KOREA: UInt32 = 8
KEYBOARD_TYPE_UNKNOWN: UInt32 = 81
NLSKBD_OEM_MICROSOFT: UInt32 = 0
NLSKBD_OEM_AX: UInt32 = 1
NLSKBD_OEM_EPSON: UInt32 = 4
NLSKBD_OEM_FUJITSU: UInt32 = 5
NLSKBD_OEM_IBM: UInt32 = 7
NLSKBD_OEM_MATSUSHITA: UInt32 = 10
NLSKBD_OEM_NEC: UInt32 = 13
NLSKBD_OEM_TOSHIBA: UInt32 = 18
NLSKBD_OEM_DEC: UInt32 = 24
MICROSOFT_KBD_101_TYPE: UInt32 = 0
MICROSOFT_KBD_AX_TYPE: UInt32 = 1
MICROSOFT_KBD_106_TYPE: UInt32 = 2
MICROSOFT_KBD_002_TYPE: UInt32 = 3
MICROSOFT_KBD_001_TYPE: UInt32 = 4
MICROSOFT_KBD_FUNC: UInt32 = 12
AX_KBD_DESKTOP_TYPE: UInt32 = 1
FMR_KBD_JIS_TYPE: UInt32 = 0
FMR_KBD_OASYS_TYPE: UInt32 = 1
FMV_KBD_OASYS_TYPE: UInt32 = 2
NEC_KBD_NORMAL_TYPE: UInt32 = 1
NEC_KBD_N_MODE_TYPE: UInt32 = 2
NEC_KBD_H_MODE_TYPE: UInt32 = 3
NEC_KBD_LAPTOP_TYPE: UInt32 = 4
NEC_KBD_106_TYPE: UInt32 = 5
TOSHIBA_KBD_DESKTOP_TYPE: UInt32 = 13
TOSHIBA_KBD_LAPTOP_TYPE: UInt32 = 15
DEC_KBD_ANSI_LAYOUT_TYPE: UInt32 = 1
DEC_KBD_JIS_LAYOUT_TYPE: UInt32 = 2
MICROSOFT_KBD_101A_TYPE: UInt32 = 0
MICROSOFT_KBD_101B_TYPE: UInt32 = 4
MICROSOFT_KBD_101C_TYPE: UInt32 = 5
MICROSOFT_KBD_103_TYPE: UInt32 = 6
NLSKBD_INFO_SEND_IME_NOTIFICATION: UInt32 = 1
NLSKBD_INFO_ACCESSIBILITY_KEYMAP: UInt32 = 2
NLSKBD_INFO_EMURATE_101_KEYBOARD: UInt32 = 16
NLSKBD_INFO_EMURATE_106_KEYBOARD: UInt32 = 32
KBDNLS_TYPE_NULL: UInt32 = 0
KBDNLS_TYPE_NORMAL: UInt32 = 1
KBDNLS_TYPE_TOGGLE: UInt32 = 2
KBDNLS_INDEX_NORMAL: UInt32 = 1
KBDNLS_INDEX_ALT: UInt32 = 2
KBDNLS_NULL: UInt32 = 0
KBDNLS_NOEVENT: UInt32 = 1
KBDNLS_SEND_BASE_VK: UInt32 = 2
KBDNLS_SEND_PARAM_VK: UInt32 = 3
KBDNLS_KANALOCK: UInt32 = 4
KBDNLS_ALPHANUM: UInt32 = 5
KBDNLS_HIRAGANA: UInt32 = 6
KBDNLS_KATAKANA: UInt32 = 7
KBDNLS_SBCSDBCS: UInt32 = 8
KBDNLS_ROMAN: UInt32 = 9
KBDNLS_CODEINPUT: UInt32 = 10
KBDNLS_HELP_OR_END: UInt32 = 11
KBDNLS_HOME_OR_CLEAR: UInt32 = 12
KBDNLS_NUMPAD: UInt32 = 13
KBDNLS_KANAEVENT: UInt32 = 14
KBDNLS_CONV_OR_NONCONV: UInt32 = 15
KBD_TYPE: UInt32 = 4
SCANCODE_LSHIFT: UInt32 = 42
SCANCODE_RSHIFT: UInt32 = 54
SCANCODE_CTRL: UInt32 = 29
SCANCODE_ALT: UInt32 = 56
SCANCODE_NUMPAD_FIRST: UInt32 = 71
SCANCODE_NUMPAD_LAST: UInt32 = 82
SCANCODE_LWIN: UInt32 = 91
SCANCODE_RWIN: UInt32 = 92
SCANCODE_THAI_LAYOUT_TOGGLE: UInt32 = 41
@winfunctype('COMCTL32.dll')
def _TrackMouseEvent(lpEventTrack: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.TRACKMOUSEEVENT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def LoadKeyboardLayoutA(pwszKLID: Windows.Win32.Foundation.PSTR, Flags: Windows.Win32.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS) -> Windows.Win32.UI.TextServices.HKL: ...
@winfunctype('USER32.dll')
def LoadKeyboardLayoutW(pwszKLID: Windows.Win32.Foundation.PWSTR, Flags: Windows.Win32.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS) -> Windows.Win32.UI.TextServices.HKL: ...
@winfunctype('USER32.dll')
def ActivateKeyboardLayout(hkl: Windows.Win32.UI.TextServices.HKL, Flags: Windows.Win32.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS) -> Windows.Win32.UI.TextServices.HKL: ...
@winfunctype('USER32.dll')
def ToUnicodeEx(wVirtKey: UInt32, wScanCode: UInt32, lpKeyState: c_char_p_no, pwszBuff: Windows.Win32.Foundation.PWSTR, cchBuff: Int32, wFlags: UInt32, dwhkl: Windows.Win32.UI.TextServices.HKL) -> Int32: ...
@winfunctype('USER32.dll')
def UnloadKeyboardLayout(hkl: Windows.Win32.UI.TextServices.HKL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetKeyboardLayoutNameA(pwszKLID: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetKeyboardLayoutNameW(pwszKLID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetKeyboardLayoutList(nBuff: Int32, lpList: POINTER(Windows.Win32.UI.TextServices.HKL)) -> Int32: ...
@winfunctype('USER32.dll')
def GetKeyboardLayout(idThread: UInt32) -> Windows.Win32.UI.TextServices.HKL: ...
@winfunctype('USER32.dll')
def GetMouseMovePointsEx(cbSize: UInt32, lppt: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.MOUSEMOVEPOINT_head), lpptBuf: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.MOUSEMOVEPOINT_head), nBufPoints: Int32, resolution: Windows.Win32.UI.Input.KeyboardAndMouse.GET_MOUSE_MOVE_POINTS_EX_RESOLUTION) -> Int32: ...
@winfunctype('USER32.dll')
def TrackMouseEvent(lpEventTrack: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.TRACKMOUSEEVENT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def RegisterHotKey(hWnd: Windows.Win32.Foundation.HWND, id: Int32, fsModifiers: Windows.Win32.UI.Input.KeyboardAndMouse.HOT_KEY_MODIFIERS, vk: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def UnregisterHotKey(hWnd: Windows.Win32.Foundation.HWND, id: Int32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SwapMouseButton(fSwap: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetDoubleClickTime() -> UInt32: ...
@winfunctype('USER32.dll')
def SetDoubleClickTime(param0: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetFocus(hWnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def GetActiveWindow() -> Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def GetFocus() -> Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def GetKBCodePage() -> UInt32: ...
@winfunctype('USER32.dll')
def GetKeyState(nVirtKey: Int32) -> Int16: ...
@winfunctype('USER32.dll')
def GetAsyncKeyState(vKey: Int32) -> Int16: ...
@winfunctype('USER32.dll')
def GetKeyboardState(lpKeyState: c_char_p_no) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetKeyboardState(lpKeyState: c_char_p_no) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetKeyNameTextA(lParam: Int32, lpString: Windows.Win32.Foundation.PSTR, cchSize: Int32) -> Int32: ...
@winfunctype('USER32.dll')
def GetKeyNameTextW(lParam: Int32, lpString: Windows.Win32.Foundation.PWSTR, cchSize: Int32) -> Int32: ...
@winfunctype('USER32.dll')
def GetKeyboardType(nTypeFlag: Int32) -> Int32: ...
@winfunctype('USER32.dll')
def ToAscii(uVirtKey: UInt32, uScanCode: UInt32, lpKeyState: c_char_p_no, lpChar: POINTER(UInt16), uFlags: UInt32) -> Int32: ...
@winfunctype('USER32.dll')
def ToAsciiEx(uVirtKey: UInt32, uScanCode: UInt32, lpKeyState: c_char_p_no, lpChar: POINTER(UInt16), uFlags: UInt32, dwhkl: Windows.Win32.UI.TextServices.HKL) -> Int32: ...
@winfunctype('USER32.dll')
def ToUnicode(wVirtKey: UInt32, wScanCode: UInt32, lpKeyState: c_char_p_no, pwszBuff: Windows.Win32.Foundation.PWSTR, cchBuff: Int32, wFlags: UInt32) -> Int32: ...
@winfunctype('USER32.dll')
def OemKeyScan(wOemChar: UInt16) -> UInt32: ...
@winfunctype('USER32.dll')
def VkKeyScanA(ch: Windows.Win32.Foundation.CHAR) -> Int16: ...
@winfunctype('USER32.dll')
def VkKeyScanW(ch: Char) -> Int16: ...
@winfunctype('USER32.dll')
def VkKeyScanExA(ch: Windows.Win32.Foundation.CHAR, dwhkl: Windows.Win32.UI.TextServices.HKL) -> Int16: ...
@winfunctype('USER32.dll')
def VkKeyScanExW(ch: Char, dwhkl: Windows.Win32.UI.TextServices.HKL) -> Int16: ...
@winfunctype('USER32.dll')
def keybd_event(bVk: Byte, bScan: Byte, dwFlags: Windows.Win32.UI.Input.KeyboardAndMouse.KEYBD_EVENT_FLAGS, dwExtraInfo: UIntPtr) -> Void: ...
@winfunctype('USER32.dll')
def mouse_event(dwFlags: Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS, dx: Int32, dy: Int32, dwData: Int32, dwExtraInfo: UIntPtr) -> Void: ...
@winfunctype('USER32.dll')
def SendInput(cInputs: UInt32, pInputs: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.INPUT_head), cbSize: Int32) -> UInt32: ...
@winfunctype('USER32.dll')
def GetLastInputInfo(plii: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.LASTINPUTINFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def MapVirtualKeyA(uCode: UInt32, uMapType: Windows.Win32.UI.Input.KeyboardAndMouse.MAP_VIRTUAL_KEY_TYPE) -> UInt32: ...
@winfunctype('USER32.dll')
def MapVirtualKeyW(uCode: UInt32, uMapType: Windows.Win32.UI.Input.KeyboardAndMouse.MAP_VIRTUAL_KEY_TYPE) -> UInt32: ...
@winfunctype('USER32.dll')
def MapVirtualKeyExA(uCode: UInt32, uMapType: Windows.Win32.UI.Input.KeyboardAndMouse.MAP_VIRTUAL_KEY_TYPE, dwhkl: Windows.Win32.UI.TextServices.HKL) -> UInt32: ...
@winfunctype('USER32.dll')
def MapVirtualKeyExW(uCode: UInt32, uMapType: Windows.Win32.UI.Input.KeyboardAndMouse.MAP_VIRTUAL_KEY_TYPE, dwhkl: Windows.Win32.UI.TextServices.HKL) -> UInt32: ...
@winfunctype('USER32.dll')
def GetCapture() -> Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def SetCapture(hWnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def ReleaseCapture() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def EnableWindow(hWnd: Windows.Win32.Foundation.HWND, bEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IsWindowEnabled(hWnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DragDetect(hwnd: Windows.Win32.Foundation.HWND, pt: Windows.Win32.Foundation.POINT) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetActiveWindow(hWnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def BlockInput(fBlockIt: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
class DEADKEY(Structure):
    dwBoth: UInt32
    wchComposed: Char
    uFlags: UInt16
GET_MOUSE_MOVE_POINTS_EX_RESOLUTION = UInt32
GMMP_USE_DISPLAY_POINTS: GET_MOUSE_MOVE_POINTS_EX_RESOLUTION = 1
GMMP_USE_HIGH_RESOLUTION_POINTS: GET_MOUSE_MOVE_POINTS_EX_RESOLUTION = 2
class HARDWAREINPUT(Structure):
    uMsg: UInt32
    wParamL: UInt16
    wParamH: UInt16
HOT_KEY_MODIFIERS = UInt32
MOD_ALT: HOT_KEY_MODIFIERS = 1
MOD_CONTROL: HOT_KEY_MODIFIERS = 2
MOD_NOREPEAT: HOT_KEY_MODIFIERS = 16384
MOD_SHIFT: HOT_KEY_MODIFIERS = 4
MOD_WIN: HOT_KEY_MODIFIERS = 8
class INPUT(Structure):
    type: Windows.Win32.UI.Input.KeyboardAndMouse.INPUT_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        mi: Windows.Win32.UI.Input.KeyboardAndMouse.MOUSEINPUT
        ki: Windows.Win32.UI.Input.KeyboardAndMouse.KEYBDINPUT
        hi: Windows.Win32.UI.Input.KeyboardAndMouse.HARDWAREINPUT
INPUT_TYPE = UInt32
INPUT_MOUSE: INPUT_TYPE = 0
INPUT_KEYBOARD: INPUT_TYPE = 1
INPUT_HARDWARE: INPUT_TYPE = 2
class KBDNLSTABLES(Structure):
    OEMIdentifier: UInt16
    LayoutInformation: UInt16
    NumOfVkToF: UInt32
    pVkToF: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.VK_F_head)
    NumOfMouseVKey: Int32
    pusMouseVKey: POINTER(UInt16)
class KBDTABLES(Structure):
    pCharModifiers: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.MODIFIERS_head)
    pVkToWcharTable: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.VK_TO_WCHAR_TABLE_head)
    pDeadKey: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.DEADKEY_head)
    pKeyNames: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.VSC_LPWSTR_head)
    pKeyNamesExt: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.VSC_LPWSTR_head)
    pKeyNamesDead: POINTER(POINTER(UInt16))
    pusVSCtoVK: POINTER(UInt16)
    bMaxVSCtoVK: Byte
    pVSCtoVK_E0: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.VSC_VK_head)
    pVSCtoVK_E1: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.VSC_VK_head)
    fLocaleFlags: UInt32
    nLgMax: Byte
    cbLgEntry: Byte
    pLigature: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.LIGATURE1_head)
    dwType: UInt32
    dwSubType: UInt32
class KBDTABLE_DESC(Structure):
    wszDllName: Char * 32
    dwType: UInt32
    dwSubType: UInt32
class KBDTABLE_MULTI(Structure):
    nTables: UInt32
    aKbdTables: Windows.Win32.UI.Input.KeyboardAndMouse.KBDTABLE_DESC * 8
class KBD_TYPE_INFO(Structure):
    dwVersion: UInt32
    dwType: UInt32
    dwSubType: UInt32
class KEYBDINPUT(Structure):
    wVk: Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY
    wScan: UInt16
    dwFlags: Windows.Win32.UI.Input.KeyboardAndMouse.KEYBD_EVENT_FLAGS
    time: UInt32
    dwExtraInfo: UIntPtr
KEYBD_EVENT_FLAGS = UInt32
KEYEVENTF_EXTENDEDKEY: KEYBD_EVENT_FLAGS = 1
KEYEVENTF_KEYUP: KEYBD_EVENT_FLAGS = 2
KEYEVENTF_SCANCODE: KEYBD_EVENT_FLAGS = 8
KEYEVENTF_UNICODE: KEYBD_EVENT_FLAGS = 4
class LASTINPUTINFO(Structure):
    cbSize: UInt32
    dwTime: UInt32
class LIGATURE1(Structure):
    VirtualKey: Byte
    ModificationNumber: UInt16
    wch: Char * 1
class LIGATURE2(Structure):
    VirtualKey: Byte
    ModificationNumber: UInt16
    wch: Char * 2
class LIGATURE3(Structure):
    VirtualKey: Byte
    ModificationNumber: UInt16
    wch: Char * 3
class LIGATURE4(Structure):
    VirtualKey: Byte
    ModificationNumber: UInt16
    wch: Char * 4
class LIGATURE5(Structure):
    VirtualKey: Byte
    ModificationNumber: UInt16
    wch: Char * 5
MAP_VIRTUAL_KEY_TYPE = UInt32
MAPVK_VK_TO_VSC: MAP_VIRTUAL_KEY_TYPE = 0
MAPVK_VSC_TO_VK: MAP_VIRTUAL_KEY_TYPE = 1
MAPVK_VK_TO_CHAR: MAP_VIRTUAL_KEY_TYPE = 2
MAPVK_VSC_TO_VK_EX: MAP_VIRTUAL_KEY_TYPE = 3
MAPVK_VK_TO_VSC_EX: MAP_VIRTUAL_KEY_TYPE = 4
class MODIFIERS(Structure):
    pVkToBit: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.VK_TO_BIT_head)
    wMaxModBits: UInt16
    ModNumber: Byte * 1
class MOUSEINPUT(Structure):
    dx: Int32
    dy: Int32
    mouseData: Int32
    dwFlags: Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS
    time: UInt32
    dwExtraInfo: UIntPtr
class MOUSEMOVEPOINT(Structure):
    x: Int32
    y: Int32
    time: UInt32
    dwExtraInfo: UIntPtr
MOUSE_EVENT_FLAGS = UInt32
MOUSEEVENTF_ABSOLUTE: MOUSE_EVENT_FLAGS = 32768
MOUSEEVENTF_LEFTDOWN: MOUSE_EVENT_FLAGS = 2
MOUSEEVENTF_LEFTUP: MOUSE_EVENT_FLAGS = 4
MOUSEEVENTF_MIDDLEDOWN: MOUSE_EVENT_FLAGS = 32
MOUSEEVENTF_MIDDLEUP: MOUSE_EVENT_FLAGS = 64
MOUSEEVENTF_MOVE: MOUSE_EVENT_FLAGS = 1
MOUSEEVENTF_RIGHTDOWN: MOUSE_EVENT_FLAGS = 8
MOUSEEVENTF_RIGHTUP: MOUSE_EVENT_FLAGS = 16
MOUSEEVENTF_WHEEL: MOUSE_EVENT_FLAGS = 2048
MOUSEEVENTF_XDOWN: MOUSE_EVENT_FLAGS = 128
MOUSEEVENTF_XUP: MOUSE_EVENT_FLAGS = 256
MOUSEEVENTF_HWHEEL: MOUSE_EVENT_FLAGS = 4096
MOUSEEVENTF_MOVE_NOCOALESCE: MOUSE_EVENT_FLAGS = 8192
MOUSEEVENTF_VIRTUALDESK: MOUSE_EVENT_FLAGS = 16384
class TRACKMOUSEEVENT(Structure):
    cbSize: UInt32
    dwFlags: Windows.Win32.UI.Input.KeyboardAndMouse.TRACKMOUSEEVENT_FLAGS
    hwndTrack: Windows.Win32.Foundation.HWND
    dwHoverTime: UInt32
TRACKMOUSEEVENT_FLAGS = UInt32
TME_CANCEL: TRACKMOUSEEVENT_FLAGS = 2147483648
TME_HOVER: TRACKMOUSEEVENT_FLAGS = 1
TME_LEAVE: TRACKMOUSEEVENT_FLAGS = 2
TME_NONCLIENT: TRACKMOUSEEVENT_FLAGS = 16
TME_QUERY: TRACKMOUSEEVENT_FLAGS = 1073741824
VIRTUAL_KEY = UInt16
VK_0: VIRTUAL_KEY = 48
VK_1: VIRTUAL_KEY = 49
VK_2: VIRTUAL_KEY = 50
VK_3: VIRTUAL_KEY = 51
VK_4: VIRTUAL_KEY = 52
VK_5: VIRTUAL_KEY = 53
VK_6: VIRTUAL_KEY = 54
VK_7: VIRTUAL_KEY = 55
VK_8: VIRTUAL_KEY = 56
VK_9: VIRTUAL_KEY = 57
VK_A: VIRTUAL_KEY = 65
VK_B: VIRTUAL_KEY = 66
VK_C: VIRTUAL_KEY = 67
VK_D: VIRTUAL_KEY = 68
VK_E: VIRTUAL_KEY = 69
VK_F: VIRTUAL_KEY = 70
VK_G: VIRTUAL_KEY = 71
VK_H: VIRTUAL_KEY = 72
VK_I: VIRTUAL_KEY = 73
VK_J: VIRTUAL_KEY = 74
VK_K: VIRTUAL_KEY = 75
VK_L: VIRTUAL_KEY = 76
VK_M: VIRTUAL_KEY = 77
VK_N: VIRTUAL_KEY = 78
VK_O: VIRTUAL_KEY = 79
VK_P: VIRTUAL_KEY = 80
VK_Q: VIRTUAL_KEY = 81
VK_R: VIRTUAL_KEY = 82
VK_S: VIRTUAL_KEY = 83
VK_T: VIRTUAL_KEY = 84
VK_U: VIRTUAL_KEY = 85
VK_V: VIRTUAL_KEY = 86
VK_W: VIRTUAL_KEY = 87
VK_X: VIRTUAL_KEY = 88
VK_Y: VIRTUAL_KEY = 89
VK_Z: VIRTUAL_KEY = 90
VK_ABNT_C1: VIRTUAL_KEY = 193
VK_ABNT_C2: VIRTUAL_KEY = 194
VK_DBE_ALPHANUMERIC: VIRTUAL_KEY = 240
VK_DBE_CODEINPUT: VIRTUAL_KEY = 250
VK_DBE_DBCSCHAR: VIRTUAL_KEY = 244
VK_DBE_DETERMINESTRING: VIRTUAL_KEY = 252
VK_DBE_ENTERDLGCONVERSIONMODE: VIRTUAL_KEY = 253
VK_DBE_ENTERIMECONFIGMODE: VIRTUAL_KEY = 248
VK_DBE_ENTERWORDREGISTERMODE: VIRTUAL_KEY = 247
VK_DBE_FLUSHSTRING: VIRTUAL_KEY = 249
VK_DBE_HIRAGANA: VIRTUAL_KEY = 242
VK_DBE_KATAKANA: VIRTUAL_KEY = 241
VK_DBE_NOCODEINPUT: VIRTUAL_KEY = 251
VK_DBE_NOROMAN: VIRTUAL_KEY = 246
VK_DBE_ROMAN: VIRTUAL_KEY = 245
VK_DBE_SBCSCHAR: VIRTUAL_KEY = 243
VK__none_: VIRTUAL_KEY = 255
VK_LBUTTON: VIRTUAL_KEY = 1
VK_RBUTTON: VIRTUAL_KEY = 2
VK_CANCEL: VIRTUAL_KEY = 3
VK_MBUTTON: VIRTUAL_KEY = 4
VK_XBUTTON1: VIRTUAL_KEY = 5
VK_XBUTTON2: VIRTUAL_KEY = 6
VK_BACK: VIRTUAL_KEY = 8
VK_TAB: VIRTUAL_KEY = 9
VK_CLEAR: VIRTUAL_KEY = 12
VK_RETURN: VIRTUAL_KEY = 13
VK_SHIFT: VIRTUAL_KEY = 16
VK_CONTROL: VIRTUAL_KEY = 17
VK_MENU: VIRTUAL_KEY = 18
VK_PAUSE: VIRTUAL_KEY = 19
VK_CAPITAL: VIRTUAL_KEY = 20
VK_KANA: VIRTUAL_KEY = 21
VK_HANGEUL: VIRTUAL_KEY = 21
VK_HANGUL: VIRTUAL_KEY = 21
VK_IME_ON: VIRTUAL_KEY = 22
VK_JUNJA: VIRTUAL_KEY = 23
VK_FINAL: VIRTUAL_KEY = 24
VK_HANJA: VIRTUAL_KEY = 25
VK_KANJI: VIRTUAL_KEY = 25
VK_IME_OFF: VIRTUAL_KEY = 26
VK_ESCAPE: VIRTUAL_KEY = 27
VK_CONVERT: VIRTUAL_KEY = 28
VK_NONCONVERT: VIRTUAL_KEY = 29
VK_ACCEPT: VIRTUAL_KEY = 30
VK_MODECHANGE: VIRTUAL_KEY = 31
VK_SPACE: VIRTUAL_KEY = 32
VK_PRIOR: VIRTUAL_KEY = 33
VK_NEXT: VIRTUAL_KEY = 34
VK_END: VIRTUAL_KEY = 35
VK_HOME: VIRTUAL_KEY = 36
VK_LEFT: VIRTUAL_KEY = 37
VK_UP: VIRTUAL_KEY = 38
VK_RIGHT: VIRTUAL_KEY = 39
VK_DOWN: VIRTUAL_KEY = 40
VK_SELECT: VIRTUAL_KEY = 41
VK_PRINT: VIRTUAL_KEY = 42
VK_EXECUTE: VIRTUAL_KEY = 43
VK_SNAPSHOT: VIRTUAL_KEY = 44
VK_INSERT: VIRTUAL_KEY = 45
VK_DELETE: VIRTUAL_KEY = 46
VK_HELP: VIRTUAL_KEY = 47
VK_LWIN: VIRTUAL_KEY = 91
VK_RWIN: VIRTUAL_KEY = 92
VK_APPS: VIRTUAL_KEY = 93
VK_SLEEP: VIRTUAL_KEY = 95
VK_NUMPAD0: VIRTUAL_KEY = 96
VK_NUMPAD1: VIRTUAL_KEY = 97
VK_NUMPAD2: VIRTUAL_KEY = 98
VK_NUMPAD3: VIRTUAL_KEY = 99
VK_NUMPAD4: VIRTUAL_KEY = 100
VK_NUMPAD5: VIRTUAL_KEY = 101
VK_NUMPAD6: VIRTUAL_KEY = 102
VK_NUMPAD7: VIRTUAL_KEY = 103
VK_NUMPAD8: VIRTUAL_KEY = 104
VK_NUMPAD9: VIRTUAL_KEY = 105
VK_MULTIPLY: VIRTUAL_KEY = 106
VK_ADD: VIRTUAL_KEY = 107
VK_SEPARATOR: VIRTUAL_KEY = 108
VK_SUBTRACT: VIRTUAL_KEY = 109
VK_DECIMAL: VIRTUAL_KEY = 110
VK_DIVIDE: VIRTUAL_KEY = 111
VK_F1: VIRTUAL_KEY = 112
VK_F2: VIRTUAL_KEY = 113
VK_F3: VIRTUAL_KEY = 114
VK_F4: VIRTUAL_KEY = 115
VK_F5: VIRTUAL_KEY = 116
VK_F6: VIRTUAL_KEY = 117
VK_F7: VIRTUAL_KEY = 118
VK_F8: VIRTUAL_KEY = 119
VK_F9: VIRTUAL_KEY = 120
VK_F10: VIRTUAL_KEY = 121
VK_F11: VIRTUAL_KEY = 122
VK_F12: VIRTUAL_KEY = 123
VK_F13: VIRTUAL_KEY = 124
VK_F14: VIRTUAL_KEY = 125
VK_F15: VIRTUAL_KEY = 126
VK_F16: VIRTUAL_KEY = 127
VK_F17: VIRTUAL_KEY = 128
VK_F18: VIRTUAL_KEY = 129
VK_F19: VIRTUAL_KEY = 130
VK_F20: VIRTUAL_KEY = 131
VK_F21: VIRTUAL_KEY = 132
VK_F22: VIRTUAL_KEY = 133
VK_F23: VIRTUAL_KEY = 134
VK_F24: VIRTUAL_KEY = 135
VK_NAVIGATION_VIEW: VIRTUAL_KEY = 136
VK_NAVIGATION_MENU: VIRTUAL_KEY = 137
VK_NAVIGATION_UP: VIRTUAL_KEY = 138
VK_NAVIGATION_DOWN: VIRTUAL_KEY = 139
VK_NAVIGATION_LEFT: VIRTUAL_KEY = 140
VK_NAVIGATION_RIGHT: VIRTUAL_KEY = 141
VK_NAVIGATION_ACCEPT: VIRTUAL_KEY = 142
VK_NAVIGATION_CANCEL: VIRTUAL_KEY = 143
VK_NUMLOCK: VIRTUAL_KEY = 144
VK_SCROLL: VIRTUAL_KEY = 145
VK_OEM_NEC_EQUAL: VIRTUAL_KEY = 146
VK_OEM_FJ_JISHO: VIRTUAL_KEY = 146
VK_OEM_FJ_MASSHOU: VIRTUAL_KEY = 147
VK_OEM_FJ_TOUROKU: VIRTUAL_KEY = 148
VK_OEM_FJ_LOYA: VIRTUAL_KEY = 149
VK_OEM_FJ_ROYA: VIRTUAL_KEY = 150
VK_LSHIFT: VIRTUAL_KEY = 160
VK_RSHIFT: VIRTUAL_KEY = 161
VK_LCONTROL: VIRTUAL_KEY = 162
VK_RCONTROL: VIRTUAL_KEY = 163
VK_LMENU: VIRTUAL_KEY = 164
VK_RMENU: VIRTUAL_KEY = 165
VK_BROWSER_BACK: VIRTUAL_KEY = 166
VK_BROWSER_FORWARD: VIRTUAL_KEY = 167
VK_BROWSER_REFRESH: VIRTUAL_KEY = 168
VK_BROWSER_STOP: VIRTUAL_KEY = 169
VK_BROWSER_SEARCH: VIRTUAL_KEY = 170
VK_BROWSER_FAVORITES: VIRTUAL_KEY = 171
VK_BROWSER_HOME: VIRTUAL_KEY = 172
VK_VOLUME_MUTE: VIRTUAL_KEY = 173
VK_VOLUME_DOWN: VIRTUAL_KEY = 174
VK_VOLUME_UP: VIRTUAL_KEY = 175
VK_MEDIA_NEXT_TRACK: VIRTUAL_KEY = 176
VK_MEDIA_PREV_TRACK: VIRTUAL_KEY = 177
VK_MEDIA_STOP: VIRTUAL_KEY = 178
VK_MEDIA_PLAY_PAUSE: VIRTUAL_KEY = 179
VK_LAUNCH_MAIL: VIRTUAL_KEY = 180
VK_LAUNCH_MEDIA_SELECT: VIRTUAL_KEY = 181
VK_LAUNCH_APP1: VIRTUAL_KEY = 182
VK_LAUNCH_APP2: VIRTUAL_KEY = 183
VK_OEM_1: VIRTUAL_KEY = 186
VK_OEM_PLUS: VIRTUAL_KEY = 187
VK_OEM_COMMA: VIRTUAL_KEY = 188
VK_OEM_MINUS: VIRTUAL_KEY = 189
VK_OEM_PERIOD: VIRTUAL_KEY = 190
VK_OEM_2: VIRTUAL_KEY = 191
VK_OEM_3: VIRTUAL_KEY = 192
VK_GAMEPAD_A: VIRTUAL_KEY = 195
VK_GAMEPAD_B: VIRTUAL_KEY = 196
VK_GAMEPAD_X: VIRTUAL_KEY = 197
VK_GAMEPAD_Y: VIRTUAL_KEY = 198
VK_GAMEPAD_RIGHT_SHOULDER: VIRTUAL_KEY = 199
VK_GAMEPAD_LEFT_SHOULDER: VIRTUAL_KEY = 200
VK_GAMEPAD_LEFT_TRIGGER: VIRTUAL_KEY = 201
VK_GAMEPAD_RIGHT_TRIGGER: VIRTUAL_KEY = 202
VK_GAMEPAD_DPAD_UP: VIRTUAL_KEY = 203
VK_GAMEPAD_DPAD_DOWN: VIRTUAL_KEY = 204
VK_GAMEPAD_DPAD_LEFT: VIRTUAL_KEY = 205
VK_GAMEPAD_DPAD_RIGHT: VIRTUAL_KEY = 206
VK_GAMEPAD_MENU: VIRTUAL_KEY = 207
VK_GAMEPAD_VIEW: VIRTUAL_KEY = 208
VK_GAMEPAD_LEFT_THUMBSTICK_BUTTON: VIRTUAL_KEY = 209
VK_GAMEPAD_RIGHT_THUMBSTICK_BUTTON: VIRTUAL_KEY = 210
VK_GAMEPAD_LEFT_THUMBSTICK_UP: VIRTUAL_KEY = 211
VK_GAMEPAD_LEFT_THUMBSTICK_DOWN: VIRTUAL_KEY = 212
VK_GAMEPAD_LEFT_THUMBSTICK_RIGHT: VIRTUAL_KEY = 213
VK_GAMEPAD_LEFT_THUMBSTICK_LEFT: VIRTUAL_KEY = 214
VK_GAMEPAD_RIGHT_THUMBSTICK_UP: VIRTUAL_KEY = 215
VK_GAMEPAD_RIGHT_THUMBSTICK_DOWN: VIRTUAL_KEY = 216
VK_GAMEPAD_RIGHT_THUMBSTICK_RIGHT: VIRTUAL_KEY = 217
VK_GAMEPAD_RIGHT_THUMBSTICK_LEFT: VIRTUAL_KEY = 218
VK_OEM_4: VIRTUAL_KEY = 219
VK_OEM_5: VIRTUAL_KEY = 220
VK_OEM_6: VIRTUAL_KEY = 221
VK_OEM_7: VIRTUAL_KEY = 222
VK_OEM_8: VIRTUAL_KEY = 223
VK_OEM_AX: VIRTUAL_KEY = 225
VK_OEM_102: VIRTUAL_KEY = 226
VK_ICO_HELP: VIRTUAL_KEY = 227
VK_ICO_00: VIRTUAL_KEY = 228
VK_PROCESSKEY: VIRTUAL_KEY = 229
VK_ICO_CLEAR: VIRTUAL_KEY = 230
VK_PACKET: VIRTUAL_KEY = 231
VK_OEM_RESET: VIRTUAL_KEY = 233
VK_OEM_JUMP: VIRTUAL_KEY = 234
VK_OEM_PA1: VIRTUAL_KEY = 235
VK_OEM_PA2: VIRTUAL_KEY = 236
VK_OEM_PA3: VIRTUAL_KEY = 237
VK_OEM_WSCTRL: VIRTUAL_KEY = 238
VK_OEM_CUSEL: VIRTUAL_KEY = 239
VK_OEM_ATTN: VIRTUAL_KEY = 240
VK_OEM_FINISH: VIRTUAL_KEY = 241
VK_OEM_COPY: VIRTUAL_KEY = 242
VK_OEM_AUTO: VIRTUAL_KEY = 243
VK_OEM_ENLW: VIRTUAL_KEY = 244
VK_OEM_BACKTAB: VIRTUAL_KEY = 245
VK_ATTN: VIRTUAL_KEY = 246
VK_CRSEL: VIRTUAL_KEY = 247
VK_EXSEL: VIRTUAL_KEY = 248
VK_EREOF: VIRTUAL_KEY = 249
VK_PLAY: VIRTUAL_KEY = 250
VK_ZOOM: VIRTUAL_KEY = 251
VK_NONAME: VIRTUAL_KEY = 252
VK_PA1: VIRTUAL_KEY = 253
VK_OEM_CLEAR: VIRTUAL_KEY = 254
class VK_F(Structure):
    Vk: Byte
    NLSFEProcType: Byte
    NLSFEProcCurrent: Byte
    NLSFEProcSwitch: Byte
    NLSFEProc: Windows.Win32.UI.Input.KeyboardAndMouse.VK_FPARAM * 8
    NLSFEProcAlt: Windows.Win32.UI.Input.KeyboardAndMouse.VK_FPARAM * 8
class VK_FPARAM(Structure):
    NLSFEProcIndex: Byte
    NLSFEProcParam: UInt32
class VK_TO_BIT(Structure):
    Vk: Byte
    ModBits: Byte
class VK_TO_WCHARS1(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 1
class VK_TO_WCHARS10(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 10
class VK_TO_WCHARS2(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 2
class VK_TO_WCHARS3(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 3
class VK_TO_WCHARS4(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 4
class VK_TO_WCHARS5(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 5
class VK_TO_WCHARS6(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 6
class VK_TO_WCHARS7(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 7
class VK_TO_WCHARS8(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 8
class VK_TO_WCHARS9(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 9
class VK_TO_WCHAR_TABLE(Structure):
    pVkToWchars: POINTER(Windows.Win32.UI.Input.KeyboardAndMouse.VK_TO_WCHARS1_head)
    nModifications: Byte
    cbSize: Byte
class VK_VSC(Structure):
    Vk: Byte
    Vsc: Byte
class VSC_LPWSTR(Structure):
    vsc: Byte
    pwsz: Windows.Win32.Foundation.PWSTR
class VSC_VK(Structure):
    Vsc: Byte
    Vk: UInt16
make_head(_module, 'DEADKEY')
make_head(_module, 'HARDWAREINPUT')
make_head(_module, 'INPUT')
make_head(_module, 'KBDNLSTABLES')
make_head(_module, 'KBDTABLES')
make_head(_module, 'KBDTABLE_DESC')
make_head(_module, 'KBDTABLE_MULTI')
make_head(_module, 'KBD_TYPE_INFO')
make_head(_module, 'KEYBDINPUT')
make_head(_module, 'LASTINPUTINFO')
make_head(_module, 'LIGATURE1')
make_head(_module, 'LIGATURE2')
make_head(_module, 'LIGATURE3')
make_head(_module, 'LIGATURE4')
make_head(_module, 'LIGATURE5')
make_head(_module, 'MODIFIERS')
make_head(_module, 'MOUSEINPUT')
make_head(_module, 'MOUSEMOVEPOINT')
make_head(_module, 'TRACKMOUSEEVENT')
make_head(_module, 'VK_F')
make_head(_module, 'VK_FPARAM')
make_head(_module, 'VK_TO_BIT')
make_head(_module, 'VK_TO_WCHARS1')
make_head(_module, 'VK_TO_WCHARS10')
make_head(_module, 'VK_TO_WCHARS2')
make_head(_module, 'VK_TO_WCHARS3')
make_head(_module, 'VK_TO_WCHARS4')
make_head(_module, 'VK_TO_WCHARS5')
make_head(_module, 'VK_TO_WCHARS6')
make_head(_module, 'VK_TO_WCHARS7')
make_head(_module, 'VK_TO_WCHARS8')
make_head(_module, 'VK_TO_WCHARS9')
make_head(_module, 'VK_TO_WCHAR_TABLE')
make_head(_module, 'VK_VSC')
make_head(_module, 'VSC_LPWSTR')
make_head(_module, 'VSC_VK')
__all__ = [
    "ACTIVATE_KEYBOARD_LAYOUT_FLAGS",
    "ACUTE",
    "AX_KBD_DESKTOP_TYPE",
    "ActivateKeyboardLayout",
    "BREVE",
    "BlockInput",
    "CAPLOK",
    "CAPLOKALTGR",
    "CEDILLA",
    "CIRCUMFLEX",
    "DEADKEY",
    "DEC_KBD_ANSI_LAYOUT_TYPE",
    "DEC_KBD_JIS_LAYOUT_TYPE",
    "DIARESIS",
    "DIARESIS_TONOS",
    "DKF_DEAD",
    "DONTCARE_BIT",
    "DOT_ABOVE",
    "DOUBLE_ACUTE",
    "DragDetect",
    "EXTENDED_BIT",
    "EnableWindow",
    "FAKE_KEYSTROKE",
    "FMR_KBD_JIS_TYPE",
    "FMR_KBD_OASYS_TYPE",
    "FMV_KBD_OASYS_TYPE",
    "GET_MOUSE_MOVE_POINTS_EX_RESOLUTION",
    "GMMP_USE_DISPLAY_POINTS",
    "GMMP_USE_HIGH_RESOLUTION_POINTS",
    "GRAVE",
    "GRPSELTAP",
    "GetActiveWindow",
    "GetAsyncKeyState",
    "GetCapture",
    "GetDoubleClickTime",
    "GetFocus",
    "GetKBCodePage",
    "GetKeyNameTextA",
    "GetKeyNameTextW",
    "GetKeyState",
    "GetKeyboardLayout",
    "GetKeyboardLayoutList",
    "GetKeyboardLayoutNameA",
    "GetKeyboardLayoutNameW",
    "GetKeyboardState",
    "GetKeyboardType",
    "GetLastInputInfo",
    "GetMouseMovePointsEx",
    "HACEK",
    "HARDWAREINPUT",
    "HOOK_ABOVE",
    "HOT_KEY_MODIFIERS",
    "INPUT",
    "INPUT_HARDWARE",
    "INPUT_KEYBOARD",
    "INPUT_MOUSE",
    "INPUT_TYPE",
    "IsWindowEnabled",
    "KANALOK",
    "KBDALT",
    "KBDBASE",
    "KBDCTRL",
    "KBDGRPSELTAP",
    "KBDKANA",
    "KBDLOYA",
    "KBDNLSTABLES",
    "KBDNLS_ALPHANUM",
    "KBDNLS_CODEINPUT",
    "KBDNLS_CONV_OR_NONCONV",
    "KBDNLS_HELP_OR_END",
    "KBDNLS_HIRAGANA",
    "KBDNLS_HOME_OR_CLEAR",
    "KBDNLS_INDEX_ALT",
    "KBDNLS_INDEX_NORMAL",
    "KBDNLS_KANAEVENT",
    "KBDNLS_KANALOCK",
    "KBDNLS_KATAKANA",
    "KBDNLS_NOEVENT",
    "KBDNLS_NULL",
    "KBDNLS_NUMPAD",
    "KBDNLS_ROMAN",
    "KBDNLS_SBCSDBCS",
    "KBDNLS_SEND_BASE_VK",
    "KBDNLS_SEND_PARAM_VK",
    "KBDNLS_TYPE_NORMAL",
    "KBDNLS_TYPE_NULL",
    "KBDNLS_TYPE_TOGGLE",
    "KBDROYA",
    "KBDSHIFT",
    "KBDTABLES",
    "KBDTABLE_DESC",
    "KBDTABLE_MULTI",
    "KBDTABLE_MULTI_MAX",
    "KBD_TYPE",
    "KBD_TYPE_INFO",
    "KBD_VERSION",
    "KEYBDINPUT",
    "KEYBD_EVENT_FLAGS",
    "KEYBOARD_TYPE_GENERIC_101",
    "KEYBOARD_TYPE_JAPAN",
    "KEYBOARD_TYPE_KOREA",
    "KEYBOARD_TYPE_UNKNOWN",
    "KEYEVENTF_EXTENDEDKEY",
    "KEYEVENTF_KEYUP",
    "KEYEVENTF_SCANCODE",
    "KEYEVENTF_UNICODE",
    "KLF_ACTIVATE",
    "KLF_NOTELLSHELL",
    "KLF_REORDER",
    "KLF_REPLACELANG",
    "KLF_RESET",
    "KLF_SETFORPROCESS",
    "KLF_SHIFTLOCK",
    "KLF_SUBSTITUTE_OK",
    "KLLF_ALTGR",
    "KLLF_GLOBAL_ATTRS",
    "KLLF_LRM_RLM",
    "KLLF_SHIFTLOCK",
    "LASTINPUTINFO",
    "LIGATURE1",
    "LIGATURE2",
    "LIGATURE3",
    "LIGATURE4",
    "LIGATURE5",
    "LoadKeyboardLayoutA",
    "LoadKeyboardLayoutW",
    "MACRON",
    "MAPVK_VK_TO_CHAR",
    "MAPVK_VK_TO_VSC",
    "MAPVK_VK_TO_VSC_EX",
    "MAPVK_VSC_TO_VK",
    "MAPVK_VSC_TO_VK_EX",
    "MAP_VIRTUAL_KEY_TYPE",
    "MICROSOFT_KBD_001_TYPE",
    "MICROSOFT_KBD_002_TYPE",
    "MICROSOFT_KBD_101A_TYPE",
    "MICROSOFT_KBD_101B_TYPE",
    "MICROSOFT_KBD_101C_TYPE",
    "MICROSOFT_KBD_101_TYPE",
    "MICROSOFT_KBD_103_TYPE",
    "MICROSOFT_KBD_106_TYPE",
    "MICROSOFT_KBD_AX_TYPE",
    "MICROSOFT_KBD_FUNC",
    "MODIFIERS",
    "MOD_ALT",
    "MOD_CONTROL",
    "MOD_NOREPEAT",
    "MOD_SHIFT",
    "MOD_WIN",
    "MOUSEEVENTF_ABSOLUTE",
    "MOUSEEVENTF_HWHEEL",
    "MOUSEEVENTF_LEFTDOWN",
    "MOUSEEVENTF_LEFTUP",
    "MOUSEEVENTF_MIDDLEDOWN",
    "MOUSEEVENTF_MIDDLEUP",
    "MOUSEEVENTF_MOVE",
    "MOUSEEVENTF_MOVE_NOCOALESCE",
    "MOUSEEVENTF_RIGHTDOWN",
    "MOUSEEVENTF_RIGHTUP",
    "MOUSEEVENTF_VIRTUALDESK",
    "MOUSEEVENTF_WHEEL",
    "MOUSEEVENTF_XDOWN",
    "MOUSEEVENTF_XUP",
    "MOUSEINPUT",
    "MOUSEMOVEPOINT",
    "MOUSE_EVENT_FLAGS",
    "MapVirtualKeyA",
    "MapVirtualKeyExA",
    "MapVirtualKeyExW",
    "MapVirtualKeyW",
    "NEC_KBD_106_TYPE",
    "NEC_KBD_H_MODE_TYPE",
    "NEC_KBD_LAPTOP_TYPE",
    "NEC_KBD_NORMAL_TYPE",
    "NEC_KBD_N_MODE_TYPE",
    "NLSKBD_INFO_ACCESSIBILITY_KEYMAP",
    "NLSKBD_INFO_EMURATE_101_KEYBOARD",
    "NLSKBD_INFO_EMURATE_106_KEYBOARD",
    "NLSKBD_INFO_SEND_IME_NOTIFICATION",
    "NLSKBD_OEM_AX",
    "NLSKBD_OEM_DEC",
    "NLSKBD_OEM_EPSON",
    "NLSKBD_OEM_FUJITSU",
    "NLSKBD_OEM_IBM",
    "NLSKBD_OEM_MATSUSHITA",
    "NLSKBD_OEM_MICROSOFT",
    "NLSKBD_OEM_NEC",
    "NLSKBD_OEM_TOSHIBA",
    "OGONEK",
    "OVERSCORE",
    "OemKeyScan",
    "RING",
    "RegisterHotKey",
    "ReleaseCapture",
    "SCANCODE_ALT",
    "SCANCODE_CTRL",
    "SCANCODE_LSHIFT",
    "SCANCODE_LWIN",
    "SCANCODE_NUMPAD_FIRST",
    "SCANCODE_NUMPAD_LAST",
    "SCANCODE_RSHIFT",
    "SCANCODE_RWIN",
    "SCANCODE_THAI_LAYOUT_TOGGLE",
    "SGCAPS",
    "SHFT_INVALID",
    "SendInput",
    "SetActiveWindow",
    "SetCapture",
    "SetDoubleClickTime",
    "SetFocus",
    "SetKeyboardState",
    "SwapMouseButton",
    "TILDE",
    "TME_CANCEL",
    "TME_HOVER",
    "TME_LEAVE",
    "TME_NONCLIENT",
    "TME_QUERY",
    "TONOS",
    "TOSHIBA_KBD_DESKTOP_TYPE",
    "TOSHIBA_KBD_LAPTOP_TYPE",
    "TRACKMOUSEEVENT",
    "TRACKMOUSEEVENT_FLAGS",
    "ToAscii",
    "ToAsciiEx",
    "ToUnicode",
    "ToUnicodeEx",
    "TrackMouseEvent",
    "UMLAUT",
    "UnloadKeyboardLayout",
    "UnregisterHotKey",
    "VIRTUAL_KEY",
    "VK_0",
    "VK_1",
    "VK_2",
    "VK_3",
    "VK_4",
    "VK_5",
    "VK_6",
    "VK_7",
    "VK_8",
    "VK_9",
    "VK_A",
    "VK_ABNT_C1",
    "VK_ABNT_C2",
    "VK_ACCEPT",
    "VK_ADD",
    "VK_APPS",
    "VK_ATTN",
    "VK_B",
    "VK_BACK",
    "VK_BROWSER_BACK",
    "VK_BROWSER_FAVORITES",
    "VK_BROWSER_FORWARD",
    "VK_BROWSER_HOME",
    "VK_BROWSER_REFRESH",
    "VK_BROWSER_SEARCH",
    "VK_BROWSER_STOP",
    "VK_C",
    "VK_CANCEL",
    "VK_CAPITAL",
    "VK_CLEAR",
    "VK_CONTROL",
    "VK_CONVERT",
    "VK_CRSEL",
    "VK_D",
    "VK_DBE_ALPHANUMERIC",
    "VK_DBE_CODEINPUT",
    "VK_DBE_DBCSCHAR",
    "VK_DBE_DETERMINESTRING",
    "VK_DBE_ENTERDLGCONVERSIONMODE",
    "VK_DBE_ENTERIMECONFIGMODE",
    "VK_DBE_ENTERWORDREGISTERMODE",
    "VK_DBE_FLUSHSTRING",
    "VK_DBE_HIRAGANA",
    "VK_DBE_KATAKANA",
    "VK_DBE_NOCODEINPUT",
    "VK_DBE_NOROMAN",
    "VK_DBE_ROMAN",
    "VK_DBE_SBCSCHAR",
    "VK_DECIMAL",
    "VK_DELETE",
    "VK_DIVIDE",
    "VK_DOWN",
    "VK_E",
    "VK_END",
    "VK_EREOF",
    "VK_ESCAPE",
    "VK_EXECUTE",
    "VK_EXSEL",
    "VK_F",
    "VK_F1",
    "VK_F10",
    "VK_F11",
    "VK_F12",
    "VK_F13",
    "VK_F14",
    "VK_F15",
    "VK_F16",
    "VK_F17",
    "VK_F18",
    "VK_F19",
    "VK_F2",
    "VK_F20",
    "VK_F21",
    "VK_F22",
    "VK_F23",
    "VK_F24",
    "VK_F3",
    "VK_F4",
    "VK_F5",
    "VK_F6",
    "VK_F7",
    "VK_F8",
    "VK_F9",
    "VK_FINAL",
    "VK_FPARAM",
    "VK_G",
    "VK_GAMEPAD_A",
    "VK_GAMEPAD_B",
    "VK_GAMEPAD_DPAD_DOWN",
    "VK_GAMEPAD_DPAD_LEFT",
    "VK_GAMEPAD_DPAD_RIGHT",
    "VK_GAMEPAD_DPAD_UP",
    "VK_GAMEPAD_LEFT_SHOULDER",
    "VK_GAMEPAD_LEFT_THUMBSTICK_BUTTON",
    "VK_GAMEPAD_LEFT_THUMBSTICK_DOWN",
    "VK_GAMEPAD_LEFT_THUMBSTICK_LEFT",
    "VK_GAMEPAD_LEFT_THUMBSTICK_RIGHT",
    "VK_GAMEPAD_LEFT_THUMBSTICK_UP",
    "VK_GAMEPAD_LEFT_TRIGGER",
    "VK_GAMEPAD_MENU",
    "VK_GAMEPAD_RIGHT_SHOULDER",
    "VK_GAMEPAD_RIGHT_THUMBSTICK_BUTTON",
    "VK_GAMEPAD_RIGHT_THUMBSTICK_DOWN",
    "VK_GAMEPAD_RIGHT_THUMBSTICK_LEFT",
    "VK_GAMEPAD_RIGHT_THUMBSTICK_RIGHT",
    "VK_GAMEPAD_RIGHT_THUMBSTICK_UP",
    "VK_GAMEPAD_RIGHT_TRIGGER",
    "VK_GAMEPAD_VIEW",
    "VK_GAMEPAD_X",
    "VK_GAMEPAD_Y",
    "VK_H",
    "VK_HANGEUL",
    "VK_HANGUL",
    "VK_HANJA",
    "VK_HELP",
    "VK_HOME",
    "VK_I",
    "VK_ICO_00",
    "VK_ICO_CLEAR",
    "VK_ICO_HELP",
    "VK_IME_OFF",
    "VK_IME_ON",
    "VK_INSERT",
    "VK_J",
    "VK_JUNJA",
    "VK_K",
    "VK_KANA",
    "VK_KANJI",
    "VK_L",
    "VK_LAUNCH_APP1",
    "VK_LAUNCH_APP2",
    "VK_LAUNCH_MAIL",
    "VK_LAUNCH_MEDIA_SELECT",
    "VK_LBUTTON",
    "VK_LCONTROL",
    "VK_LEFT",
    "VK_LMENU",
    "VK_LSHIFT",
    "VK_LWIN",
    "VK_M",
    "VK_MBUTTON",
    "VK_MEDIA_NEXT_TRACK",
    "VK_MEDIA_PLAY_PAUSE",
    "VK_MEDIA_PREV_TRACK",
    "VK_MEDIA_STOP",
    "VK_MENU",
    "VK_MODECHANGE",
    "VK_MULTIPLY",
    "VK_N",
    "VK_NAVIGATION_ACCEPT",
    "VK_NAVIGATION_CANCEL",
    "VK_NAVIGATION_DOWN",
    "VK_NAVIGATION_LEFT",
    "VK_NAVIGATION_MENU",
    "VK_NAVIGATION_RIGHT",
    "VK_NAVIGATION_UP",
    "VK_NAVIGATION_VIEW",
    "VK_NEXT",
    "VK_NONAME",
    "VK_NONCONVERT",
    "VK_NUMLOCK",
    "VK_NUMPAD0",
    "VK_NUMPAD1",
    "VK_NUMPAD2",
    "VK_NUMPAD3",
    "VK_NUMPAD4",
    "VK_NUMPAD5",
    "VK_NUMPAD6",
    "VK_NUMPAD7",
    "VK_NUMPAD8",
    "VK_NUMPAD9",
    "VK_O",
    "VK_OEM_1",
    "VK_OEM_102",
    "VK_OEM_2",
    "VK_OEM_3",
    "VK_OEM_4",
    "VK_OEM_5",
    "VK_OEM_6",
    "VK_OEM_7",
    "VK_OEM_8",
    "VK_OEM_ATTN",
    "VK_OEM_AUTO",
    "VK_OEM_AX",
    "VK_OEM_BACKTAB",
    "VK_OEM_CLEAR",
    "VK_OEM_COMMA",
    "VK_OEM_COPY",
    "VK_OEM_CUSEL",
    "VK_OEM_ENLW",
    "VK_OEM_FINISH",
    "VK_OEM_FJ_JISHO",
    "VK_OEM_FJ_LOYA",
    "VK_OEM_FJ_MASSHOU",
    "VK_OEM_FJ_ROYA",
    "VK_OEM_FJ_TOUROKU",
    "VK_OEM_JUMP",
    "VK_OEM_MINUS",
    "VK_OEM_NEC_EQUAL",
    "VK_OEM_PA1",
    "VK_OEM_PA2",
    "VK_OEM_PA3",
    "VK_OEM_PERIOD",
    "VK_OEM_PLUS",
    "VK_OEM_RESET",
    "VK_OEM_WSCTRL",
    "VK_P",
    "VK_PA1",
    "VK_PACKET",
    "VK_PAUSE",
    "VK_PLAY",
    "VK_PRINT",
    "VK_PRIOR",
    "VK_PROCESSKEY",
    "VK_Q",
    "VK_R",
    "VK_RBUTTON",
    "VK_RCONTROL",
    "VK_RETURN",
    "VK_RIGHT",
    "VK_RMENU",
    "VK_RSHIFT",
    "VK_RWIN",
    "VK_S",
    "VK_SCROLL",
    "VK_SELECT",
    "VK_SEPARATOR",
    "VK_SHIFT",
    "VK_SLEEP",
    "VK_SNAPSHOT",
    "VK_SPACE",
    "VK_SUBTRACT",
    "VK_T",
    "VK_TAB",
    "VK_TO_BIT",
    "VK_TO_WCHARS1",
    "VK_TO_WCHARS10",
    "VK_TO_WCHARS2",
    "VK_TO_WCHARS3",
    "VK_TO_WCHARS4",
    "VK_TO_WCHARS5",
    "VK_TO_WCHARS6",
    "VK_TO_WCHARS7",
    "VK_TO_WCHARS8",
    "VK_TO_WCHARS9",
    "VK_TO_WCHAR_TABLE",
    "VK_U",
    "VK_UP",
    "VK_V",
    "VK_VOLUME_DOWN",
    "VK_VOLUME_MUTE",
    "VK_VOLUME_UP",
    "VK_VSC",
    "VK_W",
    "VK_X",
    "VK_XBUTTON1",
    "VK_XBUTTON2",
    "VK_Y",
    "VK_Z",
    "VK_ZOOM",
    "VK__none_",
    "VSC_LPWSTR",
    "VSC_VK",
    "VkKeyScanA",
    "VkKeyScanExA",
    "VkKeyScanExW",
    "VkKeyScanW",
    "WCH_DEAD",
    "WCH_LGTR",
    "WCH_NONE",
    "_TrackMouseEvent",
    "keybd_event",
    "mouse_event",
    "wszACUTE",
    "wszBREVE",
    "wszCEDILLA",
    "wszCIRCUMFLEX",
    "wszDIARESIS_TONOS",
    "wszDOT_ABOVE",
    "wszDOUBLE_ACUTE",
    "wszGRAVE",
    "wszHACEK",
    "wszHOOK_ABOVE",
    "wszMACRON",
    "wszOGONEK",
    "wszOVERSCORE",
    "wszRING",
    "wszTILDE",
    "wszTONOS",
    "wszUMLAUT",
]
_arch_optional = [
]
