from __future__ import annotations
import types
import typing
import re
import sys
import uuid
from ctypes import c_byte, c_ubyte, c_short, c_ushort, c_int, c_uint, c_longlong, c_ulonglong, c_float, c_double, c_bool, c_wchar, c_char_p, c_wchar_p, c_void_p, Structure, Union, cdll, windll, CFUNCTYPE, WINFUNCTYPE, sizeof, POINTER, cast, pointer, Array, WinError, wstring_at
from importlib import import_module
from typing import TypeVar, Generic, _GenericAlias

T = TypeVar("T")

if "(arm64)" in sys.version.lower():
    ARCH = "ARM64"
elif "(amd64)" in sys.version.lower():
    ARCH = "X64"
else:
    ARCH = "X86"

MissingType = c_void_p

# to avoid auto conversion to str
class c_char_p_no(c_char_p):
    pass

class c_wchar_p_no(c_wchar_p):
    pass

Byte = c_ubyte
SByte = c_byte
Char = c_wchar
Int16 = c_short
UInt16 = c_ushort
Int32 = c_int
UInt32 = c_uint
Int64 = c_longlong
UInt64 = c_ulonglong
if sizeof(c_void_p) == sizeof(Int64):
    IntPtr = Int64
    UIntPtr = UInt64
elif sizeof(c_void_p) == sizeof(Int32):
    IntPtr = Int32
    UIntPtr = UInt32
else:
    raise NotImplementedError()
Single = c_float
Double = c_double
String = c_wchar_p_no
Boolean = c_bool
Void = None

class WinRT_String(IntPtr):  # HSTRING
    def __del__(self):
        import Windows.Win32.System.WinRT
        if self:
            hr = Windows.Win32.System.WinRT.WindowsDeleteString(self)
            if FAILED(hr):
                raise WinError(hr)

    @classmethod
    def from_param(cls, obj):
        import Windows.Win32.System.WinRT
        if isinstance(obj, str):
            pass
        elif isinstance(obj, String):
            obj = obj.value
        else:
            raise TypeError()
        value = cls()
        hr = Windows.Win32.System.WinRT.WindowsCreateString(obj, len(obj), value)
        if FAILED(hr):
            raise WinError(hr)
        return value

    def __ctypes_from_outparam__(self):
        import Windows.Win32.System.WinRT
        length = UInt32()
        pcwstr = Windows.Win32.System.WinRT.WindowsGetStringRawBuffer(self, length)
        return wstring_at(cast(pcwstr, c_void_p).value, length.value)

class EasyCastStructure(Structure):
    def __setattr__(self, name, obj):
        obj = easycast(obj, self._hints_[name])
        return super().__setattr__(name, obj)

class EasyCastUnion(Union):
    def __setattr__(self, name, obj):
        obj = easycast(obj, self._hints_[name])
        return super().__setattr__(name, obj)

class EasyCastHandler:
    def __init__(self, declared_type):
        self.declared_type = declared_type

    def from_param(self, obj):
        obj = easycast(obj, self.declared_type)
        return self.declared_type.from_param(obj)

EASY_TYPES = [ #obj_type, type_hint, c_func
    # python objects:
    (str, (POINTER(Int16), POINTER(UInt16)), c_wchar_p),
    # ctypes objects:
    (c_wchar_p, (POINTER(Int16), POINTER(UInt16)), None),
    (c_wchar_p, (POINTER(POINTER(Int16)), POINTER(POINTER(UInt16))), pointer),
]

def easycast(obj, type_):
    for obj_type, type_hint, c_func in EASY_TYPES:
        if isinstance(obj, obj_type) and issubclass(type_, type_hint):
            if c_func is not None: obj = c_func(obj)
            return cast(obj, type_)
    return obj

