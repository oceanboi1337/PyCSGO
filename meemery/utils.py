from ctypes import *
from ctypes.wintypes import *

import psutil

def process_id(name: str) -> int:
    for p in psutil.process_iter():
        if name in p.name().lower():
            return p.pid
        
def kernel_32_setup():
    kernel = WinDLL('kernel32')
    kernel.OpenProcess.argtypes = [DWORD, BOOL, DWORD]
    kernel.OpenProcess.restype = HANDLE
    
    kernel.ReadProcessMemory.argtypes = [HANDLE, LPVOID, LPVOID, c_size_t, POINTER(c_size_t)]
    kernel.ReadProcessMemory.restype = BOOL

    return kernel