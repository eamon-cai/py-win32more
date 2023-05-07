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
import Windows.ApplicationModel
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Management.Deployment
import Windows.Phone.Management.Deployment
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class Enterprise(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Phone.Management.Deployment.IEnterprise
    _classid_ = 'Windows.Phone.Management.Deployment.Enterprise'
    @winrt_mixinmethod
    def get_Id(self: Windows.Phone.Management.Deployment.IEnterprise) -> Guid: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Phone.Management.Deployment.IEnterprise) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WorkplaceId(self: Windows.Phone.Management.Deployment.IEnterprise) -> Int32: ...
    @winrt_mixinmethod
    def get_EnrollmentValidFrom(self: Windows.Phone.Management.Deployment.IEnterprise) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_EnrollmentValidTo(self: Windows.Phone.Management.Deployment.IEnterprise) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Phone.Management.Deployment.IEnterprise) -> Windows.Phone.Management.Deployment.EnterpriseStatus: ...
    Id = property(get_Id, None)
    Name = property(get_Name, None)
    WorkplaceId = property(get_WorkplaceId, None)
    EnrollmentValidFrom = property(get_EnrollmentValidFrom, None)
    EnrollmentValidTo = property(get_EnrollmentValidTo, None)
    Status = property(get_Status, None)
class _EnterpriseEnrollmentManager_Meta_(ComPtr.__class__):
    pass