class Guid(EasyCastStructure):
    _fields_ = [("Data1", UInt32),
                ("Data2", UInt16),
                ("Data3", UInt16),
                ("Data4", Byte * 8)]
    _hints_ = {
        "Data1": UInt32,
        "Data2": UInt16,
        "Data3": UInt16,
        "Data4": Byte * 8,
    }

    def __init__(self, val=None):
        if val is None:
            pass
        elif isinstance(val, self.__class__):
            self.Data1 = val.Data1
            self.Data2 = val.Data2
            self.Data3 = val.Data3
            self.Data4 = val.Data4
        elif isinstance(val, uuid.UUID):
            u = val
            self.Data1 = u.time_low
            self.Data2 = u.time_mid
            self.Data3 = u.time_hi_version
            for i in range(8):
                self.Data4[i] = u.bytes[8 + i]
        elif isinstance(val, str):
            u = uuid.UUID(val)
            self.Data1 = u.time_low
            self.Data2 = u.time_mid
            self.Data3 = u.time_hi_version
            for i in range(8):
                self.Data4[i] = u.bytes[8 + i]
        else:
            raise ValueError()

    def __str__(self):
        return f"{{{self.Data1:08x}-{self.Data2:04x}-{self.Data3:04x}-{self.Data4[0]:02x}{self.Data4[1]:02x}-{self.Data4[2]:02x}{self.Data4[3]:02x}{self.Data4[4]:02x}{self.Data4[5]:02x}{self.Data4[6]:02x}{self.Data4[7]:02x}}}"

def SUCCEEDED(hr):
    return hr >= 0

def FAILED(hr):
    return hr < 0

def get_type_hints(prototype):
    hints = typing.get_type_hints(prototype, localns=getattr(prototype, '__dict__', None))
    for name, type_ in hints.items():
        if type_ is None.__class__:
            hints[name] = None
    return hints

def commonfunctype(factory):
    def decorator(prototype):
        delegate = None
        def wrapper(*args, **kwargs):
            nonlocal delegate
            if delegate is None:
                hints = get_type_hints(prototype)
                names = list(hints.keys())
                names = names[:-1]
                types = list(hints.values())
                types = types[-1:] + [EasyCastHandler(t) for t in types[:-1]]
                delegate = factory(prototype.__name__, types, tuple((1, name) for name in names))
            return delegate(*args, **kwargs)
        return wrapper
    return decorator

def cfunctype(library):
    def factory(name, types, params):
        return CFUNCTYPE(*types)((name, cdll[library]), params)
    return commonfunctype(factory)

def winfunctype(library):
    def factory(name, types, params):
        return WINFUNCTYPE(*types)((name, windll[library]), params)
    return commonfunctype(factory)

def commethod(vtbl_index):
    def factory(name, types, params):
        return WINFUNCTYPE(*types)(vtbl_index, name, params)
    return commonfunctype(factory)

def errcheck_return(hr, func, args):
    if FAILED(hr):
        raise WinError(hr)
    return args

def errcheck_void(hr, func, args):
    if FAILED(hr):
        raise WinError(hr)
    return None

def winrt_commethod(vtbl_index):
    def factory(name, types, params):
        return WINFUNCTYPE(*types)(vtbl_index, name, params)
    def decorator(prototype):
        delegate_generic = {}
        def wrapper(self, *args, **kwargs):
            import Windows.Win32.Foundation
            nonlocal delegate_generic
            if is_generic_instance(self):
                targs = self.__orig_class__.__args__
            else:
                targs = None
            if targs in delegate_generic:
                delegate = delegate_generic[targs]
            else:
                hints = get_type_hints(prototype)
                return_ = hints.pop("return")
                params = [(1, name) for name in hints.keys()]
                type_hints = list(hints.values())
                if is_generic_instance(self):
                    tparams = self.__class__.__parameters__
                    tmap = {tparams[i]: targs[i] for i in range(len(targs))}
                    if isinstance(return_, TypeVar):
                        return_ = tmap[return_]
                    for i, t in enumerate(type_hints):
                        if isinstance(t, TypeVar):
                            type_hints[i] = tmap[t]
                types = [Windows.Win32.Foundation.HRESULT] + [EasyCastHandler(t) for t in type_hints]
                if return_ is None:
                    errcheck = errcheck_void
                else:
                    params.append((2, "return"))
                    if is_generic_class(return_):
                        class GenericReturnHelper(c_void_p):
                            def __ctypes_from_outparam__(self):
                                return return_(self.value)
                        types.append(POINTER(GenericReturnHelper))
                    else:
                        types.append(POINTER(return_))
                    errcheck = errcheck_return
                delegate_generic[targs] = factory(prototype.__name__, types, tuple(params))
                delegate_generic[targs].errcheck = errcheck
                delegate = delegate_generic[targs]
            return delegate(self, *args, **kwargs)
        return wrapper
    return decorator

