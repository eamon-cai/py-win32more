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
import Windows.Devices.Geolocation
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Globalization
import Windows.Services.Maps
import Windows.Services.Maps.LocalSearch
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ILocalCategoriesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics'
    _iid_ = Guid('{f49399f5-8261-4321-9974-ef92d49a8dca}')
    @winrt_commethod(6)
    def get_BankAndCreditUnions(self: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EatDrink(self: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Hospitals(self: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_HotelsAndMotels(self: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_All(self: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Parking(self: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_SeeDo(self: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Shop(self: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    BankAndCreditUnions = property(get_BankAndCreditUnions, None)
    EatDrink = property(get_EatDrink, None)
    Hospitals = property(get_Hospitals, None)
    HotelsAndMotels = property(get_HotelsAndMotels, None)
    All = property(get_All, None)
    Parking = property(get_Parking, None)
    SeeDo = property(get_SeeDo, None)
    Shop = property(get_Shop, None)
class ILocalLocation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.ILocalLocation'
    _iid_ = Guid('{bb0fe9ab-4502-4f2c-94a9-0d60de0e2163}')
    @winrt_commethod(6)
    def get_Address(self: Windows.Services.Maps.LocalSearch.ILocalLocation) -> Windows.Services.Maps.MapAddress: ...
    @winrt_commethod(7)
    def get_Identifier(self: Windows.Services.Maps.LocalSearch.ILocalLocation) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Description(self: Windows.Services.Maps.LocalSearch.ILocalLocation) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DisplayName(self: Windows.Services.Maps.LocalSearch.ILocalLocation) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Point(self: Windows.Services.Maps.LocalSearch.ILocalLocation) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(11)
    def get_PhoneNumber(self: Windows.Services.Maps.LocalSearch.ILocalLocation) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_DataAttribution(self: Windows.Services.Maps.LocalSearch.ILocalLocation) -> WinRT_String: ...
    Address = property(get_Address, None)
    Identifier = property(get_Identifier, None)
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Point = property(get_Point, None)
    PhoneNumber = property(get_PhoneNumber, None)
    DataAttribution = property(get_DataAttribution, None)
class ILocalLocation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.ILocalLocation2'
    _iid_ = Guid('{6e9e307c-ecb5-4ffc-bb8c-ba50ba8c2dc6}')
    @winrt_commethod(6)
    def get_Category(self: Windows.Services.Maps.LocalSearch.ILocalLocation2) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_RatingInfo(self: Windows.Services.Maps.LocalSearch.ILocalLocation2) -> Windows.Services.Maps.LocalSearch.LocalLocationRatingInfo: ...
    @winrt_commethod(8)
    def get_HoursOfOperation(self: Windows.Services.Maps.LocalSearch.ILocalLocation2) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.LocalSearch.LocalLocationHoursOfOperationItem]: ...
    Category = property(get_Category, None)
    RatingInfo = property(get_RatingInfo, None)
    HoursOfOperation = property(get_HoursOfOperation, None)
class ILocalLocationFinderResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.ILocalLocationFinderResult'
    _iid_ = Guid('{d09b6cc6-f338-4191-9fd8-5440b9a68f52}')
    @winrt_commethod(6)
    def get_LocalLocations(self: Windows.Services.Maps.LocalSearch.ILocalLocationFinderResult) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    @winrt_commethod(7)
    def get_Status(self: Windows.Services.Maps.LocalSearch.ILocalLocationFinderResult) -> Windows.Services.Maps.LocalSearch.LocalLocationFinderStatus: ...
    LocalLocations = property(get_LocalLocations, None)
    Status = property(get_Status, None)
class ILocalLocationFinderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.ILocalLocationFinderStatics'
    _iid_ = Guid('{d2ef7344-a0de-48ca-81a8-07c7dcfd37ab}')
    @winrt_commethod(6)
    def FindLocalLocationsAsync(self: Windows.Services.Maps.LocalSearch.ILocalLocationFinderStatics, searchTerm: WinRT_String, searchArea: Windows.Devices.Geolocation.Geocircle, localCategory: WinRT_String, maxResults: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.LocalSearch.LocalLocationFinderResult]: ...
class ILocalLocationHoursOfOperationItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.ILocalLocationHoursOfOperationItem'
    _iid_ = Guid('{23548c72-a1c7-43f1-a4f0-1091c39ec640}')
    @winrt_commethod(6)
    def get_Day(self: Windows.Services.Maps.LocalSearch.ILocalLocationHoursOfOperationItem) -> Windows.Globalization.DayOfWeek: ...
    @winrt_commethod(7)
    def get_Start(self: Windows.Services.Maps.LocalSearch.ILocalLocationHoursOfOperationItem) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_Span(self: Windows.Services.Maps.LocalSearch.ILocalLocationHoursOfOperationItem) -> Windows.Foundation.TimeSpan: ...
    Day = property(get_Day, None)
    Start = property(get_Start, None)
    Span = property(get_Span, None)
class ILocalLocationRatingInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.ILocalLocationRatingInfo'
    _iid_ = Guid('{cb1dab56-3354-4311-8bc0-a2d4d5eb806e}')
    @winrt_commethod(6)
    def get_AggregateRating(self: Windows.Services.Maps.LocalSearch.ILocalLocationRatingInfo) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(7)
    def get_RatingCount(self: Windows.Services.Maps.LocalSearch.ILocalLocationRatingInfo) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_ProviderIdentifier(self: Windows.Services.Maps.LocalSearch.ILocalLocationRatingInfo) -> WinRT_String: ...
    AggregateRating = property(get_AggregateRating, None)
    RatingCount = property(get_RatingCount, None)
    ProviderIdentifier = property(get_ProviderIdentifier, None)
class IPlaceInfoHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.IPlaceInfoHelperStatics'
    _iid_ = Guid('{dd1ca9a7-a9c6-491b-bc09-e80fcea48ee6}')
    @winrt_commethod(6)
    def CreateFromLocalLocation(self: Windows.Services.Maps.LocalSearch.IPlaceInfoHelperStatics, location: Windows.Services.Maps.LocalSearch.LocalLocation) -> Windows.Services.Maps.PlaceInfo: ...
class _LocalCategories_Meta_(ComPtr.__class__):
    pass
class LocalCategories(ComPtr, metaclass=_LocalCategories_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.LocalCategories'
    @winrt_classmethod
    def get_BankAndCreditUnions(cls: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_EatDrink(cls: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Hospitals(cls: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HotelsAndMotels(cls: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_All(cls: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Parking(cls: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SeeDo(cls: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Shop(cls: Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    _LocalCategories_Meta_.BankAndCreditUnions = property(get_BankAndCreditUnions.__wrapped__, None)
    _LocalCategories_Meta_.EatDrink = property(get_EatDrink.__wrapped__, None)
    _LocalCategories_Meta_.Hospitals = property(get_Hospitals.__wrapped__, None)
    _LocalCategories_Meta_.HotelsAndMotels = property(get_HotelsAndMotels.__wrapped__, None)
    _LocalCategories_Meta_.All = property(get_All.__wrapped__, None)
    _LocalCategories_Meta_.Parking = property(get_Parking.__wrapped__, None)
    _LocalCategories_Meta_.SeeDo = property(get_SeeDo.__wrapped__, None)
    _LocalCategories_Meta_.Shop = property(get_Shop.__wrapped__, None)
class LocalLocation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Services.Maps.LocalSearch.ILocalLocation
    _classid_ = 'Windows.Services.Maps.LocalSearch.LocalLocation'
    @winrt_mixinmethod
    def get_Address(self: Windows.Services.Maps.LocalSearch.ILocalLocation) -> Windows.Services.Maps.MapAddress: ...
    @winrt_mixinmethod
    def get_Identifier(self: Windows.Services.Maps.LocalSearch.ILocalLocation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Services.Maps.LocalSearch.ILocalLocation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Services.Maps.LocalSearch.ILocalLocation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Point(self: Windows.Services.Maps.LocalSearch.ILocalLocation) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_PhoneNumber(self: Windows.Services.Maps.LocalSearch.ILocalLocation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DataAttribution(self: Windows.Services.Maps.LocalSearch.ILocalLocation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Category(self: Windows.Services.Maps.LocalSearch.ILocalLocation2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RatingInfo(self: Windows.Services.Maps.LocalSearch.ILocalLocation2) -> Windows.Services.Maps.LocalSearch.LocalLocationRatingInfo: ...
    @winrt_mixinmethod
    def get_HoursOfOperation(self: Windows.Services.Maps.LocalSearch.ILocalLocation2) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.LocalSearch.LocalLocationHoursOfOperationItem]: ...
    Address = property(get_Address, None)
    Identifier = property(get_Identifier, None)
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Point = property(get_Point, None)
    PhoneNumber = property(get_PhoneNumber, None)
    DataAttribution = property(get_DataAttribution, None)
    Category = property(get_Category, None)
    RatingInfo = property(get_RatingInfo, None)
    HoursOfOperation = property(get_HoursOfOperation, None)
class LocalLocationFinder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.LocalLocationFinder'
    @winrt_classmethod
    def FindLocalLocationsAsync(cls: Windows.Services.Maps.LocalSearch.ILocalLocationFinderStatics, searchTerm: WinRT_String, searchArea: Windows.Devices.Geolocation.Geocircle, localCategory: WinRT_String, maxResults: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.LocalSearch.LocalLocationFinderResult]: ...
class LocalLocationFinderResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Services.Maps.LocalSearch.ILocalLocationFinderResult
    _classid_ = 'Windows.Services.Maps.LocalSearch.LocalLocationFinderResult'
    @winrt_mixinmethod
    def get_LocalLocations(self: Windows.Services.Maps.LocalSearch.ILocalLocationFinderResult) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Services.Maps.LocalSearch.ILocalLocationFinderResult) -> Windows.Services.Maps.LocalSearch.LocalLocationFinderStatus: ...
    LocalLocations = property(get_LocalLocations, None)
    Status = property(get_Status, None)
LocalLocationFinderStatus = Int32
LocalLocationFinderStatus_Success: LocalLocationFinderStatus = 0
LocalLocationFinderStatus_UnknownError: LocalLocationFinderStatus = 1
LocalLocationFinderStatus_InvalidCredentials: LocalLocationFinderStatus = 2
LocalLocationFinderStatus_InvalidCategory: LocalLocationFinderStatus = 3
LocalLocationFinderStatus_InvalidSearchTerm: LocalLocationFinderStatus = 4
LocalLocationFinderStatus_InvalidSearchArea: LocalLocationFinderStatus = 5
LocalLocationFinderStatus_NetworkFailure: LocalLocationFinderStatus = 6
LocalLocationFinderStatus_NotSupported: LocalLocationFinderStatus = 7
class LocalLocationHoursOfOperationItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Services.Maps.LocalSearch.ILocalLocationHoursOfOperationItem
    _classid_ = 'Windows.Services.Maps.LocalSearch.LocalLocationHoursOfOperationItem'
    @winrt_mixinmethod
    def get_Day(self: Windows.Services.Maps.LocalSearch.ILocalLocationHoursOfOperationItem) -> Windows.Globalization.DayOfWeek: ...
    @winrt_mixinmethod
    def get_Start(self: Windows.Services.Maps.LocalSearch.ILocalLocationHoursOfOperationItem) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Span(self: Windows.Services.Maps.LocalSearch.ILocalLocationHoursOfOperationItem) -> Windows.Foundation.TimeSpan: ...
    Day = property(get_Day, None)
    Start = property(get_Start, None)
    Span = property(get_Span, None)
class LocalLocationRatingInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Services.Maps.LocalSearch.ILocalLocationRatingInfo
    _classid_ = 'Windows.Services.Maps.LocalSearch.LocalLocationRatingInfo'
    @winrt_mixinmethod
    def get_AggregateRating(self: Windows.Services.Maps.LocalSearch.ILocalLocationRatingInfo) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_RatingCount(self: Windows.Services.Maps.LocalSearch.ILocalLocationRatingInfo) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ProviderIdentifier(self: Windows.Services.Maps.LocalSearch.ILocalLocationRatingInfo) -> WinRT_String: ...
    AggregateRating = property(get_AggregateRating, None)
    RatingCount = property(get_RatingCount, None)
    ProviderIdentifier = property(get_ProviderIdentifier, None)
class PlaceInfoHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.PlaceInfoHelper'
    @winrt_classmethod
    def CreateFromLocalLocation(cls: Windows.Services.Maps.LocalSearch.IPlaceInfoHelperStatics, location: Windows.Services.Maps.LocalSearch.LocalLocation) -> Windows.Services.Maps.PlaceInfo: ...
make_head(_module, 'ILocalCategoriesStatics')
make_head(_module, 'ILocalLocation')
make_head(_module, 'ILocalLocation2')
make_head(_module, 'ILocalLocationFinderResult')
make_head(_module, 'ILocalLocationFinderStatics')
make_head(_module, 'ILocalLocationHoursOfOperationItem')
make_head(_module, 'ILocalLocationRatingInfo')
make_head(_module, 'IPlaceInfoHelperStatics')
make_head(_module, 'LocalCategories')
make_head(_module, 'LocalLocation')
make_head(_module, 'LocalLocationFinder')
make_head(_module, 'LocalLocationFinderResult')
make_head(_module, 'LocalLocationHoursOfOperationItem')
make_head(_module, 'LocalLocationRatingInfo')
make_head(_module, 'PlaceInfoHelper')
