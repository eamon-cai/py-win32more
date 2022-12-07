from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.NetworkManagement.Multicast
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
MCAST_CLIENT_ID_LEN: UInt32 = 17
MCAST_API_CURRENT_VERSION: Int32 = 1
MCAST_API_VERSION_0: Int32 = 0
MCAST_API_VERSION_1: Int32 = 1
@winfunctype('dhcpcsvc.dll')
def McastApiStartup(Version: POINTER(UInt32)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def McastApiCleanup() -> Void: ...
@winfunctype('dhcpcsvc.dll')
def McastGenUID(pRequestID: POINTER(win32more.NetworkManagement.Multicast.MCAST_CLIENT_UID_head)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def McastEnumerateScopes(AddrFamily: UInt16, ReQuery: win32more.Foundation.BOOL, pScopeList: POINTER(win32more.NetworkManagement.Multicast.MCAST_SCOPE_ENTRY_head), pScopeLen: POINTER(UInt32), pScopeCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def McastRequestAddress(AddrFamily: UInt16, pRequestID: POINTER(win32more.NetworkManagement.Multicast.MCAST_CLIENT_UID_head), pScopeCtx: POINTER(win32more.NetworkManagement.Multicast.MCAST_SCOPE_CTX_head), pAddrRequest: POINTER(win32more.NetworkManagement.Multicast.MCAST_LEASE_REQUEST_head), pAddrResponse: POINTER(win32more.NetworkManagement.Multicast.MCAST_LEASE_RESPONSE_head)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def McastRenewAddress(AddrFamily: UInt16, pRequestID: POINTER(win32more.NetworkManagement.Multicast.MCAST_CLIENT_UID_head), pRenewRequest: POINTER(win32more.NetworkManagement.Multicast.MCAST_LEASE_REQUEST_head), pRenewResponse: POINTER(win32more.NetworkManagement.Multicast.MCAST_LEASE_RESPONSE_head)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def McastReleaseAddress(AddrFamily: UInt16, pRequestID: POINTER(win32more.NetworkManagement.Multicast.MCAST_CLIENT_UID_head), pReleaseRequest: POINTER(win32more.NetworkManagement.Multicast.MCAST_LEASE_REQUEST_head)) -> UInt32: ...
class IPNG_ADDRESS(Union):
    IpAddrV4: UInt32
    IpAddrV6: Byte * 16
class MCAST_CLIENT_UID(Structure):
    ClientUID: c_char_p_no
    ClientUIDLength: UInt32
class MCAST_LEASE_REQUEST(Structure):
    LeaseStartTime: Int32
    MaxLeaseStartTime: Int32
    LeaseDuration: UInt32
    MinLeaseDuration: UInt32
    ServerAddress: win32more.NetworkManagement.Multicast.IPNG_ADDRESS
    MinAddrCount: UInt16
    AddrCount: UInt16
    pAddrBuf: c_char_p_no
class MCAST_LEASE_RESPONSE(Structure):
    LeaseStartTime: Int32
    LeaseEndTime: Int32
    ServerAddress: win32more.NetworkManagement.Multicast.IPNG_ADDRESS
    AddrCount: UInt16
    pAddrBuf: c_char_p_no
class MCAST_SCOPE_CTX(Structure):
    ScopeID: win32more.NetworkManagement.Multicast.IPNG_ADDRESS
    Interface: win32more.NetworkManagement.Multicast.IPNG_ADDRESS
    ServerID: win32more.NetworkManagement.Multicast.IPNG_ADDRESS
class MCAST_SCOPE_ENTRY(Structure):
    ScopeCtx: win32more.NetworkManagement.Multicast.MCAST_SCOPE_CTX
    LastAddr: win32more.NetworkManagement.Multicast.IPNG_ADDRESS
    TTL: UInt32
    ScopeDesc: win32more.Foundation.UNICODE_STRING
make_head(_module, 'IPNG_ADDRESS')
make_head(_module, 'MCAST_CLIENT_UID')
make_head(_module, 'MCAST_LEASE_REQUEST')
make_head(_module, 'MCAST_LEASE_RESPONSE')
make_head(_module, 'MCAST_SCOPE_CTX')
make_head(_module, 'MCAST_SCOPE_ENTRY')
__all__ = [
    "IPNG_ADDRESS",
    "MCAST_API_CURRENT_VERSION",
    "MCAST_API_VERSION_0",
    "MCAST_API_VERSION_1",
    "MCAST_CLIENT_ID_LEN",
    "MCAST_CLIENT_UID",
    "MCAST_LEASE_REQUEST",
    "MCAST_LEASE_RESPONSE",
    "MCAST_SCOPE_CTX",
    "MCAST_SCOPE_ENTRY",
    "McastApiCleanup",
    "McastApiStartup",
    "McastEnumerateScopes",
    "McastGenUID",
    "McastReleaseAddress",
    "McastRenewAddress",
    "McastRequestAddress",
]
