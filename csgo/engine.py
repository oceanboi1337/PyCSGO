from meemery.manager import MemoryManager
from .models import *

from ctypes import *
from offsets import Offsets

class Engine:
    def __init__(self, manager: MemoryManager=None, multiprocess: bool=True) -> None:
        if not manager:
            self.manager = MemoryManager('csgo.exe')
        else:
            self.manager = manager
        self.multiprocess = multiprocess
        self.engine = self.manager.module_addr('engine.dll')
        self.client = self.manager.module_addr('client.dll')

    @property
    def client_state(self):
        return self.manager.read(self.engine + 0x59F19C, int)

    @property
    def local_player(self):
        return self.manager.read(self.client + 0xDEB99C, c_uint)
    
    @property
    def game_state(self):
        return self.manager.read(self.client_state + Offsets.dwClientState_State, int)
    
    @property
    def local_player_id(self):
        return 1#self.manager.read(self.client_state + Offsets.dwClientState_GetLocalPlayer, int) + 1
    
    def health(self, entity: int):
        return self.manager.read(entity + 0x100, int)
    
    def team(self, entity):
        return self.manager.read(entity + Offsets.m_iTeamNum, int)

    @property
    def entities(self):
        for i in range(32):
            entity = self.manager.read(self.client + 0x4E0102C + i * 0x10, int)
            if entity > 0:
                yield entity

    def glow_manager(self):
        return self.manager.read(self.client + 0x535BAD0, int)

    def set_glow(self, entity: int, glow: Glow):
        index = self.manager.read(entity + 0x10488, int)
        self.manager.write(self.glow_manager() + ((index * 0x38) + 0x8), glow.pack())
        self.manager.write(self.glow_manager() + ((index * 0x38) + 0x28), c_bool(1))
        self.manager.write(self.glow_manager() + ((index * 0x38) + 0x29), c_bool(0))

    def is_dormant(self, entity):
        return self.manager.read(entity + Offsets.m_bDormant, bool)

    def spotted(self, entity, id):
        return bool((self.manager.read(entity + Offsets.m_bSpottedByMask, int) & (1 << (id - 1))) != 0)
    
    def bones(self, entity):
        return self.manager.read(entity + Offsets.m_dwBoneMatrix, c_uint)
    
    def bone_position(self, entity, bone_index):
        bone_matrix = self.bones(entity)
        return Vector3(
            self.manager.read(bone_matrix + 0x30 * bone_index + 0x0C, float),
            self.manager.read(bone_matrix + 0x30 * bone_index + 0x1C, float),
            self.manager.read(bone_matrix + 0x30 * bone_index + 0x2C, float)
        )
    
    def calculate_angle(self, local: Vector3, target: Vector3, view_angle: Vector3):
        return ((target - local).radians - view_angle)
    
    @property
    def local_eyes(self) -> Vector3:
        origin = self.manager.read(self.local_player + Offsets.m_vecOrigin, Vector3)
        offset = self.manager.read(self.local_player + Offsets.m_vecViewOffset, Vector3)
        return origin + offset

    @property
    def view_angles(self):
        return self.manager.read(self.client_state + 0x4D90, Vector3)
    
    @view_angles.setter
    def view_angles(self, data: Vector3):
        self.manager.write(self.client_state + 0x4D90, data)
    
    @property
    def aim_punch(self):
        return self.manager.read(self.local_player +  0x303C, Vector3) * 2
    
    @property
    def shots_fired(self):
        return self.manager.read(self.local_player + 0x103E0, int)