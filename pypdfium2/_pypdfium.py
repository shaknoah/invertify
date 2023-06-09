r"""Wrapper for fpdf_annot.h

Generated with:
/opt/hostedtoolcache/Python/3.10.9/x64/bin/ctypesgen --library pdfium --runtime-libdir . ./fpdf_annot.h ./fpdf_attachment.h ./fpdf_catalog.h ./fpdf_dataavail.h ./fpdf_doc.h ./fpdf_edit.h ./fpdf_ext.h ./fpdf_flatten.h ./fpdf_formfill.h ./fpdf_fwlevent.h ./fpdf_javascript.h ./fpdf_ppo.h ./fpdf_progressive.h ./fpdf_save.h ./fpdf_searchex.h ./fpdf_signature.h ./fpdf_structtree.h ./fpdf_sysfontinfo.h ./fpdf_text.h ./fpdf_thumbnail.h ./fpdf_transformpage.h ./fpdfview.h -o ~/work/pypdfium2/pypdfium2/data/windows_x64/_pypdfium.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs(['.'])

# Begin libraries
_libs["pdfium"] = load_library("pdfium")

# 1 libraries
# End libraries

# No modules

enum_anon_2 = c_int# fpdfview.h: 51

FPDF_TEXTRENDERMODE_UNKNOWN = (-1)# fpdfview.h: 51

FPDF_TEXTRENDERMODE_FILL = 0# fpdfview.h: 51

FPDF_TEXTRENDERMODE_STROKE = 1# fpdfview.h: 51

FPDF_TEXTRENDERMODE_FILL_STROKE = 2# fpdfview.h: 51

FPDF_TEXTRENDERMODE_INVISIBLE = 3# fpdfview.h: 51

FPDF_TEXTRENDERMODE_FILL_CLIP = 4# fpdfview.h: 51

FPDF_TEXTRENDERMODE_STROKE_CLIP = 5# fpdfview.h: 51

FPDF_TEXTRENDERMODE_FILL_STROKE_CLIP = 6# fpdfview.h: 51

FPDF_TEXTRENDERMODE_CLIP = 7# fpdfview.h: 51

FPDF_TEXTRENDERMODE_LAST = FPDF_TEXTRENDERMODE_CLIP# fpdfview.h: 51

FPDF_TEXT_RENDERMODE = enum_anon_2# fpdfview.h: 51

# fpdfview.h: 54
class struct_fpdf_action_t__(Structure):
    pass

FPDF_ACTION = POINTER(struct_fpdf_action_t__)# fpdfview.h: 54

# fpdfview.h: 55
class struct_fpdf_annotation_t__(Structure):
    pass

FPDF_ANNOTATION = POINTER(struct_fpdf_annotation_t__)# fpdfview.h: 55

# fpdfview.h: 56
class struct_fpdf_attachment_t__(Structure):
    pass

FPDF_ATTACHMENT = POINTER(struct_fpdf_attachment_t__)# fpdfview.h: 56

# fpdfview.h: 57
class struct_fpdf_avail_t__(Structure):
    pass

FPDF_AVAIL = POINTER(struct_fpdf_avail_t__)# fpdfview.h: 57

# fpdfview.h: 58
class struct_fpdf_bitmap_t__(Structure):
    pass

FPDF_BITMAP = POINTER(struct_fpdf_bitmap_t__)# fpdfview.h: 58

# fpdfview.h: 59
class struct_fpdf_bookmark_t__(Structure):
    pass

FPDF_BOOKMARK = POINTER(struct_fpdf_bookmark_t__)# fpdfview.h: 59

# fpdfview.h: 60
class struct_fpdf_clippath_t__(Structure):
    pass

FPDF_CLIPPATH = POINTER(struct_fpdf_clippath_t__)# fpdfview.h: 60

# fpdfview.h: 61
class struct_fpdf_dest_t__(Structure):
    pass

FPDF_DEST = POINTER(struct_fpdf_dest_t__)# fpdfview.h: 61

# fpdfview.h: 62
class struct_fpdf_document_t__(Structure):
    pass

FPDF_DOCUMENT = POINTER(struct_fpdf_document_t__)# fpdfview.h: 62

# fpdfview.h: 63
class struct_fpdf_font_t__(Structure):
    pass

FPDF_FONT = POINTER(struct_fpdf_font_t__)# fpdfview.h: 63

# fpdfview.h: 64
class struct_fpdf_form_handle_t__(Structure):
    pass

FPDF_FORMHANDLE = POINTER(struct_fpdf_form_handle_t__)# fpdfview.h: 64

# fpdfview.h: 65
class struct_fpdf_glyphpath_t__(Structure):
    pass

FPDF_GLYPHPATH = POINTER(struct_fpdf_glyphpath_t__)# fpdfview.h: 65

# fpdfview.h: 66
class struct_fpdf_javascript_action_t(Structure):
    pass

FPDF_JAVASCRIPT_ACTION = POINTER(struct_fpdf_javascript_action_t)# fpdfview.h: 66

# fpdfview.h: 67
class struct_fpdf_link_t__(Structure):
    pass

FPDF_LINK = POINTER(struct_fpdf_link_t__)# fpdfview.h: 67

# fpdfview.h: 68
class struct_fpdf_page_t__(Structure):
    pass

FPDF_PAGE = POINTER(struct_fpdf_page_t__)# fpdfview.h: 68

# fpdfview.h: 69
class struct_fpdf_pagelink_t__(Structure):
    pass

FPDF_PAGELINK = POINTER(struct_fpdf_pagelink_t__)# fpdfview.h: 69

# fpdfview.h: 70
class struct_fpdf_pageobject_t__(Structure):
    pass

FPDF_PAGEOBJECT = POINTER(struct_fpdf_pageobject_t__)# fpdfview.h: 70

# fpdfview.h: 71
class struct_fpdf_pageobjectmark_t__(Structure):
    pass

FPDF_PAGEOBJECTMARK = POINTER(struct_fpdf_pageobjectmark_t__)# fpdfview.h: 71

# fpdfview.h: 72
class struct_fpdf_pagerange_t__(Structure):
    pass

FPDF_PAGERANGE = POINTER(struct_fpdf_pagerange_t__)# fpdfview.h: 72

# fpdfview.h: 73
class struct_fpdf_pathsegment_t(Structure):
    pass

FPDF_PATHSEGMENT = POINTER(struct_fpdf_pathsegment_t)# fpdfview.h: 73

FPDF_RECORDER = POINTER(None)# fpdfview.h: 74

# fpdfview.h: 75
class struct_fpdf_schhandle_t__(Structure):
    pass

FPDF_SCHHANDLE = POINTER(struct_fpdf_schhandle_t__)# fpdfview.h: 75

# fpdfview.h: 76
class struct_fpdf_signature_t__(Structure):
    pass

FPDF_SIGNATURE = POINTER(struct_fpdf_signature_t__)# fpdfview.h: 76

# fpdfview.h: 77
class struct_fpdf_structelement_t__(Structure):
    pass

FPDF_STRUCTELEMENT = POINTER(struct_fpdf_structelement_t__)# fpdfview.h: 77

# fpdfview.h: 78
class struct_fpdf_structelement_attr_t__(Structure):
    pass

FPDF_STRUCTELEMENT_ATTR = POINTER(struct_fpdf_structelement_attr_t__)# fpdfview.h: 78

# fpdfview.h: 79
class struct_fpdf_structtree_t__(Structure):
    pass

FPDF_STRUCTTREE = POINTER(struct_fpdf_structtree_t__)# fpdfview.h: 79

# fpdfview.h: 80
class struct_fpdf_textpage_t__(Structure):
    pass

FPDF_TEXTPAGE = POINTER(struct_fpdf_textpage_t__)# fpdfview.h: 80

# fpdfview.h: 81
class struct_fpdf_widget_t__(Structure):
    pass

FPDF_WIDGET = POINTER(struct_fpdf_widget_t__)# fpdfview.h: 81

# fpdfview.h: 82
class struct_fpdf_xobject_t__(Structure):
    pass

FPDF_XOBJECT = POINTER(struct_fpdf_xobject_t__)# fpdfview.h: 82

FPDF_BOOL = c_int# fpdfview.h: 85

FPDF_RESULT = c_int# fpdfview.h: 86

FPDF_DWORD = c_ulong# fpdfview.h: 87

FS_FLOAT = c_float# fpdfview.h: 88

enum__FPDF_DUPLEXTYPE_ = c_int# fpdfview.h: 96

DuplexUndefined = 0# fpdfview.h: 96

Simplex = (DuplexUndefined + 1)# fpdfview.h: 96

DuplexFlipShortEdge = (Simplex + 1)# fpdfview.h: 96

DuplexFlipLongEdge = (DuplexFlipShortEdge + 1)# fpdfview.h: 96

FPDF_DUPLEXTYPE = enum__FPDF_DUPLEXTYPE_# fpdfview.h: 96

FPDF_WCHAR = c_ushort# fpdfview.h: 99

FPDF_BYTESTRING = String# fpdfview.h: 103

FPDF_WIDESTRING = POINTER(FPDF_WCHAR)# fpdfview.h: 107

# fpdfview.h: 115
class struct_FPDF_BSTR_(Structure):
    pass

struct_FPDF_BSTR_.__slots__ = [
    'str',
    'len',
]
struct_FPDF_BSTR_._fields_ = [
    ('str', String),
    ('len', c_int),
]

FPDF_BSTR = struct_FPDF_BSTR_# fpdfview.h: 115

FPDF_STRING = String# fpdfview.h: 124

# fpdfview.h: 141
class struct__FS_MATRIX_(Structure):
    pass

struct__FS_MATRIX_.__slots__ = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
]
struct__FS_MATRIX_._fields_ = [
    ('a', c_float),
    ('b', c_float),
    ('c', c_float),
    ('d', c_float),
    ('e', c_float),
    ('f', c_float),
]

FS_MATRIX = struct__FS_MATRIX_# fpdfview.h: 141

# fpdfview.h: 144
class struct__FS_RECTF_(Structure):
    pass

struct__FS_RECTF_.__slots__ = [
    'left',
    'top',
    'right',
    'bottom',
]
struct__FS_RECTF_._fields_ = [
    ('left', c_float),
    ('top', c_float),
    ('right', c_float),
    ('bottom', c_float),
]

FS_LPRECTF = POINTER(struct__FS_RECTF_)# fpdfview.h: 153

FS_RECTF = struct__FS_RECTF_# fpdfview.h: 153

FS_LPCRECTF = POINTER(FS_RECTF)# fpdfview.h: 156

# fpdfview.h: 159
class struct_FS_SIZEF_(Structure):
    pass

struct_FS_SIZEF_.__slots__ = [
    'width',
    'height',
]
struct_FS_SIZEF_._fields_ = [
    ('width', c_float),
    ('height', c_float),
]

FS_LPSIZEF = POINTER(struct_FS_SIZEF_)# fpdfview.h: 162

FS_SIZEF = struct_FS_SIZEF_# fpdfview.h: 162

FS_LPCSIZEF = POINTER(FS_SIZEF)# fpdfview.h: 165

# fpdfview.h: 168
class struct_FS_POINTF_(Structure):
    pass

struct_FS_POINTF_.__slots__ = [
    'x',
    'y',
]
struct_FS_POINTF_._fields_ = [
    ('x', c_float),
    ('y', c_float),
]

FS_LPPOINTF = POINTER(struct_FS_POINTF_)# fpdfview.h: 171

FS_POINTF = struct_FS_POINTF_# fpdfview.h: 171

FS_LPCPOINTF = POINTER(FS_POINTF)# fpdfview.h: 174

# fpdfview.h: 185
class struct__FS_QUADPOINTSF(Structure):
    pass

struct__FS_QUADPOINTSF.__slots__ = [
    'x1',
    'y1',
    'x2',
    'y2',
    'x3',
    'y3',
    'x4',
    'y4',
]
struct__FS_QUADPOINTSF._fields_ = [
    ('x1', FS_FLOAT),
    ('y1', FS_FLOAT),
    ('x2', FS_FLOAT),
    ('y2', FS_FLOAT),
    ('x3', FS_FLOAT),
    ('y3', FS_FLOAT),
    ('x4', FS_FLOAT),
    ('y4', FS_FLOAT),
]

FS_QUADPOINTSF = struct__FS_QUADPOINTSF# fpdfview.h: 185

FPDF_ANNOTATION_SUBTYPE = c_int# fpdfview.h: 188

FPDF_ANNOT_APPEARANCEMODE = c_int# fpdfview.h: 189

FPDF_OBJECT_TYPE = c_int# fpdfview.h: 192

# fpdfview.h: 229
for _lib in _libs.values():
    if not _lib.has("FPDF_InitLibrary", "cdecl"):
        continue
    FPDF_InitLibrary = _lib.get("FPDF_InitLibrary", "cdecl")
    FPDF_InitLibrary.argtypes = []
    FPDF_InitLibrary.restype = None
    break

enum_anon_3 = c_int# fpdfview.h: 238

FPDF_RENDERERTYPE_AGG = 0# fpdfview.h: 238

FPDF_RENDERERTYPE_SKIA = 1# fpdfview.h: 238

FPDF_RENDERER_TYPE = enum_anon_3# fpdfview.h: 238

# fpdfview.h: 278
class struct_FPDF_LIBRARY_CONFIG_(Structure):
    pass

struct_FPDF_LIBRARY_CONFIG_.__slots__ = [
    'version',
    'm_pUserFontPaths',
    'm_pIsolate',
    'm_v8EmbedderSlot',
    'm_pPlatform',
    'm_RendererType',
]
struct_FPDF_LIBRARY_CONFIG_._fields_ = [
    ('version', c_int),
    ('m_pUserFontPaths', POINTER(POINTER(c_char))),
    ('m_pIsolate', POINTER(None)),
    ('m_v8EmbedderSlot', c_uint),
    ('m_pPlatform', POINTER(None)),
    ('m_RendererType', FPDF_RENDERER_TYPE),
]

FPDF_LIBRARY_CONFIG = struct_FPDF_LIBRARY_CONFIG_# fpdfview.h: 278

# fpdfview.h: 290
for _lib in _libs.values():
    if not _lib.has("FPDF_InitLibraryWithConfig", "cdecl"):
        continue
    FPDF_InitLibraryWithConfig = _lib.get("FPDF_InitLibraryWithConfig", "cdecl")
    FPDF_InitLibraryWithConfig.argtypes = [POINTER(FPDF_LIBRARY_CONFIG)]
    FPDF_InitLibraryWithConfig.restype = None
    break

# fpdfview.h: 303
for _lib in _libs.values():
    if not _lib.has("FPDF_DestroyLibrary", "cdecl"):
        continue
    FPDF_DestroyLibrary = _lib.get("FPDF_DestroyLibrary", "cdecl")
    FPDF_DestroyLibrary.argtypes = []
    FPDF_DestroyLibrary.restype = None
    break

# fpdfview.h: 316
for _lib in _libs.values():
    if not _lib.has("FPDF_SetSandBoxPolicy", "cdecl"):
        continue
    FPDF_SetSandBoxPolicy = _lib.get("FPDF_SetSandBoxPolicy", "cdecl")
    FPDF_SetSandBoxPolicy.argtypes = [FPDF_DWORD, FPDF_BOOL]
    FPDF_SetSandBoxPolicy.restype = None
    break

# fpdfview.h: 370
for _lib in _libs.values():
    if not _lib.has("FPDF_LoadDocument", "cdecl"):
        continue
    FPDF_LoadDocument = _lib.get("FPDF_LoadDocument", "cdecl")
    FPDF_LoadDocument.argtypes = [FPDF_STRING, FPDF_BYTESTRING]
    FPDF_LoadDocument.restype = FPDF_DOCUMENT
    break

# fpdfview.h: 394
for _lib in _libs.values():
    if not _lib.has("FPDF_LoadMemDocument", "cdecl"):
        continue
    FPDF_LoadMemDocument = _lib.get("FPDF_LoadMemDocument", "cdecl")
    FPDF_LoadMemDocument.argtypes = [POINTER(None), c_int, FPDF_BYTESTRING]
    FPDF_LoadMemDocument.restype = FPDF_DOCUMENT
    break

# fpdfview.h: 419
for _lib in _libs.values():
    if not _lib.has("FPDF_LoadMemDocument64", "cdecl"):
        continue
    FPDF_LoadMemDocument64 = _lib.get("FPDF_LoadMemDocument64", "cdecl")
    FPDF_LoadMemDocument64.argtypes = [POINTER(None), c_size_t, FPDF_BYTESTRING]
    FPDF_LoadMemDocument64.restype = FPDF_DOCUMENT
    break

# fpdfview.h: 443
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'm_FileLen',
    'm_GetBlock',
    'm_Param',
]
struct_anon_4._fields_ = [
    ('m_FileLen', c_ulong),
    ('m_GetBlock', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_ulong, POINTER(c_ubyte), c_ulong)),
    ('m_Param', POINTER(None)),
]

FPDF_FILEACCESS = struct_anon_4# fpdfview.h: 443

# fpdfview.h: 539
class struct_FPDF_FILEHANDLER_(Structure):
    pass

struct_FPDF_FILEHANDLER_.__slots__ = [
    'clientData',
    'Release',
    'GetSize',
    'ReadBlock',
    'WriteBlock',
    'Flush',
    'Truncate',
]
struct_FPDF_FILEHANDLER_._fields_ = [
    ('clientData', POINTER(None)),
    ('Release', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('GetSize', CFUNCTYPE(UNCHECKED(FPDF_DWORD), POINTER(None))),
    ('ReadBlock', CFUNCTYPE(UNCHECKED(FPDF_RESULT), POINTER(None), FPDF_DWORD, POINTER(None), FPDF_DWORD)),
    ('WriteBlock', CFUNCTYPE(UNCHECKED(FPDF_RESULT), POINTER(None), FPDF_DWORD, POINTER(None), FPDF_DWORD)),
    ('Flush', CFUNCTYPE(UNCHECKED(FPDF_RESULT), POINTER(None))),
    ('Truncate', CFUNCTYPE(UNCHECKED(FPDF_RESULT), POINTER(None), FPDF_DWORD)),
]

FPDF_FILEHANDLER = struct_FPDF_FILEHANDLER_# fpdfview.h: 539

# fpdfview.h: 562
for _lib in _libs.values():
    if not _lib.has("FPDF_LoadCustomDocument", "cdecl"):
        continue
    FPDF_LoadCustomDocument = _lib.get("FPDF_LoadCustomDocument", "cdecl")
    FPDF_LoadCustomDocument.argtypes = [POINTER(FPDF_FILEACCESS), FPDF_BYTESTRING]
    FPDF_LoadCustomDocument.restype = FPDF_DOCUMENT
    break

# fpdfview.h: 575
for _lib in _libs.values():
    if not _lib.has("FPDF_GetFileVersion", "cdecl"):
        continue
    FPDF_GetFileVersion = _lib.get("FPDF_GetFileVersion", "cdecl")
    FPDF_GetFileVersion.argtypes = [FPDF_DOCUMENT, POINTER(c_int)]
    FPDF_GetFileVersion.restype = FPDF_BOOL
    break

# fpdfview.h: 600
for _lib in _libs.values():
    if not _lib.has("FPDF_GetLastError", "cdecl"):
        continue
    FPDF_GetLastError = _lib.get("FPDF_GetLastError", "cdecl")
    FPDF_GetLastError.argtypes = []
    FPDF_GetLastError.restype = c_ulong
    break

# fpdfview.h: 615
for _lib in _libs.values():
    if not _lib.has("FPDF_DocumentHasValidCrossReferenceTable", "cdecl"):
        continue
    FPDF_DocumentHasValidCrossReferenceTable = _lib.get("FPDF_DocumentHasValidCrossReferenceTable", "cdecl")
    FPDF_DocumentHasValidCrossReferenceTable.argtypes = [FPDF_DOCUMENT]
    FPDF_DocumentHasValidCrossReferenceTable.restype = FPDF_BOOL
    break

# fpdfview.h: 632
for _lib in _libs.values():
    if not _lib.has("FPDF_GetTrailerEnds", "cdecl"):
        continue
    FPDF_GetTrailerEnds = _lib.get("FPDF_GetTrailerEnds", "cdecl")
    FPDF_GetTrailerEnds.argtypes = [FPDF_DOCUMENT, POINTER(c_uint), c_ulong]
    FPDF_GetTrailerEnds.restype = c_ulong
    break

# fpdfview.h: 645
for _lib in _libs.values():
    if not _lib.has("FPDF_GetDocPermissions", "cdecl"):
        continue
    FPDF_GetDocPermissions = _lib.get("FPDF_GetDocPermissions", "cdecl")
    FPDF_GetDocPermissions.argtypes = [FPDF_DOCUMENT]
    FPDF_GetDocPermissions.restype = c_ulong
    break

# fpdfview.h: 656
for _lib in _libs.values():
    if not _lib.has("FPDF_GetSecurityHandlerRevision", "cdecl"):
        continue
    FPDF_GetSecurityHandlerRevision = _lib.get("FPDF_GetSecurityHandlerRevision", "cdecl")
    FPDF_GetSecurityHandlerRevision.argtypes = [FPDF_DOCUMENT]
    FPDF_GetSecurityHandlerRevision.restype = c_int
    break

# fpdfview.h: 664
for _lib in _libs.values():
    if not _lib.has("FPDF_GetPageCount", "cdecl"):
        continue
    FPDF_GetPageCount = _lib.get("FPDF_GetPageCount", "cdecl")
    FPDF_GetPageCount.argtypes = [FPDF_DOCUMENT]
    FPDF_GetPageCount.restype = c_int
    break

# fpdfview.h: 676
for _lib in _libs.values():
    if not _lib.has("FPDF_LoadPage", "cdecl"):
        continue
    FPDF_LoadPage = _lib.get("FPDF_LoadPage", "cdecl")
    FPDF_LoadPage.argtypes = [FPDF_DOCUMENT, c_int]
    FPDF_LoadPage.restype = FPDF_PAGE
    break

# fpdfview.h: 687
for _lib in _libs.values():
    if not _lib.has("FPDF_GetPageWidthF", "cdecl"):
        continue
    FPDF_GetPageWidthF = _lib.get("FPDF_GetPageWidthF", "cdecl")
    FPDF_GetPageWidthF.argtypes = [FPDF_PAGE]
    FPDF_GetPageWidthF.restype = c_float
    break

# fpdfview.h: 699
for _lib in _libs.values():
    if not _lib.has("FPDF_GetPageWidth", "cdecl"):
        continue
    FPDF_GetPageWidth = _lib.get("FPDF_GetPageWidth", "cdecl")
    FPDF_GetPageWidth.argtypes = [FPDF_PAGE]
    FPDF_GetPageWidth.restype = c_double
    break

# fpdfview.h: 709
for _lib in _libs.values():
    if not _lib.has("FPDF_GetPageHeightF", "cdecl"):
        continue
    FPDF_GetPageHeightF = _lib.get("FPDF_GetPageHeightF", "cdecl")
    FPDF_GetPageHeightF.argtypes = [FPDF_PAGE]
    FPDF_GetPageHeightF.restype = c_float
    break

# fpdfview.h: 721
for _lib in _libs.values():
    if not _lib.has("FPDF_GetPageHeight", "cdecl"):
        continue
    FPDF_GetPageHeight = _lib.get("FPDF_GetPageHeight", "cdecl")
    FPDF_GetPageHeight.argtypes = [FPDF_PAGE]
    FPDF_GetPageHeight.restype = c_double
    break

# fpdfview.h: 733
for _lib in _libs.values():
    if not _lib.has("FPDF_GetPageBoundingBox", "cdecl"):
        continue
    FPDF_GetPageBoundingBox = _lib.get("FPDF_GetPageBoundingBox", "cdecl")
    FPDF_GetPageBoundingBox.argtypes = [FPDF_PAGE, POINTER(FS_RECTF)]
    FPDF_GetPageBoundingBox.restype = FPDF_BOOL
    break

# fpdfview.h: 747
for _lib in _libs.values():
    if not _lib.has("FPDF_GetPageSizeByIndexF", "cdecl"):
        continue
    FPDF_GetPageSizeByIndexF = _lib.get("FPDF_GetPageSizeByIndexF", "cdecl")
    FPDF_GetPageSizeByIndexF.argtypes = [FPDF_DOCUMENT, c_int, POINTER(FS_SIZEF)]
    FPDF_GetPageSizeByIndexF.restype = FPDF_BOOL
    break

# fpdfview.h: 765
for _lib in _libs.values():
    if not _lib.has("FPDF_GetPageSizeByIndex", "cdecl"):
        continue
    FPDF_GetPageSizeByIndex = _lib.get("FPDF_GetPageSizeByIndex", "cdecl")
    FPDF_GetPageSizeByIndex.argtypes = [FPDF_DOCUMENT, c_int, POINTER(c_double), POINTER(c_double)]
    FPDF_GetPageSizeByIndex.restype = c_int
    break

# fpdfview.h: 813
class struct_FPDF_COLORSCHEME_(Structure):
    pass

struct_FPDF_COLORSCHEME_.__slots__ = [
    'path_fill_color',
    'path_stroke_color',
    'text_fill_color',
    'text_stroke_color',
]
struct_FPDF_COLORSCHEME_._fields_ = [
    ('path_fill_color', FPDF_DWORD),
    ('path_stroke_color', FPDF_DWORD),
    ('text_fill_color', FPDF_DWORD),
    ('text_stroke_color', FPDF_DWORD),
]

FPDF_COLORSCHEME = struct_FPDF_COLORSCHEME_# fpdfview.h: 813

# fpdfview.h: 873
for _lib in _libs.values():
    if not _lib.has("FPDF_RenderPageBitmap", "cdecl"):
        continue
    FPDF_RenderPageBitmap = _lib.get("FPDF_RenderPageBitmap", "cdecl")
    FPDF_RenderPageBitmap.argtypes = [FPDF_BITMAP, FPDF_PAGE, c_int, c_int, c_int, c_int, c_int, c_int]
    FPDF_RenderPageBitmap.restype = None
    break

# fpdfview.h: 901
for _lib in _libs.values():
    if not _lib.has("FPDF_RenderPageBitmapWithMatrix", "cdecl"):
        continue
    FPDF_RenderPageBitmapWithMatrix = _lib.get("FPDF_RenderPageBitmapWithMatrix", "cdecl")
    FPDF_RenderPageBitmapWithMatrix.argtypes = [FPDF_BITMAP, FPDF_PAGE, POINTER(FS_MATRIX), POINTER(FS_RECTF), c_int]
    FPDF_RenderPageBitmapWithMatrix.restype = None
    break

# fpdfview.h: 929
for _lib in _libs.values():
    if not _lib.has("FPDF_ClosePage", "cdecl"):
        continue
    FPDF_ClosePage = _lib.get("FPDF_ClosePage", "cdecl")
    FPDF_ClosePage.argtypes = [FPDF_PAGE]
    FPDF_ClosePage.restype = None
    break

# fpdfview.h: 937
for _lib in _libs.values():
    if not _lib.has("FPDF_CloseDocument", "cdecl"):
        continue
    FPDF_CloseDocument = _lib.get("FPDF_CloseDocument", "cdecl")
    FPDF_CloseDocument.argtypes = [FPDF_DOCUMENT]
    FPDF_CloseDocument.restype = None
    break

# fpdfview.h: 980
for _lib in _libs.values():
    if not _lib.has("FPDF_DeviceToPage", "cdecl"):
        continue
    FPDF_DeviceToPage = _lib.get("FPDF_DeviceToPage", "cdecl")
    FPDF_DeviceToPage.argtypes = [FPDF_PAGE, c_int, c_int, c_int, c_int, c_int, c_int, c_int, POINTER(c_double), POINTER(c_double)]
    FPDF_DeviceToPage.restype = FPDF_BOOL
    break

# fpdfview.h: 1017
for _lib in _libs.values():
    if not _lib.has("FPDF_PageToDevice", "cdecl"):
        continue
    FPDF_PageToDevice = _lib.get("FPDF_PageToDevice", "cdecl")
    FPDF_PageToDevice.argtypes = [FPDF_PAGE, c_int, c_int, c_int, c_int, c_int, c_double, c_double, POINTER(c_int), POINTER(c_int)]
    FPDF_PageToDevice.restype = FPDF_BOOL
    break

# fpdfview.h: 1058
for _lib in _libs.values():
    if not _lib.has("FPDFBitmap_Create", "cdecl"):
        continue
    FPDFBitmap_Create = _lib.get("FPDFBitmap_Create", "cdecl")
    FPDFBitmap_Create.argtypes = [c_int, c_int, c_int]
    FPDFBitmap_Create.restype = FPDF_BITMAP
    break

# fpdfview.h: 1107
for _lib in _libs.values():
    if not _lib.has("FPDFBitmap_CreateEx", "cdecl"):
        continue
    FPDFBitmap_CreateEx = _lib.get("FPDFBitmap_CreateEx", "cdecl")
    FPDFBitmap_CreateEx.argtypes = [c_int, c_int, c_int, POINTER(None), c_int]
    FPDFBitmap_CreateEx.restype = FPDF_BITMAP
    break

# fpdfview.h: 1123
for _lib in _libs.values():
    if not _lib.has("FPDFBitmap_GetFormat", "cdecl"):
        continue
    FPDFBitmap_GetFormat = _lib.get("FPDFBitmap_GetFormat", "cdecl")
    FPDFBitmap_GetFormat.argtypes = [FPDF_BITMAP]
    FPDFBitmap_GetFormat.restype = c_int
    break

# fpdfview.h: 1149
for _lib in _libs.values():
    if not _lib.has("FPDFBitmap_FillRect", "cdecl"):
        continue
    FPDFBitmap_FillRect = _lib.get("FPDFBitmap_FillRect", "cdecl")
    FPDFBitmap_FillRect.argtypes = [FPDF_BITMAP, c_int, c_int, c_int, c_int, FPDF_DWORD]
    FPDFBitmap_FillRect.restype = None
    break

# fpdfview.h: 1172
for _lib in _libs.values():
    if not _lib.has("FPDFBitmap_GetBuffer", "cdecl"):
        continue
    FPDFBitmap_GetBuffer = _lib.get("FPDFBitmap_GetBuffer", "cdecl")
    FPDFBitmap_GetBuffer.argtypes = [FPDF_BITMAP]
    FPDFBitmap_GetBuffer.restype = POINTER(c_ubyte)
    FPDFBitmap_GetBuffer.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# fpdfview.h: 1181
for _lib in _libs.values():
    if not _lib.has("FPDFBitmap_GetWidth", "cdecl"):
        continue
    FPDFBitmap_GetWidth = _lib.get("FPDFBitmap_GetWidth", "cdecl")
    FPDFBitmap_GetWidth.argtypes = [FPDF_BITMAP]
    FPDFBitmap_GetWidth.restype = c_int
    break

# fpdfview.h: 1190
for _lib in _libs.values():
    if not _lib.has("FPDFBitmap_GetHeight", "cdecl"):
        continue
    FPDFBitmap_GetHeight = _lib.get("FPDFBitmap_GetHeight", "cdecl")
    FPDFBitmap_GetHeight.argtypes = [FPDF_BITMAP]
    FPDFBitmap_GetHeight.restype = c_int
    break

# fpdfview.h: 1201
for _lib in _libs.values():
    if not _lib.has("FPDFBitmap_GetStride", "cdecl"):
        continue
    FPDFBitmap_GetStride = _lib.get("FPDFBitmap_GetStride", "cdecl")
    FPDFBitmap_GetStride.argtypes = [FPDF_BITMAP]
    FPDFBitmap_GetStride.restype = c_int
    break

# fpdfview.h: 1213
for _lib in _libs.values():
    if not _lib.has("FPDFBitmap_Destroy", "cdecl"):
        continue
    FPDFBitmap_Destroy = _lib.get("FPDFBitmap_Destroy", "cdecl")
    FPDFBitmap_Destroy.argtypes = [FPDF_BITMAP]
    FPDFBitmap_Destroy.restype = None
    break

# fpdfview.h: 1222
for _lib in _libs.values():
    if not _lib.has("FPDF_VIEWERREF_GetPrintScaling", "cdecl"):
        continue
    FPDF_VIEWERREF_GetPrintScaling = _lib.get("FPDF_VIEWERREF_GetPrintScaling", "cdecl")
    FPDF_VIEWERREF_GetPrintScaling.argtypes = [FPDF_DOCUMENT]
    FPDF_VIEWERREF_GetPrintScaling.restype = FPDF_BOOL
    break

# fpdfview.h: 1231
for _lib in _libs.values():
    if not _lib.has("FPDF_VIEWERREF_GetNumCopies", "cdecl"):
        continue
    FPDF_VIEWERREF_GetNumCopies = _lib.get("FPDF_VIEWERREF_GetNumCopies", "cdecl")
    FPDF_VIEWERREF_GetNumCopies.argtypes = [FPDF_DOCUMENT]
    FPDF_VIEWERREF_GetNumCopies.restype = c_int
    break

# fpdfview.h: 1240
for _lib in _libs.values():
    if not _lib.has("FPDF_VIEWERREF_GetPrintPageRange", "cdecl"):
        continue
    FPDF_VIEWERREF_GetPrintPageRange = _lib.get("FPDF_VIEWERREF_GetPrintPageRange", "cdecl")
    FPDF_VIEWERREF_GetPrintPageRange.argtypes = [FPDF_DOCUMENT]
    FPDF_VIEWERREF_GetPrintPageRange.restype = FPDF_PAGERANGE
    break

# fpdfview.h: 1250
for _lib in _libs.values():
    if not _lib.has("FPDF_VIEWERREF_GetPrintPageRangeCount", "cdecl"):
        continue
    FPDF_VIEWERREF_GetPrintPageRangeCount = _lib.get("FPDF_VIEWERREF_GetPrintPageRangeCount", "cdecl")
    FPDF_VIEWERREF_GetPrintPageRangeCount.argtypes = [FPDF_PAGERANGE]
    FPDF_VIEWERREF_GetPrintPageRangeCount.restype = c_size_t
    break

# fpdfview.h: 1262
for _lib in _libs.values():
    if not _lib.has("FPDF_VIEWERREF_GetPrintPageRangeElement", "cdecl"):
        continue
    FPDF_VIEWERREF_GetPrintPageRangeElement = _lib.get("FPDF_VIEWERREF_GetPrintPageRangeElement", "cdecl")
    FPDF_VIEWERREF_GetPrintPageRangeElement.argtypes = [FPDF_PAGERANGE, c_size_t]
    FPDF_VIEWERREF_GetPrintPageRangeElement.restype = c_int
    break

# fpdfview.h: 1272
for _lib in _libs.values():
    if not _lib.has("FPDF_VIEWERREF_GetDuplex", "cdecl"):
        continue
    FPDF_VIEWERREF_GetDuplex = _lib.get("FPDF_VIEWERREF_GetDuplex", "cdecl")
    FPDF_VIEWERREF_GetDuplex.argtypes = [FPDF_DOCUMENT]
    FPDF_VIEWERREF_GetDuplex.restype = FPDF_DUPLEXTYPE
    break

# fpdfview.h: 1290
for _lib in _libs.values():
    if not _lib.has("FPDF_VIEWERREF_GetName", "cdecl"):
        continue
    FPDF_VIEWERREF_GetName = _lib.get("FPDF_VIEWERREF_GetName", "cdecl")
    FPDF_VIEWERREF_GetName.argtypes = [FPDF_DOCUMENT, FPDF_BYTESTRING, String, c_ulong]
    FPDF_VIEWERREF_GetName.restype = c_ulong
    break

# fpdfview.h: 1302
for _lib in _libs.values():
    if not _lib.has("FPDF_CountNamedDests", "cdecl"):
        continue
    FPDF_CountNamedDests = _lib.get("FPDF_CountNamedDests", "cdecl")
    FPDF_CountNamedDests.argtypes = [FPDF_DOCUMENT]
    FPDF_CountNamedDests.restype = FPDF_DWORD
    break

# fpdfview.h: 1312
for _lib in _libs.values():
    if not _lib.has("FPDF_GetNamedDestByName", "cdecl"):
        continue
    FPDF_GetNamedDestByName = _lib.get("FPDF_GetNamedDestByName", "cdecl")
    FPDF_GetNamedDestByName.argtypes = [FPDF_DOCUMENT, FPDF_BYTESTRING]
    FPDF_GetNamedDestByName.restype = FPDF_DEST
    break

# fpdfview.h: 1335
for _lib in _libs.values():
    if not _lib.has("FPDF_GetNamedDest", "cdecl"):
        continue
    FPDF_GetNamedDest = _lib.get("FPDF_GetNamedDest", "cdecl")
    FPDF_GetNamedDest.argtypes = [FPDF_DOCUMENT, c_int, POINTER(None), POINTER(c_long)]
    FPDF_GetNamedDest.restype = FPDF_DEST
    break

# fpdfview.h: 1347
for _lib in _libs.values():
    if not _lib.has("FPDF_GetXFAPacketCount", "cdecl"):
        continue
    FPDF_GetXFAPacketCount = _lib.get("FPDF_GetXFAPacketCount", "cdecl")
    FPDF_GetXFAPacketCount.argtypes = [FPDF_DOCUMENT]
    FPDF_GetXFAPacketCount.restype = c_int
    break

# fpdfview.h: 1365
for _lib in _libs.values():
    if not _lib.has("FPDF_GetXFAPacketName", "cdecl"):
        continue
    FPDF_GetXFAPacketName = _lib.get("FPDF_GetXFAPacketName", "cdecl")
    FPDF_GetXFAPacketName.argtypes = [FPDF_DOCUMENT, c_int, POINTER(None), c_ulong]
    FPDF_GetXFAPacketName.restype = c_ulong
    break

# fpdfview.h: 1392
for _lib in _libs.values():
    if not _lib.has("FPDF_GetXFAPacketContent", "cdecl"):
        continue
    FPDF_GetXFAPacketContent = _lib.get("FPDF_GetXFAPacketContent", "cdecl")
    FPDF_GetXFAPacketContent.argtypes = [FPDF_DOCUMENT, c_int, POINTER(None), c_ulong, POINTER(c_ulong)]
    FPDF_GetXFAPacketContent.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 52
class struct__IPDF_JsPlatform(Structure):
    pass

struct__IPDF_JsPlatform.__slots__ = [
    'version',
    'app_alert',
    'app_beep',
    'app_response',
    'Doc_getFilePath',
    'Doc_mail',
    'Doc_print',
    'Doc_submitForm',
    'Doc_gotoPage',
    'Field_browse',
    'm_pFormfillinfo',
    'm_isolate',
    'm_v8EmbedderSlot',
]
struct__IPDF_JsPlatform._fields_ = [
    ('version', c_int),
    ('app_alert', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__IPDF_JsPlatform), FPDF_WIDESTRING, FPDF_WIDESTRING, c_int, c_int)),
    ('app_beep', CFUNCTYPE(UNCHECKED(None), POINTER(struct__IPDF_JsPlatform), c_int)),
    ('app_response', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__IPDF_JsPlatform), FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_BOOL, POINTER(None), c_int)),
    ('Doc_getFilePath', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__IPDF_JsPlatform), POINTER(None), c_int)),
    ('Doc_mail', CFUNCTYPE(UNCHECKED(None), POINTER(struct__IPDF_JsPlatform), POINTER(None), c_int, FPDF_BOOL, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING)),
    ('Doc_print', CFUNCTYPE(UNCHECKED(None), POINTER(struct__IPDF_JsPlatform), FPDF_BOOL, c_int, c_int, FPDF_BOOL, FPDF_BOOL, FPDF_BOOL, FPDF_BOOL, FPDF_BOOL)),
    ('Doc_submitForm', CFUNCTYPE(UNCHECKED(None), POINTER(struct__IPDF_JsPlatform), POINTER(None), c_int, FPDF_WIDESTRING)),
    ('Doc_gotoPage', CFUNCTYPE(UNCHECKED(None), POINTER(struct__IPDF_JsPlatform), c_int)),
    ('Field_browse', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__IPDF_JsPlatform), POINTER(None), c_int)),
    ('m_pFormfillinfo', POINTER(None)),
    ('m_isolate', POINTER(None)),
    ('m_v8EmbedderSlot', c_uint),
]

IPDF_JSPLATFORM = struct__IPDF_JsPlatform# fpdf_formfill.h: 323

TimerCallback = CFUNCTYPE(UNCHECKED(None), c_int)# fpdf_formfill.h: 341

# fpdf_formfill.h: 355
class struct__FPDF_SYSTEMTIME(Structure):
    pass

struct__FPDF_SYSTEMTIME.__slots__ = [
    'wYear',
    'wMonth',
    'wDayOfWeek',
    'wDay',
    'wHour',
    'wMinute',
    'wSecond',
    'wMilliseconds',
]
struct__FPDF_SYSTEMTIME._fields_ = [
    ('wYear', c_ushort),
    ('wMonth', c_ushort),
    ('wDayOfWeek', c_ushort),
    ('wDay', c_ushort),
    ('wHour', c_ushort),
    ('wMinute', c_ushort),
    ('wSecond', c_ushort),
    ('wMilliseconds', c_ushort),
]

FPDF_SYSTEMTIME = struct__FPDF_SYSTEMTIME# fpdf_formfill.h: 355

# fpdf_formfill.h: 377
class struct__FPDF_FORMFILLINFO(Structure):
    pass

struct__FPDF_FORMFILLINFO.__slots__ = [
    'version',
    'Release',
    'FFI_Invalidate',
    'FFI_OutputSelectedRect',
    'FFI_SetCursor',
    'FFI_SetTimer',
    'FFI_KillTimer',
    'FFI_GetLocalTime',
    'FFI_OnChange',
    'FFI_GetPage',
    'FFI_GetCurrentPage',
    'FFI_GetRotation',
    'FFI_ExecuteNamedAction',
    'FFI_SetTextFieldFocus',
    'FFI_DoURIAction',
    'FFI_DoGoToAction',
    'm_pJsPlatform',
    'xfa_disabled',
    'FFI_DisplayCaret',
    'FFI_GetCurrentPageIndex',
    'FFI_SetCurrentPage',
    'FFI_GotoURL',
    'FFI_GetPageViewRect',
    'FFI_PageEvent',
    'FFI_PopupMenu',
    'FFI_OpenFile',
    'FFI_EmailTo',
    'FFI_UploadTo',
    'FFI_GetPlatform',
    'FFI_GetLanguage',
    'FFI_DownloadFromURL',
    'FFI_PostRequestURL',
    'FFI_PutRequestURL',
    'FFI_OnFocusChange',
    'FFI_DoURIActionWithKeyboardModifier',
]
struct__FPDF_FORMFILLINFO._fields_ = [
    ('version', c_int),
    ('Release', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO))),
    ('FFI_Invalidate', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_PAGE, c_double, c_double, c_double, c_double)),
    ('FFI_OutputSelectedRect', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_PAGE, c_double, c_double, c_double, c_double)),
    ('FFI_SetCursor', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), c_int)),
    ('FFI_SetTimer', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__FPDF_FORMFILLINFO), c_int, TimerCallback)),
    ('FFI_KillTimer', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), c_int)),
    ('FFI_GetLocalTime', CFUNCTYPE(UNCHECKED(FPDF_SYSTEMTIME), POINTER(struct__FPDF_FORMFILLINFO))),
    ('FFI_OnChange', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO))),
    ('FFI_GetPage', CFUNCTYPE(UNCHECKED(FPDF_PAGE), POINTER(struct__FPDF_FORMFILLINFO), FPDF_DOCUMENT, c_int)),
    ('FFI_GetCurrentPage', CFUNCTYPE(UNCHECKED(FPDF_PAGE), POINTER(struct__FPDF_FORMFILLINFO), FPDF_DOCUMENT)),
    ('FFI_GetRotation', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__FPDF_FORMFILLINFO), FPDF_PAGE)),
    ('FFI_ExecuteNamedAction', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_BYTESTRING)),
    ('FFI_SetTextFieldFocus', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_WIDESTRING, FPDF_DWORD, FPDF_BOOL)),
    ('FFI_DoURIAction', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_BYTESTRING)),
    ('FFI_DoGoToAction', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), c_int, c_int, POINTER(c_float), c_int)),
    ('m_pJsPlatform', POINTER(IPDF_JSPLATFORM)),
    ('xfa_disabled', FPDF_BOOL),
    ('FFI_DisplayCaret', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_PAGE, FPDF_BOOL, c_double, c_double, c_double, c_double)),
    ('FFI_GetCurrentPageIndex', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__FPDF_FORMFILLINFO), FPDF_DOCUMENT)),
    ('FFI_SetCurrentPage', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_DOCUMENT, c_int)),
    ('FFI_GotoURL', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_DOCUMENT, FPDF_WIDESTRING)),
    ('FFI_GetPageViewRect', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_PAGE, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double))),
    ('FFI_PageEvent', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), c_int, FPDF_DWORD)),
    ('FFI_PopupMenu', CFUNCTYPE(UNCHECKED(FPDF_BOOL), POINTER(struct__FPDF_FORMFILLINFO), FPDF_PAGE, FPDF_WIDGET, c_int, c_float, c_float)),
    ('FFI_OpenFile', CFUNCTYPE(UNCHECKED(POINTER(FPDF_FILEHANDLER)), POINTER(struct__FPDF_FORMFILLINFO), c_int, FPDF_WIDESTRING, String)),
    ('FFI_EmailTo', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), POINTER(FPDF_FILEHANDLER), FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING)),
    ('FFI_UploadTo', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), POINTER(FPDF_FILEHANDLER), c_int, FPDF_WIDESTRING)),
    ('FFI_GetPlatform', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__FPDF_FORMFILLINFO), POINTER(None), c_int)),
    ('FFI_GetLanguage', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__FPDF_FORMFILLINFO), POINTER(None), c_int)),
    ('FFI_DownloadFromURL', CFUNCTYPE(UNCHECKED(POINTER(FPDF_FILEHANDLER)), POINTER(struct__FPDF_FORMFILLINFO), FPDF_WIDESTRING)),
    ('FFI_PostRequestURL', CFUNCTYPE(UNCHECKED(FPDF_BOOL), POINTER(struct__FPDF_FORMFILLINFO), FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, POINTER(FPDF_BSTR))),
    ('FFI_PutRequestURL', CFUNCTYPE(UNCHECKED(FPDF_BOOL), POINTER(struct__FPDF_FORMFILLINFO), FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING)),
    ('FFI_OnFocusChange', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_ANNOTATION, c_int)),
    ('FFI_DoURIActionWithKeyboardModifier', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_BYTESTRING, c_int)),
]

FPDF_FORMFILLINFO = struct__FPDF_FORMFILLINFO# fpdf_formfill.h: 1139

# fpdf_formfill.h: 1155
for _lib in _libs.values():
    if not _lib.has("FPDFDOC_InitFormFillEnvironment", "cdecl"):
        continue
    FPDFDOC_InitFormFillEnvironment = _lib.get("FPDFDOC_InitFormFillEnvironment", "cdecl")
    FPDFDOC_InitFormFillEnvironment.argtypes = [FPDF_DOCUMENT, POINTER(FPDF_FORMFILLINFO)]
    FPDFDOC_InitFormFillEnvironment.restype = FPDF_FORMHANDLE
    break

# fpdf_formfill.h: 1170
for _lib in _libs.values():
    if not _lib.has("FPDFDOC_ExitFormFillEnvironment", "cdecl"):
        continue
    FPDFDOC_ExitFormFillEnvironment = _lib.get("FPDFDOC_ExitFormFillEnvironment", "cdecl")
    FPDFDOC_ExitFormFillEnvironment.argtypes = [FPDF_FORMHANDLE]
    FPDFDOC_ExitFormFillEnvironment.restype = None
    break

# fpdf_formfill.h: 1183
for _lib in _libs.values():
    if not _lib.has("FORM_OnAfterLoadPage", "cdecl"):
        continue
    FORM_OnAfterLoadPage = _lib.get("FORM_OnAfterLoadPage", "cdecl")
    FORM_OnAfterLoadPage.argtypes = [FPDF_PAGE, FPDF_FORMHANDLE]
    FORM_OnAfterLoadPage.restype = None
    break

# fpdf_formfill.h: 1197
for _lib in _libs.values():
    if not _lib.has("FORM_OnBeforeClosePage", "cdecl"):
        continue
    FORM_OnBeforeClosePage = _lib.get("FORM_OnBeforeClosePage", "cdecl")
    FORM_OnBeforeClosePage.argtypes = [FPDF_PAGE, FPDF_FORMHANDLE]
    FORM_OnBeforeClosePage.restype = None
    break

# fpdf_formfill.h: 1215
for _lib in _libs.values():
    if not _lib.has("FORM_DoDocumentJSAction", "cdecl"):
        continue
    FORM_DoDocumentJSAction = _lib.get("FORM_DoDocumentJSAction", "cdecl")
    FORM_DoDocumentJSAction.argtypes = [FPDF_FORMHANDLE]
    FORM_DoDocumentJSAction.restype = None
    break

# fpdf_formfill.h: 1231
for _lib in _libs.values():
    if not _lib.has("FORM_DoDocumentOpenAction", "cdecl"):
        continue
    FORM_DoDocumentOpenAction = _lib.get("FORM_DoDocumentOpenAction", "cdecl")
    FORM_DoDocumentOpenAction.argtypes = [FPDF_FORMHANDLE]
    FORM_DoDocumentOpenAction.restype = None
    break

# fpdf_formfill.h: 1260
for _lib in _libs.values():
    if not _lib.has("FORM_DoDocumentAAction", "cdecl"):
        continue
    FORM_DoDocumentAAction = _lib.get("FORM_DoDocumentAAction", "cdecl")
    FORM_DoDocumentAAction.argtypes = [FPDF_FORMHANDLE, c_int]
    FORM_DoDocumentAAction.restype = None
    break

# fpdf_formfill.h: 1285
for _lib in _libs.values():
    if not _lib.has("FORM_DoPageAAction", "cdecl"):
        continue
    FORM_DoPageAAction = _lib.get("FORM_DoPageAAction", "cdecl")
    FORM_DoPageAAction.argtypes = [FPDF_PAGE, FPDF_FORMHANDLE, c_int]
    FORM_DoPageAAction.restype = None
    break

# fpdf_formfill.h: 1304
for _lib in _libs.values():
    if not _lib.has("FORM_OnMouseMove", "cdecl"):
        continue
    FORM_OnMouseMove = _lib.get("FORM_OnMouseMove", "cdecl")
    FORM_OnMouseMove.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_double, c_double]
    FORM_OnMouseMove.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1335
for _lib in _libs.values():
    if not _lib.has("FORM_OnMouseWheel", "cdecl"):
        continue
    FORM_OnMouseWheel = _lib.get("FORM_OnMouseWheel", "cdecl")
    FORM_OnMouseWheel.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, POINTER(FS_POINTF), c_int, c_int]
    FORM_OnMouseWheel.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1360
for _lib in _libs.values():
    if not _lib.has("FORM_OnFocus", "cdecl"):
        continue
    FORM_OnFocus = _lib.get("FORM_OnFocus", "cdecl")
    FORM_OnFocus.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_double, c_double]
    FORM_OnFocus.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1382
for _lib in _libs.values():
    if not _lib.has("FORM_OnLButtonDown", "cdecl"):
        continue
    FORM_OnLButtonDown = _lib.get("FORM_OnLButtonDown", "cdecl")
    FORM_OnLButtonDown.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_double, c_double]
    FORM_OnLButtonDown.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1395
for _lib in _libs.values():
    if not _lib.has("FORM_OnRButtonDown", "cdecl"):
        continue
    FORM_OnRButtonDown = _lib.get("FORM_OnRButtonDown", "cdecl")
    FORM_OnRButtonDown.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_double, c_double]
    FORM_OnRButtonDown.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1414
for _lib in _libs.values():
    if not _lib.has("FORM_OnLButtonUp", "cdecl"):
        continue
    FORM_OnLButtonUp = _lib.get("FORM_OnLButtonUp", "cdecl")
    FORM_OnLButtonUp.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_double, c_double]
    FORM_OnLButtonUp.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1427
for _lib in _libs.values():
    if not _lib.has("FORM_OnRButtonUp", "cdecl"):
        continue
    FORM_OnRButtonUp = _lib.get("FORM_OnRButtonUp", "cdecl")
    FORM_OnRButtonUp.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_double, c_double]
    FORM_OnRButtonUp.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1450
for _lib in _libs.values():
    if not _lib.has("FORM_OnLButtonDoubleClick", "cdecl"):
        continue
    FORM_OnLButtonDoubleClick = _lib.get("FORM_OnLButtonDoubleClick", "cdecl")
    FORM_OnLButtonDoubleClick.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_double, c_double]
    FORM_OnLButtonDoubleClick.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1470
for _lib in _libs.values():
    if not _lib.has("FORM_OnKeyDown", "cdecl"):
        continue
    FORM_OnKeyDown = _lib.get("FORM_OnKeyDown", "cdecl")
    FORM_OnKeyDown.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_int]
    FORM_OnKeyDown.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1492
for _lib in _libs.values():
    if not _lib.has("FORM_OnKeyUp", "cdecl"):
        continue
    FORM_OnKeyUp = _lib.get("FORM_OnKeyUp", "cdecl")
    FORM_OnKeyUp.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_int]
    FORM_OnKeyUp.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1511
for _lib in _libs.values():
    if not _lib.has("FORM_OnChar", "cdecl"):
        continue
    FORM_OnChar = _lib.get("FORM_OnChar", "cdecl")
    FORM_OnChar.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_int]
    FORM_OnChar.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1534
for _lib in _libs.values():
    if not _lib.has("FORM_GetFocusedText", "cdecl"):
        continue
    FORM_GetFocusedText = _lib.get("FORM_GetFocusedText", "cdecl")
    FORM_GetFocusedText.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, POINTER(None), c_ulong]
    FORM_GetFocusedText.restype = c_ulong
    break

# fpdf_formfill.h: 1557
for _lib in _libs.values():
    if not _lib.has("FORM_GetSelectedText", "cdecl"):
        continue
    FORM_GetSelectedText = _lib.get("FORM_GetSelectedText", "cdecl")
    FORM_GetSelectedText.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, POINTER(None), c_ulong]
    FORM_GetSelectedText.restype = c_ulong
    break

# fpdf_formfill.h: 1577
for _lib in _libs.values():
    if not _lib.has("FORM_ReplaceSelection", "cdecl"):
        continue
    FORM_ReplaceSelection = _lib.get("FORM_ReplaceSelection", "cdecl")
    FORM_ReplaceSelection.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, FPDF_WIDESTRING]
    FORM_ReplaceSelection.restype = None
    break

# fpdf_formfill.h: 1594
for _lib in _libs.values():
    if not _lib.has("FORM_SelectAllText", "cdecl"):
        continue
    FORM_SelectAllText = _lib.get("FORM_SelectAllText", "cdecl")
    FORM_SelectAllText.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE]
    FORM_SelectAllText.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1607
for _lib in _libs.values():
    if not _lib.has("FORM_CanUndo", "cdecl"):
        continue
    FORM_CanUndo = _lib.get("FORM_CanUndo", "cdecl")
    FORM_CanUndo.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE]
    FORM_CanUndo.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1621
for _lib in _libs.values():
    if not _lib.has("FORM_CanRedo", "cdecl"):
        continue
    FORM_CanRedo = _lib.get("FORM_CanRedo", "cdecl")
    FORM_CanRedo.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE]
    FORM_CanRedo.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1634
for _lib in _libs.values():
    if not _lib.has("FORM_Undo", "cdecl"):
        continue
    FORM_Undo = _lib.get("FORM_Undo", "cdecl")
    FORM_Undo.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE]
    FORM_Undo.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1647
for _lib in _libs.values():
    if not _lib.has("FORM_Redo", "cdecl"):
        continue
    FORM_Redo = _lib.get("FORM_Redo", "cdecl")
    FORM_Redo.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE]
    FORM_Redo.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1662
for _lib in _libs.values():
    if not _lib.has("FORM_ForceToKillFocus", "cdecl"):
        continue
    FORM_ForceToKillFocus = _lib.get("FORM_ForceToKillFocus", "cdecl")
    FORM_ForceToKillFocus.argtypes = [FPDF_FORMHANDLE]
    FORM_ForceToKillFocus.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1687
for _lib in _libs.values():
    if not _lib.has("FORM_GetFocusedAnnot", "cdecl"):
        continue
    FORM_GetFocusedAnnot = _lib.get("FORM_GetFocusedAnnot", "cdecl")
    FORM_GetFocusedAnnot.argtypes = [FPDF_FORMHANDLE, POINTER(c_int), POINTER(FPDF_ANNOTATION)]
    FORM_GetFocusedAnnot.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1706
for _lib in _libs.values():
    if not _lib.has("FORM_SetFocusedAnnot", "cdecl"):
        continue
    FORM_SetFocusedAnnot = _lib.get("FORM_SetFocusedAnnot", "cdecl")
    FORM_SetFocusedAnnot.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION]
    FORM_SetFocusedAnnot.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1762
for _lib in _libs.values():
    if not _lib.has("FPDFPage_HasFormFieldAtPoint", "cdecl"):
        continue
    FPDFPage_HasFormFieldAtPoint = _lib.get("FPDFPage_HasFormFieldAtPoint", "cdecl")
    FPDFPage_HasFormFieldAtPoint.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_double, c_double]
    FPDFPage_HasFormFieldAtPoint.restype = c_int
    break

# fpdf_formfill.h: 1781
for _lib in _libs.values():
    if not _lib.has("FPDFPage_FormFieldZOrderAtPoint", "cdecl"):
        continue
    FPDFPage_FormFieldZOrderAtPoint = _lib.get("FPDFPage_FormFieldZOrderAtPoint", "cdecl")
    FPDFPage_FormFieldZOrderAtPoint.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_double, c_double]
    FPDFPage_FormFieldZOrderAtPoint.restype = c_int
    break

# fpdf_formfill.h: 1809
for _lib in _libs.values():
    if not _lib.has("FPDF_SetFormFieldHighlightColor", "cdecl"):
        continue
    FPDF_SetFormFieldHighlightColor = _lib.get("FPDF_SetFormFieldHighlightColor", "cdecl")
    FPDF_SetFormFieldHighlightColor.argtypes = [FPDF_FORMHANDLE, c_int, c_ulong]
    FPDF_SetFormFieldHighlightColor.restype = None
    break

# fpdf_formfill.h: 1828
for _lib in _libs.values():
    if not _lib.has("FPDF_SetFormFieldHighlightAlpha", "cdecl"):
        continue
    FPDF_SetFormFieldHighlightAlpha = _lib.get("FPDF_SetFormFieldHighlightAlpha", "cdecl")
    FPDF_SetFormFieldHighlightAlpha.argtypes = [FPDF_FORMHANDLE, c_ubyte]
    FPDF_SetFormFieldHighlightAlpha.restype = None
    break

# fpdf_formfill.h: 1843
for _lib in _libs.values():
    if not _lib.has("FPDF_RemoveFormFieldHighlight", "cdecl"):
        continue
    FPDF_RemoveFormFieldHighlight = _lib.get("FPDF_RemoveFormFieldHighlight", "cdecl")
    FPDF_RemoveFormFieldHighlight.argtypes = [FPDF_FORMHANDLE]
    FPDF_RemoveFormFieldHighlight.restype = None
    break

# fpdf_formfill.h: 1882
for _lib in _libs.values():
    if not _lib.has("FPDF_FFLDraw", "cdecl"):
        continue
    FPDF_FFLDraw = _lib.get("FPDF_FFLDraw", "cdecl")
    FPDF_FFLDraw.argtypes = [FPDF_FORMHANDLE, FPDF_BITMAP, FPDF_PAGE, c_int, c_int, c_int, c_int, c_int, c_int]
    FPDF_FFLDraw.restype = None
    break

# fpdf_formfill.h: 1915
for _lib in _libs.values():
    if not _lib.has("FPDF_GetFormType", "cdecl"):
        continue
    FPDF_GetFormType = _lib.get("FPDF_GetFormType", "cdecl")
    FPDF_GetFormType.argtypes = [FPDF_DOCUMENT]
    FPDF_GetFormType.restype = c_int
    break

# fpdf_formfill.h: 1941
for _lib in _libs.values():
    if not _lib.has("FORM_SetIndexSelected", "cdecl"):
        continue
    FORM_SetIndexSelected = _lib.get("FORM_SetIndexSelected", "cdecl")
    FORM_SetIndexSelected.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, FPDF_BOOL]
    FORM_SetIndexSelected.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1966
for _lib in _libs.values():
    if not _lib.has("FORM_IsIndexSelected", "cdecl"):
        continue
    FORM_IsIndexSelected = _lib.get("FORM_IsIndexSelected", "cdecl")
    FORM_IsIndexSelected.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int]
    FORM_IsIndexSelected.restype = FPDF_BOOL
    break

# fpdf_formfill.h: 1978
for _lib in _libs.values():
    if not _lib.has("FPDF_LoadXFA", "cdecl"):
        continue
    FPDF_LoadXFA = _lib.get("FPDF_LoadXFA", "cdecl")
    FPDF_LoadXFA.argtypes = [FPDF_DOCUMENT]
    FPDF_LoadXFA.restype = FPDF_BOOL
    break

enum_FPDFANNOT_COLORTYPE = c_int# fpdf_annot.h: 98

FPDFANNOT_COLORTYPE_Color = 0# fpdf_annot.h: 98

FPDFANNOT_COLORTYPE_InteriorColor = (FPDFANNOT_COLORTYPE_Color + 1)# fpdf_annot.h: 98

FPDFANNOT_COLORTYPE = enum_FPDFANNOT_COLORTYPE# fpdf_annot.h: 98

# fpdf_annot.h: 120
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_IsSupportedSubtype", "cdecl"):
        continue
    FPDFAnnot_IsSupportedSubtype = _lib.get("FPDFAnnot_IsSupportedSubtype", "cdecl")
    FPDFAnnot_IsSupportedSubtype.argtypes = [FPDF_ANNOTATION_SUBTYPE]
    FPDFAnnot_IsSupportedSubtype.restype = FPDF_BOOL
    break

# fpdf_annot.h: 133
for _lib in _libs.values():
    if not _lib.has("FPDFPage_CreateAnnot", "cdecl"):
        continue
    FPDFPage_CreateAnnot = _lib.get("FPDFPage_CreateAnnot", "cdecl")
    FPDFPage_CreateAnnot.argtypes = [FPDF_PAGE, FPDF_ANNOTATION_SUBTYPE]
    FPDFPage_CreateAnnot.restype = FPDF_ANNOTATION
    break

# fpdf_annot.h: 141
for _lib in _libs.values():
    if not _lib.has("FPDFPage_GetAnnotCount", "cdecl"):
        continue
    FPDFPage_GetAnnotCount = _lib.get("FPDFPage_GetAnnotCount", "cdecl")
    FPDFPage_GetAnnotCount.argtypes = [FPDF_PAGE]
    FPDFPage_GetAnnotCount.restype = c_int
    break

# fpdf_annot.h: 151
for _lib in _libs.values():
    if not _lib.has("FPDFPage_GetAnnot", "cdecl"):
        continue
    FPDFPage_GetAnnot = _lib.get("FPDFPage_GetAnnot", "cdecl")
    FPDFPage_GetAnnot.argtypes = [FPDF_PAGE, c_int]
    FPDFPage_GetAnnot.restype = FPDF_ANNOTATION
    break

# fpdf_annot.h: 162
for _lib in _libs.values():
    if not _lib.has("FPDFPage_GetAnnotIndex", "cdecl"):
        continue
    FPDFPage_GetAnnotIndex = _lib.get("FPDFPage_GetAnnotIndex", "cdecl")
    FPDFPage_GetAnnotIndex.argtypes = [FPDF_PAGE, FPDF_ANNOTATION]
    FPDFPage_GetAnnotIndex.restype = c_int
    break

# fpdf_annot.h: 171
for _lib in _libs.values():
    if not _lib.has("FPDFPage_CloseAnnot", "cdecl"):
        continue
    FPDFPage_CloseAnnot = _lib.get("FPDFPage_CloseAnnot", "cdecl")
    FPDFPage_CloseAnnot.argtypes = [FPDF_ANNOTATION]
    FPDFPage_CloseAnnot.restype = None
    break

# fpdf_annot.h: 180
for _lib in _libs.values():
    if not _lib.has("FPDFPage_RemoveAnnot", "cdecl"):
        continue
    FPDFPage_RemoveAnnot = _lib.get("FPDFPage_RemoveAnnot", "cdecl")
    FPDFPage_RemoveAnnot.argtypes = [FPDF_PAGE, c_int]
    FPDFPage_RemoveAnnot.restype = FPDF_BOOL
    break

# fpdf_annot.h: 190
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetSubtype", "cdecl"):
        continue
    FPDFAnnot_GetSubtype = _lib.get("FPDFAnnot_GetSubtype", "cdecl")
    FPDFAnnot_GetSubtype.argtypes = [FPDF_ANNOTATION]
    FPDFAnnot_GetSubtype.restype = FPDF_ANNOTATION_SUBTYPE
    break

# fpdf_annot.h: 201
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_IsObjectSupportedSubtype", "cdecl"):
        continue
    FPDFAnnot_IsObjectSupportedSubtype = _lib.get("FPDFAnnot_IsObjectSupportedSubtype", "cdecl")
    FPDFAnnot_IsObjectSupportedSubtype.argtypes = [FPDF_ANNOTATION_SUBTYPE]
    FPDFAnnot_IsObjectSupportedSubtype.restype = FPDF_BOOL
    break

# fpdf_annot.h: 215
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_UpdateObject", "cdecl"):
        continue
    FPDFAnnot_UpdateObject = _lib.get("FPDFAnnot_UpdateObject", "cdecl")
    FPDFAnnot_UpdateObject.argtypes = [FPDF_ANNOTATION, FPDF_PAGEOBJECT]
    FPDFAnnot_UpdateObject.restype = FPDF_BOOL
    break

# fpdf_annot.h: 230
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_AddInkStroke", "cdecl"):
        continue
    FPDFAnnot_AddInkStroke = _lib.get("FPDFAnnot_AddInkStroke", "cdecl")
    FPDFAnnot_AddInkStroke.argtypes = [FPDF_ANNOTATION, POINTER(FS_POINTF), c_size_t]
    FPDFAnnot_AddInkStroke.restype = c_int
    break

# fpdf_annot.h: 243
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_RemoveInkList", "cdecl"):
        continue
    FPDFAnnot_RemoveInkList = _lib.get("FPDFAnnot_RemoveInkList", "cdecl")
    FPDFAnnot_RemoveInkList.argtypes = [FPDF_ANNOTATION]
    FPDFAnnot_RemoveInkList.restype = FPDF_BOOL
    break

# fpdf_annot.h: 257
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_AppendObject", "cdecl"):
        continue
    FPDFAnnot_AppendObject = _lib.get("FPDFAnnot_AppendObject", "cdecl")
    FPDFAnnot_AppendObject.argtypes = [FPDF_ANNOTATION, FPDF_PAGEOBJECT]
    FPDFAnnot_AppendObject.restype = FPDF_BOOL
    break

# fpdf_annot.h: 266
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetObjectCount", "cdecl"):
        continue
    FPDFAnnot_GetObjectCount = _lib.get("FPDFAnnot_GetObjectCount", "cdecl")
    FPDFAnnot_GetObjectCount.argtypes = [FPDF_ANNOTATION]
    FPDFAnnot_GetObjectCount.restype = c_int
    break

# fpdf_annot.h: 276
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetObject", "cdecl"):
        continue
    FPDFAnnot_GetObject = _lib.get("FPDFAnnot_GetObject", "cdecl")
    FPDFAnnot_GetObject.argtypes = [FPDF_ANNOTATION, c_int]
    FPDFAnnot_GetObject.restype = FPDF_PAGEOBJECT
    break

# fpdf_annot.h: 286
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_RemoveObject", "cdecl"):
        continue
    FPDFAnnot_RemoveObject = _lib.get("FPDFAnnot_RemoveObject", "cdecl")
    FPDFAnnot_RemoveObject.argtypes = [FPDF_ANNOTATION, c_int]
    FPDFAnnot_RemoveObject.restype = FPDF_BOOL
    break

# fpdf_annot.h: 299
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_SetColor", "cdecl"):
        continue
    FPDFAnnot_SetColor = _lib.get("FPDFAnnot_SetColor", "cdecl")
    FPDFAnnot_SetColor.argtypes = [FPDF_ANNOTATION, FPDFANNOT_COLORTYPE, c_uint, c_uint, c_uint, c_uint]
    FPDFAnnot_SetColor.restype = FPDF_BOOL
    break

# fpdf_annot.h: 318
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetColor", "cdecl"):
        continue
    FPDFAnnot_GetColor = _lib.get("FPDFAnnot_GetColor", "cdecl")
    FPDFAnnot_GetColor.argtypes = [FPDF_ANNOTATION, FPDFANNOT_COLORTYPE, POINTER(c_uint), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)]
    FPDFAnnot_GetColor.restype = FPDF_BOOL
    break

# fpdf_annot.h: 338
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_HasAttachmentPoints", "cdecl"):
        continue
    FPDFAnnot_HasAttachmentPoints = _lib.get("FPDFAnnot_HasAttachmentPoints", "cdecl")
    FPDFAnnot_HasAttachmentPoints.argtypes = [FPDF_ANNOTATION]
    FPDFAnnot_HasAttachmentPoints.restype = FPDF_BOOL
    break

# fpdf_annot.h: 354
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_SetAttachmentPoints", "cdecl"):
        continue
    FPDFAnnot_SetAttachmentPoints = _lib.get("FPDFAnnot_SetAttachmentPoints", "cdecl")
    FPDFAnnot_SetAttachmentPoints.argtypes = [FPDF_ANNOTATION, c_size_t, POINTER(FS_QUADPOINTSF)]
    FPDFAnnot_SetAttachmentPoints.restype = FPDF_BOOL
    break

# fpdf_annot.h: 369
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_AppendAttachmentPoints", "cdecl"):
        continue
    FPDFAnnot_AppendAttachmentPoints = _lib.get("FPDFAnnot_AppendAttachmentPoints", "cdecl")
    FPDFAnnot_AppendAttachmentPoints.argtypes = [FPDF_ANNOTATION, POINTER(FS_QUADPOINTSF)]
    FPDFAnnot_AppendAttachmentPoints.restype = FPDF_BOOL
    break

# fpdf_annot.h: 379
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_CountAttachmentPoints", "cdecl"):
        continue
    FPDFAnnot_CountAttachmentPoints = _lib.get("FPDFAnnot_CountAttachmentPoints", "cdecl")
    FPDFAnnot_CountAttachmentPoints.argtypes = [FPDF_ANNOTATION]
    FPDFAnnot_CountAttachmentPoints.restype = c_size_t
    break

# fpdf_annot.h: 390
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetAttachmentPoints", "cdecl"):
        continue
    FPDFAnnot_GetAttachmentPoints = _lib.get("FPDFAnnot_GetAttachmentPoints", "cdecl")
    FPDFAnnot_GetAttachmentPoints.argtypes = [FPDF_ANNOTATION, c_size_t, POINTER(FS_QUADPOINTSF)]
    FPDFAnnot_GetAttachmentPoints.restype = FPDF_BOOL
    break

# fpdf_annot.h: 404
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_SetRect", "cdecl"):
        continue
    FPDFAnnot_SetRect = _lib.get("FPDFAnnot_SetRect", "cdecl")
    FPDFAnnot_SetRect.argtypes = [FPDF_ANNOTATION, POINTER(FS_RECTF)]
    FPDFAnnot_SetRect.restype = FPDF_BOOL
    break

# fpdf_annot.h: 414
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetRect", "cdecl"):
        continue
    FPDFAnnot_GetRect = _lib.get("FPDFAnnot_GetRect", "cdecl")
    FPDFAnnot_GetRect.argtypes = [FPDF_ANNOTATION, POINTER(FS_RECTF)]
    FPDFAnnot_GetRect.restype = FPDF_BOOL
    break

# fpdf_annot.h: 429
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetVertices", "cdecl"):
        continue
    FPDFAnnot_GetVertices = _lib.get("FPDFAnnot_GetVertices", "cdecl")
    FPDFAnnot_GetVertices.argtypes = [FPDF_ANNOTATION, POINTER(FS_POINTF), c_ulong]
    FPDFAnnot_GetVertices.restype = c_ulong
    break

# fpdf_annot.h: 441
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetInkListCount", "cdecl"):
        continue
    FPDFAnnot_GetInkListCount = _lib.get("FPDFAnnot_GetInkListCount", "cdecl")
    FPDFAnnot_GetInkListCount.argtypes = [FPDF_ANNOTATION]
    FPDFAnnot_GetInkListCount.restype = c_ulong
    break

# fpdf_annot.h: 456
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetInkListPath", "cdecl"):
        continue
    FPDFAnnot_GetInkListPath = _lib.get("FPDFAnnot_GetInkListPath", "cdecl")
    FPDFAnnot_GetInkListPath.argtypes = [FPDF_ANNOTATION, c_ulong, POINTER(FS_POINTF), c_ulong]
    FPDFAnnot_GetInkListPath.restype = c_ulong
    break

# fpdf_annot.h: 470
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetLine", "cdecl"):
        continue
    FPDFAnnot_GetLine = _lib.get("FPDFAnnot_GetLine", "cdecl")
    FPDFAnnot_GetLine.argtypes = [FPDF_ANNOTATION, POINTER(FS_POINTF), POINTER(FS_POINTF)]
    FPDFAnnot_GetLine.restype = FPDF_BOOL
    break

# fpdf_annot.h: 486
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_SetBorder", "cdecl"):
        continue
    FPDFAnnot_SetBorder = _lib.get("FPDFAnnot_SetBorder", "cdecl")
    FPDFAnnot_SetBorder.argtypes = [FPDF_ANNOTATION, c_float, c_float, c_float]
    FPDFAnnot_SetBorder.restype = FPDF_BOOL
    break

# fpdf_annot.h: 502
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetBorder", "cdecl"):
        continue
    FPDFAnnot_GetBorder = _lib.get("FPDFAnnot_GetBorder", "cdecl")
    FPDFAnnot_GetBorder.argtypes = [FPDF_ANNOTATION, POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    FPDFAnnot_GetBorder.restype = FPDF_BOOL
    break

# fpdf_annot.h: 526
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetFormAdditionalActionJavaScript", "cdecl"):
        continue
    FPDFAnnot_GetFormAdditionalActionJavaScript = _lib.get("FPDFAnnot_GetFormAdditionalActionJavaScript", "cdecl")
    FPDFAnnot_GetFormAdditionalActionJavaScript.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION, c_int, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAnnot_GetFormAdditionalActionJavaScript.restype = c_ulong
    break

# fpdf_annot.h: 539
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_HasKey", "cdecl"):
        continue
    FPDFAnnot_HasKey = _lib.get("FPDFAnnot_HasKey", "cdecl")
    FPDFAnnot_HasKey.argtypes = [FPDF_ANNOTATION, FPDF_BYTESTRING]
    FPDFAnnot_HasKey.restype = FPDF_BOOL
    break

# fpdf_annot.h: 550
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetValueType", "cdecl"):
        continue
    FPDFAnnot_GetValueType = _lib.get("FPDFAnnot_GetValueType", "cdecl")
    FPDFAnnot_GetValueType.argtypes = [FPDF_ANNOTATION, FPDF_BYTESTRING]
    FPDFAnnot_GetValueType.restype = FPDF_OBJECT_TYPE
    break

# fpdf_annot.h: 563
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_SetStringValue", "cdecl"):
        continue
    FPDFAnnot_SetStringValue = _lib.get("FPDFAnnot_SetStringValue", "cdecl")
    FPDFAnnot_SetStringValue.argtypes = [FPDF_ANNOTATION, FPDF_BYTESTRING, FPDF_WIDESTRING]
    FPDFAnnot_SetStringValue.restype = FPDF_BOOL
    break

# fpdf_annot.h: 583
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetStringValue", "cdecl"):
        continue
    FPDFAnnot_GetStringValue = _lib.get("FPDFAnnot_GetStringValue", "cdecl")
    FPDFAnnot_GetStringValue.argtypes = [FPDF_ANNOTATION, FPDF_BYTESTRING, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAnnot_GetStringValue.restype = c_ulong
    break

# fpdf_annot.h: 600
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetNumberValue", "cdecl"):
        continue
    FPDFAnnot_GetNumberValue = _lib.get("FPDFAnnot_GetNumberValue", "cdecl")
    FPDFAnnot_GetNumberValue.argtypes = [FPDF_ANNOTATION, FPDF_BYTESTRING, POINTER(c_float)]
    FPDFAnnot_GetNumberValue.restype = FPDF_BOOL
    break

# fpdf_annot.h: 617
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_SetAP", "cdecl"):
        continue
    FPDFAnnot_SetAP = _lib.get("FPDFAnnot_SetAP", "cdecl")
    FPDFAnnot_SetAP.argtypes = [FPDF_ANNOTATION, FPDF_ANNOT_APPEARANCEMODE, FPDF_WIDESTRING]
    FPDFAnnot_SetAP.restype = FPDF_BOOL
    break

# fpdf_annot.h: 639
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetAP", "cdecl"):
        continue
    FPDFAnnot_GetAP = _lib.get("FPDFAnnot_GetAP", "cdecl")
    FPDFAnnot_GetAP.argtypes = [FPDF_ANNOTATION, FPDF_ANNOT_APPEARANCEMODE, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAnnot_GetAP.restype = c_ulong
    break

# fpdf_annot.h: 655
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetLinkedAnnot", "cdecl"):
        continue
    FPDFAnnot_GetLinkedAnnot = _lib.get("FPDFAnnot_GetLinkedAnnot", "cdecl")
    FPDFAnnot_GetLinkedAnnot.argtypes = [FPDF_ANNOTATION, FPDF_BYTESTRING]
    FPDFAnnot_GetLinkedAnnot.restype = FPDF_ANNOTATION
    break

# fpdf_annot.h: 663
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetFlags", "cdecl"):
        continue
    FPDFAnnot_GetFlags = _lib.get("FPDFAnnot_GetFlags", "cdecl")
    FPDFAnnot_GetFlags.argtypes = [FPDF_ANNOTATION]
    FPDFAnnot_GetFlags.restype = c_int
    break

# fpdf_annot.h: 672
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_SetFlags", "cdecl"):
        continue
    FPDFAnnot_SetFlags = _lib.get("FPDFAnnot_SetFlags", "cdecl")
    FPDFAnnot_SetFlags.argtypes = [FPDF_ANNOTATION, c_int]
    FPDFAnnot_SetFlags.restype = FPDF_BOOL
    break

# fpdf_annot.h: 684
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetFormFieldFlags", "cdecl"):
        continue
    FPDFAnnot_GetFormFieldFlags = _lib.get("FPDFAnnot_GetFormFieldFlags", "cdecl")
    FPDFAnnot_GetFormFieldFlags.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION]
    FPDFAnnot_GetFormFieldFlags.restype = c_int
    break

# fpdf_annot.h: 701
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetFormFieldAtPoint", "cdecl"):
        continue
    FPDFAnnot_GetFormFieldAtPoint = _lib.get("FPDFAnnot_GetFormFieldAtPoint", "cdecl")
    FPDFAnnot_GetFormFieldAtPoint.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, POINTER(FS_POINTF)]
    FPDFAnnot_GetFormFieldAtPoint.restype = FPDF_ANNOTATION
    break

# fpdf_annot.h: 719
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetFormFieldName", "cdecl"):
        continue
    FPDFAnnot_GetFormFieldName = _lib.get("FPDFAnnot_GetFormFieldName", "cdecl")
    FPDFAnnot_GetFormFieldName.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAnnot_GetFormFieldName.restype = c_ulong
    break

# fpdf_annot.h: 739
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetFormFieldAlternateName", "cdecl"):
        continue
    FPDFAnnot_GetFormFieldAlternateName = _lib.get("FPDFAnnot_GetFormFieldAlternateName", "cdecl")
    FPDFAnnot_GetFormFieldAlternateName.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAnnot_GetFormFieldAlternateName.restype = c_ulong
    break

# fpdf_annot.h: 755
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetFormFieldType", "cdecl"):
        continue
    FPDFAnnot_GetFormFieldType = _lib.get("FPDFAnnot_GetFormFieldType", "cdecl")
    FPDFAnnot_GetFormFieldType.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION]
    FPDFAnnot_GetFormFieldType.restype = c_int
    break

# fpdf_annot.h: 771
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetFormFieldValue", "cdecl"):
        continue
    FPDFAnnot_GetFormFieldValue = _lib.get("FPDFAnnot_GetFormFieldValue", "cdecl")
    FPDFAnnot_GetFormFieldValue.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAnnot_GetFormFieldValue.restype = c_ulong
    break

# fpdf_annot.h: 786
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetOptionCount", "cdecl"):
        continue
    FPDFAnnot_GetOptionCount = _lib.get("FPDFAnnot_GetOptionCount", "cdecl")
    FPDFAnnot_GetOptionCount.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION]
    FPDFAnnot_GetOptionCount.restype = c_int
    break

# fpdf_annot.h: 808
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetOptionLabel", "cdecl"):
        continue
    FPDFAnnot_GetOptionLabel = _lib.get("FPDFAnnot_GetOptionLabel", "cdecl")
    FPDFAnnot_GetOptionLabel.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION, c_int, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAnnot_GetOptionLabel.restype = c_ulong
    break

# fpdf_annot.h: 826
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_IsOptionSelected", "cdecl"):
        continue
    FPDFAnnot_IsOptionSelected = _lib.get("FPDFAnnot_IsOptionSelected", "cdecl")
    FPDFAnnot_IsOptionSelected.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION, c_int]
    FPDFAnnot_IsOptionSelected.restype = FPDF_BOOL
    break

# fpdf_annot.h: 843
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetFontSize", "cdecl"):
        continue
    FPDFAnnot_GetFontSize = _lib.get("FPDFAnnot_GetFontSize", "cdecl")
    FPDFAnnot_GetFontSize.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION, POINTER(c_float)]
    FPDFAnnot_GetFontSize.restype = FPDF_BOOL
    break

# fpdf_annot.h: 856
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_IsChecked", "cdecl"):
        continue
    FPDFAnnot_IsChecked = _lib.get("FPDFAnnot_IsChecked", "cdecl")
    FPDFAnnot_IsChecked.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION]
    FPDFAnnot_IsChecked.restype = FPDF_BOOL
    break

# fpdf_annot.h: 871
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_SetFocusableSubtypes", "cdecl"):
        continue
    FPDFAnnot_SetFocusableSubtypes = _lib.get("FPDFAnnot_SetFocusableSubtypes", "cdecl")
    FPDFAnnot_SetFocusableSubtypes.argtypes = [FPDF_FORMHANDLE, POINTER(FPDF_ANNOTATION_SUBTYPE), c_size_t]
    FPDFAnnot_SetFocusableSubtypes.restype = FPDF_BOOL
    break

# fpdf_annot.h: 884
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetFocusableSubtypesCount", "cdecl"):
        continue
    FPDFAnnot_GetFocusableSubtypesCount = _lib.get("FPDFAnnot_GetFocusableSubtypesCount", "cdecl")
    FPDFAnnot_GetFocusableSubtypesCount.argtypes = [FPDF_FORMHANDLE]
    FPDFAnnot_GetFocusableSubtypesCount.restype = c_int
    break

# fpdf_annot.h: 900
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetFocusableSubtypes", "cdecl"):
        continue
    FPDFAnnot_GetFocusableSubtypes = _lib.get("FPDFAnnot_GetFocusableSubtypes", "cdecl")
    FPDFAnnot_GetFocusableSubtypes.argtypes = [FPDF_FORMHANDLE, POINTER(FPDF_ANNOTATION_SUBTYPE), c_size_t]
    FPDFAnnot_GetFocusableSubtypes.restype = FPDF_BOOL
    break

# fpdf_annot.h: 911
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetLink", "cdecl"):
        continue
    FPDFAnnot_GetLink = _lib.get("FPDFAnnot_GetLink", "cdecl")
    FPDFAnnot_GetLink.argtypes = [FPDF_ANNOTATION]
    FPDFAnnot_GetLink.restype = FPDF_LINK
    break

# fpdf_annot.h: 925
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetFormControlCount", "cdecl"):
        continue
    FPDFAnnot_GetFormControlCount = _lib.get("FPDFAnnot_GetFormControlCount", "cdecl")
    FPDFAnnot_GetFormControlCount.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION]
    FPDFAnnot_GetFormControlCount.restype = c_int
    break

# fpdf_annot.h: 939
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetFormControlIndex", "cdecl"):
        continue
    FPDFAnnot_GetFormControlIndex = _lib.get("FPDFAnnot_GetFormControlIndex", "cdecl")
    FPDFAnnot_GetFormControlIndex.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION]
    FPDFAnnot_GetFormControlIndex.restype = c_int
    break

# fpdf_annot.h: 956
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_GetFormFieldExportValue", "cdecl"):
        continue
    FPDFAnnot_GetFormFieldExportValue = _lib.get("FPDFAnnot_GetFormFieldExportValue", "cdecl")
    FPDFAnnot_GetFormFieldExportValue.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAnnot_GetFormFieldExportValue.restype = c_ulong
    break

# fpdf_annot.h: 968
for _lib in _libs.values():
    if not _lib.has("FPDFAnnot_SetURI", "cdecl"):
        continue
    FPDFAnnot_SetURI = _lib.get("FPDFAnnot_SetURI", "cdecl")
    FPDFAnnot_SetURI.argtypes = [FPDF_ANNOTATION, String]
    FPDFAnnot_SetURI.restype = FPDF_BOOL
    break

# fpdf_attachment.h: 22
for _lib in _libs.values():
    if not _lib.has("FPDFDoc_GetAttachmentCount", "cdecl"):
        continue
    FPDFDoc_GetAttachmentCount = _lib.get("FPDFDoc_GetAttachmentCount", "cdecl")
    FPDFDoc_GetAttachmentCount.argtypes = [FPDF_DOCUMENT]
    FPDFDoc_GetAttachmentCount.restype = c_int
    break

# fpdf_attachment.h: 35
for _lib in _libs.values():
    if not _lib.has("FPDFDoc_AddAttachment", "cdecl"):
        continue
    FPDFDoc_AddAttachment = _lib.get("FPDFDoc_AddAttachment", "cdecl")
    FPDFDoc_AddAttachment.argtypes = [FPDF_DOCUMENT, FPDF_WIDESTRING]
    FPDFDoc_AddAttachment.restype = FPDF_ATTACHMENT
    break

# fpdf_attachment.h: 46
for _lib in _libs.values():
    if not _lib.has("FPDFDoc_GetAttachment", "cdecl"):
        continue
    FPDFDoc_GetAttachment = _lib.get("FPDFDoc_GetAttachment", "cdecl")
    FPDFDoc_GetAttachment.argtypes = [FPDF_DOCUMENT, c_int]
    FPDFDoc_GetAttachment.restype = FPDF_ATTACHMENT
    break

# fpdf_attachment.h: 59
for _lib in _libs.values():
    if not _lib.has("FPDFDoc_DeleteAttachment", "cdecl"):
        continue
    FPDFDoc_DeleteAttachment = _lib.get("FPDFDoc_DeleteAttachment", "cdecl")
    FPDFDoc_DeleteAttachment.argtypes = [FPDF_DOCUMENT, c_int]
    FPDFDoc_DeleteAttachment.restype = FPDF_BOOL
    break

# fpdf_attachment.h: 72
for _lib in _libs.values():
    if not _lib.has("FPDFAttachment_GetName", "cdecl"):
        continue
    FPDFAttachment_GetName = _lib.get("FPDFAttachment_GetName", "cdecl")
    FPDFAttachment_GetName.argtypes = [FPDF_ATTACHMENT, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAttachment_GetName.restype = c_ulong
    break

# fpdf_attachment.h: 84
for _lib in _libs.values():
    if not _lib.has("FPDFAttachment_HasKey", "cdecl"):
        continue
    FPDFAttachment_HasKey = _lib.get("FPDFAttachment_HasKey", "cdecl")
    FPDFAttachment_HasKey.argtypes = [FPDF_ATTACHMENT, FPDF_BYTESTRING]
    FPDFAttachment_HasKey.restype = FPDF_BOOL
    break

# fpdf_attachment.h: 95
for _lib in _libs.values():
    if not _lib.has("FPDFAttachment_GetValueType", "cdecl"):
        continue
    FPDFAttachment_GetValueType = _lib.get("FPDFAttachment_GetValueType", "cdecl")
    FPDFAttachment_GetValueType.argtypes = [FPDF_ATTACHMENT, FPDF_BYTESTRING]
    FPDFAttachment_GetValueType.restype = FPDF_OBJECT_TYPE
    break

# fpdf_attachment.h: 108
for _lib in _libs.values():
    if not _lib.has("FPDFAttachment_SetStringValue", "cdecl"):
        continue
    FPDFAttachment_SetStringValue = _lib.get("FPDFAttachment_SetStringValue", "cdecl")
    FPDFAttachment_SetStringValue.argtypes = [FPDF_ATTACHMENT, FPDF_BYTESTRING, FPDF_WIDESTRING]
    FPDFAttachment_SetStringValue.restype = FPDF_BOOL
    break

# fpdf_attachment.h: 129
for _lib in _libs.values():
    if not _lib.has("FPDFAttachment_GetStringValue", "cdecl"):
        continue
    FPDFAttachment_GetStringValue = _lib.get("FPDFAttachment_GetStringValue", "cdecl")
    FPDFAttachment_GetStringValue.argtypes = [FPDF_ATTACHMENT, FPDF_BYTESTRING, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAttachment_GetStringValue.restype = c_ulong
    break

# fpdf_attachment.h: 146
for _lib in _libs.values():
    if not _lib.has("FPDFAttachment_SetFile", "cdecl"):
        continue
    FPDFAttachment_SetFile = _lib.get("FPDFAttachment_SetFile", "cdecl")
    FPDFAttachment_SetFile.argtypes = [FPDF_ATTACHMENT, FPDF_DOCUMENT, POINTER(None), c_ulong]
    FPDFAttachment_SetFile.restype = FPDF_BOOL
    break

# fpdf_attachment.h: 170
for _lib in _libs.values():
    if not _lib.has("FPDFAttachment_GetFile", "cdecl"):
        continue
    FPDFAttachment_GetFile = _lib.get("FPDFAttachment_GetFile", "cdecl")
    FPDFAttachment_GetFile.argtypes = [FPDF_ATTACHMENT, POINTER(None), c_ulong, POINTER(c_ulong)]
    FPDFAttachment_GetFile.restype = FPDF_BOOL
    break

# fpdf_catalog.h: 28
for _lib in _libs.values():
    if not _lib.has("FPDFCatalog_IsTagged", "cdecl"):
        continue
    FPDFCatalog_IsTagged = _lib.get("FPDFCatalog_IsTagged", "cdecl")
    FPDFCatalog_IsTagged.argtypes = [FPDF_DOCUMENT]
    FPDFCatalog_IsTagged.restype = FPDF_BOOL
    break

# fpdf_dataavail.h: 33
class struct__FX_FILEAVAIL(Structure):
    pass

struct__FX_FILEAVAIL.__slots__ = [
    'version',
    'IsDataAvail',
]
struct__FX_FILEAVAIL._fields_ = [
    ('version', c_int),
    ('IsDataAvail', CFUNCTYPE(UNCHECKED(FPDF_BOOL), POINTER(struct__FX_FILEAVAIL), c_size_t, c_size_t)),
]

FX_FILEAVAIL = struct__FX_FILEAVAIL# fpdf_dataavail.h: 52

# fpdf_dataavail.h: 62
for _lib in _libs.values():
    if not _lib.has("FPDFAvail_Create", "cdecl"):
        continue
    FPDFAvail_Create = _lib.get("FPDFAvail_Create", "cdecl")
    FPDFAvail_Create.argtypes = [POINTER(FX_FILEAVAIL), POINTER(FPDF_FILEACCESS)]
    FPDFAvail_Create.restype = FPDF_AVAIL
    break

# fpdf_dataavail.h: 68
for _lib in _libs.values():
    if not _lib.has("FPDFAvail_Destroy", "cdecl"):
        continue
    FPDFAvail_Destroy = _lib.get("FPDFAvail_Destroy", "cdecl")
    FPDFAvail_Destroy.argtypes = [FPDF_AVAIL]
    FPDFAvail_Destroy.restype = None
    break

# fpdf_dataavail.h: 71
class struct__FX_DOWNLOADHINTS(Structure):
    pass

struct__FX_DOWNLOADHINTS.__slots__ = [
    'version',
    'AddSegment',
]
struct__FX_DOWNLOADHINTS._fields_ = [
    ('version', c_int),
    ('AddSegment', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FX_DOWNLOADHINTS), c_size_t, c_size_t)),
]

FX_DOWNLOADHINTS = struct__FX_DOWNLOADHINTS# fpdf_dataavail.h: 90

# fpdf_dataavail.h: 109
for _lib in _libs.values():
    if not _lib.has("FPDFAvail_IsDocAvail", "cdecl"):
        continue
    FPDFAvail_IsDocAvail = _lib.get("FPDFAvail_IsDocAvail", "cdecl")
    FPDFAvail_IsDocAvail.argtypes = [FPDF_AVAIL, POINTER(FX_DOWNLOADHINTS)]
    FPDFAvail_IsDocAvail.restype = c_int
    break

# fpdf_dataavail.h: 124
for _lib in _libs.values():
    if not _lib.has("FPDFAvail_GetDocument", "cdecl"):
        continue
    FPDFAvail_GetDocument = _lib.get("FPDFAvail_GetDocument", "cdecl")
    FPDFAvail_GetDocument.argtypes = [FPDF_AVAIL, FPDF_BYTESTRING]
    FPDFAvail_GetDocument.restype = FPDF_DOCUMENT
    break

# fpdf_dataavail.h: 135
for _lib in _libs.values():
    if not _lib.has("FPDFAvail_GetFirstPageNum", "cdecl"):
        continue
    FPDFAvail_GetFirstPageNum = _lib.get("FPDFAvail_GetFirstPageNum", "cdecl")
    FPDFAvail_GetFirstPageNum.argtypes = [FPDF_DOCUMENT]
    FPDFAvail_GetFirstPageNum.restype = c_int
    break

# fpdf_dataavail.h: 157
for _lib in _libs.values():
    if not _lib.has("FPDFAvail_IsPageAvail", "cdecl"):
        continue
    FPDFAvail_IsPageAvail = _lib.get("FPDFAvail_IsPageAvail", "cdecl")
    FPDFAvail_IsPageAvail.argtypes = [FPDF_AVAIL, c_int, POINTER(FX_DOWNLOADHINTS)]
    FPDFAvail_IsPageAvail.restype = c_int
    break

# fpdf_dataavail.h: 182
for _lib in _libs.values():
    if not _lib.has("FPDFAvail_IsFormAvail", "cdecl"):
        continue
    FPDFAvail_IsFormAvail = _lib.get("FPDFAvail_IsFormAvail", "cdecl")
    FPDFAvail_IsFormAvail.argtypes = [FPDF_AVAIL, POINTER(FX_DOWNLOADHINTS)]
    FPDFAvail_IsFormAvail.restype = c_int
    break

# fpdf_dataavail.h: 198
for _lib in _libs.values():
    if not _lib.has("FPDFAvail_IsLinearized", "cdecl"):
        continue
    FPDFAvail_IsLinearized = _lib.get("FPDFAvail_IsLinearized", "cdecl")
    FPDFAvail_IsLinearized.argtypes = [FPDF_AVAIL]
    FPDFAvail_IsLinearized.restype = c_int
    break

enum_anon_5 = c_int# fpdf_doc.h: 46

FILEIDTYPE_PERMANENT = 0# fpdf_doc.h: 46

FILEIDTYPE_CHANGING = 1# fpdf_doc.h: 46

FPDF_FILEIDTYPE = enum_anon_5# fpdf_doc.h: 46

# fpdf_doc.h: 57
for _lib in _libs.values():
    if not _lib.has("FPDFBookmark_GetFirstChild", "cdecl"):
        continue
    FPDFBookmark_GetFirstChild = _lib.get("FPDFBookmark_GetFirstChild", "cdecl")
    FPDFBookmark_GetFirstChild.argtypes = [FPDF_DOCUMENT, FPDF_BOOKMARK]
    FPDFBookmark_GetFirstChild.restype = FPDF_BOOKMARK
    break

# fpdf_doc.h: 70
for _lib in _libs.values():
    if not _lib.has("FPDFBookmark_GetNextSibling", "cdecl"):
        continue
    FPDFBookmark_GetNextSibling = _lib.get("FPDFBookmark_GetNextSibling", "cdecl")
    FPDFBookmark_GetNextSibling.argtypes = [FPDF_DOCUMENT, FPDF_BOOKMARK]
    FPDFBookmark_GetNextSibling.restype = FPDF_BOOKMARK
    break

# fpdf_doc.h: 86
for _lib in _libs.values():
    if not _lib.has("FPDFBookmark_GetTitle", "cdecl"):
        continue
    FPDFBookmark_GetTitle = _lib.get("FPDFBookmark_GetTitle", "cdecl")
    FPDFBookmark_GetTitle.argtypes = [FPDF_BOOKMARK, POINTER(None), c_ulong]
    FPDFBookmark_GetTitle.restype = c_ulong
    break

# fpdf_doc.h: 100
for _lib in _libs.values():
    if not _lib.has("FPDFBookmark_GetCount", "cdecl"):
        continue
    FPDFBookmark_GetCount = _lib.get("FPDFBookmark_GetCount", "cdecl")
    FPDFBookmark_GetCount.argtypes = [FPDF_BOOKMARK]
    FPDFBookmark_GetCount.restype = c_int
    break

# fpdf_doc.h: 112
for _lib in _libs.values():
    if not _lib.has("FPDFBookmark_Find", "cdecl"):
        continue
    FPDFBookmark_Find = _lib.get("FPDFBookmark_Find", "cdecl")
    FPDFBookmark_Find.argtypes = [FPDF_DOCUMENT, FPDF_WIDESTRING]
    FPDFBookmark_Find.restype = FPDF_BOOKMARK
    break

# fpdf_doc.h: 122
for _lib in _libs.values():
    if not _lib.has("FPDFBookmark_GetDest", "cdecl"):
        continue
    FPDFBookmark_GetDest = _lib.get("FPDFBookmark_GetDest", "cdecl")
    FPDFBookmark_GetDest.argtypes = [FPDF_DOCUMENT, FPDF_BOOKMARK]
    FPDFBookmark_GetDest.restype = FPDF_DEST
    break

# fpdf_doc.h: 135
for _lib in _libs.values():
    if not _lib.has("FPDFBookmark_GetAction", "cdecl"):
        continue
    FPDFBookmark_GetAction = _lib.get("FPDFBookmark_GetAction", "cdecl")
    FPDFBookmark_GetAction.argtypes = [FPDF_BOOKMARK]
    FPDFBookmark_GetAction.restype = FPDF_ACTION
    break

# fpdf_doc.h: 147
for _lib in _libs.values():
    if not _lib.has("FPDFAction_GetType", "cdecl"):
        continue
    FPDFAction_GetType = _lib.get("FPDFAction_GetType", "cdecl")
    FPDFAction_GetType.argtypes = [FPDF_ACTION]
    FPDFAction_GetType.restype = c_ulong
    break

# fpdf_doc.h: 161
for _lib in _libs.values():
    if not _lib.has("FPDFAction_GetDest", "cdecl"):
        continue
    FPDFAction_GetDest = _lib.get("FPDFAction_GetDest", "cdecl")
    FPDFAction_GetDest.argtypes = [FPDF_DOCUMENT, FPDF_ACTION]
    FPDFAction_GetDest.restype = FPDF_DEST
    break

# fpdf_doc.h: 179
for _lib in _libs.values():
    if not _lib.has("FPDFAction_GetFilePath", "cdecl"):
        continue
    FPDFAction_GetFilePath = _lib.get("FPDFAction_GetFilePath", "cdecl")
    FPDFAction_GetFilePath.argtypes = [FPDF_ACTION, POINTER(None), c_ulong]
    FPDFAction_GetFilePath.restype = c_ulong
    break

# fpdf_doc.h: 205
for _lib in _libs.values():
    if not _lib.has("FPDFAction_GetURIPath", "cdecl"):
        continue
    FPDFAction_GetURIPath = _lib.get("FPDFAction_GetURIPath", "cdecl")
    FPDFAction_GetURIPath.argtypes = [FPDF_DOCUMENT, FPDF_ACTION, POINTER(None), c_ulong]
    FPDFAction_GetURIPath.restype = c_ulong
    break

# fpdf_doc.h: 216
for _lib in _libs.values():
    if not _lib.has("FPDFDest_GetDestPageIndex", "cdecl"):
        continue
    FPDFDest_GetDestPageIndex = _lib.get("FPDFDest_GetDestPageIndex", "cdecl")
    FPDFDest_GetDestPageIndex.argtypes = [FPDF_DOCUMENT, FPDF_DEST]
    FPDFDest_GetDestPageIndex.restype = c_int
    break

# fpdf_doc.h: 229
for _lib in _libs.values():
    if not _lib.has("FPDFDest_GetView", "cdecl"):
        continue
    FPDFDest_GetView = _lib.get("FPDFDest_GetView", "cdecl")
    FPDFDest_GetView.argtypes = [FPDF_DEST, POINTER(c_ulong), POINTER(FS_FLOAT)]
    FPDFDest_GetView.restype = c_ulong
    break

# fpdf_doc.h: 246
for _lib in _libs.values():
    if not _lib.has("FPDFDest_GetLocationInPage", "cdecl"):
        continue
    FPDFDest_GetLocationInPage = _lib.get("FPDFDest_GetLocationInPage", "cdecl")
    FPDFDest_GetLocationInPage.argtypes = [FPDF_DEST, POINTER(FPDF_BOOL), POINTER(FPDF_BOOL), POINTER(FPDF_BOOL), POINTER(FS_FLOAT), POINTER(FS_FLOAT), POINTER(FS_FLOAT)]
    FPDFDest_GetLocationInPage.restype = FPDF_BOOL
    break

# fpdf_doc.h: 264
for _lib in _libs.values():
    if not _lib.has("FPDFLink_GetLinkAtPoint", "cdecl"):
        continue
    FPDFLink_GetLinkAtPoint = _lib.get("FPDFLink_GetLinkAtPoint", "cdecl")
    FPDFLink_GetLinkAtPoint.argtypes = [FPDF_PAGE, c_double, c_double]
    FPDFLink_GetLinkAtPoint.restype = FPDF_LINK
    break

# fpdf_doc.h: 279
for _lib in _libs.values():
    if not _lib.has("FPDFLink_GetLinkZOrderAtPoint", "cdecl"):
        continue
    FPDFLink_GetLinkZOrderAtPoint = _lib.get("FPDFLink_GetLinkZOrderAtPoint", "cdecl")
    FPDFLink_GetLinkZOrderAtPoint.argtypes = [FPDF_PAGE, c_double, c_double]
    FPDFLink_GetLinkZOrderAtPoint.restype = c_int
    break

# fpdf_doc.h: 291
for _lib in _libs.values():
    if not _lib.has("FPDFLink_GetDest", "cdecl"):
        continue
    FPDFLink_GetDest = _lib.get("FPDFLink_GetDest", "cdecl")
    FPDFLink_GetDest.argtypes = [FPDF_DOCUMENT, FPDF_LINK]
    FPDFLink_GetDest.restype = FPDF_DEST
    break

# fpdf_doc.h: 301
for _lib in _libs.values():
    if not _lib.has("FPDFLink_GetAction", "cdecl"):
        continue
    FPDFLink_GetAction = _lib.get("FPDFLink_GetAction", "cdecl")
    FPDFLink_GetAction.argtypes = [FPDF_LINK]
    FPDFLink_GetAction.restype = FPDF_ACTION
    break

# fpdf_doc.h: 311
for _lib in _libs.values():
    if not _lib.has("FPDFLink_Enumerate", "cdecl"):
        continue
    FPDFLink_Enumerate = _lib.get("FPDFLink_Enumerate", "cdecl")
    FPDFLink_Enumerate.argtypes = [FPDF_PAGE, POINTER(c_int), POINTER(FPDF_LINK)]
    FPDFLink_Enumerate.restype = FPDF_BOOL
    break

# fpdf_doc.h: 324
for _lib in _libs.values():
    if not _lib.has("FPDFLink_GetAnnot", "cdecl"):
        continue
    FPDFLink_GetAnnot = _lib.get("FPDFLink_GetAnnot", "cdecl")
    FPDFLink_GetAnnot.argtypes = [FPDF_PAGE, FPDF_LINK]
    FPDFLink_GetAnnot.restype = FPDF_ANNOTATION
    break

# fpdf_doc.h: 332
for _lib in _libs.values():
    if not _lib.has("FPDFLink_GetAnnotRect", "cdecl"):
        continue
    FPDFLink_GetAnnotRect = _lib.get("FPDFLink_GetAnnotRect", "cdecl")
    FPDFLink_GetAnnotRect.argtypes = [FPDF_LINK, POINTER(FS_RECTF)]
    FPDFLink_GetAnnotRect.restype = FPDF_BOOL
    break

# fpdf_doc.h: 340
for _lib in _libs.values():
    if not _lib.has("FPDFLink_CountQuadPoints", "cdecl"):
        continue
    FPDFLink_CountQuadPoints = _lib.get("FPDFLink_CountQuadPoints", "cdecl")
    FPDFLink_CountQuadPoints.argtypes = [FPDF_LINK]
    FPDFLink_CountQuadPoints.restype = c_int
    break

# fpdf_doc.h: 350
for _lib in _libs.values():
    if not _lib.has("FPDFLink_GetQuadPoints", "cdecl"):
        continue
    FPDFLink_GetQuadPoints = _lib.get("FPDFLink_GetQuadPoints", "cdecl")
    FPDFLink_GetQuadPoints.argtypes = [FPDF_LINK, c_int, POINTER(FS_QUADPOINTSF)]
    FPDFLink_GetQuadPoints.restype = FPDF_BOOL
    break

# fpdf_doc.h: 365
for _lib in _libs.values():
    if not _lib.has("FPDF_GetPageAAction", "cdecl"):
        continue
    FPDF_GetPageAAction = _lib.get("FPDF_GetPageAAction", "cdecl")
    FPDF_GetPageAAction.argtypes = [FPDF_PAGE, c_int]
    FPDF_GetPageAAction.restype = FPDF_ACTION
    break

# fpdf_doc.h: 383
for _lib in _libs.values():
    if not _lib.has("FPDF_GetFileIdentifier", "cdecl"):
        continue
    FPDF_GetFileIdentifier = _lib.get("FPDF_GetFileIdentifier", "cdecl")
    FPDF_GetFileIdentifier.argtypes = [FPDF_DOCUMENT, FPDF_FILEIDTYPE, POINTER(None), c_ulong]
    FPDF_GetFileIdentifier.restype = c_ulong
    break

# fpdf_doc.h: 409
for _lib in _libs.values():
    if not _lib.has("FPDF_GetMetaText", "cdecl"):
        continue
    FPDF_GetMetaText = _lib.get("FPDF_GetMetaText", "cdecl")
    FPDF_GetMetaText.argtypes = [FPDF_DOCUMENT, FPDF_BYTESTRING, POINTER(None), c_ulong]
    FPDF_GetMetaText.restype = c_ulong
    break

# fpdf_doc.h: 427
for _lib in _libs.values():
    if not _lib.has("FPDF_GetPageLabel", "cdecl"):
        continue
    FPDF_GetPageLabel = _lib.get("FPDF_GetPageLabel", "cdecl")
    FPDF_GetPageLabel.argtypes = [FPDF_DOCUMENT, c_int, POINTER(None), c_ulong]
    FPDF_GetPageLabel.restype = c_ulong
    break

__uint8_t = c_ubyte# /usr/include/x86_64-linux-gnu/bits/types.h: 38

__uint16_t = c_ushort# /usr/include/x86_64-linux-gnu/bits/types.h: 40

__uint32_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 42

__time_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 160

uint8_t = __uint8_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 24

uint16_t = __uint16_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 25

uint32_t = __uint32_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 26

# fpdf_edit.h: 93
class struct_FPDF_IMAGEOBJ_METADATA(Structure):
    pass

struct_FPDF_IMAGEOBJ_METADATA.__slots__ = [
    'width',
    'height',
    'horizontal_dpi',
    'vertical_dpi',
    'bits_per_pixel',
    'colorspace',
    'marked_content_id',
]
struct_FPDF_IMAGEOBJ_METADATA._fields_ = [
    ('width', c_uint),
    ('height', c_uint),
    ('horizontal_dpi', c_float),
    ('vertical_dpi', c_float),
    ('bits_per_pixel', c_uint),
    ('colorspace', c_int),
    ('marked_content_id', c_int),
]

FPDF_IMAGEOBJ_METADATA = struct_FPDF_IMAGEOBJ_METADATA# fpdf_edit.h: 93

# fpdf_edit.h: 102
for _lib in _libs.values():
    if not _lib.has("FPDF_CreateNewDocument", "cdecl"):
        continue
    FPDF_CreateNewDocument = _lib.get("FPDF_CreateNewDocument", "cdecl")
    FPDF_CreateNewDocument.argtypes = []
    FPDF_CreateNewDocument.restype = FPDF_DOCUMENT
    break

# fpdf_edit.h: 117
for _lib in _libs.values():
    if not _lib.has("FPDFPage_New", "cdecl"):
        continue
    FPDFPage_New = _lib.get("FPDFPage_New", "cdecl")
    FPDFPage_New.argtypes = [FPDF_DOCUMENT, c_int, c_double, c_double]
    FPDFPage_New.restype = FPDF_PAGE
    break

# fpdf_edit.h: 126
for _lib in _libs.values():
    if not _lib.has("FPDFPage_Delete", "cdecl"):
        continue
    FPDFPage_Delete = _lib.get("FPDFPage_Delete", "cdecl")
    FPDFPage_Delete.argtypes = [FPDF_DOCUMENT, c_int]
    FPDFPage_Delete.restype = None
    break

# fpdf_edit.h: 138
for _lib in _libs.values():
    if not _lib.has("FPDFPage_GetRotation", "cdecl"):
        continue
    FPDFPage_GetRotation = _lib.get("FPDFPage_GetRotation", "cdecl")
    FPDFPage_GetRotation.argtypes = [FPDF_PAGE]
    FPDFPage_GetRotation.restype = c_int
    break

# fpdf_edit.h: 148
for _lib in _libs.values():
    if not _lib.has("FPDFPage_SetRotation", "cdecl"):
        continue
    FPDFPage_SetRotation = _lib.get("FPDFPage_SetRotation", "cdecl")
    FPDFPage_SetRotation.argtypes = [FPDF_PAGE, c_int]
    FPDFPage_SetRotation.restype = None
    break

# fpdf_edit.h: 155
for _lib in _libs.values():
    if not _lib.has("FPDFPage_InsertObject", "cdecl"):
        continue
    FPDFPage_InsertObject = _lib.get("FPDFPage_InsertObject", "cdecl")
    FPDFPage_InsertObject.argtypes = [FPDF_PAGE, FPDF_PAGEOBJECT]
    FPDFPage_InsertObject.restype = None
    break

# fpdf_edit.h: 169
for _lib in _libs.values():
    if not _lib.has("FPDFPage_RemoveObject", "cdecl"):
        continue
    FPDFPage_RemoveObject = _lib.get("FPDFPage_RemoveObject", "cdecl")
    FPDFPage_RemoveObject.argtypes = [FPDF_PAGE, FPDF_PAGEOBJECT]
    FPDFPage_RemoveObject.restype = FPDF_BOOL
    break

# fpdf_edit.h: 176
for _lib in _libs.values():
    if not _lib.has("FPDFPage_CountObjects", "cdecl"):
        continue
    FPDFPage_CountObjects = _lib.get("FPDFPage_CountObjects", "cdecl")
    FPDFPage_CountObjects.argtypes = [FPDF_PAGE]
    FPDFPage_CountObjects.restype = c_int
    break

# fpdf_edit.h: 184
for _lib in _libs.values():
    if not _lib.has("FPDFPage_GetObject", "cdecl"):
        continue
    FPDFPage_GetObject = _lib.get("FPDFPage_GetObject", "cdecl")
    FPDFPage_GetObject.argtypes = [FPDF_PAGE, c_int]
    FPDFPage_GetObject.restype = FPDF_PAGEOBJECT
    break

# fpdf_edit.h: 192
for _lib in _libs.values():
    if not _lib.has("FPDFPage_HasTransparency", "cdecl"):
        continue
    FPDFPage_HasTransparency = _lib.get("FPDFPage_HasTransparency", "cdecl")
    FPDFPage_HasTransparency.argtypes = [FPDF_PAGE]
    FPDFPage_HasTransparency.restype = FPDF_BOOL
    break

# fpdf_edit.h: 202
for _lib in _libs.values():
    if not _lib.has("FPDFPage_GenerateContent", "cdecl"):
        continue
    FPDFPage_GenerateContent = _lib.get("FPDFPage_GenerateContent", "cdecl")
    FPDFPage_GenerateContent.argtypes = [FPDF_PAGE]
    FPDFPage_GenerateContent.restype = FPDF_BOOL
    break

# fpdf_edit.h: 211
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_Destroy", "cdecl"):
        continue
    FPDFPageObj_Destroy = _lib.get("FPDFPageObj_Destroy", "cdecl")
    FPDFPageObj_Destroy.argtypes = [FPDF_PAGEOBJECT]
    FPDFPageObj_Destroy.restype = None
    break

# fpdf_edit.h: 219
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_HasTransparency", "cdecl"):
        continue
    FPDFPageObj_HasTransparency = _lib.get("FPDFPageObj_HasTransparency", "cdecl")
    FPDFPageObj_HasTransparency.argtypes = [FPDF_PAGEOBJECT]
    FPDFPageObj_HasTransparency.restype = FPDF_BOOL
    break

# fpdf_edit.h: 227
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_GetType", "cdecl"):
        continue
    FPDFPageObj_GetType = _lib.get("FPDFPageObj_GetType", "cdecl")
    FPDFPageObj_GetType.argtypes = [FPDF_PAGEOBJECT]
    FPDFPageObj_GetType.restype = c_int
    break

# fpdf_edit.h: 244
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_Transform", "cdecl"):
        continue
    FPDFPageObj_Transform = _lib.get("FPDFPageObj_Transform", "cdecl")
    FPDFPageObj_Transform.argtypes = [FPDF_PAGEOBJECT, c_double, c_double, c_double, c_double, c_double, c_double]
    FPDFPageObj_Transform.restype = None
    break

# fpdf_edit.h: 265
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_GetMatrix", "cdecl"):
        continue
    FPDFPageObj_GetMatrix = _lib.get("FPDFPageObj_GetMatrix", "cdecl")
    FPDFPageObj_GetMatrix.argtypes = [FPDF_PAGEOBJECT, POINTER(FS_MATRIX)]
    FPDFPageObj_GetMatrix.restype = FPDF_BOOL
    break

# fpdf_edit.h: 280
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_SetMatrix", "cdecl"):
        continue
    FPDFPageObj_SetMatrix = _lib.get("FPDFPageObj_SetMatrix", "cdecl")
    FPDFPageObj_SetMatrix.argtypes = [FPDF_PAGEOBJECT, POINTER(FS_MATRIX)]
    FPDFPageObj_SetMatrix.restype = FPDF_BOOL
    break

# fpdf_edit.h: 296
for _lib in _libs.values():
    if not _lib.has("FPDFPage_TransformAnnots", "cdecl"):
        continue
    FPDFPage_TransformAnnots = _lib.get("FPDFPage_TransformAnnots", "cdecl")
    FPDFPage_TransformAnnots.argtypes = [FPDF_PAGE, c_double, c_double, c_double, c_double, c_double, c_double]
    FPDFPage_TransformAnnots.restype = None
    break

# fpdf_edit.h: 310
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_NewImageObj", "cdecl"):
        continue
    FPDFPageObj_NewImageObj = _lib.get("FPDFPageObj_NewImageObj", "cdecl")
    FPDFPageObj_NewImageObj.argtypes = [FPDF_DOCUMENT]
    FPDFPageObj_NewImageObj.restype = FPDF_PAGEOBJECT
    break

# fpdf_edit.h: 320
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_CountMarks", "cdecl"):
        continue
    FPDFPageObj_CountMarks = _lib.get("FPDFPageObj_CountMarks", "cdecl")
    FPDFPageObj_CountMarks.argtypes = [FPDF_PAGEOBJECT]
    FPDFPageObj_CountMarks.restype = c_int
    break

# fpdf_edit.h: 333
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_GetMark", "cdecl"):
        continue
    FPDFPageObj_GetMark = _lib.get("FPDFPageObj_GetMark", "cdecl")
    FPDFPageObj_GetMark.argtypes = [FPDF_PAGEOBJECT, c_ulong]
    FPDFPageObj_GetMark.restype = FPDF_PAGEOBJECTMARK
    break

# fpdf_edit.h: 346
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_AddMark", "cdecl"):
        continue
    FPDFPageObj_AddMark = _lib.get("FPDFPageObj_AddMark", "cdecl")
    FPDFPageObj_AddMark.argtypes = [FPDF_PAGEOBJECT, FPDF_BYTESTRING]
    FPDFPageObj_AddMark.restype = FPDF_PAGEOBJECTMARK
    break

# fpdf_edit.h: 357
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_RemoveMark", "cdecl"):
        continue
    FPDFPageObj_RemoveMark = _lib.get("FPDFPageObj_RemoveMark", "cdecl")
    FPDFPageObj_RemoveMark.argtypes = [FPDF_PAGEOBJECT, FPDF_PAGEOBJECTMARK]
    FPDFPageObj_RemoveMark.restype = FPDF_BOOL
    break

# fpdf_edit.h: 373
for _lib in _libs.values():
    if not _lib.has("FPDFPageObjMark_GetName", "cdecl"):
        continue
    FPDFPageObjMark_GetName = _lib.get("FPDFPageObjMark_GetName", "cdecl")
    FPDFPageObjMark_GetName.argtypes = [FPDF_PAGEOBJECTMARK, POINTER(None), c_ulong, POINTER(c_ulong)]
    FPDFPageObjMark_GetName.restype = FPDF_BOOL
    break

# fpdf_edit.h: 386
for _lib in _libs.values():
    if not _lib.has("FPDFPageObjMark_CountParams", "cdecl"):
        continue
    FPDFPageObjMark_CountParams = _lib.get("FPDFPageObjMark_CountParams", "cdecl")
    FPDFPageObjMark_CountParams.argtypes = [FPDF_PAGEOBJECTMARK]
    FPDFPageObjMark_CountParams.restype = c_int
    break

# fpdf_edit.h: 403
for _lib in _libs.values():
    if not _lib.has("FPDFPageObjMark_GetParamKey", "cdecl"):
        continue
    FPDFPageObjMark_GetParamKey = _lib.get("FPDFPageObjMark_GetParamKey", "cdecl")
    FPDFPageObjMark_GetParamKey.argtypes = [FPDF_PAGEOBJECTMARK, c_ulong, POINTER(None), c_ulong, POINTER(c_ulong)]
    FPDFPageObjMark_GetParamKey.restype = FPDF_BOOL
    break

# fpdf_edit.h: 417
for _lib in _libs.values():
    if not _lib.has("FPDFPageObjMark_GetParamValueType", "cdecl"):
        continue
    FPDFPageObjMark_GetParamValueType = _lib.get("FPDFPageObjMark_GetParamValueType", "cdecl")
    FPDFPageObjMark_GetParamValueType.argtypes = [FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING]
    FPDFPageObjMark_GetParamValueType.restype = FPDF_OBJECT_TYPE
    break

# fpdf_edit.h: 432
for _lib in _libs.values():
    if not _lib.has("FPDFPageObjMark_GetParamIntValue", "cdecl"):
        continue
    FPDFPageObjMark_GetParamIntValue = _lib.get("FPDFPageObjMark_GetParamIntValue", "cdecl")
    FPDFPageObjMark_GetParamIntValue.argtypes = [FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING, POINTER(c_int)]
    FPDFPageObjMark_GetParamIntValue.restype = FPDF_BOOL
    break

# fpdf_edit.h: 452
for _lib in _libs.values():
    if not _lib.has("FPDFPageObjMark_GetParamStringValue", "cdecl"):
        continue
    FPDFPageObjMark_GetParamStringValue = _lib.get("FPDFPageObjMark_GetParamStringValue", "cdecl")
    FPDFPageObjMark_GetParamStringValue.argtypes = [FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING, POINTER(None), c_ulong, POINTER(c_ulong)]
    FPDFPageObjMark_GetParamStringValue.restype = FPDF_BOOL
    break

# fpdf_edit.h: 473
for _lib in _libs.values():
    if not _lib.has("FPDFPageObjMark_GetParamBlobValue", "cdecl"):
        continue
    FPDFPageObjMark_GetParamBlobValue = _lib.get("FPDFPageObjMark_GetParamBlobValue", "cdecl")
    FPDFPageObjMark_GetParamBlobValue.argtypes = [FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING, POINTER(None), c_ulong, POINTER(c_ulong)]
    FPDFPageObjMark_GetParamBlobValue.restype = FPDF_BOOL
    break

# fpdf_edit.h: 492
for _lib in _libs.values():
    if not _lib.has("FPDFPageObjMark_SetIntParam", "cdecl"):
        continue
    FPDFPageObjMark_SetIntParam = _lib.get("FPDFPageObjMark_SetIntParam", "cdecl")
    FPDFPageObjMark_SetIntParam.argtypes = [FPDF_DOCUMENT, FPDF_PAGEOBJECT, FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING, c_int]
    FPDFPageObjMark_SetIntParam.restype = FPDF_BOOL
    break

# fpdf_edit.h: 511
for _lib in _libs.values():
    if not _lib.has("FPDFPageObjMark_SetStringParam", "cdecl"):
        continue
    FPDFPageObjMark_SetStringParam = _lib.get("FPDFPageObjMark_SetStringParam", "cdecl")
    FPDFPageObjMark_SetStringParam.argtypes = [FPDF_DOCUMENT, FPDF_PAGEOBJECT, FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING, FPDF_BYTESTRING]
    FPDFPageObjMark_SetStringParam.restype = FPDF_BOOL
    break

# fpdf_edit.h: 531
for _lib in _libs.values():
    if not _lib.has("FPDFPageObjMark_SetBlobParam", "cdecl"):
        continue
    FPDFPageObjMark_SetBlobParam = _lib.get("FPDFPageObjMark_SetBlobParam", "cdecl")
    FPDFPageObjMark_SetBlobParam.argtypes = [FPDF_DOCUMENT, FPDF_PAGEOBJECT, FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING, POINTER(None), c_ulong]
    FPDFPageObjMark_SetBlobParam.restype = FPDF_BOOL
    break

# fpdf_edit.h: 547
for _lib in _libs.values():
    if not _lib.has("FPDFPageObjMark_RemoveParam", "cdecl"):
        continue
    FPDFPageObjMark_RemoveParam = _lib.get("FPDFPageObjMark_RemoveParam", "cdecl")
    FPDFPageObjMark_RemoveParam.argtypes = [FPDF_PAGEOBJECT, FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING]
    FPDFPageObjMark_RemoveParam.restype = FPDF_BOOL
    break

# fpdf_edit.h: 566
for _lib in _libs.values():
    if not _lib.has("FPDFImageObj_LoadJpegFile", "cdecl"):
        continue
    FPDFImageObj_LoadJpegFile = _lib.get("FPDFImageObj_LoadJpegFile", "cdecl")
    FPDFImageObj_LoadJpegFile.argtypes = [POINTER(FPDF_PAGE), c_int, FPDF_PAGEOBJECT, POINTER(FPDF_FILEACCESS)]
    FPDFImageObj_LoadJpegFile.restype = FPDF_BOOL
    break

# fpdf_edit.h: 588
for _lib in _libs.values():
    if not _lib.has("FPDFImageObj_LoadJpegFileInline", "cdecl"):
        continue
    FPDFImageObj_LoadJpegFileInline = _lib.get("FPDFImageObj_LoadJpegFileInline", "cdecl")
    FPDFImageObj_LoadJpegFileInline.argtypes = [POINTER(FPDF_PAGE), c_int, FPDF_PAGEOBJECT, POINTER(FPDF_FILEACCESS)]
    FPDFImageObj_LoadJpegFileInline.restype = FPDF_BOOL
    break

# fpdf_edit.h: 612
for _lib in _libs.values():
    if not _lib.has("FPDFImageObj_SetMatrix", "cdecl"):
        continue
    FPDFImageObj_SetMatrix = _lib.get("FPDFImageObj_SetMatrix", "cdecl")
    FPDFImageObj_SetMatrix.argtypes = [FPDF_PAGEOBJECT, c_double, c_double, c_double, c_double, c_double, c_double]
    FPDFImageObj_SetMatrix.restype = FPDF_BOOL
    break

# fpdf_edit.h: 629
for _lib in _libs.values():
    if not _lib.has("FPDFImageObj_SetBitmap", "cdecl"):
        continue
    FPDFImageObj_SetBitmap = _lib.get("FPDFImageObj_SetBitmap", "cdecl")
    FPDFImageObj_SetBitmap.argtypes = [POINTER(FPDF_PAGE), c_int, FPDF_PAGEOBJECT, FPDF_BITMAP]
    FPDFImageObj_SetBitmap.restype = FPDF_BOOL
    break

# fpdf_edit.h: 644
for _lib in _libs.values():
    if not _lib.has("FPDFImageObj_GetBitmap", "cdecl"):
        continue
    FPDFImageObj_GetBitmap = _lib.get("FPDFImageObj_GetBitmap", "cdecl")
    FPDFImageObj_GetBitmap.argtypes = [FPDF_PAGEOBJECT]
    FPDFImageObj_GetBitmap.restype = FPDF_BITMAP
    break

# fpdf_edit.h: 660
for _lib in _libs.values():
    if not _lib.has("FPDFImageObj_GetRenderedBitmap", "cdecl"):
        continue
    FPDFImageObj_GetRenderedBitmap = _lib.get("FPDFImageObj_GetRenderedBitmap", "cdecl")
    FPDFImageObj_GetRenderedBitmap.argtypes = [FPDF_DOCUMENT, FPDF_PAGE, FPDF_PAGEOBJECT]
    FPDFImageObj_GetRenderedBitmap.restype = FPDF_BITMAP
    break

# fpdf_edit.h: 675
for _lib in _libs.values():
    if not _lib.has("FPDFImageObj_GetImageDataDecoded", "cdecl"):
        continue
    FPDFImageObj_GetImageDataDecoded = _lib.get("FPDFImageObj_GetImageDataDecoded", "cdecl")
    FPDFImageObj_GetImageDataDecoded.argtypes = [FPDF_PAGEOBJECT, POINTER(None), c_ulong]
    FPDFImageObj_GetImageDataDecoded.restype = c_ulong
    break

# fpdf_edit.h: 689
for _lib in _libs.values():
    if not _lib.has("FPDFImageObj_GetImageDataRaw", "cdecl"):
        continue
    FPDFImageObj_GetImageDataRaw = _lib.get("FPDFImageObj_GetImageDataRaw", "cdecl")
    FPDFImageObj_GetImageDataRaw.argtypes = [FPDF_PAGEOBJECT, POINTER(None), c_ulong]
    FPDFImageObj_GetImageDataRaw.restype = c_ulong
    break

# fpdf_edit.h: 699
for _lib in _libs.values():
    if not _lib.has("FPDFImageObj_GetImageFilterCount", "cdecl"):
        continue
    FPDFImageObj_GetImageFilterCount = _lib.get("FPDFImageObj_GetImageFilterCount", "cdecl")
    FPDFImageObj_GetImageFilterCount.argtypes = [FPDF_PAGEOBJECT]
    FPDFImageObj_GetImageFilterCount.restype = c_int
    break

# fpdf_edit.h: 713
for _lib in _libs.values():
    if not _lib.has("FPDFImageObj_GetImageFilter", "cdecl"):
        continue
    FPDFImageObj_GetImageFilter = _lib.get("FPDFImageObj_GetImageFilter", "cdecl")
    FPDFImageObj_GetImageFilter.argtypes = [FPDF_PAGEOBJECT, c_int, POINTER(None), c_ulong]
    FPDFImageObj_GetImageFilter.restype = c_ulong
    break

# fpdf_edit.h: 730
for _lib in _libs.values():
    if not _lib.has("FPDFImageObj_GetImageMetadata", "cdecl"):
        continue
    FPDFImageObj_GetImageMetadata = _lib.get("FPDFImageObj_GetImageMetadata", "cdecl")
    FPDFImageObj_GetImageMetadata.argtypes = [FPDF_PAGEOBJECT, FPDF_PAGE, POINTER(FPDF_IMAGEOBJ_METADATA)]
    FPDFImageObj_GetImageMetadata.restype = FPDF_BOOL
    break

# fpdf_edit.h: 740
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_CreateNewPath", "cdecl"):
        continue
    FPDFPageObj_CreateNewPath = _lib.get("FPDFPageObj_CreateNewPath", "cdecl")
    FPDFPageObj_CreateNewPath.argtypes = [c_float, c_float]
    FPDFPageObj_CreateNewPath.restype = FPDF_PAGEOBJECT
    break

# fpdf_edit.h: 751
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_CreateNewRect", "cdecl"):
        continue
    FPDFPageObj_CreateNewRect = _lib.get("FPDFPageObj_CreateNewRect", "cdecl")
    FPDFPageObj_CreateNewRect.argtypes = [c_float, c_float, c_float, c_float]
    FPDFPageObj_CreateNewRect.restype = FPDF_PAGEOBJECT
    break

# fpdf_edit.h: 766
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_GetBounds", "cdecl"):
        continue
    FPDFPageObj_GetBounds = _lib.get("FPDFPageObj_GetBounds", "cdecl")
    FPDFPageObj_GetBounds.argtypes = [FPDF_PAGEOBJECT, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    FPDFPageObj_GetBounds.restype = FPDF_BOOL
    break

# fpdf_edit.h: 788
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_GetRotatedBounds", "cdecl"):
        continue
    FPDFPageObj_GetRotatedBounds = _lib.get("FPDFPageObj_GetRotatedBounds", "cdecl")
    FPDFPageObj_GetRotatedBounds.argtypes = [FPDF_PAGEOBJECT, POINTER(FS_QUADPOINTSF)]
    FPDFPageObj_GetRotatedBounds.restype = FPDF_BOOL
    break

# fpdf_edit.h: 800
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_SetBlendMode", "cdecl"):
        continue
    FPDFPageObj_SetBlendMode = _lib.get("FPDFPageObj_SetBlendMode", "cdecl")
    FPDFPageObj_SetBlendMode.argtypes = [FPDF_PAGEOBJECT, FPDF_BYTESTRING]
    FPDFPageObj_SetBlendMode.restype = None
    break

# fpdf_edit.h: 813
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_SetStrokeColor", "cdecl"):
        continue
    FPDFPageObj_SetStrokeColor = _lib.get("FPDFPageObj_SetStrokeColor", "cdecl")
    FPDFPageObj_SetStrokeColor.argtypes = [FPDF_PAGEOBJECT, c_uint, c_uint, c_uint, c_uint]
    FPDFPageObj_SetStrokeColor.restype = FPDF_BOOL
    break

# fpdf_edit.h: 829
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_GetStrokeColor", "cdecl"):
        continue
    FPDFPageObj_GetStrokeColor = _lib.get("FPDFPageObj_GetStrokeColor", "cdecl")
    FPDFPageObj_GetStrokeColor.argtypes = [FPDF_PAGEOBJECT, POINTER(c_uint), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)]
    FPDFPageObj_GetStrokeColor.restype = FPDF_BOOL
    break

# fpdf_edit.h: 842
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_SetStrokeWidth", "cdecl"):
        continue
    FPDFPageObj_SetStrokeWidth = _lib.get("FPDFPageObj_SetStrokeWidth", "cdecl")
    FPDFPageObj_SetStrokeWidth.argtypes = [FPDF_PAGEOBJECT, c_float]
    FPDFPageObj_SetStrokeWidth.restype = FPDF_BOOL
    break

# fpdf_edit.h: 851
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_GetStrokeWidth", "cdecl"):
        continue
    FPDFPageObj_GetStrokeWidth = _lib.get("FPDFPageObj_GetStrokeWidth", "cdecl")
    FPDFPageObj_GetStrokeWidth.argtypes = [FPDF_PAGEOBJECT, POINTER(c_float)]
    FPDFPageObj_GetStrokeWidth.restype = FPDF_BOOL
    break

# fpdf_edit.h: 861
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_GetLineJoin", "cdecl"):
        continue
    FPDFPageObj_GetLineJoin = _lib.get("FPDFPageObj_GetLineJoin", "cdecl")
    FPDFPageObj_GetLineJoin.argtypes = [FPDF_PAGEOBJECT]
    FPDFPageObj_GetLineJoin.restype = c_int
    break

# fpdf_edit.h: 871
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_SetLineJoin", "cdecl"):
        continue
    FPDFPageObj_SetLineJoin = _lib.get("FPDFPageObj_SetLineJoin", "cdecl")
    FPDFPageObj_SetLineJoin.argtypes = [FPDF_PAGEOBJECT, c_int]
    FPDFPageObj_SetLineJoin.restype = FPDF_BOOL
    break

# fpdf_edit.h: 881
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_GetLineCap", "cdecl"):
        continue
    FPDFPageObj_GetLineCap = _lib.get("FPDFPageObj_GetLineCap", "cdecl")
    FPDFPageObj_GetLineCap.argtypes = [FPDF_PAGEOBJECT]
    FPDFPageObj_GetLineCap.restype = c_int
    break

# fpdf_edit.h: 891
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_SetLineCap", "cdecl"):
        continue
    FPDFPageObj_SetLineCap = _lib.get("FPDFPageObj_SetLineCap", "cdecl")
    FPDFPageObj_SetLineCap.argtypes = [FPDF_PAGEOBJECT, c_int]
    FPDFPageObj_SetLineCap.restype = FPDF_BOOL
    break

# fpdf_edit.h: 903
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_SetFillColor", "cdecl"):
        continue
    FPDFPageObj_SetFillColor = _lib.get("FPDFPageObj_SetFillColor", "cdecl")
    FPDFPageObj_SetFillColor.argtypes = [FPDF_PAGEOBJECT, c_uint, c_uint, c_uint, c_uint]
    FPDFPageObj_SetFillColor.restype = FPDF_BOOL
    break

# fpdf_edit.h: 919
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_GetFillColor", "cdecl"):
        continue
    FPDFPageObj_GetFillColor = _lib.get("FPDFPageObj_GetFillColor", "cdecl")
    FPDFPageObj_GetFillColor.argtypes = [FPDF_PAGEOBJECT, POINTER(c_uint), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)]
    FPDFPageObj_GetFillColor.restype = FPDF_BOOL
    break

# fpdf_edit.h: 933
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_GetDashPhase", "cdecl"):
        continue
    FPDFPageObj_GetDashPhase = _lib.get("FPDFPageObj_GetDashPhase", "cdecl")
    FPDFPageObj_GetDashPhase.argtypes = [FPDF_PAGEOBJECT, POINTER(c_float)]
    FPDFPageObj_GetDashPhase.restype = FPDF_BOOL
    break

# fpdf_edit.h: 943
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_SetDashPhase", "cdecl"):
        continue
    FPDFPageObj_SetDashPhase = _lib.get("FPDFPageObj_SetDashPhase", "cdecl")
    FPDFPageObj_SetDashPhase.argtypes = [FPDF_PAGEOBJECT, c_float]
    FPDFPageObj_SetDashPhase.restype = FPDF_BOOL
    break

# fpdf_edit.h: 952
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_GetDashCount", "cdecl"):
        continue
    FPDFPageObj_GetDashCount = _lib.get("FPDFPageObj_GetDashCount", "cdecl")
    FPDFPageObj_GetDashCount.argtypes = [FPDF_PAGEOBJECT]
    FPDFPageObj_GetDashCount.restype = c_int
    break

# fpdf_edit.h: 963
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_GetDashArray", "cdecl"):
        continue
    FPDFPageObj_GetDashArray = _lib.get("FPDFPageObj_GetDashArray", "cdecl")
    FPDFPageObj_GetDashArray.argtypes = [FPDF_PAGEOBJECT, POINTER(c_float), c_size_t]
    FPDFPageObj_GetDashArray.restype = FPDF_BOOL
    break

# fpdf_edit.h: 977
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_SetDashArray", "cdecl"):
        continue
    FPDFPageObj_SetDashArray = _lib.get("FPDFPageObj_SetDashArray", "cdecl")
    FPDFPageObj_SetDashArray.argtypes = [FPDF_PAGEOBJECT, POINTER(c_float), c_size_t, c_float]
    FPDFPageObj_SetDashArray.restype = FPDF_BOOL
    break

# fpdf_edit.h: 990
for _lib in _libs.values():
    if not _lib.has("FPDFPath_CountSegments", "cdecl"):
        continue
    FPDFPath_CountSegments = _lib.get("FPDFPath_CountSegments", "cdecl")
    FPDFPath_CountSegments.argtypes = [FPDF_PAGEOBJECT]
    FPDFPath_CountSegments.restype = c_int
    break

# fpdf_edit.h: 999
for _lib in _libs.values():
    if not _lib.has("FPDFPath_GetPathSegment", "cdecl"):
        continue
    FPDFPath_GetPathSegment = _lib.get("FPDFPath_GetPathSegment", "cdecl")
    FPDFPath_GetPathSegment.argtypes = [FPDF_PAGEOBJECT, c_int]
    FPDFPath_GetPathSegment.restype = FPDF_PATHSEGMENT
    break

# fpdf_edit.h: 1009
for _lib in _libs.values():
    if not _lib.has("FPDFPathSegment_GetPoint", "cdecl"):
        continue
    FPDFPathSegment_GetPoint = _lib.get("FPDFPathSegment_GetPoint", "cdecl")
    FPDFPathSegment_GetPoint.argtypes = [FPDF_PATHSEGMENT, POINTER(c_float), POINTER(c_float)]
    FPDFPathSegment_GetPoint.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1017
for _lib in _libs.values():
    if not _lib.has("FPDFPathSegment_GetType", "cdecl"):
        continue
    FPDFPathSegment_GetType = _lib.get("FPDFPathSegment_GetType", "cdecl")
    FPDFPathSegment_GetType.argtypes = [FPDF_PATHSEGMENT]
    FPDFPathSegment_GetType.restype = c_int
    break

# fpdf_edit.h: 1025
for _lib in _libs.values():
    if not _lib.has("FPDFPathSegment_GetClose", "cdecl"):
        continue
    FPDFPathSegment_GetClose = _lib.get("FPDFPathSegment_GetClose", "cdecl")
    FPDFPathSegment_GetClose.argtypes = [FPDF_PATHSEGMENT]
    FPDFPathSegment_GetClose.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1037
for _lib in _libs.values():
    if not _lib.has("FPDFPath_MoveTo", "cdecl"):
        continue
    FPDFPath_MoveTo = _lib.get("FPDFPath_MoveTo", "cdecl")
    FPDFPath_MoveTo.argtypes = [FPDF_PAGEOBJECT, c_float, c_float]
    FPDFPath_MoveTo.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1050
for _lib in _libs.values():
    if not _lib.has("FPDFPath_LineTo", "cdecl"):
        continue
    FPDFPath_LineTo = _lib.get("FPDFPath_LineTo", "cdecl")
    FPDFPath_LineTo.argtypes = [FPDF_PAGEOBJECT, c_float, c_float]
    FPDFPath_LineTo.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1065
for _lib in _libs.values():
    if not _lib.has("FPDFPath_BezierTo", "cdecl"):
        continue
    FPDFPath_BezierTo = _lib.get("FPDFPath_BezierTo", "cdecl")
    FPDFPath_BezierTo.argtypes = [FPDF_PAGEOBJECT, c_float, c_float, c_float, c_float, c_float, c_float]
    FPDFPath_BezierTo.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1081
for _lib in _libs.values():
    if not _lib.has("FPDFPath_Close", "cdecl"):
        continue
    FPDFPath_Close = _lib.get("FPDFPath_Close", "cdecl")
    FPDFPath_Close.argtypes = [FPDF_PAGEOBJECT]
    FPDFPath_Close.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1090
for _lib in _libs.values():
    if not _lib.has("FPDFPath_SetDrawMode", "cdecl"):
        continue
    FPDFPath_SetDrawMode = _lib.get("FPDFPath_SetDrawMode", "cdecl")
    FPDFPath_SetDrawMode.argtypes = [FPDF_PAGEOBJECT, c_int, FPDF_BOOL]
    FPDFPath_SetDrawMode.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1101
for _lib in _libs.values():
    if not _lib.has("FPDFPath_GetDrawMode", "cdecl"):
        continue
    FPDFPath_GetDrawMode = _lib.get("FPDFPath_GetDrawMode", "cdecl")
    FPDFPath_GetDrawMode.argtypes = [FPDF_PAGEOBJECT, POINTER(c_int), POINTER(FPDF_BOOL)]
    FPDFPath_GetDrawMode.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1113
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_NewTextObj", "cdecl"):
        continue
    FPDFPageObj_NewTextObj = _lib.get("FPDFPageObj_NewTextObj", "cdecl")
    FPDFPageObj_NewTextObj.argtypes = [FPDF_DOCUMENT, FPDF_BYTESTRING, c_float]
    FPDFPageObj_NewTextObj.restype = FPDF_PAGEOBJECT
    break

# fpdf_edit.h: 1124
for _lib in _libs.values():
    if not _lib.has("FPDFText_SetText", "cdecl"):
        continue
    FPDFText_SetText = _lib.get("FPDFText_SetText", "cdecl")
    FPDFText_SetText.argtypes = [FPDF_PAGEOBJECT, FPDF_WIDESTRING]
    FPDFText_SetText.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1136
for _lib in _libs.values():
    if not _lib.has("FPDFText_SetCharcodes", "cdecl"):
        continue
    FPDFText_SetCharcodes = _lib.get("FPDFText_SetCharcodes", "cdecl")
    FPDFText_SetCharcodes.argtypes = [FPDF_PAGEOBJECT, POINTER(uint32_t), c_size_t]
    FPDFText_SetCharcodes.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1153
for _lib in _libs.values():
    if not _lib.has("FPDFText_LoadFont", "cdecl"):
        continue
    FPDFText_LoadFont = _lib.get("FPDFText_LoadFont", "cdecl")
    FPDFText_LoadFont.argtypes = [FPDF_DOCUMENT, POINTER(uint8_t), uint32_t, c_int, FPDF_BOOL]
    FPDFText_LoadFont.restype = FPDF_FONT
    break

# fpdf_edit.h: 1171
for _lib in _libs.values():
    if not _lib.has("FPDFText_LoadStandardFont", "cdecl"):
        continue
    FPDFText_LoadStandardFont = _lib.get("FPDFText_LoadStandardFont", "cdecl")
    FPDFText_LoadStandardFont.argtypes = [FPDF_DOCUMENT, FPDF_BYTESTRING]
    FPDFText_LoadStandardFont.restype = FPDF_FONT
    break

# fpdf_edit.h: 1181
for _lib in _libs.values():
    if not _lib.has("FPDFTextObj_GetFontSize", "cdecl"):
        continue
    FPDFTextObj_GetFontSize = _lib.get("FPDFTextObj_GetFontSize", "cdecl")
    FPDFTextObj_GetFontSize.argtypes = [FPDF_PAGEOBJECT, POINTER(c_float)]
    FPDFTextObj_GetFontSize.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1186
for _lib in _libs.values():
    if not _lib.has("FPDFFont_Close", "cdecl"):
        continue
    FPDFFont_Close = _lib.get("FPDFFont_Close", "cdecl")
    FPDFFont_Close.argtypes = [FPDF_FONT]
    FPDFFont_Close.restype = None
    break

# fpdf_edit.h: 1196
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_CreateTextObj", "cdecl"):
        continue
    FPDFPageObj_CreateTextObj = _lib.get("FPDFPageObj_CreateTextObj", "cdecl")
    FPDFPageObj_CreateTextObj.argtypes = [FPDF_DOCUMENT, FPDF_FONT, c_float]
    FPDFPageObj_CreateTextObj.restype = FPDF_PAGEOBJECT
    break

# fpdf_edit.h: 1207
for _lib in _libs.values():
    if not _lib.has("FPDFTextObj_GetTextRenderMode", "cdecl"):
        continue
    FPDFTextObj_GetTextRenderMode = _lib.get("FPDFTextObj_GetTextRenderMode", "cdecl")
    FPDFTextObj_GetTextRenderMode.argtypes = [FPDF_PAGEOBJECT]
    FPDFTextObj_GetTextRenderMode.restype = FPDF_TEXT_RENDERMODE
    break

# fpdf_edit.h: 1218
for _lib in _libs.values():
    if not _lib.has("FPDFTextObj_SetTextRenderMode", "cdecl"):
        continue
    FPDFTextObj_SetTextRenderMode = _lib.get("FPDFTextObj_SetTextRenderMode", "cdecl")
    FPDFTextObj_SetTextRenderMode.argtypes = [FPDF_PAGEOBJECT, FPDF_TEXT_RENDERMODE]
    FPDFTextObj_SetTextRenderMode.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1235
for _lib in _libs.values():
    if not _lib.has("FPDFTextObj_GetText", "cdecl"):
        continue
    FPDFTextObj_GetText = _lib.get("FPDFTextObj_GetText", "cdecl")
    FPDFTextObj_GetText.argtypes = [FPDF_PAGEOBJECT, FPDF_TEXTPAGE, POINTER(FPDF_WCHAR), c_ulong]
    FPDFTextObj_GetText.restype = c_ulong
    break

# fpdf_edit.h: 1254
for _lib in _libs.values():
    if not _lib.has("FPDFTextObj_GetRenderedBitmap", "cdecl"):
        continue
    FPDFTextObj_GetRenderedBitmap = _lib.get("FPDFTextObj_GetRenderedBitmap", "cdecl")
    FPDFTextObj_GetRenderedBitmap.argtypes = [FPDF_DOCUMENT, FPDF_PAGE, FPDF_PAGEOBJECT, c_float]
    FPDFTextObj_GetRenderedBitmap.restype = FPDF_BITMAP
    break

# fpdf_edit.h: 1265
for _lib in _libs.values():
    if not _lib.has("FPDFTextObj_GetFont", "cdecl"):
        continue
    FPDFTextObj_GetFont = _lib.get("FPDFTextObj_GetFont", "cdecl")
    FPDFTextObj_GetFont.argtypes = [FPDF_PAGEOBJECT]
    FPDFTextObj_GetFont.restype = FPDF_FONT
    break

# fpdf_edit.h: 1281
for _lib in _libs.values():
    if not _lib.has("FPDFFont_GetFontName", "cdecl"):
        continue
    FPDFFont_GetFontName = _lib.get("FPDFFont_GetFontName", "cdecl")
    FPDFFont_GetFontName.argtypes = [FPDF_FONT, String, c_ulong]
    FPDFFont_GetFontName.restype = c_ulong
    break

# fpdf_edit.h: 1302
for _lib in _libs.values():
    if not _lib.has("FPDFFont_GetFontData", "cdecl"):
        continue
    FPDFFont_GetFontData = _lib.get("FPDFFont_GetFontData", "cdecl")
    FPDFFont_GetFontData.argtypes = [FPDF_FONT, POINTER(uint8_t), c_size_t, POINTER(c_size_t)]
    FPDFFont_GetFontData.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1313
for _lib in _libs.values():
    if not _lib.has("FPDFFont_GetIsEmbedded", "cdecl"):
        continue
    FPDFFont_GetIsEmbedded = _lib.get("FPDFFont_GetIsEmbedded", "cdecl")
    FPDFFont_GetIsEmbedded.argtypes = [FPDF_FONT]
    FPDFFont_GetIsEmbedded.restype = c_int
    break

# fpdf_edit.h: 1322
for _lib in _libs.values():
    if not _lib.has("FPDFFont_GetFlags", "cdecl"):
        continue
    FPDFFont_GetFlags = _lib.get("FPDFFont_GetFlags", "cdecl")
    FPDFFont_GetFlags.argtypes = [FPDF_FONT]
    FPDFFont_GetFlags.restype = c_int
    break

# fpdf_edit.h: 1331
for _lib in _libs.values():
    if not _lib.has("FPDFFont_GetWeight", "cdecl"):
        continue
    FPDFFont_GetWeight = _lib.get("FPDFFont_GetWeight", "cdecl")
    FPDFFont_GetWeight.argtypes = [FPDF_FONT]
    FPDFFont_GetWeight.restype = c_int
    break

# fpdf_edit.h: 1343
for _lib in _libs.values():
    if not _lib.has("FPDFFont_GetItalicAngle", "cdecl"):
        continue
    FPDFFont_GetItalicAngle = _lib.get("FPDFFont_GetItalicAngle", "cdecl")
    FPDFFont_GetItalicAngle.argtypes = [FPDF_FONT, POINTER(c_int)]
    FPDFFont_GetItalicAngle.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1357
for _lib in _libs.values():
    if not _lib.has("FPDFFont_GetAscent", "cdecl"):
        continue
    FPDFFont_GetAscent = _lib.get("FPDFFont_GetAscent", "cdecl")
    FPDFFont_GetAscent.argtypes = [FPDF_FONT, c_float, POINTER(c_float)]
    FPDFFont_GetAscent.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1372
for _lib in _libs.values():
    if not _lib.has("FPDFFont_GetDescent", "cdecl"):
        continue
    FPDFFont_GetDescent = _lib.get("FPDFFont_GetDescent", "cdecl")
    FPDFFont_GetDescent.argtypes = [FPDF_FONT, c_float, POINTER(c_float)]
    FPDFFont_GetDescent.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1388
for _lib in _libs.values():
    if not _lib.has("FPDFFont_GetGlyphWidth", "cdecl"):
        continue
    FPDFFont_GetGlyphWidth = _lib.get("FPDFFont_GetGlyphWidth", "cdecl")
    FPDFFont_GetGlyphWidth.argtypes = [FPDF_FONT, uint32_t, c_float, POINTER(c_float)]
    FPDFFont_GetGlyphWidth.restype = FPDF_BOOL
    break

# fpdf_edit.h: 1401
for _lib in _libs.values():
    if not _lib.has("FPDFFont_GetGlyphPath", "cdecl"):
        continue
    FPDFFont_GetGlyphPath = _lib.get("FPDFFont_GetGlyphPath", "cdecl")
    FPDFFont_GetGlyphPath.argtypes = [FPDF_FONT, uint32_t, c_float]
    FPDFFont_GetGlyphPath.restype = FPDF_GLYPHPATH
    break

# fpdf_edit.h: 1412
for _lib in _libs.values():
    if not _lib.has("FPDFGlyphPath_CountGlyphSegments", "cdecl"):
        continue
    FPDFGlyphPath_CountGlyphSegments = _lib.get("FPDFGlyphPath_CountGlyphSegments", "cdecl")
    FPDFGlyphPath_CountGlyphSegments.argtypes = [FPDF_GLYPHPATH]
    FPDFGlyphPath_CountGlyphSegments.restype = c_int
    break

# fpdf_edit.h: 1422
for _lib in _libs.values():
    if not _lib.has("FPDFGlyphPath_GetGlyphPathSegment", "cdecl"):
        continue
    FPDFGlyphPath_GetGlyphPathSegment = _lib.get("FPDFGlyphPath_GetGlyphPathSegment", "cdecl")
    FPDFGlyphPath_GetGlyphPathSegment.argtypes = [FPDF_GLYPHPATH, c_int]
    FPDFGlyphPath_GetGlyphPathSegment.restype = FPDF_PATHSEGMENT
    break

# fpdf_edit.h: 1430
for _lib in _libs.values():
    if not _lib.has("FPDFFormObj_CountObjects", "cdecl"):
        continue
    FPDFFormObj_CountObjects = _lib.get("FPDFFormObj_CountObjects", "cdecl")
    FPDFFormObj_CountObjects.argtypes = [FPDF_PAGEOBJECT]
    FPDFFormObj_CountObjects.restype = c_int
    break

# fpdf_edit.h: 1439
for _lib in _libs.values():
    if not _lib.has("FPDFFormObj_GetObject", "cdecl"):
        continue
    FPDFFormObj_GetObject = _lib.get("FPDFFormObj_GetObject", "cdecl")
    FPDFFormObj_GetObject.argtypes = [FPDF_PAGEOBJECT, c_ulong]
    FPDFFormObj_GetObject.restype = FPDF_PAGEOBJECT
    break

time_t = __time_t# /usr/include/x86_64-linux-gnu/bits/types/time_t.h: 10

# /usr/include/x86_64-linux-gnu/bits/types/struct_tm.h: 7
class struct_tm(Structure):
    pass

struct_tm.__slots__ = [
    'tm_sec',
    'tm_min',
    'tm_hour',
    'tm_mday',
    'tm_mon',
    'tm_year',
    'tm_wday',
    'tm_yday',
    'tm_isdst',
    'tm_gmtoff',
    'tm_zone',
]
struct_tm._fields_ = [
    ('tm_sec', c_int),
    ('tm_min', c_int),
    ('tm_hour', c_int),
    ('tm_mday', c_int),
    ('tm_mon', c_int),
    ('tm_year', c_int),
    ('tm_wday', c_int),
    ('tm_yday', c_int),
    ('tm_isdst', c_int),
    ('tm_gmtoff', c_long),
    ('tm_zone', String),
]

# fpdf_ext.h: 51
class struct__UNSUPPORT_INFO(Structure):
    pass

struct__UNSUPPORT_INFO.__slots__ = [
    'version',
    'FSDK_UnSupport_Handler',
]
struct__UNSUPPORT_INFO._fields_ = [
    ('version', c_int),
    ('FSDK_UnSupport_Handler', CFUNCTYPE(UNCHECKED(None), POINTER(struct__UNSUPPORT_INFO), c_int)),
]

UNSUPPORT_INFO = struct__UNSUPPORT_INFO# fpdf_ext.h: 62

# fpdf_ext.h: 70
for _lib in _libs.values():
    if not _lib.has("FSDK_SetUnSpObjProcessHandler", "cdecl"):
        continue
    FSDK_SetUnSpObjProcessHandler = _lib.get("FSDK_SetUnSpObjProcessHandler", "cdecl")
    FSDK_SetUnSpObjProcessHandler.argtypes = [POINTER(UNSUPPORT_INFO)]
    FSDK_SetUnSpObjProcessHandler.restype = FPDF_BOOL
    break

# fpdf_ext.h: 79
for _lib in _libs.values():
    if not _lib.has("FSDK_SetTimeFunction", "cdecl"):
        continue
    FSDK_SetTimeFunction = _lib.get("FSDK_SetTimeFunction", "cdecl")
    FSDK_SetTimeFunction.argtypes = [CFUNCTYPE(UNCHECKED(time_t), )]
    FSDK_SetTimeFunction.restype = None
    break

# fpdf_ext.h: 89
for _lib in _libs.values():
    if not _lib.has("FSDK_SetLocaltimeFunction", "cdecl"):
        continue
    FSDK_SetLocaltimeFunction = _lib.get("FSDK_SetLocaltimeFunction", "cdecl")
    FSDK_SetLocaltimeFunction.argtypes = [CFUNCTYPE(UNCHECKED(POINTER(struct_tm)), POINTER(time_t))]
    FSDK_SetLocaltimeFunction.restype = None
    break

# fpdf_ext.h: 113
for _lib in _libs.values():
    if not _lib.has("FPDFDoc_GetPageMode", "cdecl"):
        continue
    FPDFDoc_GetPageMode = _lib.get("FPDFDoc_GetPageMode", "cdecl")
    FPDFDoc_GetPageMode.argtypes = [FPDF_DOCUMENT]
    FPDFDoc_GetPageMode.restype = c_int
    break

# fpdf_flatten.h: 38
for _lib in _libs.values():
    if not _lib.has("FPDFPage_Flatten", "cdecl"):
        continue
    FPDFPage_Flatten = _lib.get("FPDFPage_Flatten", "cdecl")
    FPDFPage_Flatten.argtypes = [FPDF_PAGE, c_int]
    FPDFPage_Flatten.restype = c_int
    break

enum_anon_7 = c_int# fpdf_fwlevent.h: 28

FWL_EVENTFLAG_ShiftKey = (1 << 0)# fpdf_fwlevent.h: 28

FWL_EVENTFLAG_ControlKey = (1 << 1)# fpdf_fwlevent.h: 28

FWL_EVENTFLAG_AltKey = (1 << 2)# fpdf_fwlevent.h: 28

FWL_EVENTFLAG_MetaKey = (1 << 3)# fpdf_fwlevent.h: 28

FWL_EVENTFLAG_KeyPad = (1 << 4)# fpdf_fwlevent.h: 28

FWL_EVENTFLAG_AutoRepeat = (1 << 5)# fpdf_fwlevent.h: 28

FWL_EVENTFLAG_LeftButtonDown = (1 << 6)# fpdf_fwlevent.h: 28

FWL_EVENTFLAG_MiddleButtonDown = (1 << 7)# fpdf_fwlevent.h: 28

FWL_EVENTFLAG_RightButtonDown = (1 << 8)# fpdf_fwlevent.h: 28

FWL_EVENTFLAG = enum_anon_7# fpdf_fwlevent.h: 28

enum_anon_8 = c_int# fpdf_fwlevent.h: 201

FWL_VKEY_Back = 0x08# fpdf_fwlevent.h: 201

FWL_VKEY_Tab = 0x09# fpdf_fwlevent.h: 201

FWL_VKEY_NewLine = 0x0A# fpdf_fwlevent.h: 201

FWL_VKEY_Clear = 0x0C# fpdf_fwlevent.h: 201

FWL_VKEY_Return = 0x0D# fpdf_fwlevent.h: 201

FWL_VKEY_Shift = 0x10# fpdf_fwlevent.h: 201

FWL_VKEY_Control = 0x11# fpdf_fwlevent.h: 201

FWL_VKEY_Menu = 0x12# fpdf_fwlevent.h: 201

FWL_VKEY_Pause = 0x13# fpdf_fwlevent.h: 201

FWL_VKEY_Capital = 0x14# fpdf_fwlevent.h: 201

FWL_VKEY_Kana = 0x15# fpdf_fwlevent.h: 201

FWL_VKEY_Hangul = 0x15# fpdf_fwlevent.h: 201

FWL_VKEY_Junja = 0x17# fpdf_fwlevent.h: 201

FWL_VKEY_Final = 0x18# fpdf_fwlevent.h: 201

FWL_VKEY_Hanja = 0x19# fpdf_fwlevent.h: 201

FWL_VKEY_Kanji = 0x19# fpdf_fwlevent.h: 201

FWL_VKEY_Escape = 0x1B# fpdf_fwlevent.h: 201

FWL_VKEY_Convert = 0x1C# fpdf_fwlevent.h: 201

FWL_VKEY_NonConvert = 0x1D# fpdf_fwlevent.h: 201

FWL_VKEY_Accept = 0x1E# fpdf_fwlevent.h: 201

FWL_VKEY_ModeChange = 0x1F# fpdf_fwlevent.h: 201

FWL_VKEY_Space = 0x20# fpdf_fwlevent.h: 201

FWL_VKEY_Prior = 0x21# fpdf_fwlevent.h: 201

FWL_VKEY_Next = 0x22# fpdf_fwlevent.h: 201

FWL_VKEY_End = 0x23# fpdf_fwlevent.h: 201

FWL_VKEY_Home = 0x24# fpdf_fwlevent.h: 201

FWL_VKEY_Left = 0x25# fpdf_fwlevent.h: 201

FWL_VKEY_Up = 0x26# fpdf_fwlevent.h: 201

FWL_VKEY_Right = 0x27# fpdf_fwlevent.h: 201

FWL_VKEY_Down = 0x28# fpdf_fwlevent.h: 201

FWL_VKEY_Select = 0x29# fpdf_fwlevent.h: 201

FWL_VKEY_Print = 0x2A# fpdf_fwlevent.h: 201

FWL_VKEY_Execute = 0x2B# fpdf_fwlevent.h: 201

FWL_VKEY_Snapshot = 0x2C# fpdf_fwlevent.h: 201

FWL_VKEY_Insert = 0x2D# fpdf_fwlevent.h: 201

FWL_VKEY_Delete = 0x2E# fpdf_fwlevent.h: 201

FWL_VKEY_Help = 0x2F# fpdf_fwlevent.h: 201

FWL_VKEY_0 = 0x30# fpdf_fwlevent.h: 201

FWL_VKEY_1 = 0x31# fpdf_fwlevent.h: 201

FWL_VKEY_2 = 0x32# fpdf_fwlevent.h: 201

FWL_VKEY_3 = 0x33# fpdf_fwlevent.h: 201

FWL_VKEY_4 = 0x34# fpdf_fwlevent.h: 201

FWL_VKEY_5 = 0x35# fpdf_fwlevent.h: 201

FWL_VKEY_6 = 0x36# fpdf_fwlevent.h: 201

FWL_VKEY_7 = 0x37# fpdf_fwlevent.h: 201

FWL_VKEY_8 = 0x38# fpdf_fwlevent.h: 201

FWL_VKEY_9 = 0x39# fpdf_fwlevent.h: 201

FWL_VKEY_A = 0x41# fpdf_fwlevent.h: 201

FWL_VKEY_B = 0x42# fpdf_fwlevent.h: 201

FWL_VKEY_C = 0x43# fpdf_fwlevent.h: 201

FWL_VKEY_D = 0x44# fpdf_fwlevent.h: 201

FWL_VKEY_E = 0x45# fpdf_fwlevent.h: 201

FWL_VKEY_F = 0x46# fpdf_fwlevent.h: 201

FWL_VKEY_G = 0x47# fpdf_fwlevent.h: 201

FWL_VKEY_H = 0x48# fpdf_fwlevent.h: 201

FWL_VKEY_I = 0x49# fpdf_fwlevent.h: 201

FWL_VKEY_J = 0x4A# fpdf_fwlevent.h: 201

FWL_VKEY_K = 0x4B# fpdf_fwlevent.h: 201

FWL_VKEY_L = 0x4C# fpdf_fwlevent.h: 201

FWL_VKEY_M = 0x4D# fpdf_fwlevent.h: 201

FWL_VKEY_N = 0x4E# fpdf_fwlevent.h: 201

FWL_VKEY_O = 0x4F# fpdf_fwlevent.h: 201

FWL_VKEY_P = 0x50# fpdf_fwlevent.h: 201

FWL_VKEY_Q = 0x51# fpdf_fwlevent.h: 201

FWL_VKEY_R = 0x52# fpdf_fwlevent.h: 201

FWL_VKEY_S = 0x53# fpdf_fwlevent.h: 201

FWL_VKEY_T = 0x54# fpdf_fwlevent.h: 201

FWL_VKEY_U = 0x55# fpdf_fwlevent.h: 201

FWL_VKEY_V = 0x56# fpdf_fwlevent.h: 201

FWL_VKEY_W = 0x57# fpdf_fwlevent.h: 201

FWL_VKEY_X = 0x58# fpdf_fwlevent.h: 201

FWL_VKEY_Y = 0x59# fpdf_fwlevent.h: 201

FWL_VKEY_Z = 0x5A# fpdf_fwlevent.h: 201

FWL_VKEY_LWin = 0x5B# fpdf_fwlevent.h: 201

FWL_VKEY_Command = 0x5B# fpdf_fwlevent.h: 201

FWL_VKEY_RWin = 0x5C# fpdf_fwlevent.h: 201

FWL_VKEY_Apps = 0x5D# fpdf_fwlevent.h: 201

FWL_VKEY_Sleep = 0x5F# fpdf_fwlevent.h: 201

FWL_VKEY_NumPad0 = 0x60# fpdf_fwlevent.h: 201

FWL_VKEY_NumPad1 = 0x61# fpdf_fwlevent.h: 201

FWL_VKEY_NumPad2 = 0x62# fpdf_fwlevent.h: 201

FWL_VKEY_NumPad3 = 0x63# fpdf_fwlevent.h: 201

FWL_VKEY_NumPad4 = 0x64# fpdf_fwlevent.h: 201

FWL_VKEY_NumPad5 = 0x65# fpdf_fwlevent.h: 201

FWL_VKEY_NumPad6 = 0x66# fpdf_fwlevent.h: 201

FWL_VKEY_NumPad7 = 0x67# fpdf_fwlevent.h: 201

FWL_VKEY_NumPad8 = 0x68# fpdf_fwlevent.h: 201

FWL_VKEY_NumPad9 = 0x69# fpdf_fwlevent.h: 201

FWL_VKEY_Multiply = 0x6A# fpdf_fwlevent.h: 201

FWL_VKEY_Add = 0x6B# fpdf_fwlevent.h: 201

FWL_VKEY_Separator = 0x6C# fpdf_fwlevent.h: 201

FWL_VKEY_Subtract = 0x6D# fpdf_fwlevent.h: 201

FWL_VKEY_Decimal = 0x6E# fpdf_fwlevent.h: 201

FWL_VKEY_Divide = 0x6F# fpdf_fwlevent.h: 201

FWL_VKEY_F1 = 0x70# fpdf_fwlevent.h: 201

FWL_VKEY_F2 = 0x71# fpdf_fwlevent.h: 201

FWL_VKEY_F3 = 0x72# fpdf_fwlevent.h: 201

FWL_VKEY_F4 = 0x73# fpdf_fwlevent.h: 201

FWL_VKEY_F5 = 0x74# fpdf_fwlevent.h: 201

FWL_VKEY_F6 = 0x75# fpdf_fwlevent.h: 201

FWL_VKEY_F7 = 0x76# fpdf_fwlevent.h: 201

FWL_VKEY_F8 = 0x77# fpdf_fwlevent.h: 201

FWL_VKEY_F9 = 0x78# fpdf_fwlevent.h: 201

FWL_VKEY_F10 = 0x79# fpdf_fwlevent.h: 201

FWL_VKEY_F11 = 0x7A# fpdf_fwlevent.h: 201

FWL_VKEY_F12 = 0x7B# fpdf_fwlevent.h: 201

FWL_VKEY_F13 = 0x7C# fpdf_fwlevent.h: 201

FWL_VKEY_F14 = 0x7D# fpdf_fwlevent.h: 201

FWL_VKEY_F15 = 0x7E# fpdf_fwlevent.h: 201

FWL_VKEY_F16 = 0x7F# fpdf_fwlevent.h: 201

FWL_VKEY_F17 = 0x80# fpdf_fwlevent.h: 201

FWL_VKEY_F18 = 0x81# fpdf_fwlevent.h: 201

FWL_VKEY_F19 = 0x82# fpdf_fwlevent.h: 201

FWL_VKEY_F20 = 0x83# fpdf_fwlevent.h: 201

FWL_VKEY_F21 = 0x84# fpdf_fwlevent.h: 201

FWL_VKEY_F22 = 0x85# fpdf_fwlevent.h: 201

FWL_VKEY_F23 = 0x86# fpdf_fwlevent.h: 201

FWL_VKEY_F24 = 0x87# fpdf_fwlevent.h: 201

FWL_VKEY_NunLock = 0x90# fpdf_fwlevent.h: 201

FWL_VKEY_Scroll = 0x91# fpdf_fwlevent.h: 201

FWL_VKEY_LShift = 0xA0# fpdf_fwlevent.h: 201

FWL_VKEY_RShift = 0xA1# fpdf_fwlevent.h: 201

FWL_VKEY_LControl = 0xA2# fpdf_fwlevent.h: 201

FWL_VKEY_RControl = 0xA3# fpdf_fwlevent.h: 201

FWL_VKEY_LMenu = 0xA4# fpdf_fwlevent.h: 201

FWL_VKEY_RMenu = 0xA5# fpdf_fwlevent.h: 201

FWL_VKEY_BROWSER_Back = 0xA6# fpdf_fwlevent.h: 201

FWL_VKEY_BROWSER_Forward = 0xA7# fpdf_fwlevent.h: 201

FWL_VKEY_BROWSER_Refresh = 0xA8# fpdf_fwlevent.h: 201

FWL_VKEY_BROWSER_Stop = 0xA9# fpdf_fwlevent.h: 201

FWL_VKEY_BROWSER_Search = 0xAA# fpdf_fwlevent.h: 201

FWL_VKEY_BROWSER_Favorites = 0xAB# fpdf_fwlevent.h: 201

FWL_VKEY_BROWSER_Home = 0xAC# fpdf_fwlevent.h: 201

FWL_VKEY_VOLUME_Mute = 0xAD# fpdf_fwlevent.h: 201

FWL_VKEY_VOLUME_Down = 0xAE# fpdf_fwlevent.h: 201

FWL_VKEY_VOLUME_Up = 0xAF# fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_NEXT_Track = 0xB0# fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_PREV_Track = 0xB1# fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_Stop = 0xB2# fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_PLAY_Pause = 0xB3# fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_LAUNCH_Mail = 0xB4# fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_LAUNCH_MEDIA_Select = 0xB5# fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_LAUNCH_APP1 = 0xB6# fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_LAUNCH_APP2 = 0xB7# fpdf_fwlevent.h: 201

FWL_VKEY_OEM_1 = 0xBA# fpdf_fwlevent.h: 201

FWL_VKEY_OEM_Plus = 0xBB# fpdf_fwlevent.h: 201

FWL_VKEY_OEM_Comma = 0xBC# fpdf_fwlevent.h: 201

FWL_VKEY_OEM_Minus = 0xBD# fpdf_fwlevent.h: 201

FWL_VKEY_OEM_Period = 0xBE# fpdf_fwlevent.h: 201

FWL_VKEY_OEM_2 = 0xBF# fpdf_fwlevent.h: 201

FWL_VKEY_OEM_3 = 0xC0# fpdf_fwlevent.h: 201

FWL_VKEY_OEM_4 = 0xDB# fpdf_fwlevent.h: 201

FWL_VKEY_OEM_5 = 0xDC# fpdf_fwlevent.h: 201

FWL_VKEY_OEM_6 = 0xDD# fpdf_fwlevent.h: 201

FWL_VKEY_OEM_7 = 0xDE# fpdf_fwlevent.h: 201

FWL_VKEY_OEM_8 = 0xDF# fpdf_fwlevent.h: 201

FWL_VKEY_OEM_102 = 0xE2# fpdf_fwlevent.h: 201

FWL_VKEY_ProcessKey = 0xE5# fpdf_fwlevent.h: 201

FWL_VKEY_Packet = 0xE7# fpdf_fwlevent.h: 201

FWL_VKEY_Attn = 0xF6# fpdf_fwlevent.h: 201

FWL_VKEY_Crsel = 0xF7# fpdf_fwlevent.h: 201

FWL_VKEY_Exsel = 0xF8# fpdf_fwlevent.h: 201

FWL_VKEY_Ereof = 0xF9# fpdf_fwlevent.h: 201

FWL_VKEY_Play = 0xFA# fpdf_fwlevent.h: 201

FWL_VKEY_Zoom = 0xFB# fpdf_fwlevent.h: 201

FWL_VKEY_NoName = 0xFC# fpdf_fwlevent.h: 201

FWL_VKEY_PA1 = 0xFD# fpdf_fwlevent.h: 201

FWL_VKEY_OEM_Clear = 0xFE# fpdf_fwlevent.h: 201

FWL_VKEY_Unknown = 0# fpdf_fwlevent.h: 201

FWL_VKEYCODE = enum_anon_8# fpdf_fwlevent.h: 201

# fpdf_javascript.h: 22
for _lib in _libs.values():
    if not _lib.has("FPDFDoc_GetJavaScriptActionCount", "cdecl"):
        continue
    FPDFDoc_GetJavaScriptActionCount = _lib.get("FPDFDoc_GetJavaScriptActionCount", "cdecl")
    FPDFDoc_GetJavaScriptActionCount.argtypes = [FPDF_DOCUMENT]
    FPDFDoc_GetJavaScriptActionCount.restype = c_int
    break

# fpdf_javascript.h: 34
for _lib in _libs.values():
    if not _lib.has("FPDFDoc_GetJavaScriptAction", "cdecl"):
        continue
    FPDFDoc_GetJavaScriptAction = _lib.get("FPDFDoc_GetJavaScriptAction", "cdecl")
    FPDFDoc_GetJavaScriptAction.argtypes = [FPDF_DOCUMENT, c_int]
    FPDFDoc_GetJavaScriptAction.restype = FPDF_JAVASCRIPT_ACTION
    break

# fpdf_javascript.h: 41
for _lib in _libs.values():
    if not _lib.has("FPDFDoc_CloseJavaScriptAction", "cdecl"):
        continue
    FPDFDoc_CloseJavaScriptAction = _lib.get("FPDFDoc_CloseJavaScriptAction", "cdecl")
    FPDFDoc_CloseJavaScriptAction.argtypes = [FPDF_JAVASCRIPT_ACTION]
    FPDFDoc_CloseJavaScriptAction.restype = None
    break

# fpdf_javascript.h: 54
for _lib in _libs.values():
    if not _lib.has("FPDFJavaScriptAction_GetName", "cdecl"):
        continue
    FPDFJavaScriptAction_GetName = _lib.get("FPDFJavaScriptAction_GetName", "cdecl")
    FPDFJavaScriptAction_GetName.argtypes = [FPDF_JAVASCRIPT_ACTION, POINTER(FPDF_WCHAR), c_ulong]
    FPDFJavaScriptAction_GetName.restype = c_ulong
    break

# fpdf_javascript.h: 69
for _lib in _libs.values():
    if not _lib.has("FPDFJavaScriptAction_GetScript", "cdecl"):
        continue
    FPDFJavaScriptAction_GetScript = _lib.get("FPDFJavaScriptAction_GetScript", "cdecl")
    FPDFJavaScriptAction_GetScript.argtypes = [FPDF_JAVASCRIPT_ACTION, POINTER(FPDF_WCHAR), c_ulong]
    FPDFJavaScriptAction_GetScript.restype = c_ulong
    break

# fpdf_ppo.h: 32
for _lib in _libs.values():
    if not _lib.has("FPDF_ImportPagesByIndex", "cdecl"):
        continue
    FPDF_ImportPagesByIndex = _lib.get("FPDF_ImportPagesByIndex", "cdecl")
    FPDF_ImportPagesByIndex.argtypes = [FPDF_DOCUMENT, FPDF_DOCUMENT, POINTER(c_int), c_ulong, c_int]
    FPDF_ImportPagesByIndex.restype = FPDF_BOOL
    break

# fpdf_ppo.h: 49
for _lib in _libs.values():
    if not _lib.has("FPDF_ImportPages", "cdecl"):
        continue
    FPDF_ImportPages = _lib.get("FPDF_ImportPages", "cdecl")
    FPDF_ImportPages.argtypes = [FPDF_DOCUMENT, FPDF_DOCUMENT, FPDF_BYTESTRING, c_int]
    FPDF_ImportPages.restype = FPDF_BOOL
    break

# fpdf_ppo.h: 72
for _lib in _libs.values():
    if not _lib.has("FPDF_ImportNPagesToOne", "cdecl"):
        continue
    FPDF_ImportNPagesToOne = _lib.get("FPDF_ImportNPagesToOne", "cdecl")
    FPDF_ImportNPagesToOne.argtypes = [FPDF_DOCUMENT, c_float, c_float, c_size_t, c_size_t]
    FPDF_ImportNPagesToOne.restype = FPDF_DOCUMENT
    break

# fpdf_ppo.h: 85
for _lib in _libs.values():
    if not _lib.has("FPDF_NewXObjectFromPage", "cdecl"):
        continue
    FPDF_NewXObjectFromPage = _lib.get("FPDF_NewXObjectFromPage", "cdecl")
    FPDF_NewXObjectFromPage.argtypes = [FPDF_DOCUMENT, FPDF_DOCUMENT, c_int]
    FPDF_NewXObjectFromPage.restype = FPDF_XOBJECT
    break

# fpdf_ppo.h: 92
for _lib in _libs.values():
    if not _lib.has("FPDF_CloseXObject", "cdecl"):
        continue
    FPDF_CloseXObject = _lib.get("FPDF_CloseXObject", "cdecl")
    FPDF_CloseXObject.argtypes = [FPDF_XOBJECT]
    FPDF_CloseXObject.restype = None
    break

# fpdf_ppo.h: 100
for _lib in _libs.values():
    if not _lib.has("FPDF_NewFormObjectFromXObject", "cdecl"):
        continue
    FPDF_NewFormObjectFromXObject = _lib.get("FPDF_NewFormObjectFromXObject", "cdecl")
    FPDF_NewFormObjectFromXObject.argtypes = [FPDF_XOBJECT]
    FPDF_NewFormObjectFromXObject.restype = FPDF_PAGEOBJECT
    break

# fpdf_ppo.h: 109
for _lib in _libs.values():
    if not _lib.has("FPDF_CopyViewerPreferences", "cdecl"):
        continue
    FPDF_CopyViewerPreferences = _lib.get("FPDF_CopyViewerPreferences", "cdecl")
    FPDF_CopyViewerPreferences.argtypes = [FPDF_DOCUMENT, FPDF_DOCUMENT]
    FPDF_CopyViewerPreferences.restype = FPDF_BOOL
    break

# fpdf_progressive.h: 25
class struct__IFSDK_PAUSE(Structure):
    pass

struct__IFSDK_PAUSE.__slots__ = [
    'version',
    'NeedToPauseNow',
    'user',
]
struct__IFSDK_PAUSE._fields_ = [
    ('version', c_int),
    ('NeedToPauseNow', CFUNCTYPE(UNCHECKED(FPDF_BOOL), POINTER(struct__IFSDK_PAUSE))),
    ('user', POINTER(None)),
]

IFSDK_PAUSE = struct__IFSDK_PAUSE# fpdf_progressive.h: 47

# fpdf_progressive.h: 83
for _lib in _libs.values():
    if not _lib.has("FPDF_RenderPageBitmapWithColorScheme_Start", "cdecl"):
        continue
    FPDF_RenderPageBitmapWithColorScheme_Start = _lib.get("FPDF_RenderPageBitmapWithColorScheme_Start", "cdecl")
    FPDF_RenderPageBitmapWithColorScheme_Start.argtypes = [FPDF_BITMAP, FPDF_PAGE, c_int, c_int, c_int, c_int, c_int, c_int, POINTER(FPDF_COLORSCHEME), POINTER(IFSDK_PAUSE)]
    FPDF_RenderPageBitmapWithColorScheme_Start.restype = c_int
    break

# fpdf_progressive.h: 121
for _lib in _libs.values():
    if not _lib.has("FPDF_RenderPageBitmap_Start", "cdecl"):
        continue
    FPDF_RenderPageBitmap_Start = _lib.get("FPDF_RenderPageBitmap_Start", "cdecl")
    FPDF_RenderPageBitmap_Start.argtypes = [FPDF_BITMAP, FPDF_PAGE, c_int, c_int, c_int, c_int, c_int, c_int, POINTER(IFSDK_PAUSE)]
    FPDF_RenderPageBitmap_Start.restype = c_int
    break

# fpdf_progressive.h: 142
for _lib in _libs.values():
    if not _lib.has("FPDF_RenderPage_Continue", "cdecl"):
        continue
    FPDF_RenderPage_Continue = _lib.get("FPDF_RenderPage_Continue", "cdecl")
    FPDF_RenderPage_Continue.argtypes = [FPDF_PAGE, POINTER(IFSDK_PAUSE)]
    FPDF_RenderPage_Continue.restype = c_int
    break

# fpdf_progressive.h: 153
for _lib in _libs.values():
    if not _lib.has("FPDF_RenderPage_Close", "cdecl"):
        continue
    FPDF_RenderPage_Close = _lib.get("FPDF_RenderPage_Close", "cdecl")
    FPDF_RenderPage_Close.argtypes = [FPDF_PAGE]
    FPDF_RenderPage_Close.restype = None
    break

# fpdf_save.h: 19
class struct_FPDF_FILEWRITE_(Structure):
    pass

struct_FPDF_FILEWRITE_.__slots__ = [
    'version',
    'WriteBlock',
]
struct_FPDF_FILEWRITE_._fields_ = [
    ('version', c_int),
    ('WriteBlock', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_FPDF_FILEWRITE_), POINTER(None), c_ulong)),
]

FPDF_FILEWRITE = struct_FPDF_FILEWRITE_# fpdf_save.h: 42

# fpdf_save.h: 59
for _lib in _libs.values():
    if not _lib.has("FPDF_SaveAsCopy", "cdecl"):
        continue
    FPDF_SaveAsCopy = _lib.get("FPDF_SaveAsCopy", "cdecl")
    FPDF_SaveAsCopy.argtypes = [FPDF_DOCUMENT, POINTER(FPDF_FILEWRITE), FPDF_DWORD]
    FPDF_SaveAsCopy.restype = FPDF_BOOL
    break

# fpdf_save.h: 76
for _lib in _libs.values():
    if not _lib.has("FPDF_SaveWithVersion", "cdecl"):
        continue
    FPDF_SaveWithVersion = _lib.get("FPDF_SaveWithVersion", "cdecl")
    FPDF_SaveWithVersion.argtypes = [FPDF_DOCUMENT, POINTER(FPDF_FILEWRITE), FPDF_DWORD, c_int]
    FPDF_SaveWithVersion.restype = FPDF_BOOL
    break

# fpdf_searchex.h: 24
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetCharIndexFromTextIndex", "cdecl"):
        continue
    FPDFText_GetCharIndexFromTextIndex = _lib.get("FPDFText_GetCharIndexFromTextIndex", "cdecl")
    FPDFText_GetCharIndexFromTextIndex.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_GetCharIndexFromTextIndex.restype = c_int
    break

# fpdf_searchex.h: 33
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetTextIndexFromCharIndex", "cdecl"):
        continue
    FPDFText_GetTextIndexFromCharIndex = _lib.get("FPDFText_GetTextIndexFromCharIndex", "cdecl")
    FPDFText_GetTextIndexFromCharIndex.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_GetTextIndexFromCharIndex.restype = c_int
    break

# fpdf_signature.h: 22
for _lib in _libs.values():
    if not _lib.has("FPDF_GetSignatureCount", "cdecl"):
        continue
    FPDF_GetSignatureCount = _lib.get("FPDF_GetSignatureCount", "cdecl")
    FPDF_GetSignatureCount.argtypes = [FPDF_DOCUMENT]
    FPDF_GetSignatureCount.restype = c_int
    break

# fpdf_signature.h: 35
for _lib in _libs.values():
    if not _lib.has("FPDF_GetSignatureObject", "cdecl"):
        continue
    FPDF_GetSignatureObject = _lib.get("FPDF_GetSignatureObject", "cdecl")
    FPDF_GetSignatureObject.argtypes = [FPDF_DOCUMENT, c_int]
    FPDF_GetSignatureObject.restype = FPDF_SIGNATURE
    break

# fpdf_signature.h: 52
for _lib in _libs.values():
    if not _lib.has("FPDFSignatureObj_GetContents", "cdecl"):
        continue
    FPDFSignatureObj_GetContents = _lib.get("FPDFSignatureObj_GetContents", "cdecl")
    FPDFSignatureObj_GetContents.argtypes = [FPDF_SIGNATURE, POINTER(None), c_ulong]
    FPDFSignatureObj_GetContents.restype = c_ulong
    break

# fpdf_signature.h: 74
for _lib in _libs.values():
    if not _lib.has("FPDFSignatureObj_GetByteRange", "cdecl"):
        continue
    FPDFSignatureObj_GetByteRange = _lib.get("FPDFSignatureObj_GetByteRange", "cdecl")
    FPDFSignatureObj_GetByteRange.argtypes = [FPDF_SIGNATURE, POINTER(c_int), c_ulong]
    FPDFSignatureObj_GetByteRange.restype = c_ulong
    break

# fpdf_signature.h: 93
for _lib in _libs.values():
    if not _lib.has("FPDFSignatureObj_GetSubFilter", "cdecl"):
        continue
    FPDFSignatureObj_GetSubFilter = _lib.get("FPDFSignatureObj_GetSubFilter", "cdecl")
    FPDFSignatureObj_GetSubFilter.argtypes = [FPDF_SIGNATURE, String, c_ulong]
    FPDFSignatureObj_GetSubFilter.restype = c_ulong
    break

# fpdf_signature.h: 112
for _lib in _libs.values():
    if not _lib.has("FPDFSignatureObj_GetReason", "cdecl"):
        continue
    FPDFSignatureObj_GetReason = _lib.get("FPDFSignatureObj_GetReason", "cdecl")
    FPDFSignatureObj_GetReason.argtypes = [FPDF_SIGNATURE, POINTER(None), c_ulong]
    FPDFSignatureObj_GetReason.restype = c_ulong
    break

# fpdf_signature.h: 136
for _lib in _libs.values():
    if not _lib.has("FPDFSignatureObj_GetTime", "cdecl"):
        continue
    FPDFSignatureObj_GetTime = _lib.get("FPDFSignatureObj_GetTime", "cdecl")
    FPDFSignatureObj_GetTime.argtypes = [FPDF_SIGNATURE, String, c_ulong]
    FPDFSignatureObj_GetTime.restype = c_ulong
    break

# fpdf_signature.h: 149
for _lib in _libs.values():
    if not _lib.has("FPDFSignatureObj_GetDocMDPPermission", "cdecl"):
        continue
    FPDFSignatureObj_GetDocMDPPermission = _lib.get("FPDFSignatureObj_GetDocMDPPermission", "cdecl")
    FPDFSignatureObj_GetDocMDPPermission.argtypes = [FPDF_SIGNATURE]
    FPDFSignatureObj_GetDocMDPPermission.restype = c_uint
    break

# fpdf_structtree.h: 25
for _lib in _libs.values():
    if not _lib.has("FPDF_StructTree_GetForPage", "cdecl"):
        continue
    FPDF_StructTree_GetForPage = _lib.get("FPDF_StructTree_GetForPage", "cdecl")
    FPDF_StructTree_GetForPage.argtypes = [FPDF_PAGE]
    FPDF_StructTree_GetForPage.restype = FPDF_STRUCTTREE
    break

# fpdf_structtree.h: 35
for _lib in _libs.values():
    if not _lib.has("FPDF_StructTree_Close", "cdecl"):
        continue
    FPDF_StructTree_Close = _lib.get("FPDF_StructTree_Close", "cdecl")
    FPDF_StructTree_Close.argtypes = [FPDF_STRUCTTREE]
    FPDF_StructTree_Close.restype = None
    break

# fpdf_structtree.h: 45
for _lib in _libs.values():
    if not _lib.has("FPDF_StructTree_CountChildren", "cdecl"):
        continue
    FPDF_StructTree_CountChildren = _lib.get("FPDF_StructTree_CountChildren", "cdecl")
    FPDF_StructTree_CountChildren.argtypes = [FPDF_STRUCTTREE]
    FPDF_StructTree_CountChildren.restype = c_int
    break

# fpdf_structtree.h: 56
for _lib in _libs.values():
    if not _lib.has("FPDF_StructTree_GetChildAtIndex", "cdecl"):
        continue
    FPDF_StructTree_GetChildAtIndex = _lib.get("FPDF_StructTree_GetChildAtIndex", "cdecl")
    FPDF_StructTree_GetChildAtIndex.argtypes = [FPDF_STRUCTTREE, c_int]
    FPDF_StructTree_GetChildAtIndex.restype = FPDF_STRUCTELEMENT
    break

# fpdf_structtree.h: 74
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_GetAltText", "cdecl"):
        continue
    FPDF_StructElement_GetAltText = _lib.get("FPDF_StructElement_GetAltText", "cdecl")
    FPDF_StructElement_GetAltText.argtypes = [FPDF_STRUCTELEMENT, POINTER(None), c_ulong]
    FPDF_StructElement_GetAltText.restype = c_ulong
    break

# fpdf_structtree.h: 95
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_GetActualText", "cdecl"):
        continue
    FPDF_StructElement_GetActualText = _lib.get("FPDF_StructElement_GetActualText", "cdecl")
    FPDF_StructElement_GetActualText.argtypes = [FPDF_STRUCTELEMENT, POINTER(None), c_ulong]
    FPDF_StructElement_GetActualText.restype = c_ulong
    break

# fpdf_structtree.h: 115
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_GetID", "cdecl"):
        continue
    FPDF_StructElement_GetID = _lib.get("FPDF_StructElement_GetID", "cdecl")
    FPDF_StructElement_GetID.argtypes = [FPDF_STRUCTELEMENT, POINTER(None), c_ulong]
    FPDF_StructElement_GetID.restype = c_ulong
    break

# fpdf_structtree.h: 136
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_GetLang", "cdecl"):
        continue
    FPDF_StructElement_GetLang = _lib.get("FPDF_StructElement_GetLang", "cdecl")
    FPDF_StructElement_GetLang.argtypes = [FPDF_STRUCTELEMENT, POINTER(None), c_ulong]
    FPDF_StructElement_GetLang.restype = c_ulong
    break

# fpdf_structtree.h: 158
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_GetStringAttribute", "cdecl"):
        continue
    FPDF_StructElement_GetStringAttribute = _lib.get("FPDF_StructElement_GetStringAttribute", "cdecl")
    FPDF_StructElement_GetStringAttribute.argtypes = [FPDF_STRUCTELEMENT, FPDF_BYTESTRING, POINTER(None), c_ulong]
    FPDF_StructElement_GetStringAttribute.restype = c_ulong
    break

# fpdf_structtree.h: 171
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_GetMarkedContentID", "cdecl"):
        continue
    FPDF_StructElement_GetMarkedContentID = _lib.get("FPDF_StructElement_GetMarkedContentID", "cdecl")
    FPDF_StructElement_GetMarkedContentID.argtypes = [FPDF_STRUCTELEMENT]
    FPDF_StructElement_GetMarkedContentID.restype = c_int
    break

# fpdf_structtree.h: 189
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_GetType", "cdecl"):
        continue
    FPDF_StructElement_GetType = _lib.get("FPDF_StructElement_GetType", "cdecl")
    FPDF_StructElement_GetType.argtypes = [FPDF_STRUCTELEMENT, POINTER(None), c_ulong]
    FPDF_StructElement_GetType.restype = c_ulong
    break

# fpdf_structtree.h: 210
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_GetObjType", "cdecl"):
        continue
    FPDF_StructElement_GetObjType = _lib.get("FPDF_StructElement_GetObjType", "cdecl")
    FPDF_StructElement_GetObjType.argtypes = [FPDF_STRUCTELEMENT, POINTER(None), c_ulong]
    FPDF_StructElement_GetObjType.restype = c_ulong
    break

# fpdf_structtree.h: 230
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_GetTitle", "cdecl"):
        continue
    FPDF_StructElement_GetTitle = _lib.get("FPDF_StructElement_GetTitle", "cdecl")
    FPDF_StructElement_GetTitle.argtypes = [FPDF_STRUCTELEMENT, POINTER(None), c_ulong]
    FPDF_StructElement_GetTitle.restype = c_ulong
    break

# fpdf_structtree.h: 241
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_CountChildren", "cdecl"):
        continue
    FPDF_StructElement_CountChildren = _lib.get("FPDF_StructElement_CountChildren", "cdecl")
    FPDF_StructElement_CountChildren.argtypes = [FPDF_STRUCTELEMENT]
    FPDF_StructElement_CountChildren.restype = c_int
    break

# fpdf_structtree.h: 254
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_GetChildAtIndex", "cdecl"):
        continue
    FPDF_StructElement_GetChildAtIndex = _lib.get("FPDF_StructElement_GetChildAtIndex", "cdecl")
    FPDF_StructElement_GetChildAtIndex.argtypes = [FPDF_STRUCTELEMENT, c_int]
    FPDF_StructElement_GetChildAtIndex.restype = FPDF_STRUCTELEMENT
    break

# fpdf_structtree.h: 268
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_GetParent", "cdecl"):
        continue
    FPDF_StructElement_GetParent = _lib.get("FPDF_StructElement_GetParent", "cdecl")
    FPDF_StructElement_GetParent.argtypes = [FPDF_STRUCTELEMENT]
    FPDF_StructElement_GetParent.restype = FPDF_STRUCTELEMENT
    break

# fpdf_structtree.h: 277
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_GetAttributeCount", "cdecl"):
        continue
    FPDF_StructElement_GetAttributeCount = _lib.get("FPDF_StructElement_GetAttributeCount", "cdecl")
    FPDF_StructElement_GetAttributeCount.argtypes = [FPDF_STRUCTELEMENT]
    FPDF_StructElement_GetAttributeCount.restype = c_int
    break

# fpdf_structtree.h: 292
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_GetAttributeAtIndex", "cdecl"):
        continue
    FPDF_StructElement_GetAttributeAtIndex = _lib.get("FPDF_StructElement_GetAttributeAtIndex", "cdecl")
    FPDF_StructElement_GetAttributeAtIndex.argtypes = [FPDF_STRUCTELEMENT, c_int]
    FPDF_StructElement_GetAttributeAtIndex.restype = FPDF_STRUCTELEMENT_ATTR
    break

# fpdf_structtree.h: 302
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_Attr_GetCount", "cdecl"):
        continue
    FPDF_StructElement_Attr_GetCount = _lib.get("FPDF_StructElement_Attr_GetCount", "cdecl")
    FPDF_StructElement_Attr_GetCount.argtypes = [FPDF_STRUCTELEMENT_ATTR]
    FPDF_StructElement_Attr_GetCount.restype = c_int
    break

# fpdf_structtree.h: 322
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_Attr_GetName", "cdecl"):
        continue
    FPDF_StructElement_Attr_GetName = _lib.get("FPDF_StructElement_Attr_GetName", "cdecl")
    FPDF_StructElement_Attr_GetName.argtypes = [FPDF_STRUCTELEMENT_ATTR, c_int, POINTER(None), c_ulong, POINTER(c_ulong)]
    FPDF_StructElement_Attr_GetName.restype = FPDF_BOOL
    break

# fpdf_structtree.h: 338
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_Attr_GetType", "cdecl"):
        continue
    FPDF_StructElement_Attr_GetType = _lib.get("FPDF_StructElement_Attr_GetType", "cdecl")
    FPDF_StructElement_Attr_GetType.argtypes = [FPDF_STRUCTELEMENT_ATTR, FPDF_BYTESTRING]
    FPDF_StructElement_Attr_GetType.restype = FPDF_OBJECT_TYPE
    break

# fpdf_structtree.h: 354
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_Attr_GetBooleanValue", "cdecl"):
        continue
    FPDF_StructElement_Attr_GetBooleanValue = _lib.get("FPDF_StructElement_Attr_GetBooleanValue", "cdecl")
    FPDF_StructElement_Attr_GetBooleanValue.argtypes = [FPDF_STRUCTELEMENT_ATTR, FPDF_BYTESTRING, POINTER(FPDF_BOOL)]
    FPDF_StructElement_Attr_GetBooleanValue.restype = FPDF_BOOL
    break

# fpdf_structtree.h: 372
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_Attr_GetNumberValue", "cdecl"):
        continue
    FPDF_StructElement_Attr_GetNumberValue = _lib.get("FPDF_StructElement_Attr_GetNumberValue", "cdecl")
    FPDF_StructElement_Attr_GetNumberValue.argtypes = [FPDF_STRUCTELEMENT_ATTR, FPDF_BYTESTRING, POINTER(c_float)]
    FPDF_StructElement_Attr_GetNumberValue.restype = FPDF_BOOL
    break

# fpdf_structtree.h: 396
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_Attr_GetStringValue", "cdecl"):
        continue
    FPDF_StructElement_Attr_GetStringValue = _lib.get("FPDF_StructElement_Attr_GetStringValue", "cdecl")
    FPDF_StructElement_Attr_GetStringValue.argtypes = [FPDF_STRUCTELEMENT_ATTR, FPDF_BYTESTRING, POINTER(None), c_ulong, POINTER(c_ulong)]
    FPDF_StructElement_Attr_GetStringValue.restype = FPDF_BOOL
    break

# fpdf_structtree.h: 421
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_Attr_GetBlobValue", "cdecl"):
        continue
    FPDF_StructElement_Attr_GetBlobValue = _lib.get("FPDF_StructElement_Attr_GetBlobValue", "cdecl")
    FPDF_StructElement_Attr_GetBlobValue.argtypes = [FPDF_STRUCTELEMENT_ATTR, FPDF_BYTESTRING, POINTER(None), c_ulong, POINTER(c_ulong)]
    FPDF_StructElement_Attr_GetBlobValue.restype = FPDF_BOOL
    break

# fpdf_structtree.h: 435
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_GetMarkedContentIdCount", "cdecl"):
        continue
    FPDF_StructElement_GetMarkedContentIdCount = _lib.get("FPDF_StructElement_GetMarkedContentIdCount", "cdecl")
    FPDF_StructElement_GetMarkedContentIdCount.argtypes = [FPDF_STRUCTELEMENT]
    FPDF_StructElement_GetMarkedContentIdCount.restype = c_int
    break

# fpdf_structtree.h: 447
for _lib in _libs.values():
    if not _lib.has("FPDF_StructElement_GetMarkedContentIdAtIndex", "cdecl"):
        continue
    FPDF_StructElement_GetMarkedContentIdAtIndex = _lib.get("FPDF_StructElement_GetMarkedContentIdAtIndex", "cdecl")
    FPDF_StructElement_GetMarkedContentIdAtIndex.argtypes = [FPDF_STRUCTELEMENT, c_int]
    FPDF_StructElement_GetMarkedContentIdAtIndex.restype = c_int
    break

# fpdf_sysfontinfo.h: 48
class struct__FPDF_SYSFONTINFO(Structure):
    pass

struct__FPDF_SYSFONTINFO.__slots__ = [
    'version',
    'Release',
    'EnumFonts',
    'MapFont',
    'GetFont',
    'GetFontData',
    'GetFaceName',
    'GetFontCharset',
    'DeleteFont',
]
struct__FPDF_SYSFONTINFO._fields_ = [
    ('version', c_int),
    ('Release', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_SYSFONTINFO))),
    ('EnumFonts', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_SYSFONTINFO), POINTER(None))),
    ('MapFont', CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(struct__FPDF_SYSFONTINFO), c_int, FPDF_BOOL, c_int, c_int, String, POINTER(FPDF_BOOL))),
    ('GetFont', CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(struct__FPDF_SYSFONTINFO), String)),
    ('GetFontData', CFUNCTYPE(UNCHECKED(c_ulong), POINTER(struct__FPDF_SYSFONTINFO), POINTER(None), c_uint, POINTER(c_ubyte), c_ulong)),
    ('GetFaceName', CFUNCTYPE(UNCHECKED(c_ulong), POINTER(struct__FPDF_SYSFONTINFO), POINTER(None), String, c_ulong)),
    ('GetFontCharset', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__FPDF_SYSFONTINFO), POINTER(None))),
    ('DeleteFont', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_SYSFONTINFO), POINTER(None))),
]

FPDF_SYSFONTINFO = struct__FPDF_SYSFONTINFO# fpdf_sysfontinfo.h: 227

# fpdf_sysfontinfo.h: 236
class struct_FPDF_CharsetFontMap_(Structure):
    pass

struct_FPDF_CharsetFontMap_.__slots__ = [
    'charset',
    'fontname',
]
struct_FPDF_CharsetFontMap_._fields_ = [
    ('charset', c_int),
    ('fontname', String),
]

FPDF_CharsetFontMap = struct_FPDF_CharsetFontMap_# fpdf_sysfontinfo.h: 236

# fpdf_sysfontinfo.h: 248
for _lib in _libs.values():
    if not _lib.has("FPDF_GetDefaultTTFMap", "cdecl"):
        continue
    FPDF_GetDefaultTTFMap = _lib.get("FPDF_GetDefaultTTFMap", "cdecl")
    FPDF_GetDefaultTTFMap.argtypes = []
    FPDF_GetDefaultTTFMap.restype = POINTER(FPDF_CharsetFontMap)
    break

# fpdf_sysfontinfo.h: 263
for _lib in _libs.values():
    if not _lib.has("FPDF_AddInstalledFont", "cdecl"):
        continue
    FPDF_AddInstalledFont = _lib.get("FPDF_AddInstalledFont", "cdecl")
    FPDF_AddInstalledFont.argtypes = [POINTER(None), String, c_int]
    FPDF_AddInstalledFont.restype = None
    break

# fpdf_sysfontinfo.h: 280
for _lib in _libs.values():
    if not _lib.has("FPDF_SetSystemFontInfo", "cdecl"):
        continue
    FPDF_SetSystemFontInfo = _lib.get("FPDF_SetSystemFontInfo", "cdecl")
    FPDF_SetSystemFontInfo.argtypes = [POINTER(FPDF_SYSFONTINFO)]
    FPDF_SetSystemFontInfo.restype = None
    break

# fpdf_sysfontinfo.h: 297
for _lib in _libs.values():
    if not _lib.has("FPDF_GetDefaultSystemFontInfo", "cdecl"):
        continue
    FPDF_GetDefaultSystemFontInfo = _lib.get("FPDF_GetDefaultSystemFontInfo", "cdecl")
    FPDF_GetDefaultSystemFontInfo.argtypes = []
    FPDF_GetDefaultSystemFontInfo.restype = POINTER(FPDF_SYSFONTINFO)
    break

# fpdf_sysfontinfo.h: 311
for _lib in _libs.values():
    if not _lib.has("FPDF_FreeDefaultSystemFontInfo", "cdecl"):
        continue
    FPDF_FreeDefaultSystemFontInfo = _lib.get("FPDF_FreeDefaultSystemFontInfo", "cdecl")
    FPDF_FreeDefaultSystemFontInfo.argtypes = [POINTER(FPDF_SYSFONTINFO)]
    FPDF_FreeDefaultSystemFontInfo.restype = None
    break

# fpdf_text.h: 31
for _lib in _libs.values():
    if not _lib.has("FPDFText_LoadPage", "cdecl"):
        continue
    FPDFText_LoadPage = _lib.get("FPDFText_LoadPage", "cdecl")
    FPDFText_LoadPage.argtypes = [FPDF_PAGE]
    FPDFText_LoadPage.restype = FPDF_TEXTPAGE
    break

# fpdf_text.h: 42
for _lib in _libs.values():
    if not _lib.has("FPDFText_ClosePage", "cdecl"):
        continue
    FPDFText_ClosePage = _lib.get("FPDFText_ClosePage", "cdecl")
    FPDFText_ClosePage.argtypes = [FPDF_TEXTPAGE]
    FPDFText_ClosePage.restype = None
    break

# fpdf_text.h: 60
for _lib in _libs.values():
    if not _lib.has("FPDFText_CountChars", "cdecl"):
        continue
    FPDFText_CountChars = _lib.get("FPDFText_CountChars", "cdecl")
    FPDFText_CountChars.argtypes = [FPDF_TEXTPAGE]
    FPDFText_CountChars.restype = c_int
    break

# fpdf_text.h: 75
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetUnicode", "cdecl"):
        continue
    FPDFText_GetUnicode = _lib.get("FPDFText_GetUnicode", "cdecl")
    FPDFText_GetUnicode.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_GetUnicode.restype = c_uint
    break

# fpdf_text.h: 90
for _lib in _libs.values():
    if not _lib.has("FPDFText_IsGenerated", "cdecl"):
        continue
    FPDFText_IsGenerated = _lib.get("FPDFText_IsGenerated", "cdecl")
    FPDFText_IsGenerated.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_IsGenerated.restype = c_int
    break

# fpdf_text.h: 105
for _lib in _libs.values():
    if not _lib.has("FPDFText_HasUnicodeMapError", "cdecl"):
        continue
    FPDFText_HasUnicodeMapError = _lib.get("FPDFText_HasUnicodeMapError", "cdecl")
    FPDFText_HasUnicodeMapError.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_HasUnicodeMapError.restype = c_int
    break

# fpdf_text.h: 118
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetFontSize", "cdecl"):
        continue
    FPDFText_GetFontSize = _lib.get("FPDFText_GetFontSize", "cdecl")
    FPDFText_GetFontSize.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_GetFontSize.restype = c_double
    break

# fpdf_text.h: 141
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetFontInfo", "cdecl"):
        continue
    FPDFText_GetFontInfo = _lib.get("FPDFText_GetFontInfo", "cdecl")
    FPDFText_GetFontInfo.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(None), c_ulong, POINTER(c_int)]
    FPDFText_GetFontInfo.restype = c_ulong
    break

# fpdf_text.h: 159
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetFontWeight", "cdecl"):
        continue
    FPDFText_GetFontWeight = _lib.get("FPDFText_GetFontWeight", "cdecl")
    FPDFText_GetFontWeight.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_GetFontWeight.restype = c_int
    break

# fpdf_text.h: 176
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetTextRenderMode", "cdecl"):
        continue
    FPDFText_GetTextRenderMode = _lib.get("FPDFText_GetTextRenderMode", "cdecl")
    FPDFText_GetTextRenderMode.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_GetTextRenderMode.restype = FPDF_TEXT_RENDERMODE
    break

# fpdf_text.h: 198
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetFillColor", "cdecl"):
        continue
    FPDFText_GetFillColor = _lib.get("FPDFText_GetFillColor", "cdecl")
    FPDFText_GetFillColor.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(c_uint), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)]
    FPDFText_GetFillColor.restype = FPDF_BOOL
    break

# fpdf_text.h: 225
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetStrokeColor", "cdecl"):
        continue
    FPDFText_GetStrokeColor = _lib.get("FPDFText_GetStrokeColor", "cdecl")
    FPDFText_GetStrokeColor.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(c_uint), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)]
    FPDFText_GetStrokeColor.restype = FPDF_BOOL
    break

# fpdf_text.h: 244
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetCharAngle", "cdecl"):
        continue
    FPDFText_GetCharAngle = _lib.get("FPDFText_GetCharAngle", "cdecl")
    FPDFText_GetCharAngle.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_GetCharAngle.restype = c_float
    break

# fpdf_text.h: 268
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetCharBox", "cdecl"):
        continue
    FPDFText_GetCharBox = _lib.get("FPDFText_GetCharBox", "cdecl")
    FPDFText_GetCharBox.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    FPDFText_GetCharBox.restype = FPDF_BOOL
    break

# fpdf_text.h: 293
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetLooseCharBox", "cdecl"):
        continue
    FPDFText_GetLooseCharBox = _lib.get("FPDFText_GetLooseCharBox", "cdecl")
    FPDFText_GetLooseCharBox.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(FS_RECTF)]
    FPDFText_GetLooseCharBox.restype = FPDF_BOOL
    break

# fpdf_text.h: 309
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetMatrix", "cdecl"):
        continue
    FPDFText_GetMatrix = _lib.get("FPDFText_GetMatrix", "cdecl")
    FPDFText_GetMatrix.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(FS_MATRIX)]
    FPDFText_GetMatrix.restype = FPDF_BOOL
    break

# fpdf_text.h: 329
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetCharOrigin", "cdecl"):
        continue
    FPDFText_GetCharOrigin = _lib.get("FPDFText_GetCharOrigin", "cdecl")
    FPDFText_GetCharOrigin.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(c_double), POINTER(c_double)]
    FPDFText_GetCharOrigin.restype = FPDF_BOOL
    break

# fpdf_text.h: 352
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetCharIndexAtPos", "cdecl"):
        continue
    FPDFText_GetCharIndexAtPos = _lib.get("FPDFText_GetCharIndexAtPos", "cdecl")
    FPDFText_GetCharIndexAtPos.argtypes = [FPDF_TEXTPAGE, c_double, c_double, c_double, c_double]
    FPDFText_GetCharIndexAtPos.restype = c_int
    break

# fpdf_text.h: 379
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetText", "cdecl"):
        continue
    FPDFText_GetText = _lib.get("FPDFText_GetText", "cdecl")
    FPDFText_GetText.argtypes = [FPDF_TEXTPAGE, c_int, c_int, POINTER(c_ushort)]
    FPDFText_GetText.restype = c_int
    break

# fpdf_text.h: 402
for _lib in _libs.values():
    if not _lib.has("FPDFText_CountRects", "cdecl"):
        continue
    FPDFText_CountRects = _lib.get("FPDFText_CountRects", "cdecl")
    FPDFText_CountRects.argtypes = [FPDF_TEXTPAGE, c_int, c_int]
    FPDFText_CountRects.restype = c_int
    break

# fpdf_text.h: 428
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetRect", "cdecl"):
        continue
    FPDFText_GetRect = _lib.get("FPDFText_GetRect", "cdecl")
    FPDFText_GetRect.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    FPDFText_GetRect.restype = FPDF_BOOL
    break

# fpdf_text.h: 459
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetBoundedText", "cdecl"):
        continue
    FPDFText_GetBoundedText = _lib.get("FPDFText_GetBoundedText", "cdecl")
    FPDFText_GetBoundedText.argtypes = [FPDF_TEXTPAGE, c_double, c_double, c_double, c_double, POINTER(c_ushort), c_int]
    FPDFText_GetBoundedText.restype = c_int
    break

# fpdf_text.h: 489
for _lib in _libs.values():
    if not _lib.has("FPDFText_FindStart", "cdecl"):
        continue
    FPDFText_FindStart = _lib.get("FPDFText_FindStart", "cdecl")
    FPDFText_FindStart.argtypes = [FPDF_TEXTPAGE, FPDF_WIDESTRING, c_ulong, c_int]
    FPDFText_FindStart.restype = FPDF_SCHHANDLE
    break

# fpdf_text.h: 502
for _lib in _libs.values():
    if not _lib.has("FPDFText_FindNext", "cdecl"):
        continue
    FPDFText_FindNext = _lib.get("FPDFText_FindNext", "cdecl")
    FPDFText_FindNext.argtypes = [FPDF_SCHHANDLE]
    FPDFText_FindNext.restype = FPDF_BOOL
    break

# fpdf_text.h: 512
for _lib in _libs.values():
    if not _lib.has("FPDFText_FindPrev", "cdecl"):
        continue
    FPDFText_FindPrev = _lib.get("FPDFText_FindPrev", "cdecl")
    FPDFText_FindPrev.argtypes = [FPDF_SCHHANDLE]
    FPDFText_FindPrev.restype = FPDF_BOOL
    break

# fpdf_text.h: 522
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetSchResultIndex", "cdecl"):
        continue
    FPDFText_GetSchResultIndex = _lib.get("FPDFText_GetSchResultIndex", "cdecl")
    FPDFText_GetSchResultIndex.argtypes = [FPDF_SCHHANDLE]
    FPDFText_GetSchResultIndex.restype = c_int
    break

# fpdf_text.h: 532
for _lib in _libs.values():
    if not _lib.has("FPDFText_GetSchCount", "cdecl"):
        continue
    FPDFText_GetSchCount = _lib.get("FPDFText_GetSchCount", "cdecl")
    FPDFText_GetSchCount.argtypes = [FPDF_SCHHANDLE]
    FPDFText_GetSchCount.restype = c_int
    break

# fpdf_text.h: 542
for _lib in _libs.values():
    if not _lib.has("FPDFText_FindClose", "cdecl"):
        continue
    FPDFText_FindClose = _lib.get("FPDFText_FindClose", "cdecl")
    FPDFText_FindClose.argtypes = [FPDF_SCHHANDLE]
    FPDFText_FindClose.restype = None
    break

# fpdf_text.h: 564
for _lib in _libs.values():
    if not _lib.has("FPDFLink_LoadWebLinks", "cdecl"):
        continue
    FPDFLink_LoadWebLinks = _lib.get("FPDFLink_LoadWebLinks", "cdecl")
    FPDFLink_LoadWebLinks.argtypes = [FPDF_TEXTPAGE]
    FPDFLink_LoadWebLinks.restype = FPDF_PAGELINK
    break

# fpdf_text.h: 573
for _lib in _libs.values():
    if not _lib.has("FPDFLink_CountWebLinks", "cdecl"):
        continue
    FPDFLink_CountWebLinks = _lib.get("FPDFLink_CountWebLinks", "cdecl")
    FPDFLink_CountWebLinks.argtypes = [FPDF_PAGELINK]
    FPDFLink_CountWebLinks.restype = c_int
    break

# fpdf_text.h: 594
for _lib in _libs.values():
    if not _lib.has("FPDFLink_GetURL", "cdecl"):
        continue
    FPDFLink_GetURL = _lib.get("FPDFLink_GetURL", "cdecl")
    FPDFLink_GetURL.argtypes = [FPDF_PAGELINK, c_int, POINTER(c_ushort), c_int]
    FPDFLink_GetURL.restype = c_int
    break

# fpdf_text.h: 608
for _lib in _libs.values():
    if not _lib.has("FPDFLink_CountRects", "cdecl"):
        continue
    FPDFLink_CountRects = _lib.get("FPDFLink_CountRects", "cdecl")
    FPDFLink_CountRects.argtypes = [FPDF_PAGELINK, c_int]
    FPDFLink_CountRects.restype = c_int
    break

# fpdf_text.h: 631
for _lib in _libs.values():
    if not _lib.has("FPDFLink_GetRect", "cdecl"):
        continue
    FPDFLink_GetRect = _lib.get("FPDFLink_GetRect", "cdecl")
    FPDFLink_GetRect.argtypes = [FPDF_PAGELINK, c_int, c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    FPDFLink_GetRect.restype = FPDF_BOOL
    break

# fpdf_text.h: 654
for _lib in _libs.values():
    if not _lib.has("FPDFLink_GetTextRange", "cdecl"):
        continue
    FPDFLink_GetTextRange = _lib.get("FPDFLink_GetTextRange", "cdecl")
    FPDFLink_GetTextRange.argtypes = [FPDF_PAGELINK, c_int, POINTER(c_int), POINTER(c_int)]
    FPDFLink_GetTextRange.restype = FPDF_BOOL
    break

# fpdf_text.h: 666
for _lib in _libs.values():
    if not _lib.has("FPDFLink_CloseWebLinks", "cdecl"):
        continue
    FPDFLink_CloseWebLinks = _lib.get("FPDFLink_CloseWebLinks", "cdecl")
    FPDFLink_CloseWebLinks.argtypes = [FPDF_PAGELINK]
    FPDFLink_CloseWebLinks.restype = None
    break

# fpdf_thumbnail.h: 28
for _lib in _libs.values():
    if not _lib.has("FPDFPage_GetDecodedThumbnailData", "cdecl"):
        continue
    FPDFPage_GetDecodedThumbnailData = _lib.get("FPDFPage_GetDecodedThumbnailData", "cdecl")
    FPDFPage_GetDecodedThumbnailData.argtypes = [FPDF_PAGE, POINTER(None), c_ulong]
    FPDFPage_GetDecodedThumbnailData.restype = c_ulong
    break

# fpdf_thumbnail.h: 43
for _lib in _libs.values():
    if not _lib.has("FPDFPage_GetRawThumbnailData", "cdecl"):
        continue
    FPDFPage_GetRawThumbnailData = _lib.get("FPDFPage_GetRawThumbnailData", "cdecl")
    FPDFPage_GetRawThumbnailData.argtypes = [FPDF_PAGE, POINTER(None), c_ulong]
    FPDFPage_GetRawThumbnailData.restype = c_ulong
    break

# fpdf_thumbnail.h: 53
for _lib in _libs.values():
    if not _lib.has("FPDFPage_GetThumbnailAsBitmap", "cdecl"):
        continue
    FPDFPage_GetThumbnailAsBitmap = _lib.get("FPDFPage_GetThumbnailAsBitmap", "cdecl")
    FPDFPage_GetThumbnailAsBitmap.argtypes = [FPDF_PAGE]
    FPDFPage_GetThumbnailAsBitmap.restype = FPDF_BITMAP
    break

# fpdf_transformpage.h: 26
for _lib in _libs.values():
    if not _lib.has("FPDFPage_SetMediaBox", "cdecl"):
        continue
    FPDFPage_SetMediaBox = _lib.get("FPDFPage_SetMediaBox", "cdecl")
    FPDFPage_SetMediaBox.argtypes = [FPDF_PAGE, c_float, c_float, c_float, c_float]
    FPDFPage_SetMediaBox.restype = None
    break

# fpdf_transformpage.h: 41
for _lib in _libs.values():
    if not _lib.has("FPDFPage_SetCropBox", "cdecl"):
        continue
    FPDFPage_SetCropBox = _lib.get("FPDFPage_SetCropBox", "cdecl")
    FPDFPage_SetCropBox.argtypes = [FPDF_PAGE, c_float, c_float, c_float, c_float]
    FPDFPage_SetCropBox.restype = None
    break

# fpdf_transformpage.h: 56
for _lib in _libs.values():
    if not _lib.has("FPDFPage_SetBleedBox", "cdecl"):
        continue
    FPDFPage_SetBleedBox = _lib.get("FPDFPage_SetBleedBox", "cdecl")
    FPDFPage_SetBleedBox.argtypes = [FPDF_PAGE, c_float, c_float, c_float, c_float]
    FPDFPage_SetBleedBox.restype = None
    break

# fpdf_transformpage.h: 71
for _lib in _libs.values():
    if not _lib.has("FPDFPage_SetTrimBox", "cdecl"):
        continue
    FPDFPage_SetTrimBox = _lib.get("FPDFPage_SetTrimBox", "cdecl")
    FPDFPage_SetTrimBox.argtypes = [FPDF_PAGE, c_float, c_float, c_float, c_float]
    FPDFPage_SetTrimBox.restype = None
    break

# fpdf_transformpage.h: 86
for _lib in _libs.values():
    if not _lib.has("FPDFPage_SetArtBox", "cdecl"):
        continue
    FPDFPage_SetArtBox = _lib.get("FPDFPage_SetArtBox", "cdecl")
    FPDFPage_SetArtBox.argtypes = [FPDF_PAGE, c_float, c_float, c_float, c_float]
    FPDFPage_SetArtBox.restype = None
    break

# fpdf_transformpage.h: 104
for _lib in _libs.values():
    if not _lib.has("FPDFPage_GetMediaBox", "cdecl"):
        continue
    FPDFPage_GetMediaBox = _lib.get("FPDFPage_GetMediaBox", "cdecl")
    FPDFPage_GetMediaBox.argtypes = [FPDF_PAGE, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    FPDFPage_GetMediaBox.restype = FPDF_BOOL
    break

# fpdf_transformpage.h: 122
for _lib in _libs.values():
    if not _lib.has("FPDFPage_GetCropBox", "cdecl"):
        continue
    FPDFPage_GetCropBox = _lib.get("FPDFPage_GetCropBox", "cdecl")
    FPDFPage_GetCropBox.argtypes = [FPDF_PAGE, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    FPDFPage_GetCropBox.restype = FPDF_BOOL
    break

# fpdf_transformpage.h: 140
for _lib in _libs.values():
    if not _lib.has("FPDFPage_GetBleedBox", "cdecl"):
        continue
    FPDFPage_GetBleedBox = _lib.get("FPDFPage_GetBleedBox", "cdecl")
    FPDFPage_GetBleedBox.argtypes = [FPDF_PAGE, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    FPDFPage_GetBleedBox.restype = FPDF_BOOL
    break

# fpdf_transformpage.h: 158
for _lib in _libs.values():
    if not _lib.has("FPDFPage_GetTrimBox", "cdecl"):
        continue
    FPDFPage_GetTrimBox = _lib.get("FPDFPage_GetTrimBox", "cdecl")
    FPDFPage_GetTrimBox.argtypes = [FPDF_PAGE, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    FPDFPage_GetTrimBox.restype = FPDF_BOOL
    break

# fpdf_transformpage.h: 176
for _lib in _libs.values():
    if not _lib.has("FPDFPage_GetArtBox", "cdecl"):
        continue
    FPDFPage_GetArtBox = _lib.get("FPDFPage_GetArtBox", "cdecl")
    FPDFPage_GetArtBox.argtypes = [FPDF_PAGE, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    FPDFPage_GetArtBox.restype = FPDF_BOOL
    break

# fpdf_transformpage.h: 198
for _lib in _libs.values():
    if not _lib.has("FPDFPage_TransFormWithClip", "cdecl"):
        continue
    FPDFPage_TransFormWithClip = _lib.get("FPDFPage_TransFormWithClip", "cdecl")
    FPDFPage_TransFormWithClip.argtypes = [FPDF_PAGE, POINTER(FS_MATRIX), POINTER(FS_RECTF)]
    FPDFPage_TransFormWithClip.restype = FPDF_BOOL
    break

# fpdf_transformpage.h: 215
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_TransformClipPath", "cdecl"):
        continue
    FPDFPageObj_TransformClipPath = _lib.get("FPDFPageObj_TransformClipPath", "cdecl")
    FPDFPageObj_TransformClipPath.argtypes = [FPDF_PAGEOBJECT, c_double, c_double, c_double, c_double, c_double, c_double]
    FPDFPageObj_TransformClipPath.restype = None
    break

# fpdf_transformpage.h: 233
for _lib in _libs.values():
    if not _lib.has("FPDFPageObj_GetClipPath", "cdecl"):
        continue
    FPDFPageObj_GetClipPath = _lib.get("FPDFPageObj_GetClipPath", "cdecl")
    FPDFPageObj_GetClipPath.argtypes = [FPDF_PAGEOBJECT]
    FPDFPageObj_GetClipPath.restype = FPDF_CLIPPATH
    break

# fpdf_transformpage.h: 241
for _lib in _libs.values():
    if not _lib.has("FPDFClipPath_CountPaths", "cdecl"):
        continue
    FPDFClipPath_CountPaths = _lib.get("FPDFClipPath_CountPaths", "cdecl")
    FPDFClipPath_CountPaths.argtypes = [FPDF_CLIPPATH]
    FPDFClipPath_CountPaths.restype = c_int
    break

# fpdf_transformpage.h: 251
for _lib in _libs.values():
    if not _lib.has("FPDFClipPath_CountPathSegments", "cdecl"):
        continue
    FPDFClipPath_CountPathSegments = _lib.get("FPDFClipPath_CountPathSegments", "cdecl")
    FPDFClipPath_CountPathSegments.argtypes = [FPDF_CLIPPATH, c_int]
    FPDFClipPath_CountPathSegments.restype = c_int
    break

# fpdf_transformpage.h: 264
for _lib in _libs.values():
    if not _lib.has("FPDFClipPath_GetPathSegment", "cdecl"):
        continue
    FPDFClipPath_GetPathSegment = _lib.get("FPDFClipPath_GetPathSegment", "cdecl")
    FPDFClipPath_GetPathSegment.argtypes = [FPDF_CLIPPATH, c_int, c_int]
    FPDFClipPath_GetPathSegment.restype = FPDF_PATHSEGMENT
    break

# fpdf_transformpage.h: 279
for _lib in _libs.values():
    if not _lib.has("FPDF_CreateClipPath", "cdecl"):
        continue
    FPDF_CreateClipPath = _lib.get("FPDF_CreateClipPath", "cdecl")
    FPDF_CreateClipPath.argtypes = [c_float, c_float, c_float, c_float]
    FPDF_CreateClipPath.restype = FPDF_CLIPPATH
    break

# fpdf_transformpage.h: 289
for _lib in _libs.values():
    if not _lib.has("FPDF_DestroyClipPath", "cdecl"):
        continue
    FPDF_DestroyClipPath = _lib.get("FPDF_DestroyClipPath", "cdecl")
    FPDF_DestroyClipPath.argtypes = [FPDF_CLIPPATH]
    FPDF_DestroyClipPath.restype = None
    break

# fpdf_transformpage.h: 301
for _lib in _libs.values():
    if not _lib.has("FPDFPage_InsertClipPath", "cdecl"):
        continue
    FPDFPage_InsertClipPath = _lib.get("FPDFPage_InsertClipPath", "cdecl")
    FPDFPage_InsertClipPath.argtypes = [FPDF_PAGE, FPDF_CLIPPATH]
    FPDFPage_InsertClipPath.restype = None
    break

# fpdfview.h: 28
try:
    FPDF_OBJECT_UNKNOWN = 0
except:
    pass

# fpdfview.h: 29
try:
    FPDF_OBJECT_BOOLEAN = 1
except:
    pass

# fpdfview.h: 30
try:
    FPDF_OBJECT_NUMBER = 2
except:
    pass

# fpdfview.h: 31
try:
    FPDF_OBJECT_STRING = 3
except:
    pass

# fpdfview.h: 32
try:
    FPDF_OBJECT_NAME = 4
except:
    pass

# fpdfview.h: 33
try:
    FPDF_OBJECT_ARRAY = 5
except:
    pass

# fpdfview.h: 34
try:
    FPDF_OBJECT_DICTIONARY = 6
except:
    pass

# fpdfview.h: 35
try:
    FPDF_OBJECT_STREAM = 7
except:
    pass

# fpdfview.h: 36
try:
    FPDF_OBJECT_NULLOBJ = 8
except:
    pass

# fpdfview.h: 37
try:
    FPDF_OBJECT_REFERENCE = 9
except:
    pass

# fpdfview.h: 306
try:
    FPDF_POLICY_MACHINETIME_ACCESS = 0
except:
    pass

# fpdfview.h: 578
try:
    FPDF_ERR_SUCCESS = 0
except:
    pass

# fpdfview.h: 579
try:
    FPDF_ERR_UNKNOWN = 1
except:
    pass

# fpdfview.h: 580
try:
    FPDF_ERR_FILE = 2
except:
    pass

# fpdfview.h: 581
try:
    FPDF_ERR_FORMAT = 3
except:
    pass

# fpdfview.h: 582
try:
    FPDF_ERR_PASSWORD = 4
except:
    pass

# fpdfview.h: 583
try:
    FPDF_ERR_SECURITY = 5
except:
    pass

# fpdfview.h: 584
try:
    FPDF_ERR_PAGE = 6
except:
    pass

# fpdfview.h: 773
try:
    FPDF_ANNOT = 0x01
except:
    pass

# fpdfview.h: 776
try:
    FPDF_LCD_TEXT = 0x02
except:
    pass

# fpdfview.h: 778
try:
    FPDF_NO_NATIVETEXT = 0x04
except:
    pass

# fpdfview.h: 780
try:
    FPDF_GRAYSCALE = 0x08
except:
    pass

# fpdfview.h: 782
try:
    FPDF_DEBUG_INFO = 0x80
except:
    pass

# fpdfview.h: 784
try:
    FPDF_NO_CATCH = 0x100
except:
    pass

# fpdfview.h: 786
try:
    FPDF_RENDER_LIMITEDIMAGECACHE = 0x200
except:
    pass

# fpdfview.h: 788
try:
    FPDF_RENDER_FORCEHALFTONE = 0x400
except:
    pass

# fpdfview.h: 790
try:
    FPDF_PRINTING = 0x800
except:
    pass

# fpdfview.h: 793
try:
    FPDF_RENDER_NO_SMOOTHTEXT = 0x1000
except:
    pass

# fpdfview.h: 795
try:
    FPDF_RENDER_NO_SMOOTHIMAGE = 0x2000
except:
    pass

# fpdfview.h: 797
try:
    FPDF_RENDER_NO_SMOOTHPATH = 0x4000
except:
    pass

# fpdfview.h: 800
try:
    FPDF_REVERSE_BYTE_ORDER = 0x10
except:
    pass

# fpdfview.h: 804
try:
    FPDF_CONVERT_FILL_TO_STROKE = 0x20
except:
    pass

# fpdfview.h: 1064
try:
    FPDFBitmap_Unknown = 0
except:
    pass

# fpdfview.h: 1066
try:
    FPDFBitmap_Gray = 1
except:
    pass

# fpdfview.h: 1068
try:
    FPDFBitmap_BGR = 2
except:
    pass

# fpdfview.h: 1070
try:
    FPDFBitmap_BGRx = 3
except:
    pass

# fpdfview.h: 1072
try:
    FPDFBitmap_BGRA = 4
except:
    pass

# fpdf_formfill.h: 16
try:
    FORMTYPE_NONE = 0
except:
    pass

# fpdf_formfill.h: 17
try:
    FORMTYPE_ACRO_FORM = 1
except:
    pass

# fpdf_formfill.h: 18
try:
    FORMTYPE_XFA_FULL = 2
except:
    pass

# fpdf_formfill.h: 19
try:
    FORMTYPE_XFA_FOREGROUND = 3
except:
    pass

# fpdf_formfill.h: 21
try:
    FORMTYPE_COUNT = 4
except:
    pass

# fpdf_formfill.h: 23
try:
    JSPLATFORM_ALERT_BUTTON_OK = 0
except:
    pass

# fpdf_formfill.h: 24
try:
    JSPLATFORM_ALERT_BUTTON_OKCANCEL = 1
except:
    pass

# fpdf_formfill.h: 25
try:
    JSPLATFORM_ALERT_BUTTON_YESNO = 2
except:
    pass

# fpdf_formfill.h: 26
try:
    JSPLATFORM_ALERT_BUTTON_YESNOCANCEL = 3
except:
    pass

# fpdf_formfill.h: 27
try:
    JSPLATFORM_ALERT_BUTTON_DEFAULT = JSPLATFORM_ALERT_BUTTON_OK
except:
    pass

# fpdf_formfill.h: 29
try:
    JSPLATFORM_ALERT_ICON_ERROR = 0
except:
    pass

# fpdf_formfill.h: 30
try:
    JSPLATFORM_ALERT_ICON_WARNING = 1
except:
    pass

# fpdf_formfill.h: 31
try:
    JSPLATFORM_ALERT_ICON_QUESTION = 2
except:
    pass

# fpdf_formfill.h: 32
try:
    JSPLATFORM_ALERT_ICON_STATUS = 3
except:
    pass

# fpdf_formfill.h: 33
try:
    JSPLATFORM_ALERT_ICON_ASTERISK = 4
except:
    pass

# fpdf_formfill.h: 34
try:
    JSPLATFORM_ALERT_ICON_DEFAULT = JSPLATFORM_ALERT_ICON_ERROR
except:
    pass

# fpdf_formfill.h: 36
try:
    JSPLATFORM_ALERT_RETURN_OK = 1
except:
    pass

# fpdf_formfill.h: 37
try:
    JSPLATFORM_ALERT_RETURN_CANCEL = 2
except:
    pass

# fpdf_formfill.h: 38
try:
    JSPLATFORM_ALERT_RETURN_NO = 3
except:
    pass

# fpdf_formfill.h: 39
try:
    JSPLATFORM_ALERT_RETURN_YES = 4
except:
    pass

# fpdf_formfill.h: 41
try:
    JSPLATFORM_BEEP_ERROR = 0
except:
    pass

# fpdf_formfill.h: 42
try:
    JSPLATFORM_BEEP_WARNING = 1
except:
    pass

# fpdf_formfill.h: 43
try:
    JSPLATFORM_BEEP_QUESTION = 2
except:
    pass

# fpdf_formfill.h: 44
try:
    JSPLATFORM_BEEP_STATUS = 3
except:
    pass

# fpdf_formfill.h: 45
try:
    JSPLATFORM_BEEP_DEFAULT = 4
except:
    pass

# fpdf_formfill.h: 326
try:
    FXCT_ARROW = 0
except:
    pass

# fpdf_formfill.h: 327
try:
    FXCT_NESW = 1
except:
    pass

# fpdf_formfill.h: 328
try:
    FXCT_NWSE = 2
except:
    pass

# fpdf_formfill.h: 329
try:
    FXCT_VBEAM = 3
except:
    pass

# fpdf_formfill.h: 330
try:
    FXCT_HBEAM = 4
except:
    pass

# fpdf_formfill.h: 331
try:
    FXCT_HAND = 5
except:
    pass

# fpdf_formfill.h: 1239
try:
    FPDFDOC_AACTION_WC = 0x10
except:
    pass

# fpdf_formfill.h: 1240
try:
    FPDFDOC_AACTION_WS = 0x11
except:
    pass

# fpdf_formfill.h: 1241
try:
    FPDFDOC_AACTION_DS = 0x12
except:
    pass

# fpdf_formfill.h: 1242
try:
    FPDFDOC_AACTION_WP = 0x13
except:
    pass

# fpdf_formfill.h: 1243
try:
    FPDFDOC_AACTION_DP = 0x14
except:
    pass

# fpdf_formfill.h: 1266
try:
    FPDFPAGE_AACTION_OPEN = 0
except:
    pass

# fpdf_formfill.h: 1267
try:
    FPDFPAGE_AACTION_CLOSE = 1
except:
    pass

# fpdf_formfill.h: 1711
try:
    FPDF_FORMFIELD_UNKNOWN = 0
except:
    pass

# fpdf_formfill.h: 1712
try:
    FPDF_FORMFIELD_PUSHBUTTON = 1
except:
    pass

# fpdf_formfill.h: 1713
try:
    FPDF_FORMFIELD_CHECKBOX = 2
except:
    pass

# fpdf_formfill.h: 1714
try:
    FPDF_FORMFIELD_RADIOBUTTON = 3
except:
    pass

# fpdf_formfill.h: 1715
try:
    FPDF_FORMFIELD_COMBOBOX = 4
except:
    pass

# fpdf_formfill.h: 1716
try:
    FPDF_FORMFIELD_LISTBOX = 5
except:
    pass

# fpdf_formfill.h: 1717
try:
    FPDF_FORMFIELD_TEXTFIELD = 6
except:
    pass

# fpdf_formfill.h: 1718
try:
    FPDF_FORMFIELD_SIGNATURE = 7
except:
    pass

# fpdf_formfill.h: 1733
try:
    FPDF_FORMFIELD_COUNT = 8
except:
    pass

# fpdf_annot.h: 20
try:
    FPDF_ANNOT_UNKNOWN = 0
except:
    pass

# fpdf_annot.h: 21
try:
    FPDF_ANNOT_TEXT = 1
except:
    pass

# fpdf_annot.h: 22
try:
    FPDF_ANNOT_LINK = 2
except:
    pass

# fpdf_annot.h: 23
try:
    FPDF_ANNOT_FREETEXT = 3
except:
    pass

# fpdf_annot.h: 24
try:
    FPDF_ANNOT_LINE = 4
except:
    pass

# fpdf_annot.h: 25
try:
    FPDF_ANNOT_SQUARE = 5
except:
    pass

# fpdf_annot.h: 26
try:
    FPDF_ANNOT_CIRCLE = 6
except:
    pass

# fpdf_annot.h: 27
try:
    FPDF_ANNOT_POLYGON = 7
except:
    pass

# fpdf_annot.h: 28
try:
    FPDF_ANNOT_POLYLINE = 8
except:
    pass

# fpdf_annot.h: 29
try:
    FPDF_ANNOT_HIGHLIGHT = 9
except:
    pass

# fpdf_annot.h: 30
try:
    FPDF_ANNOT_UNDERLINE = 10
except:
    pass

# fpdf_annot.h: 31
try:
    FPDF_ANNOT_SQUIGGLY = 11
except:
    pass

# fpdf_annot.h: 32
try:
    FPDF_ANNOT_STRIKEOUT = 12
except:
    pass

# fpdf_annot.h: 33
try:
    FPDF_ANNOT_STAMP = 13
except:
    pass

# fpdf_annot.h: 34
try:
    FPDF_ANNOT_CARET = 14
except:
    pass

# fpdf_annot.h: 35
try:
    FPDF_ANNOT_INK = 15
except:
    pass

# fpdf_annot.h: 36
try:
    FPDF_ANNOT_POPUP = 16
except:
    pass

# fpdf_annot.h: 37
try:
    FPDF_ANNOT_FILEATTACHMENT = 17
except:
    pass

# fpdf_annot.h: 38
try:
    FPDF_ANNOT_SOUND = 18
except:
    pass

# fpdf_annot.h: 39
try:
    FPDF_ANNOT_MOVIE = 19
except:
    pass

# fpdf_annot.h: 40
try:
    FPDF_ANNOT_WIDGET = 20
except:
    pass

# fpdf_annot.h: 41
try:
    FPDF_ANNOT_SCREEN = 21
except:
    pass

# fpdf_annot.h: 42
try:
    FPDF_ANNOT_PRINTERMARK = 22
except:
    pass

# fpdf_annot.h: 43
try:
    FPDF_ANNOT_TRAPNET = 23
except:
    pass

# fpdf_annot.h: 44
try:
    FPDF_ANNOT_WATERMARK = 24
except:
    pass

# fpdf_annot.h: 45
try:
    FPDF_ANNOT_THREED = 25
except:
    pass

# fpdf_annot.h: 46
try:
    FPDF_ANNOT_RICHMEDIA = 26
except:
    pass

# fpdf_annot.h: 47
try:
    FPDF_ANNOT_XFAWIDGET = 27
except:
    pass

# fpdf_annot.h: 48
try:
    FPDF_ANNOT_REDACT = 28
except:
    pass

# fpdf_annot.h: 51
try:
    FPDF_ANNOT_FLAG_NONE = 0
except:
    pass

# fpdf_annot.h: 52
try:
    FPDF_ANNOT_FLAG_INVISIBLE = (1 << 0)
except:
    pass

# fpdf_annot.h: 53
try:
    FPDF_ANNOT_FLAG_HIDDEN = (1 << 1)
except:
    pass

# fpdf_annot.h: 54
try:
    FPDF_ANNOT_FLAG_PRINT = (1 << 2)
except:
    pass

# fpdf_annot.h: 55
try:
    FPDF_ANNOT_FLAG_NOZOOM = (1 << 3)
except:
    pass

# fpdf_annot.h: 56
try:
    FPDF_ANNOT_FLAG_NOROTATE = (1 << 4)
except:
    pass

# fpdf_annot.h: 57
try:
    FPDF_ANNOT_FLAG_NOVIEW = (1 << 5)
except:
    pass

# fpdf_annot.h: 58
try:
    FPDF_ANNOT_FLAG_READONLY = (1 << 6)
except:
    pass

# fpdf_annot.h: 59
try:
    FPDF_ANNOT_FLAG_LOCKED = (1 << 7)
except:
    pass

# fpdf_annot.h: 60
try:
    FPDF_ANNOT_FLAG_TOGGLENOVIEW = (1 << 8)
except:
    pass

# fpdf_annot.h: 62
try:
    FPDF_ANNOT_APPEARANCEMODE_NORMAL = 0
except:
    pass

# fpdf_annot.h: 63
try:
    FPDF_ANNOT_APPEARANCEMODE_ROLLOVER = 1
except:
    pass

# fpdf_annot.h: 64
try:
    FPDF_ANNOT_APPEARANCEMODE_DOWN = 2
except:
    pass

# fpdf_annot.h: 65
try:
    FPDF_ANNOT_APPEARANCEMODE_COUNT = 3
except:
    pass

# fpdf_annot.h: 69
try:
    FPDF_FORMFLAG_NONE = 0
except:
    pass

# fpdf_annot.h: 70
try:
    FPDF_FORMFLAG_READONLY = (1 << 0)
except:
    pass

# fpdf_annot.h: 71
try:
    FPDF_FORMFLAG_REQUIRED = (1 << 1)
except:
    pass

# fpdf_annot.h: 72
try:
    FPDF_FORMFLAG_NOEXPORT = (1 << 2)
except:
    pass

# fpdf_annot.h: 76
try:
    FPDF_FORMFLAG_TEXT_MULTILINE = (1 << 12)
except:
    pass

# fpdf_annot.h: 77
try:
    FPDF_FORMFLAG_TEXT_PASSWORD = (1 << 13)
except:
    pass

# fpdf_annot.h: 81
try:
    FPDF_FORMFLAG_CHOICE_COMBO = (1 << 17)
except:
    pass

# fpdf_annot.h: 82
try:
    FPDF_FORMFLAG_CHOICE_EDIT = (1 << 18)
except:
    pass

# fpdf_annot.h: 83
try:
    FPDF_FORMFLAG_CHOICE_MULTI_SELECT = (1 << 21)
except:
    pass

# fpdf_annot.h: 90
try:
    FPDF_ANNOT_AACTION_KEY_STROKE = 12
except:
    pass

# fpdf_annot.h: 91
try:
    FPDF_ANNOT_AACTION_FORMAT = 13
except:
    pass

# fpdf_annot.h: 92
try:
    FPDF_ANNOT_AACTION_VALIDATE = 14
except:
    pass

# fpdf_annot.h: 93
try:
    FPDF_ANNOT_AACTION_CALCULATE = 15
except:
    pass

# fpdf_dataavail.h: 15
try:
    PDF_LINEARIZATION_UNKNOWN = (-1)
except:
    pass

# fpdf_dataavail.h: 16
try:
    PDF_NOT_LINEARIZED = 0
except:
    pass

# fpdf_dataavail.h: 17
try:
    PDF_LINEARIZED = 1
except:
    pass

# fpdf_dataavail.h: 19
try:
    PDF_DATA_ERROR = (-1)
except:
    pass

# fpdf_dataavail.h: 20
try:
    PDF_DATA_NOTAVAIL = 0
except:
    pass

# fpdf_dataavail.h: 21
try:
    PDF_DATA_AVAIL = 1
except:
    pass

# fpdf_dataavail.h: 23
try:
    PDF_FORM_ERROR = (-1)
except:
    pass

# fpdf_dataavail.h: 24
try:
    PDF_FORM_NOTAVAIL = 0
except:
    pass

# fpdf_dataavail.h: 25
try:
    PDF_FORM_AVAIL = 1
except:
    pass

# fpdf_dataavail.h: 26
try:
    PDF_FORM_NOTEXIST = 2
except:
    pass

# fpdf_doc.h: 18
try:
    PDFACTION_UNSUPPORTED = 0
except:
    pass

# fpdf_doc.h: 20
try:
    PDFACTION_GOTO = 1
except:
    pass

# fpdf_doc.h: 22
try:
    PDFACTION_REMOTEGOTO = 2
except:
    pass

# fpdf_doc.h: 24
try:
    PDFACTION_URI = 3
except:
    pass

# fpdf_doc.h: 26
try:
    PDFACTION_LAUNCH = 4
except:
    pass

# fpdf_doc.h: 28
try:
    PDFACTION_EMBEDDEDGOTO = 5
except:
    pass

# fpdf_doc.h: 31
try:
    PDFDEST_VIEW_UNKNOWN_MODE = 0
except:
    pass

# fpdf_doc.h: 32
try:
    PDFDEST_VIEW_XYZ = 1
except:
    pass

# fpdf_doc.h: 33
try:
    PDFDEST_VIEW_FIT = 2
except:
    pass

# fpdf_doc.h: 34
try:
    PDFDEST_VIEW_FITH = 3
except:
    pass

# fpdf_doc.h: 35
try:
    PDFDEST_VIEW_FITV = 4
except:
    pass

# fpdf_doc.h: 36
try:
    PDFDEST_VIEW_FITR = 5
except:
    pass

# fpdf_doc.h: 37
try:
    PDFDEST_VIEW_FITB = 6
except:
    pass

# fpdf_doc.h: 38
try:
    PDFDEST_VIEW_FITBH = 7
except:
    pass

# fpdf_doc.h: 39
try:
    PDFDEST_VIEW_FITBV = 8
except:
    pass

# fpdf_edit.h: 15
def FPDF_ARGB(a, r, g, b):
    return (uint32_t (ord_if_char((((((uint32_t (ord_if_char(b))).value & 0xff) | (((uint32_t (ord_if_char(g))).value & 0xff) << 8)) | (((uint32_t (ord_if_char(r))).value & 0xff) << 16)) | (((uint32_t (ord_if_char(a))).value & 0xff) << 24))))).value

# fpdf_edit.h: 18
def FPDF_GetBValue(argb):
    return (uint8_t (ord_if_char(argb))).value

# fpdf_edit.h: 19
def FPDF_GetGValue(argb):
    return (uint8_t (ord_if_char(((uint16_t (ord_if_char(argb))).value >> 8)))).value

# fpdf_edit.h: 20
def FPDF_GetRValue(argb):
    return (uint8_t (ord_if_char((argb >> 16)))).value

# fpdf_edit.h: 21
def FPDF_GetAValue(argb):
    return (uint8_t (ord_if_char((argb >> 24)))).value

# fpdf_edit.h: 24
try:
    FPDF_COLORSPACE_UNKNOWN = 0
except:
    pass

# fpdf_edit.h: 25
try:
    FPDF_COLORSPACE_DEVICEGRAY = 1
except:
    pass

# fpdf_edit.h: 26
try:
    FPDF_COLORSPACE_DEVICERGB = 2
except:
    pass

# fpdf_edit.h: 27
try:
    FPDF_COLORSPACE_DEVICECMYK = 3
except:
    pass

# fpdf_edit.h: 28
try:
    FPDF_COLORSPACE_CALGRAY = 4
except:
    pass

# fpdf_edit.h: 29
try:
    FPDF_COLORSPACE_CALRGB = 5
except:
    pass

# fpdf_edit.h: 30
try:
    FPDF_COLORSPACE_LAB = 6
except:
    pass

# fpdf_edit.h: 31
try:
    FPDF_COLORSPACE_ICCBASED = 7
except:
    pass

# fpdf_edit.h: 32
try:
    FPDF_COLORSPACE_SEPARATION = 8
except:
    pass

# fpdf_edit.h: 33
try:
    FPDF_COLORSPACE_DEVICEN = 9
except:
    pass

# fpdf_edit.h: 34
try:
    FPDF_COLORSPACE_INDEXED = 10
except:
    pass

# fpdf_edit.h: 35
try:
    FPDF_COLORSPACE_PATTERN = 11
except:
    pass

# fpdf_edit.h: 38
try:
    FPDF_PAGEOBJ_UNKNOWN = 0
except:
    pass

# fpdf_edit.h: 39
try:
    FPDF_PAGEOBJ_TEXT = 1
except:
    pass

# fpdf_edit.h: 40
try:
    FPDF_PAGEOBJ_PATH = 2
except:
    pass

# fpdf_edit.h: 41
try:
    FPDF_PAGEOBJ_IMAGE = 3
except:
    pass

# fpdf_edit.h: 42
try:
    FPDF_PAGEOBJ_SHADING = 4
except:
    pass

# fpdf_edit.h: 43
try:
    FPDF_PAGEOBJ_FORM = 5
except:
    pass

# fpdf_edit.h: 46
try:
    FPDF_SEGMENT_UNKNOWN = (-1)
except:
    pass

# fpdf_edit.h: 47
try:
    FPDF_SEGMENT_LINETO = 0
except:
    pass

# fpdf_edit.h: 48
try:
    FPDF_SEGMENT_BEZIERTO = 1
except:
    pass

# fpdf_edit.h: 49
try:
    FPDF_SEGMENT_MOVETO = 2
except:
    pass

# fpdf_edit.h: 51
try:
    FPDF_FILLMODE_NONE = 0
except:
    pass

# fpdf_edit.h: 52
try:
    FPDF_FILLMODE_ALTERNATE = 1
except:
    pass

# fpdf_edit.h: 53
try:
    FPDF_FILLMODE_WINDING = 2
except:
    pass

# fpdf_edit.h: 55
try:
    FPDF_FONT_TYPE1 = 1
except:
    pass

# fpdf_edit.h: 56
try:
    FPDF_FONT_TRUETYPE = 2
except:
    pass

# fpdf_edit.h: 58
try:
    FPDF_LINECAP_BUTT = 0
except:
    pass

# fpdf_edit.h: 59
try:
    FPDF_LINECAP_ROUND = 1
except:
    pass

# fpdf_edit.h: 60
try:
    FPDF_LINECAP_PROJECTING_SQUARE = 2
except:
    pass

# fpdf_edit.h: 62
try:
    FPDF_LINEJOIN_MITER = 0
except:
    pass

# fpdf_edit.h: 63
try:
    FPDF_LINEJOIN_ROUND = 1
except:
    pass

# fpdf_edit.h: 64
try:
    FPDF_LINEJOIN_BEVEL = 2
except:
    pass

# fpdf_edit.h: 67
try:
    FPDF_PRINTMODE_EMF = 0
except:
    pass

# fpdf_edit.h: 68
try:
    FPDF_PRINTMODE_TEXTONLY = 1
except:
    pass

# fpdf_edit.h: 69
try:
    FPDF_PRINTMODE_POSTSCRIPT2 = 2
except:
    pass

# fpdf_edit.h: 70
try:
    FPDF_PRINTMODE_POSTSCRIPT3 = 3
except:
    pass

# fpdf_edit.h: 71
try:
    FPDF_PRINTMODE_POSTSCRIPT2_PASSTHROUGH = 4
except:
    pass

# fpdf_edit.h: 72
try:
    FPDF_PRINTMODE_POSTSCRIPT3_PASSTHROUGH = 5
except:
    pass

# fpdf_edit.h: 73
try:
    FPDF_PRINTMODE_EMF_IMAGE_MASKS = 6
except:
    pass

# fpdf_edit.h: 74
try:
    FPDF_PRINTMODE_POSTSCRIPT3_TYPE42 = 7
except:
    pass

# fpdf_edit.h: 75
try:
    FPDF_PRINTMODE_POSTSCRIPT3_TYPE42_PASSTHROUGH = 8
except:
    pass

# fpdf_ext.h: 20
try:
    FPDF_UNSP_DOC_XFAFORM = 1
except:
    pass

# fpdf_ext.h: 22
try:
    FPDF_UNSP_DOC_PORTABLECOLLECTION = 2
except:
    pass

# fpdf_ext.h: 24
try:
    FPDF_UNSP_DOC_ATTACHMENT = 3
except:
    pass

# fpdf_ext.h: 26
try:
    FPDF_UNSP_DOC_SECURITY = 4
except:
    pass

# fpdf_ext.h: 28
try:
    FPDF_UNSP_DOC_SHAREDREVIEW = 5
except:
    pass

# fpdf_ext.h: 30
try:
    FPDF_UNSP_DOC_SHAREDFORM_ACROBAT = 6
except:
    pass

# fpdf_ext.h: 32
try:
    FPDF_UNSP_DOC_SHAREDFORM_FILESYSTEM = 7
except:
    pass

# fpdf_ext.h: 34
try:
    FPDF_UNSP_DOC_SHAREDFORM_EMAIL = 8
except:
    pass

# fpdf_ext.h: 36
try:
    FPDF_UNSP_ANNOT_3DANNOT = 11
except:
    pass

# fpdf_ext.h: 38
try:
    FPDF_UNSP_ANNOT_MOVIE = 12
except:
    pass

# fpdf_ext.h: 40
try:
    FPDF_UNSP_ANNOT_SOUND = 13
except:
    pass

# fpdf_ext.h: 42
try:
    FPDF_UNSP_ANNOT_SCREEN_MEDIA = 14
except:
    pass

# fpdf_ext.h: 44
try:
    FPDF_UNSP_ANNOT_SCREEN_RICHMEDIA = 15
except:
    pass

# fpdf_ext.h: 46
try:
    FPDF_UNSP_ANNOT_ATTACHMENT = 16
except:
    pass

# fpdf_ext.h: 48
try:
    FPDF_UNSP_ANNOT_SIG = 17
except:
    pass

# fpdf_ext.h: 92
try:
    PAGEMODE_UNKNOWN = (-1)
except:
    pass

# fpdf_ext.h: 94
try:
    PAGEMODE_USENONE = 0
except:
    pass

# fpdf_ext.h: 96
try:
    PAGEMODE_USEOUTLINES = 1
except:
    pass

# fpdf_ext.h: 98
try:
    PAGEMODE_USETHUMBS = 2
except:
    pass

# fpdf_ext.h: 100
try:
    PAGEMODE_FULLSCREEN = 3
except:
    pass

# fpdf_ext.h: 102
try:
    PAGEMODE_USEOC = 4
except:
    pass

# fpdf_ext.h: 104
try:
    PAGEMODE_USEATTACHMENTS = 5
except:
    pass

# fpdf_flatten.h: 14
try:
    FLATTEN_FAIL = 0
except:
    pass

# fpdf_flatten.h: 16
try:
    FLATTEN_SUCCESS = 1
except:
    pass

# fpdf_flatten.h: 18
try:
    FLATTEN_NOTHINGTODO = 2
except:
    pass

# fpdf_flatten.h: 21
try:
    FLAT_NORMALDISPLAY = 0
except:
    pass

# fpdf_flatten.h: 23
try:
    FLAT_PRINT = 1
except:
    pass

# fpdf_progressive.h: 15
try:
    FPDF_RENDER_READY = 0
except:
    pass

# fpdf_progressive.h: 16
try:
    FPDF_RENDER_TOBECONTINUED = 1
except:
    pass

# fpdf_progressive.h: 17
try:
    FPDF_RENDER_DONE = 2
except:
    pass

# fpdf_progressive.h: 18
try:
    FPDF_RENDER_FAILED = 3
except:
    pass

# fpdf_save.h: 45
try:
    FPDF_INCREMENTAL = 1
except:
    pass

# fpdf_save.h: 46
try:
    FPDF_NO_INCREMENTAL = 2
except:
    pass

# fpdf_save.h: 47
try:
    FPDF_REMOVE_SECURITY = 3
except:
    pass

# fpdf_sysfontinfo.h: 15
try:
    FXFONT_ANSI_CHARSET = 0
except:
    pass

# fpdf_sysfontinfo.h: 16
try:
    FXFONT_DEFAULT_CHARSET = 1
except:
    pass

# fpdf_sysfontinfo.h: 17
try:
    FXFONT_SYMBOL_CHARSET = 2
except:
    pass

# fpdf_sysfontinfo.h: 18
try:
    FXFONT_SHIFTJIS_CHARSET = 128
except:
    pass

# fpdf_sysfontinfo.h: 19
try:
    FXFONT_HANGEUL_CHARSET = 129
except:
    pass

# fpdf_sysfontinfo.h: 20
try:
    FXFONT_GB2312_CHARSET = 134
except:
    pass

# fpdf_sysfontinfo.h: 21
try:
    FXFONT_CHINESEBIG5_CHARSET = 136
except:
    pass

# fpdf_sysfontinfo.h: 22
try:
    FXFONT_GREEK_CHARSET = 161
except:
    pass

# fpdf_sysfontinfo.h: 23
try:
    FXFONT_VIETNAMESE_CHARSET = 163
except:
    pass

# fpdf_sysfontinfo.h: 24
try:
    FXFONT_HEBREW_CHARSET = 177
except:
    pass

# fpdf_sysfontinfo.h: 25
try:
    FXFONT_ARABIC_CHARSET = 178
except:
    pass

# fpdf_sysfontinfo.h: 26
try:
    FXFONT_CYRILLIC_CHARSET = 204
except:
    pass

# fpdf_sysfontinfo.h: 27
try:
    FXFONT_THAI_CHARSET = 222
except:
    pass

# fpdf_sysfontinfo.h: 28
try:
    FXFONT_EASTERNEUROPEAN_CHARSET = 238
except:
    pass

# fpdf_sysfontinfo.h: 31
try:
    FXFONT_FF_FIXEDPITCH = (1 << 0)
except:
    pass

# fpdf_sysfontinfo.h: 32
try:
    FXFONT_FF_ROMAN = (1 << 4)
except:
    pass

# fpdf_sysfontinfo.h: 33
try:
    FXFONT_FF_SCRIPT = (4 << 4)
except:
    pass

# fpdf_sysfontinfo.h: 36
try:
    FXFONT_FW_NORMAL = 400
except:
    pass

# fpdf_sysfontinfo.h: 37
try:
    FXFONT_FW_BOLD = 700
except:
    pass

# fpdf_text.h: 470
try:
    FPDF_MATCHCASE = 0x00000001
except:
    pass

# fpdf_text.h: 472
try:
    FPDF_MATCHWHOLEWORD = 0x00000002
except:
    pass

# fpdf_text.h: 474
try:
    FPDF_CONSECUTIVE = 0x00000004
except:
    pass

fpdf_action_t__ = struct_fpdf_action_t__# fpdfview.h: 54

fpdf_annotation_t__ = struct_fpdf_annotation_t__# fpdfview.h: 55

fpdf_attachment_t__ = struct_fpdf_attachment_t__# fpdfview.h: 56

fpdf_avail_t__ = struct_fpdf_avail_t__# fpdfview.h: 57

fpdf_bitmap_t__ = struct_fpdf_bitmap_t__# fpdfview.h: 58

fpdf_bookmark_t__ = struct_fpdf_bookmark_t__# fpdfview.h: 59

fpdf_clippath_t__ = struct_fpdf_clippath_t__# fpdfview.h: 60

fpdf_dest_t__ = struct_fpdf_dest_t__# fpdfview.h: 61

fpdf_document_t__ = struct_fpdf_document_t__# fpdfview.h: 62

fpdf_font_t__ = struct_fpdf_font_t__# fpdfview.h: 63

fpdf_form_handle_t__ = struct_fpdf_form_handle_t__# fpdfview.h: 64

fpdf_glyphpath_t__ = struct_fpdf_glyphpath_t__# fpdfview.h: 65

fpdf_javascript_action_t = struct_fpdf_javascript_action_t# fpdfview.h: 66

fpdf_link_t__ = struct_fpdf_link_t__# fpdfview.h: 67

fpdf_page_t__ = struct_fpdf_page_t__# fpdfview.h: 68

fpdf_pagelink_t__ = struct_fpdf_pagelink_t__# fpdfview.h: 69

fpdf_pageobject_t__ = struct_fpdf_pageobject_t__# fpdfview.h: 70

fpdf_pageobjectmark_t__ = struct_fpdf_pageobjectmark_t__# fpdfview.h: 71

fpdf_pagerange_t__ = struct_fpdf_pagerange_t__# fpdfview.h: 72

fpdf_pathsegment_t = struct_fpdf_pathsegment_t# fpdfview.h: 73

fpdf_schhandle_t__ = struct_fpdf_schhandle_t__# fpdfview.h: 75

fpdf_signature_t__ = struct_fpdf_signature_t__# fpdfview.h: 76

fpdf_structelement_t__ = struct_fpdf_structelement_t__# fpdfview.h: 77

fpdf_structelement_attr_t__ = struct_fpdf_structelement_attr_t__# fpdfview.h: 78

fpdf_structtree_t__ = struct_fpdf_structtree_t__# fpdfview.h: 79

fpdf_textpage_t__ = struct_fpdf_textpage_t__# fpdfview.h: 80

fpdf_widget_t__ = struct_fpdf_widget_t__# fpdfview.h: 81

fpdf_xobject_t__ = struct_fpdf_xobject_t__# fpdfview.h: 82

FPDF_BSTR_ = struct_FPDF_BSTR_# fpdfview.h: 115

_FS_MATRIX_ = struct__FS_MATRIX_# fpdfview.h: 141

_FS_RECTF_ = struct__FS_RECTF_# fpdfview.h: 144

FS_SIZEF_ = struct_FS_SIZEF_# fpdfview.h: 159

FS_POINTF_ = struct_FS_POINTF_# fpdfview.h: 168

_FS_QUADPOINTSF = struct__FS_QUADPOINTSF# fpdfview.h: 185

FPDF_LIBRARY_CONFIG_ = struct_FPDF_LIBRARY_CONFIG_# fpdfview.h: 278

FPDF_FILEHANDLER_ = struct_FPDF_FILEHANDLER_# fpdfview.h: 539

FPDF_COLORSCHEME_ = struct_FPDF_COLORSCHEME_# fpdfview.h: 813

_IPDF_JsPlatform = struct__IPDF_JsPlatform# fpdf_formfill.h: 52

_FPDF_SYSTEMTIME = struct__FPDF_SYSTEMTIME# fpdf_formfill.h: 355

_FPDF_FORMFILLINFO = struct__FPDF_FORMFILLINFO# fpdf_formfill.h: 377

_FX_FILEAVAIL = struct__FX_FILEAVAIL# fpdf_dataavail.h: 33

_FX_DOWNLOADHINTS = struct__FX_DOWNLOADHINTS# fpdf_dataavail.h: 71

FPDF_IMAGEOBJ_METADATA = struct_FPDF_IMAGEOBJ_METADATA# fpdf_edit.h: 93

_UNSUPPORT_INFO = struct__UNSUPPORT_INFO# fpdf_ext.h: 51

_IFSDK_PAUSE = struct__IFSDK_PAUSE# fpdf_progressive.h: 25

FPDF_FILEWRITE_ = struct_FPDF_FILEWRITE_# fpdf_save.h: 19

_FPDF_SYSFONTINFO = struct__FPDF_SYSFONTINFO# fpdf_sysfontinfo.h: 48

FPDF_CharsetFontMap_ = struct_FPDF_CharsetFontMap_# fpdf_sysfontinfo.h: 236

# No inserted files

# No prefix-stripping

