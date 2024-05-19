from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Gaming
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
ID_GDF_XML_STR: String = '__GDF_XML'
ID_GDF_THUMBNAIL_STR: String = '__GDF_THUMBNAIL'
@winfunctype('api-ms-win-gaming-expandedresources-l1-1-0.dll')
def HasExpandedResources(hasExpandedResources: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-expandedresources-l1-1-0.dll')
def GetExpandedResourceExclusiveCpuCount(exclusiveCpuCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-expandedresources-l1-1-0.dll')
def ReleaseExclusiveCpuSets() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-deviceinformation-l1-1-0.dll')
def GetGamingDeviceModelInformation(information: POINTER(win32more.Windows.Win32.Gaming.GAMING_DEVICE_MODEL_INFORMATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ShowGameInviteUI(serviceConfigurationId: win32more.Windows.Win32.System.WinRT.HSTRING, sessionTemplateName: win32more.Windows.Win32.System.WinRT.HSTRING, sessionId: win32more.Windows.Win32.System.WinRT.HSTRING, invitationDisplayText: win32more.Windows.Win32.System.WinRT.HSTRING, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ShowPlayerPickerUI(promptDisplayText: win32more.Windows.Win32.System.WinRT.HSTRING, xuids: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING), xuidsCount: UIntPtr, preSelectedXuids: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING), preSelectedXuidsCount: UIntPtr, minSelectionCount: UIntPtr, maxSelectionCount: UIntPtr, completionRoutine: win32more.Windows.Win32.Gaming.PlayerPickerUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ShowProfileCardUI(targetUserXuid: win32more.Windows.Win32.System.WinRT.HSTRING, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ShowChangeFriendRelationshipUI(targetUserXuid: win32more.Windows.Win32.System.WinRT.HSTRING, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ShowTitleAchievementsUI(titleId: UInt32, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ProcessPendingGameUI(waitForCompletion: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def TryCancelPendingGameUI() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-1.dll')
def CheckGamingPrivilegeWithUI(privilegeId: UInt32, scope: win32more.Windows.Win32.System.WinRT.HSTRING, policy: win32more.Windows.Win32.System.WinRT.HSTRING, friendlyMessage: win32more.Windows.Win32.System.WinRT.HSTRING, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-1.dll')
def CheckGamingPrivilegeSilently(privilegeId: UInt32, scope: win32more.Windows.Win32.System.WinRT.HSTRING, policy: win32more.Windows.Win32.System.WinRT.HSTRING, hasPrivilege: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def ShowGameInviteUIForUser(user: win32more.Windows.Win32.System.WinRT.IInspectable, serviceConfigurationId: win32more.Windows.Win32.System.WinRT.HSTRING, sessionTemplateName: win32more.Windows.Win32.System.WinRT.HSTRING, sessionId: win32more.Windows.Win32.System.WinRT.HSTRING, invitationDisplayText: win32more.Windows.Win32.System.WinRT.HSTRING, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def ShowPlayerPickerUIForUser(user: win32more.Windows.Win32.System.WinRT.IInspectable, promptDisplayText: win32more.Windows.Win32.System.WinRT.HSTRING, xuids: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING), xuidsCount: UIntPtr, preSelectedXuids: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING), preSelectedXuidsCount: UIntPtr, minSelectionCount: UIntPtr, maxSelectionCount: UIntPtr, completionRoutine: win32more.Windows.Win32.Gaming.PlayerPickerUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def ShowProfileCardUIForUser(user: win32more.Windows.Win32.System.WinRT.IInspectable, targetUserXuid: win32more.Windows.Win32.System.WinRT.HSTRING, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def ShowChangeFriendRelationshipUIForUser(user: win32more.Windows.Win32.System.WinRT.IInspectable, targetUserXuid: win32more.Windows.Win32.System.WinRT.HSTRING, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def ShowTitleAchievementsUIForUser(user: win32more.Windows.Win32.System.WinRT.IInspectable, titleId: UInt32, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def CheckGamingPrivilegeWithUIForUser(user: win32more.Windows.Win32.System.WinRT.IInspectable, privilegeId: UInt32, scope: win32more.Windows.Win32.System.WinRT.HSTRING, policy: win32more.Windows.Win32.System.WinRT.HSTRING, friendlyMessage: win32more.Windows.Win32.System.WinRT.HSTRING, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def CheckGamingPrivilegeSilentlyForUser(user: win32more.Windows.Win32.System.WinRT.IInspectable, privilegeId: UInt32, scope: win32more.Windows.Win32.System.WinRT.HSTRING, policy: win32more.Windows.Win32.System.WinRT.HSTRING, hasPrivilege: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-3.dll')
def ShowGameInviteUIWithContext(serviceConfigurationId: win32more.Windows.Win32.System.WinRT.HSTRING, sessionTemplateName: win32more.Windows.Win32.System.WinRT.HSTRING, sessionId: win32more.Windows.Win32.System.WinRT.HSTRING, invitationDisplayText: win32more.Windows.Win32.System.WinRT.HSTRING, customActivationContext: win32more.Windows.Win32.System.WinRT.HSTRING, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-3.dll')
def ShowGameInviteUIWithContextForUser(user: win32more.Windows.Win32.System.WinRT.IInspectable, serviceConfigurationId: win32more.Windows.Win32.System.WinRT.HSTRING, sessionTemplateName: win32more.Windows.Win32.System.WinRT.HSTRING, sessionId: win32more.Windows.Win32.System.WinRT.HSTRING, invitationDisplayText: win32more.Windows.Win32.System.WinRT.HSTRING, customActivationContext: win32more.Windows.Win32.System.WinRT.HSTRING, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowGameInfoUI(titleId: UInt32, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowGameInfoUIForUser(user: win32more.Windows.Win32.System.WinRT.IInspectable, titleId: UInt32, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowFindFriendsUI(completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowFindFriendsUIForUser(user: win32more.Windows.Win32.System.WinRT.IInspectable, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowCustomizeUserProfileUI(completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowCustomizeUserProfileUIForUser(user: win32more.Windows.Win32.System.WinRT.IInspectable, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowUserSettingsUI(completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowUserSettingsUIForUser(user: win32more.Windows.Win32.System.WinRT.IInspectable, completionRoutine: win32more.Windows.Win32.Gaming.GameUICompletionRoutine, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
GAMESTATS_OPEN_RESULT = Int32
GAMESTATS_OPEN_CREATED: win32more.Windows.Win32.Gaming.GAMESTATS_OPEN_RESULT = 0
GAMESTATS_OPEN_OPENED: win32more.Windows.Win32.Gaming.GAMESTATS_OPEN_RESULT = 1
GAMESTATS_OPEN_TYPE = Int32
GAMESTATS_OPEN_OPENORCREATE: win32more.Windows.Win32.Gaming.GAMESTATS_OPEN_TYPE = 0
GAMESTATS_OPEN_OPENONLY: win32more.Windows.Win32.Gaming.GAMESTATS_OPEN_TYPE = 1
GAME_INSTALL_SCOPE = Int32
GIS_NOT_INSTALLED: win32more.Windows.Win32.Gaming.GAME_INSTALL_SCOPE = 1
GIS_CURRENT_USER: win32more.Windows.Win32.Gaming.GAME_INSTALL_SCOPE = 2
GIS_ALL_USERS: win32more.Windows.Win32.Gaming.GAME_INSTALL_SCOPE = 3
GAMING_DEVICE_DEVICE_ID = Int32
GAMING_DEVICE_DEVICE_ID_NONE: win32more.Windows.Win32.Gaming.GAMING_DEVICE_DEVICE_ID = 0
GAMING_DEVICE_DEVICE_ID_XBOX_ONE: win32more.Windows.Win32.Gaming.GAMING_DEVICE_DEVICE_ID = 1988865574
GAMING_DEVICE_DEVICE_ID_XBOX_ONE_S: win32more.Windows.Win32.Gaming.GAMING_DEVICE_DEVICE_ID = 712204761
GAMING_DEVICE_DEVICE_ID_XBOX_ONE_X: win32more.Windows.Win32.Gaming.GAMING_DEVICE_DEVICE_ID = 1523980231
GAMING_DEVICE_DEVICE_ID_XBOX_ONE_X_DEVKIT: win32more.Windows.Win32.Gaming.GAMING_DEVICE_DEVICE_ID = 284675555
GAMING_DEVICE_DEVICE_ID_XBOX_SERIES_S: win32more.Windows.Win32.Gaming.GAMING_DEVICE_DEVICE_ID = 489159355
GAMING_DEVICE_DEVICE_ID_XBOX_SERIES_X: win32more.Windows.Win32.Gaming.GAMING_DEVICE_DEVICE_ID = 796540415
GAMING_DEVICE_DEVICE_ID_XBOX_SERIES_X_DEVKIT: win32more.Windows.Win32.Gaming.GAMING_DEVICE_DEVICE_ID = -561359263
class GAMING_DEVICE_MODEL_INFORMATION(Structure):
    vendorId: win32more.Windows.Win32.Gaming.GAMING_DEVICE_VENDOR_ID
    deviceId: win32more.Windows.Win32.Gaming.GAMING_DEVICE_DEVICE_ID
GAMING_DEVICE_VENDOR_ID = Int32
GAMING_DEVICE_VENDOR_ID_NONE: win32more.Windows.Win32.Gaming.GAMING_DEVICE_VENDOR_ID = 0
GAMING_DEVICE_VENDOR_ID_MICROSOFT: win32more.Windows.Win32.Gaming.GAMING_DEVICE_VENDOR_ID = -1024700366
GameExplorer = Guid('{9a5ea990-3034-4d6f-9128-01f3c61022bc}')
GameStatistics = Guid('{dbc85a2c-c0dc-4961-b6e2-d28b62c11ad4}')
@winfunctype_pointer
def GameUICompletionRoutine(returnCode: win32more.Windows.Win32.Foundation.HRESULT, context: VoidPtr) -> Void: ...
class IGameExplorer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e7b2fb72-d728-49b3-a5f2-18ebf5f1349e}')
    @commethod(3)
    def AddGame(self, bstrGDFBinaryPath: win32more.Windows.Win32.Foundation.BSTR, bstrGameInstallDirectory: win32more.Windows.Win32.Foundation.BSTR, installScope: win32more.Windows.Win32.Gaming.GAME_INSTALL_SCOPE, pguidInstanceID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveGame(self, guidInstanceID: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateGame(self, guidInstanceID: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def VerifyAccess(self, bstrGDFBinaryPath: win32more.Windows.Win32.Foundation.BSTR, pfHasAccess: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGameExplorer2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{86874aa7-a1ed-450d-a7eb-b89e20b2fff3}')
    @commethod(3)
    def InstallGame(self, binaryGDFPath: win32more.Windows.Win32.Foundation.PWSTR, installDirectory: win32more.Windows.Win32.Foundation.PWSTR, installScope: win32more.Windows.Win32.Gaming.GAME_INSTALL_SCOPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UninstallGame(self, binaryGDFPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CheckAccess(self, binaryGDFPath: win32more.Windows.Win32.Foundation.PWSTR, pHasAccess: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGameStatistics(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3887c9ca-04a0-42ae-bc4c-5fa6c7721145}')
    @commethod(3)
    def GetMaxCategoryLength(self, cch: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMaxNameLength(self, cch: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxValueLength(self, cch: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMaxCategories(self, pMax: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMaxStatsPerCategory(self, pMax: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetCategoryTitle(self, categoryIndex: UInt16, title: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCategoryTitle(self, categoryIndex: UInt16, pTitle: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStatistic(self, categoryIndex: UInt16, statIndex: UInt16, pName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetStatistic(self, categoryIndex: UInt16, statIndex: UInt16, name: win32more.Windows.Win32.Foundation.PWSTR, value: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Save(self, trackChanges: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetLastPlayedCategory(self, categoryIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetLastPlayedCategory(self, pCategoryIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGameStatisticsMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aff3ea11-e70e-407d-95dd-35e612c41ce2}')
    @commethod(3)
    def GetGameStatistics(self, GDFBinaryPath: win32more.Windows.Win32.Foundation.PWSTR, openType: win32more.Windows.Win32.Gaming.GAMESTATS_OPEN_TYPE, pOpenResult: POINTER(win32more.Windows.Win32.Gaming.GAMESTATS_OPEN_RESULT), ppiStats: POINTER(win32more.Windows.Win32.Gaming.IGameStatistics)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveGameStatistics(self, GDFBinaryPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXblIdpAuthManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eb5ddb08-8bbf-449b-ac21-b02ddeb3b136}')
    @commethod(3)
    def SetGamerAccount(self, msaAccountId: win32more.Windows.Win32.Foundation.PWSTR, xuid: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetGamerAccount(self, msaAccountId: POINTER(win32more.Windows.Win32.Foundation.PWSTR), xuid: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetAppViewInitialized(self, appSid: win32more.Windows.Win32.Foundation.PWSTR, msaAccountId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEnvironment(self, environment: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSandbox(self, sandbox: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTokenAndSignatureWithTokenResult(self, msaAccountId: win32more.Windows.Win32.Foundation.PWSTR, appSid: win32more.Windows.Win32.Foundation.PWSTR, msaTarget: win32more.Windows.Win32.Foundation.PWSTR, msaPolicy: win32more.Windows.Win32.Foundation.PWSTR, httpMethod: win32more.Windows.Win32.Foundation.PWSTR, uri: win32more.Windows.Win32.Foundation.PWSTR, headers: win32more.Windows.Win32.Foundation.PWSTR, body: POINTER(Byte), bodySize: UInt32, forceRefresh: win32more.Windows.Win32.Foundation.BOOL, result: POINTER(win32more.Windows.Win32.Gaming.IXblIdpAuthTokenResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXblIdpAuthManager2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bf8c0950-8389-43dd-9a76-a19728ec5dc5}')
    @commethod(3)
    def GetUserlessTokenAndSignatureWithTokenResult(self, appSid: win32more.Windows.Win32.Foundation.PWSTR, msaTarget: win32more.Windows.Win32.Foundation.PWSTR, msaPolicy: win32more.Windows.Win32.Foundation.PWSTR, httpMethod: win32more.Windows.Win32.Foundation.PWSTR, uri: win32more.Windows.Win32.Foundation.PWSTR, headers: win32more.Windows.Win32.Foundation.PWSTR, body: POINTER(Byte), bodySize: UInt32, forceRefresh: win32more.Windows.Win32.Foundation.BOOL, result: POINTER(win32more.Windows.Win32.Gaming.IXblIdpAuthTokenResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXblIdpAuthTokenResult(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{46ce0225-f267-4d68-b299-b2762552dec1}')
    @commethod(3)
    def GetStatus(self, status: POINTER(win32more.Windows.Win32.Gaming.XBL_IDP_AUTH_TOKEN_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetErrorCode(self, errorCode: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetToken(self, token: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSignature(self, signature: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSandbox(self, sandbox: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetEnvironment(self, environment: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetMsaAccountId(self, msaAccountId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetXuid(self, xuid: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetGamertag(self, gamertag: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetAgeGroup(self, ageGroup: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPrivileges(self, privileges: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetMsaTarget(self, msaTarget: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetMsaPolicy(self, msaPolicy: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetMsaAppId(self, msaAppId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetRedirect(self, redirect: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetMessage(self, message: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetHelpId(self, helpId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetEnforcementBans(self, enforcementBans: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetRestrictions(self, restrictions: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetTitleRestrictions(self, titleRestrictions: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXblIdpAuthTokenResult2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75d760b0-60b9-412d-994f-26b2cd5f7812}')
    @commethod(3)
    def GetModernGamertag(self, value: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetModernGamertagSuffix(self, value: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetUniqueModernGamertag(self, value: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
KnownGamingPrivileges = Int32
XPRIVILEGE_BROADCAST: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 190
XPRIVILEGE_VIEW_FRIENDS_LIST: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 197
XPRIVILEGE_GAME_DVR: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 198
XPRIVILEGE_SHARE_KINECT_CONTENT: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 199
XPRIVILEGE_MULTIPLAYER_PARTIES: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 203
XPRIVILEGE_COMMUNICATION_VOICE_INGAME: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 205
XPRIVILEGE_COMMUNICATION_VOICE_SKYPE: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 206
XPRIVILEGE_CLOUD_GAMING_MANAGE_SESSION: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 207
XPRIVILEGE_CLOUD_GAMING_JOIN_SESSION: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 208
XPRIVILEGE_CLOUD_SAVED_GAMES: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 209
XPRIVILEGE_SHARE_CONTENT: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 211
XPRIVILEGE_PREMIUM_CONTENT: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 214
XPRIVILEGE_SUBSCRIPTION_CONTENT: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 219
XPRIVILEGE_SOCIAL_NETWORK_SHARING: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 220
XPRIVILEGE_PREMIUM_VIDEO: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 224
XPRIVILEGE_VIDEO_COMMUNICATIONS: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 235
XPRIVILEGE_PURCHASE_CONTENT: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 245
XPRIVILEGE_USER_CREATED_CONTENT: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 247
XPRIVILEGE_PROFILE_VIEWING: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 249
XPRIVILEGE_COMMUNICATIONS: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 252
XPRIVILEGE_MULTIPLAYER_SESSIONS: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 254
XPRIVILEGE_ADD_FRIEND: win32more.Windows.Win32.Gaming.KnownGamingPrivileges = 255
@winfunctype_pointer
def PlayerPickerUICompletionRoutine(returnCode: win32more.Windows.Win32.Foundation.HRESULT, context: VoidPtr, selectedXuids: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING), selectedXuidsCount: UIntPtr) -> Void: ...
XBL_IDP_AUTH_TOKEN_STATUS = Int32
XBL_IDP_AUTH_TOKEN_STATUS_SUCCESS: win32more.Windows.Win32.Gaming.XBL_IDP_AUTH_TOKEN_STATUS = 0
XBL_IDP_AUTH_TOKEN_STATUS_OFFLINE_SUCCESS: win32more.Windows.Win32.Gaming.XBL_IDP_AUTH_TOKEN_STATUS = 1
XBL_IDP_AUTH_TOKEN_STATUS_NO_ACCOUNT_SET: win32more.Windows.Win32.Gaming.XBL_IDP_AUTH_TOKEN_STATUS = 2
XBL_IDP_AUTH_TOKEN_STATUS_LOAD_MSA_ACCOUNT_FAILED: win32more.Windows.Win32.Gaming.XBL_IDP_AUTH_TOKEN_STATUS = 3
XBL_IDP_AUTH_TOKEN_STATUS_XBOX_VETO: win32more.Windows.Win32.Gaming.XBL_IDP_AUTH_TOKEN_STATUS = 4
XBL_IDP_AUTH_TOKEN_STATUS_MSA_INTERRUPT: win32more.Windows.Win32.Gaming.XBL_IDP_AUTH_TOKEN_STATUS = 5
XBL_IDP_AUTH_TOKEN_STATUS_OFFLINE_NO_CONSENT: win32more.Windows.Win32.Gaming.XBL_IDP_AUTH_TOKEN_STATUS = 6
XBL_IDP_AUTH_TOKEN_STATUS_VIEW_NOT_SET: win32more.Windows.Win32.Gaming.XBL_IDP_AUTH_TOKEN_STATUS = 7
XBL_IDP_AUTH_TOKEN_STATUS_UNKNOWN: win32more.Windows.Win32.Gaming.XBL_IDP_AUTH_TOKEN_STATUS = -1
XblIdpAuthManager = Guid('{ce23534b-56d8-4978-86a2-7ee570640468}')
XblIdpAuthTokenResult = Guid('{9f493441-744a-410c-ae2b-9a22f7c7731f}')


make_ready(__name__)
