import enum
from ctypes import *

class Access(enum.IntEnum):
    ALL_ACCESS = 0x1fffff

class TH32CS(enum.IntEnum):
    SNAPMODULE = 0x00000008

class MODULEENTRY32(Structure):
    _fields_ = [("dwSize", c_ulong),
                ("th32ModuleID", c_ulong),
                ("th32ProcessID", c_ulong),
                ("GlblcntUsage", c_ulong),
                ("ProccntUsage", c_ulong),
                ("modBaseAddr", c_void_p),  # Changed the type to c_void_p
                ("modBaseSize", c_ulong),
                ("hModule", c_void_p),
                ("szModule", c_char * 256),
                ("szExePath", c_char * 260)]