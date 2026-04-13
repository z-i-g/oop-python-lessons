from dataclasses import dataclass
from typing import Protocol
import math

@dataclass(frozen=True)
class _InternalState:
    x: float
    y: float
    angle: float
    water_level: int

class BaseRobot(Protocol):
    def get_info(self) -> str: ...
    def turn(self, angle: float) -> "RobotWithMove": ...

class RobotWithMove(BaseRobot, Protocol):
    def move(self, dist: float) -> "RobotWithMove": ...
    def try_clean(self) -> "RobotWithCleaning": ...

class RobotWithCleaning(BaseRobot, Protocol):
    def set_mode(self, mode: int) -> "RobotWithCleaning": ...
    def stop_cleaning(self) -> "RobotWithMove": ...

@dataclass(frozen=True)
class RobotCapabilities:
    __state: _InternalState
    __is_blocked: bool = False

    def get_info(self) -> str:
        s = self.__state
        status = "BLOCKED" if self.__is_blocked else "OK"
        return f"Pos:({s.x:.1f}, {s.y:.1f}), Angle:{s.angle}, Water:{s.water_level}, Status:{status}"

    def turn(self, angle: float) -> "RobotWithMove":
        new_state = _InternalState(
            self.__state.x, self.__state.y, 
            self.__state.angle + angle, 
            self.__state.water_level
        )
        return RobotCapabilities(new_state, self.__is_blocked)

    def move(self, dist: float) -> "RobotWithMove":
        if dist > 100 or self.__is_blocked:
            print("Ошибка или робот заблокирован!")
            return RobotBlocked(self.__state)
        
        rads = math.radians(self.__state.angle)
        new_state = _InternalState(
            self.__state.x + dist * math.cos(rads),
            self.__state.y + dist * math.sin(rads),
            self.__state.angle,
            self.__state.water_level
        )
        return RobotCapabilities(new_state)

    def try_clean(self) -> "RobotWithCleaning":
        if self.__state.water_level <= 0:
            raise RuntimeError("Ошибка - вода отсутствует!")
        return self

    def set_mode(self, mode: int) -> "RobotWithCleaning":
        new_state = _InternalState(
            self.__state.x, self.__state.y, self.__state.angle,
            self.__state.water_level - 1
        )
        return RobotCapabilities(new_state)

@dataclass(frozen=True)
class RobotBlocked:
    __state: _InternalState

    def get_info(self) -> str:
                return (f"РОБОТ ЗАБЛОКИРОВАН на позиции ({self.__state.x}, {self.__state.y}). "
                f"Дальнейшее движение невозможно.")
    
    def turn(self, angle: float) -> "RobotBlocked":
        print("Движение всё еще заблокировано!")
        return self