class EnterpriseEnrollmentManager(ComPtr, metaclass=_EnterpriseEnrollmentManager_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.EnterpriseEnrollmentManager'
    @winrt_classmethod
    def get_EnrolledEnterprises(cls: Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager) -> Windows.Foundation.Collections.IVectorView[Windows.Phone.Management.Deployment.Enterprise]: ...
    @winrt_classmethod
    def get_CurrentEnterprise(cls: Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager) -> Windows.Phone.Management.Deployment.Enterprise: ...
    @winrt_classmethod
    def ValidateEnterprisesAsync(cls: Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def RequestEnrollmentAsync(cls: Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager, enrollmentToken: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Phone.Management.Deployment.EnterpriseEnrollmentResult]: ...
    @winrt_classmethod
    def RequestUnenrollmentAsync(cls: Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager, enterprise: Windows.Phone.Management.Deployment.Enterprise) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    _EnterpriseEnrollmentManager_Meta_.EnrolledEnterprises = property(get_EnrolledEnterprises.__wrapped__, None)
    _EnterpriseEnrollmentManager_Meta_.CurrentEnterprise = property(get_CurrentEnterprise.__wrapped__, None)
class EnterpriseEnrollmentResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Phone.Management.Deployment.IEnterpriseEnrollmentResult
    _classid_ = 'Windows.Phone.Management.Deployment.EnterpriseEnrollmentResult'
    @winrt_mixinmethod
    def get_EnrolledEnterprise(self: Windows.Phone.Management.Deployment.IEnterpriseEnrollmentResult) -> Windows.Phone.Management.Deployment.Enterprise: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Phone.Management.Deployment.IEnterpriseEnrollmentResult) -> Windows.Phone.Management.Deployment.EnterpriseEnrollmentStatus: ...
    EnrolledEnterprise = property(get_EnrolledEnterprise, None)
    Status = property(get_Status, None)
EnterpriseEnrollmentStatus = Int32
EnterpriseEnrollmentStatus_Success: EnterpriseEnrollmentStatus = 0
EnterpriseEnrollmentStatus_CancelledByUser: EnterpriseEnrollmentStatus = 1
EnterpriseEnrollmentStatus_UnknownFailure: EnterpriseEnrollmentStatus = 2
EnterpriseStatus = Int32
EnterpriseStatus_Enrolled: EnterpriseStatus = 0
EnterpriseStatus_Disabled: EnterpriseStatus = 1
EnterpriseStatus_Revoked: EnterpriseStatus = 2
EnterpriseStatus_Expired: EnterpriseStatus = 3
class IEnterprise(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.IEnterprise'
    _iid_ = Guid('{96592f8d-856c-4426-a947-b06307718078}')
    @winrt_commethod(6)
    def get_Id(self: Windows.Phone.Management.Deployment.IEnterprise) -> Guid: ...
    @winrt_commethod(7)
    def get_Name(self: Windows.Phone.Management.Deployment.IEnterprise) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_WorkplaceId(self: Windows.Phone.Management.Deployment.IEnterprise) -> Int32: ...
    @winrt_commethod(9)
    def get_EnrollmentValidFrom(self: Windows.Phone.Management.Deployment.IEnterprise) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def get_EnrollmentValidTo(self: Windows.Phone.Management.Deployment.IEnterprise) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(11)
    def get_Status(self: Windows.Phone.Management.Deployment.IEnterprise) -> Windows.Phone.Management.Deployment.EnterpriseStatus: ...
    Id = property(get_Id, None)
    Name = property(get_Name, None)
    WorkplaceId = property(get_WorkplaceId, None)
    EnrollmentValidFrom = property(get_EnrollmentValidFrom, None)
    EnrollmentValidTo = property(get_EnrollmentValidTo, None)
    Status = property(get_Status, None)
class IEnterpriseEnrollmentManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager'
    _iid_ = Guid('{20f9f390-2c69-41d8-88e6-e4b3884026cb}')
    @winrt_commethod(6)
    def get_EnrolledEnterprises(self: Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager) -> Windows.Foundation.Collections.IVectorView[Windows.Phone.Management.Deployment.Enterprise]: ...
    @winrt_commethod(7)
    def get_CurrentEnterprise(self: Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager) -> Windows.Phone.Management.Deployment.Enterprise: ...
    @winrt_commethod(8)
    def ValidateEnterprisesAsync(self: Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def RequestEnrollmentAsync(self: Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager, enrollmentToken: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Phone.Management.Deployment.EnterpriseEnrollmentResult]: ...
    @winrt_commethod(10)
    def RequestUnenrollmentAsync(self: Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager, enterprise: Windows.Phone.Management.Deployment.Enterprise) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    EnrolledEnterprises = property(get_EnrolledEnterprises, None)
    CurrentEnterprise = property(get_CurrentEnterprise, None)
class IEnterpriseEnrollmentResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.IEnterpriseEnrollmentResult'
    _iid_ = Guid('{9ff71ce6-90db-4342-b326-1729aa91301c}')
    @winrt_commethod(6)
    def get_EnrolledEnterprise(self: Windows.Phone.Management.Deployment.IEnterpriseEnrollmentResult) -> Windows.Phone.Management.Deployment.Enterprise: ...
    @winrt_commethod(7)
    def get_Status(self: Windows.Phone.Management.Deployment.IEnterpriseEnrollmentResult) -> Windows.Phone.Management.Deployment.EnterpriseEnrollmentStatus: ...
    EnrolledEnterprise = property(get_EnrolledEnterprise, None)
    Status = property(get_Status, None)
class IInstallationManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.IInstallationManagerStatics'
    _iid_ = Guid('{929aa738-8d49-42ac-80c9-b4ad793c43f2}')
    @winrt_commethod(6)
    def AddPackageAsync(self: Windows.Phone.Management.Deployment.IInstallationManagerStatics, title: WinRT_String, sourceLocation: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_commethod(7)
    def AddPackagePreloadedAsync(self: Windows.Phone.Management.Deployment.IInstallationManagerStatics, title: WinRT_String, sourceLocation: Windows.Foundation.Uri, instanceId: WinRT_String, offerId: WinRT_String, license: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_commethod(8)
    def GetPendingPackageInstalls(self: Windows.Phone.Management.Deployment.IInstallationManagerStatics) -> Windows.Foundation.Collections.IIterable[Windows.Foundation.IAsyncOperationWithProgress[Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]]: ...
    @winrt_commethod(9)
    def FindPackagesForCurrentPublisher(self: Windows.Phone.Management.Deployment.IInstallationManagerStatics) -> Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Package]: ...
    @winrt_commethod(10)
    def FindPackages(self: Windows.Phone.Management.Deployment.IInstallationManagerStatics) -> Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Package]: ...
class IInstallationManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.IInstallationManagerStatics2'
    _iid_ = Guid('{7c6c2cbd-fa4a-4c8e-ab97-d959452f19e5}')
    @winrt_commethod(6)
    def RemovePackageAsync(self: Windows.Phone.Management.Deployment.IInstallationManagerStatics2, packageFullName: WinRT_String, removalOptions: Windows.Management.Deployment.RemovalOptions) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_commethod(7)
    def RegisterPackageAsync(self: Windows.Phone.Management.Deployment.IInstallationManagerStatics2, manifestUri: Windows.Foundation.Uri, dependencyPackageUris: Windows.Foundation.Collections.IIterable[Windows.Foundation.Uri], deploymentOptions: Windows.Management.Deployment.DeploymentOptions) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_commethod(8)
    def FindPackagesByNamePublisher(self: Windows.Phone.Management.Deployment.IInstallationManagerStatics2, packageName: WinRT_String, packagePublisher: WinRT_String) -> Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Package]: ...
class IPackageInstallResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.IPackageInstallResult'
    _iid_ = Guid('{33e8eed5-0f7e-4473-967c-7d6e1c0e7de1}')
    @winrt_commethod(6)
    def get_ProductId(self: Windows.Phone.Management.Deployment.IPackageInstallResult) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_InstallState(self: Windows.Phone.Management.Deployment.IPackageInstallResult) -> Windows.Management.Deployment.PackageInstallState: ...
    ProductId = property(get_ProductId, None)
    InstallState = property(get_InstallState, None)
class IPackageInstallResult2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.IPackageInstallResult2'
    _iid_ = Guid('{7149d909-3ff9-41ed-a717-2bc65ffc61d2}')
    @winrt_commethod(6)
    def get_ErrorText(self: Windows.Phone.Management.Deployment.IPackageInstallResult2) -> WinRT_String: ...
    ErrorText = property(get_ErrorText, None)
class InstallationManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.InstallationManager'
    @winrt_classmethod
    def RemovePackageAsync(cls: Windows.Phone.Management.Deployment.IInstallationManagerStatics2, packageFullName: WinRT_String, removalOptions: Windows.Management.Deployment.RemovalOptions) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_classmethod
    def RegisterPackageAsync(cls: Windows.Phone.Management.Deployment.IInstallationManagerStatics2, manifestUri: Windows.Foundation.Uri, dependencyPackageUris: Windows.Foundation.Collections.IIterable[Windows.Foundation.Uri], deploymentOptions: Windows.Management.Deployment.DeploymentOptions) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_classmethod
    def FindPackagesByNamePublisher(cls: Windows.Phone.Management.Deployment.IInstallationManagerStatics2, packageName: WinRT_String, packagePublisher: WinRT_String) -> Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Package]: ...
    @winrt_classmethod
    def AddPackageAsync(cls: Windows.Phone.Management.Deployment.IInstallationManagerStatics, title: WinRT_String, sourceLocation: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_classmethod
    def AddPackagePreloadedAsync(cls: Windows.Phone.Management.Deployment.IInstallationManagerStatics, title: WinRT_String, sourceLocation: Windows.Foundation.Uri, instanceId: WinRT_String, offerId: WinRT_String, license: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_classmethod
    def GetPendingPackageInstalls(cls: Windows.Phone.Management.Deployment.IInstallationManagerStatics) -> Windows.Foundation.Collections.IIterable[Windows.Foundation.IAsyncOperationWithProgress[Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]]: ...
    @winrt_classmethod
    def FindPackagesForCurrentPublisher(cls: Windows.Phone.Management.Deployment.IInstallationManagerStatics) -> Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Package]: ...
    @winrt_classmethod
    def FindPackages(cls: Windows.Phone.Management.Deployment.IInstallationManagerStatics) -> Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Package]: ...
class PackageInstallResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Phone.Management.Deployment.IPackageInstallResult
    _classid_ = 'Windows.Phone.Management.Deployment.PackageInstallResult'
    @winrt_mixinmethod
    def get_ProductId(self: Windows.Phone.Management.Deployment.IPackageInstallResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InstallState(self: Windows.Phone.Management.Deployment.IPackageInstallResult) -> Windows.Management.Deployment.PackageInstallState: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Phone.Management.Deployment.IPackageInstallResult2) -> WinRT_String: ...
    ProductId = property(get_ProductId, None)
    InstallState = property(get_InstallState, None)
    ErrorText = property(get_ErrorText, None)
make_head(_module, 'Enterprise')
make_head(_module, 'EnterpriseEnrollmentManager')
make_head(_module, 'EnterpriseEnrollmentResult')
make_head(_module, 'IEnterprise')
make_head(_module, 'IEnterpriseEnrollmentManager')
make_head(_module, 'IEnterpriseEnrollmentResult')
make_head(_module, 'IInstallationManagerStatics')
make_head(_module, 'IInstallationManagerStatics2')
make_head(_module, 'IPackageInstallResult')
make_head(_module, 'IPackageInstallResult2')
make_head(_module, 'InstallationManager')
make_head(_module, 'PackageInstallResult')
