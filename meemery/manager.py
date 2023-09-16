from ctypes import *
import ctypes
from ctypes.wintypes import *

from meemery import utils
from .defines import *

import time

class MemoryManager:
    def __init__(self, process_name: str, mp: bool=False) -> None:
        self.process_name = process_name
        self.mp = mp
        self.pid = utils.process_id(process_name)
        self.kernel = utils.kernel_32_setup()
        self.process = self.kernel.OpenProcess(Access.ALL_ACCESS, 0, self.pid)

    def type2size(self, t: type):
        if t == int:
            return 4
        elif t == bool:
            return 1
        elif t == float:
            return 4
        
    def read(self, address: int, t):
        size = 0
        if isinstance(t, ctypes._SimpleCData) or issubclass(t, Structure) or t == c_uint:
            size = sizeof(t)
        else:
            size = self.type2size(t)

        buffer = (c_byte * size)()
        bytes_read = c_size_t()

        if self.kernel.ReadProcessMemory(self.process, address, buffer, size, byref(bytes_read)):
            if t == int or t == c_uint:
                return int(cast(buffer, POINTER(c_int)).contents.value)
            elif t == bool:
                return bool(cast(buffer, POINTER(c_bool)).contents.value)
            elif t == float:
                return float(cast(buffer, POINTER(c_float)).contents.value)
            else:
                return cast(buffer, POINTER(t)).contents
        else:
            print(f'RPM failed with error {GetLastError()} while trying to read address {address} of size {size}')

    def write(self, address: int, data):
        written = c_size_t()
        if self.kernel.WriteProcessMemory(self.process, cast(address, c_void_p), cast(byref(data), c_void_p), sizeof(data), byref(written)):
            return written
        
    def module_addr(self, name: str) -> int:
        base = 0
        snapshot = self.kernel.CreateToolhelp32Snapshot(TH32CS.SNAPMODULE, self.pid)
        if snapshot < 0:
            return None
        
        entry = MODULEENTRY32()
        entry.dwSize = sizeof(MODULEENTRY32)

        if self.kernel.Module32First(snapshot, byref(entry)):
            while 1:
                if name.encode('utf-8') == entry.szModule:
                    base = entry.modBaseAddr
                    break
                if not self.kernel.Module32Next(snapshot, byref(entry)):
                    break
        
        self.kernel.CloseHandle(snapshot)
        return int(base)