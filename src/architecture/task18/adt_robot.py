import math
from abc import ABC, abstractmethod
from dataclasses import dataclass, replace
from typing import List, Tuple

@dataclass(frozen=True)
class RobotState:
    x: float
    y: float
    angle: float
    mode: int
    history: Tuple[str, ...] = ()

class CleanerApi(ABC):
    WATER =1
    SOAP = 2
    BRUSH = 3

    @abstractmethod
    def move(self, state: RobotState, dist: float) -> RobotState: pass
    
    @abstractmethod
    def turn(self, state: RobotState, angle: float) -> RobotState: pass
    
    @abstractmethod
    def set_mode(self, state: RobotState, mode_name: str) -> RobotState: pass

class Cleaner(CleanerApi):
    
    def get_start_state(self) -> RobotState:
        return RobotState(0.0, 0.0, 0.0, self.WATER)

    def _add_log(self, state: RobotState, message: str) -> RobotState:
        new_history = state.history + (message,)
        return replace(state, history=new_history)

    def move(self, state: RobotState, dist: float) -> RobotState:
        rads = math.radians(state.angle)
        new_x = state.x + dist * math.cos(rads)
        new_y = state.y + dist * math.sin(rads)
        
        msg = f"POS({new_x:.1f}, {new_y:.1f})"
        return self._add_log(replace(state, x=new_x, y=new_y), msg)

    def turn(self, state: RobotState, angle: float) -> RobotState:
        new_angle = (state.angle + angle) % 360
        msg = f"ANGLE {new_angle}"
        return self._add_log(replace(state, angle=new_angle), msg)

    def set_mode(self, state: RobotState, mode_name: str) -> RobotState:
        modes = {'water': self.WATER, 'soap': self.SOAP, 'brush': self.BRUSH}
        target_mode = modes.get(mode_name, state.mode)
        msg = f"STATE {target_mode}"
        return self._add_log(replace(state, mode=target_mode), msg)

    def make(self, state: RobotState, commands: List[str]) -> RobotState:
        current_state = state
        
        for command in commands:
            parts = command.split()
            cmd_type = parts[0]
            
            if cmd_type == 'move':
                current_state = self.move(current_state, float(parts[1]))
            elif cmd_type == 'turn':
                current_state = self.turn(current_state, float(parts[1]))
            elif cmd_type == 'set':
                current_state = self.set_mode(current_state, parts[1])
            elif cmd_type == 'start':
                print(f"START WITH {current_state.mode}")
                current_state = self._add_log(current_state, "START")
            elif cmd_type == 'stop':
                print("STOP")
                current_state = self._add_log(current_state, "STOP")
        return current_state