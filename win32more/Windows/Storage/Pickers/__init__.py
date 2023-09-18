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
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Storage.Pickers
import win32more.Windows.System
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class FileExtensionVector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.Collections.IVector[WinRT_String]
    _classid_ = 'Windows.Storage.Pickers.FileExtensionVector'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[WinRT_String], index: UInt32) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[WinRT_String]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[WinRT_String]) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[WinRT_String], value: WinRT_String, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[WinRT_String], index: UInt32, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[WinRT_String], index: UInt32, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[WinRT_String], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[WinRT_String], value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[WinRT_String], startIndex: UInt32, items: Annotated[SZArray[WinRT_String], 'Out']) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[WinRT_String], items: Annotated[SZArray[WinRT_String], 'In']) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.Collections.IIterator[WinRT_String]: ...
    Size = property(get_Size, None)
class FileOpenPicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Pickers.IFileOpenPicker
    _classid_ = 'Windows.Storage.Pickers.FileOpenPicker'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Storage.Pickers.FileOpenPicker: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: win32more.Windows.Storage.Pickers.IFileOpenPicker2) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def PickSingleFileAndContinue(self: win32more.Windows.Storage.Pickers.IFileOpenPicker2) -> Void: ...
    @winrt_mixinmethod
    def PickMultipleFilesAndContinue(self: win32more.Windows.Storage.Pickers.IFileOpenPicker2) -> Void: ...
    @winrt_mixinmethod
    def PickSingleFileAsync(self: win32more.Windows.Storage.Pickers.IFileOpenPickerWithOperationId, pickerOperationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def get_ViewMode(self: win32more.Windows.Storage.Pickers.IFileOpenPicker) -> win32more.Windows.Storage.Pickers.PickerViewMode: ...
    @winrt_mixinmethod
    def put_ViewMode(self: win32more.Windows.Storage.Pickers.IFileOpenPicker, value: win32more.Windows.Storage.Pickers.PickerViewMode) -> Void: ...
    @winrt_mixinmethod
    def get_SettingsIdentifier(self: win32more.Windows.Storage.Pickers.IFileOpenPicker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SettingsIdentifier(self: win32more.Windows.Storage.Pickers.IFileOpenPicker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedStartLocation(self: win32more.Windows.Storage.Pickers.IFileOpenPicker) -> win32more.Windows.Storage.Pickers.PickerLocationId: ...
    @winrt_mixinmethod
    def put_SuggestedStartLocation(self: win32more.Windows.Storage.Pickers.IFileOpenPicker, value: win32more.Windows.Storage.Pickers.PickerLocationId) -> Void: ...
    @winrt_mixinmethod
    def get_CommitButtonText(self: win32more.Windows.Storage.Pickers.IFileOpenPicker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CommitButtonText(self: win32more.Windows.Storage.Pickers.IFileOpenPicker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FileTypeFilter(self: win32more.Windows.Storage.Pickers.IFileOpenPicker) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def PickSingleFileAsync_2(self: win32more.Windows.Storage.Pickers.IFileOpenPicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def PickMultipleFilesAsync(self: win32more.Windows.Storage.Pickers.IFileOpenPicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]]: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Storage.Pickers.IFileOpenPicker3) -> win32more.Windows.System.User: ...
    @winrt_classmethod
    def CreateForUser(cls: win32more.Windows.Storage.Pickers.IFileOpenPickerStatics2, user: win32more.Windows.System.User) -> win32more.Windows.Storage.Pickers.FileOpenPicker: ...
    @winrt_classmethod
    def ResumePickSingleFileAsync(cls: win32more.Windows.Storage.Pickers.IFileOpenPickerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    ContinuationData = property(get_ContinuationData, None)
    ViewMode = property(get_ViewMode, put_ViewMode)
    SettingsIdentifier = property(get_SettingsIdentifier, put_SettingsIdentifier)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    FileTypeFilter = property(get_FileTypeFilter, None)
    User = property(get_User, None)
class FilePickerFileTypesOrderedMap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Foundation.Collections.IVector[WinRT_String]]
    _classid_ = 'Windows.Storage.Pickers.FilePickerFileTypesOrderedMap'
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Foundation.Collections.IVector[WinRT_String]], key: WinRT_String) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Foundation.Collections.IVector[WinRT_String]]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Foundation.Collections.IVector[WinRT_String]], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Foundation.Collections.IVector[WinRT_String]]) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Foundation.Collections.IVector[WinRT_String]], key: WinRT_String, value: win32more.Windows.Foundation.Collections.IVector[WinRT_String]) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Foundation.Collections.IVector[WinRT_String]], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Foundation.Collections.IVector[WinRT_String]]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Foundation.Collections.IVector[WinRT_String]]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Foundation.Collections.IVector[WinRT_String]]]: ...
    Size = property(get_Size, None)
