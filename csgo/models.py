import struct, ctypes, math

class Glow:
    def __init__(self, r: float=0, g: float=0, b: float=0, alpha: float=1.7) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.alpha = alpha

    def pack(self):
        return ctypes.create_string_buffer(struct.pack('ffff', self.r, self.g, self.b, self.alpha))
    
class Vector2(ctypes.LittleEndianStructure):
    _fields_ = [('x', ctypes.c_float),
               ('y', ctypes.c_float)]
    
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)
    
class Vector3(ctypes.LittleEndianStructure):
    _fields_ = [('x', ctypes.c_float),
               ('y', ctypes.c_float),
               ('z', ctypes.c_float)]
    
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other)
    
    def __truediv__(self, other):
        return Vector3(self.x / other, self.y / other, self.z / other)
    
    def __str__(self):
        return f'{self.x} {self.y} {self.z}'
    
    @property
    def is_zero(self):
        return self.x == 0. and self.y == 0. and self.z == 0.
    
    @property
    def radians(self):
        return Vector3(
            math.atan2(-self.z, math.hypot(self.x, self.y)) * 180 / math.pi,
            math.atan2(self.y, self.x) * 180 / math.pi,
            0
        )