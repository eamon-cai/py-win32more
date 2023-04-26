from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.Graphics.DirectManipulation
import Windows.Win32.System.Com
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
DIRECTMANIPULATION_KEYBOARDFOCUS: UInt32 = 4294967294
DIRECTMANIPULATION_MOUSEFOCUS: UInt32 = 4294967293
CLSID_VerticalIndicatorContent: Guid = Guid('a10b5f17-afe0-4aa2-91-e9-3e-70-01-d2-e6-b4')
CLSID_HorizontalIndicatorContent: Guid = Guid('e7d18cf5-3ec7-44d5-a7-6b-37-70-f3-cf-90-3d')
CLSID_VirtualViewportContent: Guid = Guid('3206a19a-86f0-4cb4-a7-f3-16-e3-b7-e2-d8-52')
CLSID_DragDropConfigurationBehavior: Guid = Guid('09b01b3e-ba6c-454d-82-e8-95-e3-52-32-9f-23')
CLSID_AutoScrollBehavior: Guid = Guid('26126a51-3c70-4c9a-ae-c2-94-88-49-ee-b0-93')
CLSID_DeferContactService: Guid = Guid('d7b67cf4-84bb-434e-86-ae-65-92-bb-c9-ab-d9')
DCompManipulationCompositor = Guid('79dea627-a08a-43ac-8e-f5-69-00-b9-29-91-26')
DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION = Int32
DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION_STOP: DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION = 0
DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION_FORWARD: DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION = 1
DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION_REVERSE: DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION = 2
DIRECTMANIPULATION_CONFIGURATION = Int32
DIRECTMANIPULATION_CONFIGURATION_NONE: DIRECTMANIPULATION_CONFIGURATION = 0
DIRECTMANIPULATION_CONFIGURATION_INTERACTION: DIRECTMANIPULATION_CONFIGURATION = 1
DIRECTMANIPULATION_CONFIGURATION_TRANSLATION_X: DIRECTMANIPULATION_CONFIGURATION = 2
DIRECTMANIPULATION_CONFIGURATION_TRANSLATION_Y: DIRECTMANIPULATION_CONFIGURATION = 4
DIRECTMANIPULATION_CONFIGURATION_SCALING: DIRECTMANIPULATION_CONFIGURATION = 16
DIRECTMANIPULATION_CONFIGURATION_TRANSLATION_INERTIA: DIRECTMANIPULATION_CONFIGURATION = 32
DIRECTMANIPULATION_CONFIGURATION_SCALING_INERTIA: DIRECTMANIPULATION_CONFIGURATION = 128
DIRECTMANIPULATION_CONFIGURATION_RAILS_X: DIRECTMANIPULATION_CONFIGURATION = 256
DIRECTMANIPULATION_CONFIGURATION_RAILS_Y: DIRECTMANIPULATION_CONFIGURATION = 512
DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION = Int32
DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION_VERTICAL: DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION = 1
DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION_HORIZONTAL: DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION = 2
DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION_SELECT_ONLY: DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION = 16
DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION_SELECT_DRAG: DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION = 32
DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION_HOLD_DRAG: DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION = 64
DIRECTMANIPULATION_DRAG_DROP_STATUS = Int32
DIRECTMANIPULATION_DRAG_DROP_READY: DIRECTMANIPULATION_DRAG_DROP_STATUS = 0
DIRECTMANIPULATION_DRAG_DROP_PRESELECT: DIRECTMANIPULATION_DRAG_DROP_STATUS = 1
DIRECTMANIPULATION_DRAG_DROP_SELECTING: DIRECTMANIPULATION_DRAG_DROP_STATUS = 2
DIRECTMANIPULATION_DRAG_DROP_DRAGGING: DIRECTMANIPULATION_DRAG_DROP_STATUS = 3
DIRECTMANIPULATION_DRAG_DROP_CANCELLED: DIRECTMANIPULATION_DRAG_DROP_STATUS = 4
DIRECTMANIPULATION_DRAG_DROP_COMMITTED: DIRECTMANIPULATION_DRAG_DROP_STATUS = 5
DIRECTMANIPULATION_GESTURE_CONFIGURATION = Int32
DIRECTMANIPULATION_GESTURE_NONE: DIRECTMANIPULATION_GESTURE_CONFIGURATION = 0
DIRECTMANIPULATION_GESTURE_DEFAULT: DIRECTMANIPULATION_GESTURE_CONFIGURATION = 0
DIRECTMANIPULATION_GESTURE_CROSS_SLIDE_VERTICAL: DIRECTMANIPULATION_GESTURE_CONFIGURATION = 8
DIRECTMANIPULATION_GESTURE_CROSS_SLIDE_HORIZONTAL: DIRECTMANIPULATION_GESTURE_CONFIGURATION = 16
DIRECTMANIPULATION_GESTURE_PINCH_ZOOM: DIRECTMANIPULATION_GESTURE_CONFIGURATION = 32
DIRECTMANIPULATION_HITTEST_TYPE = Int32
DIRECTMANIPULATION_HITTEST_TYPE_ASYNCHRONOUS: DIRECTMANIPULATION_HITTEST_TYPE = 0
DIRECTMANIPULATION_HITTEST_TYPE_SYNCHRONOUS: DIRECTMANIPULATION_HITTEST_TYPE = 1
DIRECTMANIPULATION_HITTEST_TYPE_AUTO_SYNCHRONOUS: DIRECTMANIPULATION_HITTEST_TYPE = 2
DIRECTMANIPULATION_HORIZONTALALIGNMENT = Int32
DIRECTMANIPULATION_HORIZONTALALIGNMENT_NONE: DIRECTMANIPULATION_HORIZONTALALIGNMENT = 0
DIRECTMANIPULATION_HORIZONTALALIGNMENT_LEFT: DIRECTMANIPULATION_HORIZONTALALIGNMENT = 1
DIRECTMANIPULATION_HORIZONTALALIGNMENT_CENTER: DIRECTMANIPULATION_HORIZONTALALIGNMENT = 2
DIRECTMANIPULATION_HORIZONTALALIGNMENT_RIGHT: DIRECTMANIPULATION_HORIZONTALALIGNMENT = 4
DIRECTMANIPULATION_HORIZONTALALIGNMENT_UNLOCKCENTER: DIRECTMANIPULATION_HORIZONTALALIGNMENT = 8
DIRECTMANIPULATION_INPUT_MODE = Int32
DIRECTMANIPULATION_INPUT_MODE_AUTOMATIC: DIRECTMANIPULATION_INPUT_MODE = 0
DIRECTMANIPULATION_INPUT_MODE_MANUAL: DIRECTMANIPULATION_INPUT_MODE = 1
DIRECTMANIPULATION_INTERACTION_TYPE = Int32
DIRECTMANIPULATION_INTERACTION_BEGIN: DIRECTMANIPULATION_INTERACTION_TYPE = 0
DIRECTMANIPULATION_INTERACTION_TYPE_MANIPULATION: DIRECTMANIPULATION_INTERACTION_TYPE = 1
DIRECTMANIPULATION_INTERACTION_TYPE_GESTURE_TAP: DIRECTMANIPULATION_INTERACTION_TYPE = 2
DIRECTMANIPULATION_INTERACTION_TYPE_GESTURE_HOLD: DIRECTMANIPULATION_INTERACTION_TYPE = 3
DIRECTMANIPULATION_INTERACTION_TYPE_GESTURE_CROSS_SLIDE: DIRECTMANIPULATION_INTERACTION_TYPE = 4
DIRECTMANIPULATION_INTERACTION_TYPE_GESTURE_PINCH_ZOOM: DIRECTMANIPULATION_INTERACTION_TYPE = 5
DIRECTMANIPULATION_INTERACTION_END: DIRECTMANIPULATION_INTERACTION_TYPE = 100
DIRECTMANIPULATION_MOTION_TYPES = Int32
DIRECTMANIPULATION_MOTION_NONE: DIRECTMANIPULATION_MOTION_TYPES = 0
DIRECTMANIPULATION_MOTION_TRANSLATEX: DIRECTMANIPULATION_MOTION_TYPES = 1
DIRECTMANIPULATION_MOTION_TRANSLATEY: DIRECTMANIPULATION_MOTION_TYPES = 2
DIRECTMANIPULATION_MOTION_ZOOM: DIRECTMANIPULATION_MOTION_TYPES = 4
DIRECTMANIPULATION_MOTION_CENTERX: DIRECTMANIPULATION_MOTION_TYPES = 16
DIRECTMANIPULATION_MOTION_CENTERY: DIRECTMANIPULATION_MOTION_TYPES = 32
DIRECTMANIPULATION_MOTION_ALL: DIRECTMANIPULATION_MOTION_TYPES = 55
DIRECTMANIPULATION_SNAPPOINT_COORDINATE = Int32
DIRECTMANIPULATION_COORDINATE_BOUNDARY: DIRECTMANIPULATION_SNAPPOINT_COORDINATE = 0
DIRECTMANIPULATION_COORDINATE_ORIGIN: DIRECTMANIPULATION_SNAPPOINT_COORDINATE = 1
DIRECTMANIPULATION_COORDINATE_MIRRORED: DIRECTMANIPULATION_SNAPPOINT_COORDINATE = 16
DIRECTMANIPULATION_SNAPPOINT_TYPE = Int32
DIRECTMANIPULATION_SNAPPOINT_MANDATORY: DIRECTMANIPULATION_SNAPPOINT_TYPE = 0
DIRECTMANIPULATION_SNAPPOINT_OPTIONAL: DIRECTMANIPULATION_SNAPPOINT_TYPE = 1
DIRECTMANIPULATION_SNAPPOINT_MANDATORY_SINGLE: DIRECTMANIPULATION_SNAPPOINT_TYPE = 2
DIRECTMANIPULATION_SNAPPOINT_OPTIONAL_SINGLE: DIRECTMANIPULATION_SNAPPOINT_TYPE = 3
DIRECTMANIPULATION_STATUS = Int32
DIRECTMANIPULATION_BUILDING: DIRECTMANIPULATION_STATUS = 0
DIRECTMANIPULATION_ENABLED: DIRECTMANIPULATION_STATUS = 1
DIRECTMANIPULATION_DISABLED: DIRECTMANIPULATION_STATUS = 2
DIRECTMANIPULATION_RUNNING: DIRECTMANIPULATION_STATUS = 3
DIRECTMANIPULATION_INERTIA: DIRECTMANIPULATION_STATUS = 4
DIRECTMANIPULATION_READY: DIRECTMANIPULATION_STATUS = 5
DIRECTMANIPULATION_SUSPENDED: DIRECTMANIPULATION_STATUS = 6
DIRECTMANIPULATION_VERTICALALIGNMENT = Int32
DIRECTMANIPULATION_VERTICALALIGNMENT_NONE: DIRECTMANIPULATION_VERTICALALIGNMENT = 0
DIRECTMANIPULATION_VERTICALALIGNMENT_TOP: DIRECTMANIPULATION_VERTICALALIGNMENT = 1
DIRECTMANIPULATION_VERTICALALIGNMENT_CENTER: DIRECTMANIPULATION_VERTICALALIGNMENT = 2
DIRECTMANIPULATION_VERTICALALIGNMENT_BOTTOM: DIRECTMANIPULATION_VERTICALALIGNMENT = 4
DIRECTMANIPULATION_VERTICALALIGNMENT_UNLOCKCENTER: DIRECTMANIPULATION_VERTICALALIGNMENT = 8
DIRECTMANIPULATION_VIEWPORT_OPTIONS = Int32
DIRECTMANIPULATION_VIEWPORT_OPTIONS_DEFAULT: DIRECTMANIPULATION_VIEWPORT_OPTIONS = 0
DIRECTMANIPULATION_VIEWPORT_OPTIONS_AUTODISABLE: DIRECTMANIPULATION_VIEWPORT_OPTIONS = 1
DIRECTMANIPULATION_VIEWPORT_OPTIONS_MANUALUPDATE: DIRECTMANIPULATION_VIEWPORT_OPTIONS = 2
DIRECTMANIPULATION_VIEWPORT_OPTIONS_INPUT: DIRECTMANIPULATION_VIEWPORT_OPTIONS = 4
DIRECTMANIPULATION_VIEWPORT_OPTIONS_EXPLICITHITTEST: DIRECTMANIPULATION_VIEWPORT_OPTIONS = 8
DIRECTMANIPULATION_VIEWPORT_OPTIONS_DISABLEPIXELSNAPPING: DIRECTMANIPULATION_VIEWPORT_OPTIONS = 16
DirectManipulationManager = Guid('54e211b6-3650-4f75-83-34-fa-35-95-98-e1-c5')
DirectManipulationPrimaryContent = Guid('caa02661-d59e-41c7-83-93-3b-a3-ba-cb-6b-57')
DirectManipulationSharedManager = Guid('99793286-77cc-4b57-96-db-3b-35-4f-6f-9f-b5')
DirectManipulationUpdateManager = Guid('9fc1bfd5-1835-441a-b3-b1-b6-cc-74-b7-27-d0')
DirectManipulationViewport = Guid('34e211b6-3650-4f75-83-34-fa-35-95-98-e1-c5')
class IDirectManipulationAutoScrollBehavior(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6d5954d4-2003-4356-9b-31-d0-51-c9-ff-0a-f7')
    @commethod(3)
    def SetConfiguration(self, motionTypes: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_MOTION_TYPES, scrollMotion: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationCompositor(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('537a0825-0387-4efa-b6-2f-71-eb-1f-08-5a-7e')
    @commethod(3)
    def AddContent(self, content: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationContent_head, device: Windows.Win32.System.Com.IUnknown_head, parentVisual: Windows.Win32.System.Com.IUnknown_head, childVisual: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveContent(self, content: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationContent_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetUpdateManager(self, updateManager: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationUpdateManager_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Flush(self) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationCompositor2(c_void_p):
    extends: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationCompositor
    Guid = Guid('d38c7822-f1cb-43cb-b4-b9-ac-0c-76-7a-41-2e')
    @commethod(7)
    def AddContentWithCrossProcessChaining(self, content: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationPrimaryContent_head, device: Windows.Win32.System.Com.IUnknown_head, parentVisual: Windows.Win32.System.Com.IUnknown_head, childVisual: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationContent(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b89962cb-3d89-442b-bb-58-50-98-fa-0f-9f-16')
    @commethod(3)
    def GetContentRect(self, contentSize: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetContentRect(self, contentSize: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetViewport(self, riid: POINTER(Guid), object: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTag(self, riid: POINTER(Guid), object: POINTER(c_void_p), id: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetTag(self, object: Windows.Win32.System.Com.IUnknown_head, id: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetOutputTransform(self, matrix: POINTER(Single), pointCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetContentTransform(self, matrix: POINTER(Single), pointCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SyncContentTransform(self, matrix: POINTER(Single), pointCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationDeferContactService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('652d5c71-fe60-4a98-be-70-e5-f2-12-91-e7-f1')
    @commethod(3)
    def DeferContact(self, pointerId: UInt32, timeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelContact(self, pointerId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CancelDeferral(self, pointerId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationDragDropBehavior(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('814b5af5-c2c8-4270-a9-b7-a1-98-ce-8d-02-fa')
    @commethod(3)
    def SetConfiguration(self, configuration: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStatus(self, status: POINTER(Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_DRAG_DROP_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationDragDropEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1fa11b10-701b-41ae-b5-f2-49-e3-6b-d5-95-aa')
    @commethod(3)
    def OnDragDropStatusChange(self, viewport: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationViewport2_head, current: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_DRAG_DROP_STATUS, previous: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_DRAG_DROP_STATUS) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationFrameInfoProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fb759dba-6f4c-4c01-87-4e-19-c8-a0-59-07-f9')
    @commethod(3)
    def GetNextFrameInfo(self, time: POINTER(UInt64), processTime: POINTER(UInt64), compositionTime: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationInteractionEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e43f45b8-42b4-403e-b1-f2-27-3b-8f-51-08-30')
    @commethod(3)
    def OnInteraction(self, viewport: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationViewport2_head, interaction: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_INTERACTION_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fbf5d3b4-70c7-4163-93-22-5a-6f-66-0d-6f-bc')
    @commethod(3)
    def Activate(self, window: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Deactivate(self, window: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterHitTestTarget(self, window: Windows.Win32.Foundation.HWND, hitTestWindow: Windows.Win32.Foundation.HWND, type: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_HITTEST_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ProcessInput(self, message: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head), handled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetUpdateManager(self, riid: POINTER(Guid), object: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateViewport(self, frameInfo: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationFrameInfoProvider_head, window: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), object: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateContent(self, frameInfo: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationFrameInfoProvider_head, clsid: POINTER(Guid), riid: POINTER(Guid), object: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationManager2(c_void_p):
    extends: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationManager
    Guid = Guid('fa1005e9-3d16-484c-bf-c9-62-b6-1e-56-ec-4e')
    @commethod(10)
    def CreateBehavior(self, clsid: POINTER(Guid), riid: POINTER(Guid), object: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationManager3(c_void_p):
    extends: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationManager2
    Guid = Guid('2cb6b33d-ffe8-488c-b7-50-fb-df-e8-8d-ca-8c')
    @commethod(11)
    def GetService(self, clsid: POINTER(Guid), riid: POINTER(Guid), object: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationPrimaryContent(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c12851e4-1698-4625-b9-b1-7c-a3-ec-18-63-0b')
    @commethod(3)
    def SetSnapInterval(self, motion: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_MOTION_TYPES, interval: Single, offset: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSnapPoints(self, motion: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_MOTION_TYPES, points: POINTER(Single), pointCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSnapType(self, motion: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_MOTION_TYPES, type: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_SNAPPOINT_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSnapCoordinate(self, motion: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_MOTION_TYPES, coordinate: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_SNAPPOINT_COORDINATE, origin: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetZoomBoundaries(self, zoomMinimum: Single, zoomMaximum: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetHorizontalAlignment(self, alignment: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_HORIZONTALALIGNMENT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetVerticalAlignment(self, alignment: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_VERTICALALIGNMENT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetInertiaEndTransform(self, matrix: POINTER(Single), pointCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCenterPoint(self, centerX: POINTER(Single), centerY: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationUpdateHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('790b6337-64f8-4ff5-a2-69-b3-2b-c2-af-27-a7')
    @commethod(3)
    def Update(self) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationUpdateManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b0ae62fd-be34-46e7-9c-aa-d3-61-fa-cb-b9-cc')
    @commethod(3)
    def RegisterWaitHandleCallback(self, handle: Windows.Win32.Foundation.HANDLE, eventHandler: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationUpdateHandler_head, cookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterWaitHandleCallback(self, cookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Update(self, frameInfo: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationFrameInfoProvider_head) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationViewport(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('28b85a3d-60a0-48bd-9b-a1-5c-e8-d9-ea-3a-6d')
    @commethod(3)
    def Enable(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Disable(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetContact(self, pointerId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReleaseContact(self, pointerId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ReleaseAllContacts(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStatus(self, status: POINTER(Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTag(self, riid: POINTER(Guid), object: POINTER(c_void_p), id: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetTag(self, object: Windows.Win32.System.Com.IUnknown_head, id: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetViewportRect(self, viewport: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetViewportRect(self, viewport: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ZoomToRect(self, left: Single, top: Single, right: Single, bottom: Single, animate: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetViewportTransform(self, matrix: POINTER(Single), pointCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SyncDisplayTransform(self, matrix: POINTER(Single), pointCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetPrimaryContent(self, riid: POINTER(Guid), object: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def AddContent(self, content: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationContent_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RemoveContent(self, content: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationContent_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetViewportOptions(self, options: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_VIEWPORT_OPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def AddConfiguration(self, configuration: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_CONFIGURATION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def RemoveConfiguration(self, configuration: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_CONFIGURATION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ActivateConfiguration(self, configuration: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_CONFIGURATION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetManualGesture(self, configuration: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_GESTURE_CONFIGURATION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetChaining(self, enabledTypes: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_MOTION_TYPES) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def AddEventHandler(self, window: Windows.Win32.Foundation.HWND, eventHandler: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationViewportEventHandler_head, cookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def RemoveEventHandler(self, cookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetInputMode(self, mode: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_INPUT_MODE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetUpdateMode(self, mode: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_INPUT_MODE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Abandon(self) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationViewport2(c_void_p):
    extends: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationViewport
    Guid = Guid('923ccaac-61e1-4385-b7-26-01-7a-f1-89-88-2a')
    @commethod(31)
    def AddBehavior(self, behavior: Windows.Win32.System.Com.IUnknown_head, cookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def RemoveBehavior(self, cookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def RemoveAllBehaviors(self) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectManipulationViewportEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('952121da-d69f-45f9-b0-f9-f2-39-44-32-1a-6d')
    @commethod(3)
    def OnViewportStatusChanged(self, viewport: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationViewport_head, current: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_STATUS, previous: Windows.Win32.Graphics.DirectManipulation.DIRECTMANIPULATION_STATUS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnViewportUpdated(self, viewport: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationViewport_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnContentUpdated(self, viewport: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationViewport_head, content: Windows.Win32.Graphics.DirectManipulation.IDirectManipulationContent_head) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IDirectManipulationAutoScrollBehavior')
make_head(_module, 'IDirectManipulationCompositor')
make_head(_module, 'IDirectManipulationCompositor2')
make_head(_module, 'IDirectManipulationContent')
make_head(_module, 'IDirectManipulationDeferContactService')
make_head(_module, 'IDirectManipulationDragDropBehavior')
make_head(_module, 'IDirectManipulationDragDropEventHandler')
make_head(_module, 'IDirectManipulationFrameInfoProvider')
make_head(_module, 'IDirectManipulationInteractionEventHandler')
make_head(_module, 'IDirectManipulationManager')
make_head(_module, 'IDirectManipulationManager2')
make_head(_module, 'IDirectManipulationManager3')
make_head(_module, 'IDirectManipulationPrimaryContent')
make_head(_module, 'IDirectManipulationUpdateHandler')
make_head(_module, 'IDirectManipulationUpdateManager')
make_head(_module, 'IDirectManipulationViewport')
make_head(_module, 'IDirectManipulationViewport2')
make_head(_module, 'IDirectManipulationViewportEventHandler')