def winrt_mixinmethod(prototype):
    interface_class = None
    def wrapper(self, *args, **kwargs):
        nonlocal interface_class
        if interface_class is None:
            hints = get_type_hints(prototype)
            interface_class = hints["self"]
        interface = interface_class()
        if is_generic_class(interface_class):
            guid = _ro_get_parameterized_type_instance_iid(interface_class)
        else:
            guid = interface_class.Guid
        hr = self.QueryInterface(guid, interface)
        if FAILED(hr):
            raise WinError(hr)
        try:
            return getattr(interface, prototype.__name__)(*args, **kwargs)
        finally:
            interface.Release()
    return wrapper

# Cls[T]?
def is_generic_class(cls):
    return isinstance(cls, _GenericAlias)

# Cls[T]()?
def is_generic_instance(obj):
    return isinstance(obj, Generic)

def winrt_classmethod(prototype):
    factory_class = None
    @classmethod
    def wrapper(cls, *args, **kwargs):
        nonlocal factory_class
        if factory_class is None:
            hints = get_type_hints(prototype)
            factory_class = hints["cls"]
        factory = _winrt_get_activation_factory(cls.ClassId, factory_class)
        try:
            return getattr(factory, prototype.__name__)(*args, **kwargs)
        finally:
            factory.Release
    return wrapper

def winrt_factorymethod(prototype):
    factory_class = None
    @classmethod
    def wrapper(cls, *args):
        nonlocal factory_class
        if factory_class is None:
            hints = get_type_hints(prototype)
            factory_class = hints["cls"]
        factory = _winrt_get_activation_factory(cls.ClassId, factory_class)
        try:
            return getattr(factory, prototype.__name__)(*args)
        finally:
            factory.Release
    return wrapper

def winrt_activatemethod(prototype):
    @classmethod
    def wrapper(cls):
        return _winrt_activate_instance(cls.ClassId, cls)
    return wrapper

def _winrt_create_string(s: str):
    import Windows.Win32.System.WinRT as winrt
    hs = winrt.HSTRING()
    hr = winrt.WindowsCreateString(s, len(s), hs)
    if FAILED(hr):
        raise WinError(hr)
    return hs

def _winrt_get_activation_factory(classid: str, factory_class: type[T]) -> T:
    import Windows.Win32.System.WinRT as winrt
    hs = _winrt_create_string(classid)
    factory = factory_class()
    hr = winrt.RoGetActivationFactory(hs, factory_class.Guid, factory)
    winrt.WindowsDeleteString(hs)
    if FAILED(hr):
        raise WinError(hr)
    return factory

def _winrt_activate_instance(classid: str, cls: type[T]) -> T:
    import Windows.Win32.System.WinRT as winrt
    hs = _winrt_create_string(classid)
    instance = cls()
    hr = winrt.RoActivateInstance(hs, instance)
    winrt.WindowsDeleteString(hs)
    if FAILED(hr):
        raise WinError(hr)
    return instance