class FilePickerSelectedFilesArray(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]
    _classid_ = 'Windows.Storage.Pickers.FilePickerSelectedFilesArray'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile], index: UInt32) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile], value: win32more.Windows.Storage.StorageFile, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile], startIndex: UInt32, items: Annotated[SZArray[win32more.Windows.Storage.StorageFile], 'Out']) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.StorageFile]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Storage.StorageFile]: ...
    Size = property(get_Size, None)
class FileSavePicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Pickers.IFileSavePicker
    _classid_ = 'Windows.Storage.Pickers.FileSavePicker'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Storage.Pickers.FileSavePicker: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: win32more.Windows.Storage.Pickers.IFileSavePicker2) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def PickSaveFileAndContinue(self: win32more.Windows.Storage.Pickers.IFileSavePicker2) -> Void: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: win32more.Windows.Storage.Pickers.IFileSavePicker3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_EnterpriseId(self: win32more.Windows.Storage.Pickers.IFileSavePicker3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SettingsIdentifier(self: win32more.Windows.Storage.Pickers.IFileSavePicker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SettingsIdentifier(self: win32more.Windows.Storage.Pickers.IFileSavePicker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedStartLocation(self: win32more.Windows.Storage.Pickers.IFileSavePicker) -> win32more.Windows.Storage.Pickers.PickerLocationId: ...
    @winrt_mixinmethod
    def put_SuggestedStartLocation(self: win32more.Windows.Storage.Pickers.IFileSavePicker, value: win32more.Windows.Storage.Pickers.PickerLocationId) -> Void: ...
    @winrt_mixinmethod
    def get_CommitButtonText(self: win32more.Windows.Storage.Pickers.IFileSavePicker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CommitButtonText(self: win32more.Windows.Storage.Pickers.IFileSavePicker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FileTypeChoices(self: win32more.Windows.Storage.Pickers.IFileSavePicker) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_mixinmethod
    def get_DefaultFileExtension(self: win32more.Windows.Storage.Pickers.IFileSavePicker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DefaultFileExtension(self: win32more.Windows.Storage.Pickers.IFileSavePicker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedSaveFile(self: win32more.Windows.Storage.Pickers.IFileSavePicker) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def put_SuggestedSaveFile(self: win32more.Windows.Storage.Pickers.IFileSavePicker, value: win32more.Windows.Storage.StorageFile) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedFileName(self: win32more.Windows.Storage.Pickers.IFileSavePicker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SuggestedFileName(self: win32more.Windows.Storage.Pickers.IFileSavePicker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def PickSaveFileAsync(self: win32more.Windows.Storage.Pickers.IFileSavePicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Storage.Pickers.IFileSavePicker4) -> win32more.Windows.System.User: ...
    @winrt_classmethod
    def CreateForUser(cls: win32more.Windows.Storage.Pickers.IFileSavePickerStatics, user: win32more.Windows.System.User) -> win32more.Windows.Storage.Pickers.FileSavePicker: ...
    ContinuationData = property(get_ContinuationData, None)
    EnterpriseId = property(get_EnterpriseId, put_EnterpriseId)
    SettingsIdentifier = property(get_SettingsIdentifier, put_SettingsIdentifier)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    FileTypeChoices = property(get_FileTypeChoices, None)
    DefaultFileExtension = property(get_DefaultFileExtension, put_DefaultFileExtension)
    SuggestedSaveFile = property(get_SuggestedSaveFile, put_SuggestedSaveFile)
    SuggestedFileName = property(get_SuggestedFileName, put_SuggestedFileName)
    User = property(get_User, None)
class FolderPicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Pickers.IFolderPicker
    _classid_ = 'Windows.Storage.Pickers.FolderPicker'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Storage.Pickers.FolderPicker: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: win32more.Windows.Storage.Pickers.IFolderPicker2) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def PickFolderAndContinue(self: win32more.Windows.Storage.Pickers.IFolderPicker2) -> Void: ...
    @winrt_mixinmethod
    def get_ViewMode(self: win32more.Windows.Storage.Pickers.IFolderPicker) -> win32more.Windows.Storage.Pickers.PickerViewMode: ...
    @winrt_mixinmethod
    def put_ViewMode(self: win32more.Windows.Storage.Pickers.IFolderPicker, value: win32more.Windows.Storage.Pickers.PickerViewMode) -> Void: ...
    @winrt_mixinmethod
    def get_SettingsIdentifier(self: win32more.Windows.Storage.Pickers.IFolderPicker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SettingsIdentifier(self: win32more.Windows.Storage.Pickers.IFolderPicker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedStartLocation(self: win32more.Windows.Storage.Pickers.IFolderPicker) -> win32more.Windows.Storage.Pickers.PickerLocationId: ...
    @winrt_mixinmethod
    def put_SuggestedStartLocation(self: win32more.Windows.Storage.Pickers.IFolderPicker, value: win32more.Windows.Storage.Pickers.PickerLocationId) -> Void: ...
    @winrt_mixinmethod
    def get_CommitButtonText(self: win32more.Windows.Storage.Pickers.IFolderPicker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CommitButtonText(self: win32more.Windows.Storage.Pickers.IFolderPicker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FileTypeFilter(self: win32more.Windows.Storage.Pickers.IFolderPicker) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def PickSingleFolderAsync(self: win32more.Windows.Storage.Pickers.IFolderPicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Storage.Pickers.IFolderPicker3) -> win32more.Windows.System.User: ...
    @winrt_classmethod
    def CreateForUser(cls: win32more.Windows.Storage.Pickers.IFolderPickerStatics, user: win32more.Windows.System.User) -> win32more.Windows.Storage.Pickers.FolderPicker: ...
    ContinuationData = property(get_ContinuationData, None)
    ViewMode = property(get_ViewMode, put_ViewMode)
    SettingsIdentifier = property(get_SettingsIdentifier, put_SettingsIdentifier)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    FileTypeFilter = property(get_FileTypeFilter, None)
    User = property(get_User, None)
class IFileOpenPicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.IFileOpenPicker'
    _iid_ = Guid('{2ca8278a-12c5-4c5f-8977-94547793c241}')
    @winrt_commethod(6)
    def get_ViewMode(self) -> win32more.Windows.Storage.Pickers.PickerViewMode: ...
    @winrt_commethod(7)
    def put_ViewMode(self, value: win32more.Windows.Storage.Pickers.PickerViewMode) -> Void: ...
    @winrt_commethod(8)
    def get_SettingsIdentifier(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_SettingsIdentifier(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_SuggestedStartLocation(self) -> win32more.Windows.Storage.Pickers.PickerLocationId: ...
    @winrt_commethod(11)
    def put_SuggestedStartLocation(self, value: win32more.Windows.Storage.Pickers.PickerLocationId) -> Void: ...
    @winrt_commethod(12)
    def get_CommitButtonText(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_CommitButtonText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_FileTypeFilter(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(15)
    def PickSingleFileAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(16)
    def PickMultipleFilesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]]: ...
    ViewMode = property(get_ViewMode, put_ViewMode)
    SettingsIdentifier = property(get_SettingsIdentifier, put_SettingsIdentifier)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    FileTypeFilter = property(get_FileTypeFilter, None)
class IFileOpenPicker2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.IFileOpenPicker2'
    _iid_ = Guid('{8ceb6cd2-b446-46f7-b265-90f8e55ad650}')
    @winrt_commethod(6)
    def get_ContinuationData(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(7)
    def PickSingleFileAndContinue(self) -> Void: ...
    @winrt_commethod(8)
    def PickMultipleFilesAndContinue(self) -> Void: ...
    ContinuationData = property(get_ContinuationData, None)
class IFileOpenPicker3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.IFileOpenPicker3'
    _iid_ = Guid('{d9a5c5b3-c5dc-5b98-bd80-a8d0ca0584d8}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IFileOpenPickerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.IFileOpenPickerStatics'
    _iid_ = Guid('{6821573b-2f02-4833-96d4-abbfad72b67b}')
    @winrt_commethod(6)
    def ResumePickSingleFileAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
class IFileOpenPickerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.IFileOpenPickerStatics2'
    _iid_ = Guid('{e8917415-eddd-5c98-b6f3-366fdfcad392}')
    @winrt_commethod(6)
    def CreateForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Storage.Pickers.FileOpenPicker: ...
class IFileOpenPickerWithOperationId(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.IFileOpenPickerWithOperationId'
    _iid_ = Guid('{3f57b569-2522-4ca5-aa73-a15509f1fcbf}')
    @winrt_commethod(6)
    def PickSingleFileAsync(self, pickerOperationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
class IFileSavePicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.IFileSavePicker'
    _iid_ = Guid('{3286ffcb-617f-4cc5-af6a-b3fdf29ad145}')
    @winrt_commethod(6)
    def get_SettingsIdentifier(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_SettingsIdentifier(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_SuggestedStartLocation(self) -> win32more.Windows.Storage.Pickers.PickerLocationId: ...
    @winrt_commethod(9)
    def put_SuggestedStartLocation(self, value: win32more.Windows.Storage.Pickers.PickerLocationId) -> Void: ...
    @winrt_commethod(10)
    def get_CommitButtonText(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_CommitButtonText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_FileTypeChoices(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_commethod(13)
    def get_DefaultFileExtension(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_DefaultFileExtension(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_SuggestedSaveFile(self) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_commethod(16)
    def put_SuggestedSaveFile(self, value: win32more.Windows.Storage.StorageFile) -> Void: ...
    @winrt_commethod(17)
    def get_SuggestedFileName(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def put_SuggestedFileName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(19)
    def PickSaveFileAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    SettingsIdentifier = property(get_SettingsIdentifier, put_SettingsIdentifier)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    FileTypeChoices = property(get_FileTypeChoices, None)
    DefaultFileExtension = property(get_DefaultFileExtension, put_DefaultFileExtension)
    SuggestedSaveFile = property(get_SuggestedSaveFile, put_SuggestedSaveFile)
    SuggestedFileName = property(get_SuggestedFileName, put_SuggestedFileName)
class IFileSavePicker2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.IFileSavePicker2'
    _iid_ = Guid('{0ec313a2-d24b-449a-8197-e89104fd42cc}')
    @winrt_commethod(6)
    def get_ContinuationData(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(7)
    def PickSaveFileAndContinue(self) -> Void: ...
    ContinuationData = property(get_ContinuationData, None)
class IFileSavePicker3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.IFileSavePicker3'
    _iid_ = Guid('{698aec69-ba3c-4e51-bd90-4abcbbf4cfaf}')
    @winrt_commethod(6)
    def get_EnterpriseId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_EnterpriseId(self, value: WinRT_String) -> Void: ...
    EnterpriseId = property(get_EnterpriseId, put_EnterpriseId)
class IFileSavePicker4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.IFileSavePicker4'
    _iid_ = Guid('{e7d83a5a-ddfa-5de0-8b70-c842c21988ec}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IFileSavePickerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.IFileSavePickerStatics'
    _iid_ = Guid('{28e3cf9e-961c-5e2c-aed7-e64737f4ce37}')
    @winrt_commethod(6)
    def CreateForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Storage.Pickers.FileSavePicker: ...
class IFolderPicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.IFolderPicker'
    _iid_ = Guid('{084f7799-f3fb-400a-99b1-7b4a772fd60d}')
    @winrt_commethod(6)
    def get_ViewMode(self) -> win32more.Windows.Storage.Pickers.PickerViewMode: ...
    @winrt_commethod(7)
    def put_ViewMode(self, value: win32more.Windows.Storage.Pickers.PickerViewMode) -> Void: ...
    @winrt_commethod(8)
    def get_SettingsIdentifier(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_SettingsIdentifier(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_SuggestedStartLocation(self) -> win32more.Windows.Storage.Pickers.PickerLocationId: ...
    @winrt_commethod(11)
    def put_SuggestedStartLocation(self, value: win32more.Windows.Storage.Pickers.PickerLocationId) -> Void: ...
    @winrt_commethod(12)
    def get_CommitButtonText(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_CommitButtonText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_FileTypeFilter(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(15)
    def PickSingleFolderAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    ViewMode = property(get_ViewMode, put_ViewMode)
    SettingsIdentifier = property(get_SettingsIdentifier, put_SettingsIdentifier)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    FileTypeFilter = property(get_FileTypeFilter, None)
class IFolderPicker2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.IFolderPicker2'
    _iid_ = Guid('{8eb3ba97-dc85-4616-be94-9660881f2f5d}')
    @winrt_commethod(6)
    def get_ContinuationData(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(7)
    def PickFolderAndContinue(self) -> Void: ...
    ContinuationData = property(get_ContinuationData, None)
class IFolderPicker3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.IFolderPicker3'
    _iid_ = Guid('{673b1e29-d326-53c0-bd24-a25c714cee36}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IFolderPickerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.IFolderPickerStatics'
    _iid_ = Guid('{9be34740-7ca1-5942-a3c8-46f2551ecff3}')
    @winrt_commethod(6)
    def CreateForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Storage.Pickers.FolderPicker: ...
PickerLocationId = Int32
PickerLocationId_DocumentsLibrary: PickerLocationId = 0
PickerLocationId_ComputerFolder: PickerLocationId = 1
PickerLocationId_Desktop: PickerLocationId = 2
PickerLocationId_Downloads: PickerLocationId = 3
PickerLocationId_HomeGroup: PickerLocationId = 4
PickerLocationId_MusicLibrary: PickerLocationId = 5
PickerLocationId_PicturesLibrary: PickerLocationId = 6
PickerLocationId_VideosLibrary: PickerLocationId = 7
PickerLocationId_Objects3D: PickerLocationId = 8
PickerLocationId_Unspecified: PickerLocationId = 9
PickerViewMode = Int32
PickerViewMode_List: PickerViewMode = 0
PickerViewMode_Thumbnail: PickerViewMode = 1
make_head(_module, 'FileExtensionVector')
make_head(_module, 'FileOpenPicker')
make_head(_module, 'FilePickerFileTypesOrderedMap')
make_head(_module, 'FilePickerSelectedFilesArray')
make_head(_module, 'FileSavePicker')
make_head(_module, 'FolderPicker')
make_head(_module, 'IFileOpenPicker')
make_head(_module, 'IFileOpenPicker2')
make_head(_module, 'IFileOpenPicker3')
make_head(_module, 'IFileOpenPickerStatics')
make_head(_module, 'IFileOpenPickerStatics2')
make_head(_module, 'IFileOpenPickerWithOperationId')
make_head(_module, 'IFileSavePicker')
make_head(_module, 'IFileSavePicker2')
make_head(_module, 'IFileSavePicker3')
make_head(_module, 'IFileSavePicker4')
make_head(_module, 'IFileSavePickerStatics')
make_head(_module, 'IFolderPicker')
make_head(_module, 'IFolderPicker2')
make_head(_module, 'IFolderPicker3')
make_head(_module, 'IFolderPickerStatics')