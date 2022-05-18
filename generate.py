# https://github.com/microsoft/win32metadata
# https://github.com/marlersoft/win32json

import io
import json
import re
from pathlib import Path

ARCHITECTURE = "X64"

class Generator:
    def __init__(self, out) -> None:
        self.out = out

    def write_import(self, ns: dict, modapi: str) -> None:
        for api in sorted(self.collect_apiref(ns, {modapi})):
            self.writeline(f"import win32more.{api}")

    def collect_apiref(self, node, apiref: set) -> set:
        match node:
            case {"Kind": "ApiRef", "Api": api}:
                apiref.add(api)
            case {}:
                for x in node.values():
                    self.collect_apiref(x, apiref)
            case [*_]:
                for x in node:
                    self.collect_apiref(x, apiref)
        return apiref

    def write_getattr(self) -> None:
        self.write(f"""
def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{{name}}"]
    except KeyError:
        raise AttributeError(f"module '{{__name__}}' has no attribute '{{name}}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
""")

    def write_export(self, ns: dict) -> None:
        self.writeline("__all__ = [")
        for name in self.collect_export(ns):
            self.writeline(f'    "{name}",')
        self.writeline("]")

    def collect_export(self, ns: dict):
        for e in ns.values():
            yield e["Name"]
            match e:
                case {"_Category": "Types", "Kind": "Enum"}:
                    for v in e["Values"]:
                        yield v["Name"]
                case {"_Category": "Functions", "_UnicodeAlias": ua} if ua is not None:
                    yield ua

    def write_define(self, ns: dict) -> None:
        for e in ns.values():
            match e["_Category"]:
                case "Types":
                    self.visit_type(e)
                case "Functions":
                    self.visit_function(e)
                case "Constants":
                    self.visit_constant(e)

    def visit_type(self, mt) -> None:
        match mt["Kind"]:
            case "Com":
                self.visit_com(mt)
            case "ComClassID":
                self.visit_com_class_id(mt)
            case "Enum":
                self.visit_enum(mt)
            case "FunctionPointer":
                self.visit_function_pointer(mt)
            case "NativeTypedef":
                self.visit_typedef(mt)
            case "Struct":
                self.visit_struct(mt)
            case "Union":
                self.visit_struct(mt)
            case _:
                raise RuntimeError(f"unknown type {mt['Kind']}")

    def visit_com(self, mt) -> None:
        base = f"win32more.{mt['Interface']['Api']}.{mt['Interface']['Name']}_head" if mt["Interface"] else "c_void_p"
        guid = repr(mt["Guid"])
        self.writeline(f"def _define_{mt['Name']}_head():")
        self.writeline(f"    class {mt['Name']}({base}):")
        self.writeline(f"        Guid = Guid({guid})")
        self.writeline(f"    return {mt['Name']}")
        self.writeline(f"def _define_{mt['Name']}():")
        self.writeline(f"    {mt['Name']} = win32more.{mt['_ApiName']}_head")
        for m in mt["Methods"]:
            types = [self.to_pytype(m["ReturnType"])]
            params = []
            for p in m["Params"]:
                types.append(self.to_pytype(p["Type"]))
                inout = 1
                params.append((inout, p["Name"]))
            ts = ",".join(types)
            if params:
                ps = "(" + ",".join(f"({inout}, '{name}')" for inout, name in params) + ",)"
            else:
                ps = "()"
            self.writeline(f"    {mt['Name']}.{m['Name']} = COMMETHOD(WINFUNCTYPE({ts}, use_last_error={m['SetLastError']})({m['_vtbl_index']}, '{m['Name']}', {ps}))")
        self.writeline(f"    return {mt['Name']}")

    def visit_com_class_id(self, mt) -> None:
        guid = repr(mt["Guid"])
        self.writeline(f"{mt['Name']} = Guid({guid})")

    def visit_enum(self, mt) -> None:
        self.writeline(f"{mt['Name']} = {mt['IntegerBase']}")
        for v in mt["Values"]:
            self.writeline(f"{v['Name']} = {v['Value']}")

    def visit_function_pointer(self, mt) -> None:
        types = [self.to_pytype(mt["ReturnType"])]
        for p in mt["Params"]:
            types.append(self.to_pytype(p["Type"]))
        ts = ",".join(types)
        self.writeline(f"def _define_{mt['Name']}():")
        self.writeline(f"""    return CFUNCTYPE({ts}, use_last_error={mt['SetLastError']})""")

    def visit_typedef(self, mt) -> None:
        pytype = self.to_pytype(mt["Def"])
        self.writeline(f"{mt['Name']} = {pytype}")

    def visit_struct(self, mt, nested: bool = False) -> None:
        base = self.get_struct_base(mt)
        if not nested:
            self.writeline(f"def _define_{mt['Name']}_head():")
            self.writeline(f"    class {mt['Name']}({base}):")
            self.writeline(f"        pass")
            self.writeline(f"    return {mt['Name']}")
            self.writeline(f"def _define_{mt['Name']}():")
            self.writeline(f"    {mt['Name']} = win32more.{mt['_ApiName']}_head")
        else:
            self.writeline(f"    class {mt['Name']}({base}):")
            self.writeline(f"        pass")
        for nt in mt["NestedTypes"]:
            self.visit_struct(nt, True)
        if mt["PackingSize"] != 0:
            self.writeline(f"    {mt['Name']}._pack_ = {mt['PackingSize']}")
        anonymous = []
        for f in mt["Fields"]:
            if re.match(r"^Anonymous\d*$", f["Name"]):
                anonymous.append(f["Name"])
        if anonymous:
            self.writeline(f"    {mt['Name']}._anonymous_ = [")
            for name in anonymous:
                self.writeline(f"        '{name}',")
            self.writeline("    ]")
        if mt["Fields"]:
            self.writeline(f"    {mt['Name']}._fields_ = [")
            for f in mt["Fields"]:
                pytype = self.to_pytype(f["Type"])
                self.writeline(f"""        ("{f['Name']}", {pytype}),""")
            self.writeline("    ]")
        if not nested:
            self.writeline(f"    return {mt['Name']}")

    def get_struct_base(slef, mt) -> str:
        match mt["Kind"]:
            case "Struct":
                return "Structure"
            case "Union":
                return "Union"
            case _:
                raise RuntimeError(f"unknown struct kind {mt['Kind']}")

    def visit_function(self, ft) -> None:
        self.writeline(f"def _define_{ft['Name']}():")
        dll = ft["DllImport"]
        types = [self.to_pytype(ft["ReturnType"])]
        params = []
        for p in ft["Params"]:
            types.append(self.to_pytype(p["Type"]))
            inout = 1   # p["Attrs"] has "In" (1) or "Out" (2) or both (3)
            params.append((inout, p["Name"]))
        ts = ",".join(types)
        if params:
            ps = "(" + ",".join(f"({inout}, '{name}')" for inout, name in params) + ",)"
        else:
            ps = "()"
        self.writeline(f"    try:")
        self.writeline(f"""        return WINFUNCTYPE({ts}, use_last_error={ft['SetLastError']})(("{ft['Name']}", windll["{dll}"]), {ps})""")
        self.writeline(f"    except (FileNotFoundError, AttributeError):")
        self.writeline(f"        return None")
        if ua := ft.get("_UnicodeAlias"):
            self.writeline(f"def _define_{ua}():")
            self.writeline(f"    return win32more.{ft['_ApiName']}")

    def visit_constant(self, ct) -> None:
        pyvalue = self.to_pyvalue(ct)
        self.writeline(f"{ct['Name']} = {pyvalue}")

    def to_pytype(self, mt) -> str:
        match mt:
            case {"Kind": "PointerTo", "Child": {"Kind": "MissingClrType"}}:
                return "c_void_p"       # MissingClrType?
            case {"Kind": "PointerTo", "Child": {"Kind": "Native", "Name": "Void"}}:
                return "c_void_p"
            case {"Kind": "PointerTo", "Child": {"Kind": "Native", "Name": "Byte"}}:
                return "c_char_p_no"    # safe?
            case {"Kind": "PointerTo", "Child": {"Kind": "Native", "Name": "Char"}}:
                return "c_wchar_p_no"   # safe?
            case {"Kind": "PointerTo" | "LPArray", "Child": c}:
                pointee = self.to_pytype(c)
                return f"POINTER({pointee})"
            case {"Kind": "Array", "Shape": shape, "Child": c}:
                size = shape["Size"] if shape else 0
                element_type = self.to_pytype(c)
                return f"{element_type} * {size}"
            case {"Kind": "ApiRef", "Name": name, "Api": api, "_nested": True}:
                return name
            case {"Kind": "ApiRef", "Name": name, "Api": api, "_head": True}:
                return f"win32more.{api}.{name}_head"
            case {"Kind": "ApiRef", "Name": name, "Api": api}:
                return f"win32more.{api}.{name}"
            case {"Kind": "Native", "Name": name}:
                return name
            case _:
                raise RuntimeError(f"unknown type {mt}")

    def to_pyvalue(self, ct) -> str:
        match ct["ValueType"]:
            case ("Byte"| "SByte"| "Char"| "Int16"| "UInt16"| "Int32"| "UInt32"| "Int64"| "UInt64" |
                  "Single" | "Double" | "String"):
                return repr(ct["Value"])
            case "PropertyKey":
                # TODO: other type?
                fmtid = repr(ct["Value"]["Fmtid"])
                pid = ct["Value"]["Pid"]
                return f"PROPERTYKEY(Fmtid={fmtid}, Pid={pid})"
            case _:
                raise RuntimeError(f"unknown value type {ct['ValueType']}")

    def write(self, s: str) -> None:
        self.out.write(s)

    def writeline(self, s: str) -> None:
        self.write(s)
        self.write("\n")