# https://learn.microsoft.com/en-us/uwp/winrt-cref/winrt-type-system
#
# signature_octets => guid_to_octets(wrt_pinterface_namespace) string_to_utf8_octets(ptype_instance_signature)
#         wrt_pinterface_namespace => "11f47ad5-7b73-42c0-abae-878b1e16adee"
#         ptype_instance_signature => pinterface_instance_signature | pdelegate_instance_ signature
#         pinterface_instance_signature => "pinterface(" piid_guid  ";" args ")"
#         pdelegate_instance_signature => "pinterface(" piid_guid ";" args ")"
#         piid_guid => guid
#         args => arg | arg ";" args
#         arg => type_signature
#         type_signature => base_type_identifer | com_interface_signature | interface_signature | delegate_signature  | interface_group_signature | runtime_class_signature | struct_signature | enum_signature | pinterface_instance_signature | pdelegate_instance_signature
#         com_interface_signature => "cinterface(IInspectable)"
#         base_type_identifier is defined below
#         interface_signature => guid
#         interface_group_signature => "ig(" interface_group_name ";" default_interface ")"
#         runtime_class_signature => "rc(" runtime_class_name ";" default_interface ")"
#         default_interface => type_signature
#         struct_signature => "struct(" struct_name ";" args ")"
#         enum_signature => "enum(" enum_name ";" enum_underlying_type ")"
#         enum_underlying_type => type_signature
#         delegate_signature => "delegate(" guid ")"
#         guid => "{" dashed_hex "}"
#         dashed_hex is the format that uuidgen writes in when passed no arguments.
#             dashed_hex => hex{8} "-" hex{4} "-" hex{4} "-" hex{4} "-" hex{12}
#             hex => [0-9a-f]
def _ro_get_parameterized_type_instance_iid(ga: _GenericAlias) -> Guid:
    wrt_pinterface_namespace = uuid.UUID("{11f47ad5-7b73-42c0-abae-878b1e16adee}")
    ptype_instance_signature = _get_type_signature(ga)
    return Guid(uuid.uuid5(wrt_pinterface_namespace, ptype_instance_signature))

# FIXME: not completed
def _get_type_signature(cls) -> str:
    if isinstance(cls, _GenericAlias):
        piid_guid = str(cls.Guid)
        args = ";".join(_get_type_signature(arg) for arg in cls.__args__)
        return f"pinterface({piid_guid};{args})"
    elif issubclass(cls, c_void_p):
        return str(cls.Guid)
    elif issubclass(cls, WinRT_String):
        return "string"
    elif issubclass(cls, Char16):
        return "c2"
    elif issubclass(cls, Int32):
        return "i4"
    elif issubclass(cls, Int64):
        return "i8"
    elif issubclass(cls, Byte):
        return "u1"
    elif issubclass(cls, UInt32):
        return "u4"
    elif issubclass(cls, UInt64):
        return "u8"
    elif issubclass(cls, Single):
        return "f4"
    elif issubclass(cls, Double):
        return "f8"
    elif issubclass(cls, Boolean):
        return "b1"
    elif issubclass(cls, Guid):
        return "g16"
    else:
        raise NotImplementedError()

def commonfunctype_pointer(prototype, functype):
    def press_functype_pointer():
        hints = get_type_hints(prototype)
        types = list(hints.values())
        types = types[-1:] + types[:-1]
        return functype(*types)
    return press_functype_pointer

def cfunctype_pointer(prototype):
    return commonfunctype_pointer(prototype, CFUNCTYPE)

def winfunctype_pointer(prototype):
    return commonfunctype_pointer(prototype, WINFUNCTYPE)

def press(prototype):
    if isinstance(prototype, types.FunctionType):
        # constant or function_pointer
        return prototype()
    elif issubclass(prototype, (Structure, Union)):
        return press_struct(prototype)
    elif issubclass(prototype, c_void_p):
        return press_interface(prototype)
    else:
        raise NotImplementedError()

def press_struct(prototype):
    # FIXME: not work for Union.
    #if hasattr(prototype, "_fields_"):
    if "_fields_" in dir(prototype):
        return prototype
    hints = get_type_hints(prototype)
    anonymous = [name  for name in hints.keys() if re.match(r"^Anonymous\d*$", name)]
    if anonymous:
        prototype._anonymous_ = anonymous
    for type_ in hints.values():
        if type_ is not prototype and issubclass(type_, (Structure, Union)):
            press_struct(type_)
    prototype._fields_ = list(hints.items())
    for name in anonymous:
        hints.update(hints[name]._hints_)
    prototype._hints_ = hints
    return prototype

def press_interface(prototype):
    hints = get_type_hints(prototype)
    if hints["extends"] is None:
        return prototype
    prototype.__bases__ = tuple(hints["extends"] if t is c_void_p else t for t in prototype.__bases__)
    return prototype

def make_head(module, name):
    setattr(module, f"{name}_head", getattr(module, name))
    delattr(module, name)

