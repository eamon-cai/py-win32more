import unittest
from ctypes import POINTER, Array, c_char_p, c_void_p, c_wchar_p, cast

from Windows import (
    Boolean,
    Char,
    Double,
    EasyCastStructure,
    EasyCastUnion,
    Int32,
    UInt32,
    UIntPtr,
    press,
)
from Windows.Win32.UI.Shell import StrChrA, StrChrW


class TestMarshalling(unittest.TestCase):
    def test_c_void_p(self):
        @press
        class S(EasyCastStructure):
            c_void_p: c_void_p

        s = S()

        self.assertIsNone(s.c_void_p)

        s.c_void_p = False
        self.assertIsNone(s.c_void_p)

        s.c_void_p = True
        self.assertIsInstance(s.c_void_p, int)
        self.assertEqual(s.c_void_p, 1)

        s.c_void_p = 0
        self.assertIsNone(s.c_void_p)

        s.c_void_p = 1234
        self.assertIsInstance(s.c_void_p, int)
        self.assertEqual(s.c_void_p, 1234)

        s.c_void_p = -1
        self.assertIsInstance(s.c_void_p, int)
        self.assertEqual(s.c_void_p, UIntPtr(-1).value)

        with self.assertRaises(TypeError):
            s.c_void_p = 0.14

        with self.assertRaises(TypeError):
            s.c_void_p = "abcdefg"

        with self.assertRaises(TypeError):
            s.c_void_p = b"abcdefg"

    def test_c_char_p(self):
        @press
        class S(EasyCastStructure):
            c_char_p: c_char_p

        s = S()

        self.assertIsNone(s.c_char_p)

        s.c_char_p = False
        self.assertIsNone(s.c_char_p)

        # Test with c_char_p_as_intptr for invalid address.
        s.c_char_p = True
        self.assertIsInstance(s.c_char_p_as_intptr, int)
        self.assertEqual(s.c_char_p_as_intptr, 1)

        s.c_char_p = 0
        self.assertIsNone(s.c_char_p)

        s.c_char_p = 1234
        self.assertIsInstance(s.c_char_p_as_intptr, int)
        self.assertEqual(s.c_char_p_as_intptr, 1234)

        s.c_char_p = -1
        self.assertIsInstance(s.c_char_p_as_intptr, int)
        self.assertEqual(s.c_char_p_as_intptr, UIntPtr(-1).value)

        with self.assertRaises(TypeError):
            s.c_char_p = 0.14

        s.c_char_p = b"abcdefg"
        self.assertIsInstance(s.c_char_p, bytes)
        self.assertEqual(s.c_char_p, b"abcdefg")

        with self.assertRaises(TypeError):
            s.c_char_p = "abcdefg"

        s.c_char_p = c_char_p(b"abcdefg")
        self.assertIsInstance(s.c_char_p, bytes)
        self.assertEqual(s.c_char_p, b"abcdefg")

    def test_c_wchar_p(self):
        @press
        class S(EasyCastStructure):
            c_wchar_p: c_wchar_p

        s = S()

        self.assertIsNone(s.c_wchar_p)

        s.c_wchar_p = False
        self.assertIsNone(s.c_wchar_p)

        # Test with c_wchar_p_as_intptr for invalid address.
        s.c_wchar_p = True
        self.assertIsInstance(s.c_wchar_p_as_intptr, int)
        self.assertEqual(s.c_wchar_p_as_intptr, 1)

        s.c_wchar_p = 0
        self.assertIsNone(s.c_wchar_p)

        s.c_wchar_p = 1234
        self.assertIsInstance(s.c_wchar_p_as_intptr, int)
        self.assertEqual(s.c_wchar_p_as_intptr, 1234)

        s.c_wchar_p = -1
        self.assertIsInstance(s.c_wchar_p_as_intptr, int)
        self.assertEqual(s.c_wchar_p_as_intptr, UIntPtr(-1).value)

        with self.assertRaises(TypeError):
            s.c_wchar_p = 0.14

        with self.assertRaises(TypeError):
            s.c_wchar_p = b"abcdefg"

        s.c_wchar_p = "abcdefg"
        self.assertIsInstance(s.c_wchar_p, str)
        self.assertEqual(s.c_wchar_p, "abcdefg")

        s.c_wchar_p = c_wchar_p("abcdefg")
        self.assertIsInstance(s.c_wchar_p, str)
        self.assertEqual(s.c_wchar_p, "abcdefg")

    def test_boolean(self):
        @press
        class S(EasyCastStructure):
            boolean: Boolean

        s = S()

        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, False)

        s.boolean = False
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, False)

        s.boolean = True
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, True)

        s.boolean = 0
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, False)

        s.boolean = 1234
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, True)

        s.boolean = -1
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, True)

        s.boolean = 0.14
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, True)

        s.boolean = b"abcdefg"
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, True)

        s.boolean = "abcdefg"
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, True)

    def test_int32(self):
        @press
        class S(EasyCastStructure):
            int32: Int32

        s = S()

        self.assertIsInstance(s.int32, int)
        self.assertEqual(s.int32, 0)

        s.int32 = 0
        self.assertIsInstance(s.int32, int)
        self.assertEqual(s.int32, 0)

        s.int32 = 1234
        self.assertIsInstance(s.int32, int)
        self.assertEqual(s.int32, 1234)

        s.int32 = -1
        self.assertIsInstance(s.int32, int)
        self.assertEqual(s.int32, -1)

        with self.assertRaises(TypeError):
            s.int32 = 0.14

        with self.assertRaises(TypeError):
            s.int32 = b"abcdefg"

        with self.assertRaises(TypeError):
            s.int32 = "abcdefg"

        s.int32 = 0x100000000
        self.assertIsInstance(s.int32, int)
        self.assertEqual(s.int32, 0)

        s.int32 = 0x100000001
        self.assertIsInstance(s.int32, int)
        self.assertEqual(s.int32, 1)

        s.int32 = 0x1FFFFFFFF
        self.assertIsInstance(s.int32, int)
        self.assertEqual(s.int32, -1)

    def test_uint32(self):
        @press
        class S(EasyCastStructure):
            uint32: UInt32

        s = S()

        self.assertIsInstance(s.uint32, int)
        self.assertEqual(s.uint32, 0)

        s.uint32 = 0
        self.assertIsInstance(s.uint32, int)
        self.assertEqual(s.uint32, 0)

        s.uint32 = 1234
        self.assertIsInstance(s.uint32, int)
        self.assertEqual(s.uint32, 1234)

        s.uint32 = -1
        self.assertIsInstance(s.uint32, int)
        self.assertEqual(s.uint32, 0xFFFFFFFF)

        with self.assertRaises(TypeError):
            s.uint32 = 0.14

        with self.assertRaises(TypeError):
            s.uint32 = b"abcdefg"

        with self.assertRaises(TypeError):
            s.uint32 = "abcdefg"

        s.uint32 = 0x100000000
        self.assertIsInstance(s.uint32, int)
        self.assertEqual(s.uint32, 0)

        s.uint32 = 0x100000001
        self.assertIsInstance(s.uint32, int)
        self.assertEqual(s.uint32, 1)

        s.uint32 = 0x1FFFFFFFF
        self.assertIsInstance(s.uint32, int)
        self.assertEqual(s.uint32, 0xFFFFFFFF)

    def test_double(self):
        @press
        class S(EasyCastStructure):
            double: Double

        s = S()

        self.assertIsInstance(s.double, float)
        self.assertEqual(s.double, 0)

        s.double = 0
        self.assertIsInstance(s.double, float)
        self.assertEqual(s.double, 0)

        s.double = 1234
        self.assertIsInstance(s.double, float)
        self.assertEqual(s.double, 1234)

        s.double = -1
        self.assertIsInstance(s.double, float)
        self.assertEqual(s.double, -1)

        s.double = 0.14
        self.assertIsInstance(s.double, float)
        self.assertEqual(s.double, 0.14)

        with self.assertRaises(TypeError):
            s.double = b"abcdefg"

        with self.assertRaises(TypeError):
            s.double = "abcdefg"

    def test_char(self):
        @press
        class S(EasyCastStructure):
            char: Char

        s = S()

        self.assertIsInstance(s.char, str)
        self.assertEqual(s.char, "\x00")

        with self.assertRaises(TypeError):
            s.char = 0

        with self.assertRaises(TypeError):
            s.char = 1234

        with self.assertRaises(TypeError):
            s.char = -1

        with self.assertRaises(TypeError):
            s.char = 0.14

        with self.assertRaises(TypeError):
            s.char = b"abcdefg"

        with self.assertRaises(TypeError):
            s.char = "abcdefg"

        s.char = "a"
        self.assertIsInstance(s.char, str)
        self.assertEqual(s.char, "a")

        with self.assertRaises(TypeError):
            s.char = b"a"

    def test_int32_array(self):
        @press
        class S(EasyCastStructure):
            int32_array_3: Int32 * 3

        s = S()

        self.assertIsInstance(s.int32_array_3, Array)
        self.assertEqual(s.int32_array_3[0], 0)
        self.assertEqual(s.int32_array_3[1], 0)
        self.assertEqual(s.int32_array_3[2], 0)
        self.assertEqual(s.int32_array_3[:], [0, 0, 0])

        s.int32_array_3 = (3, 4, 5)
        self.assertIsInstance(s.int32_array_3, Array)
        self.assertEqual(s.int32_array_3[0], 3)
        self.assertEqual(s.int32_array_3[1], 4)
        self.assertEqual(s.int32_array_3[2], 5)
        self.assertEqual(s.int32_array_3[:], [3, 4, 5])

        with self.assertRaises(TypeError):
            s.int32_array_3 = [3, 4, 5]

        with self.assertRaises(RuntimeError):
            s.int32_array_3 = (3, 4, "5")

    def test_c_void_p_array(self):
        @press
        class S(EasyCastStructure):
            c_void_p_array_3: c_void_p * 3

        s = S()

        self.assertIsInstance(s.c_void_p_array_3, Array)
        self.assertIsNone(s.c_void_p_array_3[0])
        self.assertIsNone(s.c_void_p_array_3[1])
        self.assertIsNone(s.c_void_p_array_3[2])
        self.assertEqual(s.c_void_p_array_3[:], [None, None, None])

        s.c_void_p_array_3 = (3, 4, 5)
        self.assertEqual(s.c_void_p_array_3[0], 3)
        self.assertEqual(s.c_void_p_array_3[1], 4)
        self.assertEqual(s.c_void_p_array_3[2], 5)
        self.assertEqual(s.c_void_p_array_3[:], [3, 4, 5])

        with self.assertRaises(TypeError):
            s.c_void_p_array_3 = [3, 4, 5]

        with self.assertRaises(RuntimeError):
            s.c_void_p_array_3 = (3, 4, "5")

    def test_c_wchar_p_array(self):
        @press
        class S(EasyCastStructure):
            c_wchar_p_array_3: c_wchar_p * 3

        s = S()

        self.assertIsInstance(s.c_wchar_p_array_3, Array)
        self.assertIsNone(s.c_wchar_p_array_3[0])
        self.assertIsNone(s.c_wchar_p_array_3[1])
        self.assertIsNone(s.c_wchar_p_array_3[2])
        self.assertEqual(s.c_wchar_p_array_3[:], [None, None, None])

        # Access to invalid address indirectly.
        s.c_wchar_p_array_3 = (3, 4, 5)
        self.assertEqual(cast(s.c_wchar_p_array_3, POINTER(c_void_p))[0], 3)
        self.assertEqual(cast(s.c_wchar_p_array_3, POINTER(c_void_p))[1], 4)
        self.assertEqual(cast(s.c_wchar_p_array_3, POINTER(c_void_p))[2], 5)

        s.c_wchar_p_array_3 = ("3", "4", "5")
        self.assertEqual(s.c_wchar_p_array_3[0], "3")
        self.assertEqual(s.c_wchar_p_array_3[1], "4")
        self.assertEqual(s.c_wchar_p_array_3[2], "5")
        self.assertEqual(s.c_wchar_p_array_3[:], ["3", "4", "5"])

    def test_function_return_char_p(self):
        s = c_char_p(b"abcdefg")
        i = cast(s, c_void_p).value

        p = StrChrA(s, ord("x"))
        self.assertIsNone(p)

        p = StrChrA(s, ord("d"))
        self.assertEqual(p, b"defg")

        p = StrChrA(s, ord("d"), _as_intptr=True)
        self.assertEqual(p, i + 3)

    def test_function_return_wchar_p(self):
        s = c_wchar_p("abcdefg")
        i = cast(s, c_void_p).value

        p = StrChrW(s, "x")
        self.assertIsNone(p)

        p = StrChrW(s, "d")
        self.assertEqual(p, "defg")

        p = StrChrW(s, "d", _as_intptr=True)
        self.assertEqual(p, i + 6)

    def test_function_int_as_char_p(self):
        s = c_char_p(b"abcdefg")
        i = cast(s, c_void_p).value

        p = StrChrA(i, ord("a"), _as_intptr=True)
        self.assertEqual(p, i)

    def test_function_int_as_wchar_p(self):
        s = c_wchar_p("abcdefg")
        i = cast(s, c_void_p).value

        p = StrChrW(i, "a", _as_intptr=True)
        self.assertEqual(p, i)


if __name__ == "__main__":
    unittest.main()