class Preprocessor:
    def preprocess(self, allmeta: dict) -> dict:
        ns = self.make_namespace(allmeta)
        ns = self.patch_struct_nested_type(ns)
        ns = self.patch_enum(ns)
        ns = self.patch_com_vtbl_index(ns)
        ns = self.patch_apiref(ns)
        return ns

    def make_namespace(self, allmeta: dict) -> dict:
        ns = {}
        ua = {}
        for api, meta in allmeta.items():
            for a in meta["UnicodeAliases"]:
                ua[f"{a}W"] = a
        for api, meta in allmeta.items():
            for e in meta["Constants"]:
                apiname = f"{api}.{e['Name']}"
                e["_Category"] = "Constants"
                e["_Api"] = api
                e["_ApiName"] = apiname
                ns[apiname] = e
        for api, meta in allmeta.items():
            for e in meta["Types"]:
                if e["Architectures"] and ARCHITECTURE not in e["Architectures"]:
                    continue
                apiname = f"{api}.{e['Name']}"
                e["_Category"] = "Types"
                e["_Api"] = api
                e["_ApiName"] = apiname
                ns[apiname] = e
        for api, meta in allmeta.items():
            for e in meta["Functions"]:
                if e["Architectures"] and ARCHITECTURE not in e["Architectures"]:
                    continue
                apiname = f"{api}.{e['Name']}"
                e["_Category"] = "Functions"
                e["_Api"] = api
                e["_ApiName"] = apiname
                e["_UnicodeAlias"] = ua.get(e["Name"])
                ns[apiname] = e
        return ns

    def patch_struct_nested_type(self, ns: dict) -> dict:
        for e in ns.values():
            match e:
                case {"_Category": "Types", "Kind": "Struct" | "Union"}:
                    self.patch_nested_type(e)
        return ns

    # Rename nested type to {struct_name}_{nested_name}_e__{Struct|Union}.
    def patch_nested_type(self, e: dict) -> None:
        renamed = {}
        for n in e["NestedTypes"]:
            newname = f"{e['Name']}_{n['Name']}"
            renamed[n["Name"]] = newname
            n["Name"] = newname
            self.patch_nested_type(n)
        for f in e["Fields"]:
            t = self.get_element_type(f["Type"])
            if t["Name"] in renamed:
                t["Name"] = renamed[t["Name"]]

    def get_element_type(self, e) -> str:
        match e:
            case {"Child": c}:
                return self.get_element_type(c)
            case _:
                return e

    def patch_enum(self, ns: dict) -> dict:
        for e in ns.values():
            match e:
                case {"_Category": "Types", "Kind": "Enum"}:
                    # IntegerBase can be null.  Default to Int32.
                    if not e["IntegerBase"]:
                        e["IntegerBase"] = "Int32"
                    # FIXME: enum value name? (NAME or ENUM_NAME or ENUM.Name?)
                    if self.enum_need_prefix(e):
                        for v in e["Values"]:
                            v["Name"] = f"{e['Name']}_{v['Name']}"
        return ns

    def enum_need_prefix(self, e: dict) -> bool:
        for v in e["Values"]:
            if not ("_" in v["Name"] or v["Name"].isupper()):
                return True
        return False

    # Add vtbl_index to COM methods.
    def patch_com_vtbl_index(self, ns: dict):
        for e in ns.values():
            match e:
                case {"_Category": "Types", "Kind": "Com", "Interface": interface, "Methods": [*methods]}:
                    vtbl_index = self.count_interface_method(interface, ns)
                    for m in methods:
                        m["_vtbl_index"] = vtbl_index
                        vtbl_index += 1
        return ns

    def count_interface_method(self, interface: dict, ns: dict) -> int:
        if not interface:
            return 0
        cls = ns[f"{interface['Api']}.{interface['Name']}"]
        return len(cls["Methods"]) + self.count_interface_method(cls["Interface"], ns)

    # Add additional information to ApiRef.
    # _head: require header only.
    # _nested: is nested type.
    def patch_apiref(self, ns: dict):
        for e in ns.values():
            self.add_apiref_attr(e, ns)
        return ns

    def add_apiref_attr(self, node, ns) -> None:
        match node:
            case {"Kind": "Com", "Interface": interface, "Methods": [*methods]}:
                if interface:
                    interface["_head"] = True
                for e in methods:
                    self.add_apiref_attr(e, ns)
            case {"Kind": "PointerTo", "Child": {"Kind": "ApiRef", "Name": name, "Api": api} as apiref}:
                if f"{api}.{name}" not in ns:
                    apiref["_nested"] = True
                elif ns[f"{api}.{name}"]["Kind"] in ("Struct", "Union", "Com"):
                    apiref["_head"] = True
            case {"Kind": "ApiRef", "Name": name, "Api": api, "TargetKind": targetkind} as apiref:
                if f"{api}.{name}" not in ns:
                    apiref["_nested"] = True
                elif targetkind == "Com":
                    apiref["_head"] = True
            case {}:
                for e in node.values():
                    self.add_apiref_attr(e, ns)
            case [*_]:
                for e in node:
                    self.add_apiref_attr(e, ns)

