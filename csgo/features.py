from .engine import Engine
from csgo.models import *

import math

class Features:
    def __init__(self, engine: Engine, multiprocess: bool=False) -> None:
        self.engine = engine
        self.multiprocess = multiprocess

        self.storage = {}

    def recoil_control(self):
        if self.engine.shots_fired > 1:
            view_angles = self.engine.view_angles
            aim_punch = self.engine.aim_punch

            new_angles = view_angles + self.storage['old_punch'] - aim_punch

            self.engine.view_angles = new_angles
            self.storage['old_punch'] = aim_punch
        else:
            self.storage['old_punch'] = Vector3(0, 0, 0)

    def wallhack(self):
        for entity in self.engine.entities:
            if self.engine.team(entity) != self.engine.team(self.engine.local_player):
                self.engine.set_glow(entity, Glow(1, 0, 0, 0.7))

    def aimbot(self):
        targets = []

        best_fov = 5
        best_angle = Vector3(0, 0, 0)

        for player in self.engine.entities:
            if self.engine.is_dormant(player): continue
            if self.engine.team(player) == self.engine.team(self.engine.local_player): continue
            if self.engine.health(player) <= 0: continue
            if not self.engine.spotted(player, self.engine.local_player_id): continue
            if player == self.engine.local_player: continue

            head_position = self.engine.bone_position(player, 8)

            local_pos = self.engine.local_eyes
            view_angles = self.engine.view_angles
            aim_punch = self.engine.aim_punch

            #print(head_position.x, head_position.y, head_position.z)
            #print(local_pos.x, local_pos.y, local_pos.z)

            angle = self.engine.calculate_angle(local_pos, head_position, view_angles + aim_punch)

            fov = math.hypot(angle.x, angle.y)
            if fov < best_fov:
                best_fov = fov
                best_angle = angle

        if best_angle.is_zero: return

        if abs(best_angle.x) > 0.0001 and abs(best_angle.y) > 0.0001:
            self.engine.view_angles = self.engine.view_angles + best_angle / 10