class JsonLoader:
    def loadall(self, apipath):
        allmeta = {}
        for jsonfile in Path(apipath).glob("*.json"):
            api = jsonfile.stem
            allmeta[api] = json.loads(jsonfile.read_text())
        return allmeta

def main():
    allmeta = JsonLoader().loadall("win32json/api")
    ns = Preprocessor().preprocess(allmeta)
    for modapi in allmeta:
        mod = {k: v for k, v in ns.items() if v["_Api"] == modapi}
        is_dir = any(api.startswith(modapi + ".") for api in allmeta)
        if is_dir:
            p = Path("win32more") / modapi.replace(".", "/") / "__init__.py"
        else:
            p = Path("win32more") / (modapi.replace(".", "/") + ".py")
        if not p.parent.exists():
            p.parent.mkdir(parents=True)
        with p.open("w") as f:
            g = Generator(f)
            g.writeline(f"from win32more import *")
            g.write_import(mod, modapi)
            g.write_getattr()
            g.write_define(mod)
            g.write_export(mod)
    # generate __init__.py
    for p in Path("win32more").glob("**/*"):
        if p.is_dir() and not (p / "__init__.py").exists():
            (p / "__init__.py").write_text("")
    # generate all.py module
    with open("win32more/all.py", "w") as f:
        f.write("from win32more import *\n")
        for api in sorted(allmeta):
            f.write(f"from win32more.{api} import *\n")

if __name__ == "__main__":
    main()
