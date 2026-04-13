from dataclasses import dataclass, replace
from typing import Protocol, Callable, TypeVar, Generic, Any, Self, Final, Union
from enum import Enum
import math

class CleaningMode(Enum):
    WATER = 1
    SOAP = 2
    BRUSH = 3

@dataclass(frozen=True)
class RobotState:
    __x: float
    __y: float
    __angle: float
    __mode: CleaningMode

    @property
    def position(self) -> tuple[float, float]:
        return (self.__x, self.__y)

    @property
    def angle(self) -> float:
        return self.__angle

    @property
    def mode(self) -> CleaningMode:
        return self.__mode

    def update_position(self, dx: float, dy: float) -> Self:
        return replace(self, _RobotState__x=self.__x + dx, _RobotState__y=self.__y + dy)

    def update_angle(self, da: float) -> Self:
        return replace(self, _RobotState__angle=self.__angle + da)

    def update_mode(self, mode: CleaningMode) -> Self:
        return replace(self, _RobotState__mode=mode)

@dataclass(frozen=True)
class MoveResponse:
    distance: float
    success: bool

@dataclass(frozen=True)
class TurnResponse:
    angle: float
    success: bool

@dataclass(frozen=True)
class ModeResponse:
    mode: CleaningMode
    success: bool

T = TypeVar('T')

class RobotProgram(Protocol):
    def interpret(self, state: RobotState) -> tuple[Any, RobotState]: ...

@dataclass(frozen=True)
class Stop:
    def interpret(self, state: RobotState) -> tuple[None, RobotState]:
        return None, state

@dataclass(frozen=True)
class Move(Generic[T]):
    distance: float
    next: Callable[[MoveResponse], T]
    
    def interpret(self, state: RobotState) -> tuple[T, RobotState]:
        rads = math.radians(state.angle)
        new_state = state.update_position(
            self.distance * math.cos(rads),
            self.distance * math.sin(rads)
        )
        return self.next(MoveResponse(self.distance, True)), new_state

@dataclass(frozen=True)
class Turn(Generic[T]):
    angle: float
    next: Callable[[TurnResponse], T]
    
    def interpret(self, state: RobotState) -> tuple[T, RobotState]:
        new_state = state.update_angle(self.angle)
        return self.next(TurnResponse(self.angle, True)), new_state

@dataclass(frozen=True)
class SetMode(Generic[T]):
    mode: CleaningMode
    next: Callable[[ModeResponse], T]
    
    def interpret(self, state: RobotState) -> tuple[T, RobotState]:
        new_state = state.update_mode(self.mode)
        return self.next(ModeResponse(self.mode, True)), new_state

class Interpreter:
    @staticmethod
    def run(program: RobotProgram, state: RobotState) -> RobotState:
        curr_p, curr_s = program, state
        while curr_p is not None and not isinstance(curr_p, Stop):
            curr_p, curr_s = curr_p.interpret(curr_s) # type: ignore
        return curr_s

class RobotDSL:
    def __init__(self):
        self._commands: list[Callable[[Any], RobotProgram]] = []
    
    def move(self, distance: float) -> Self:
        self._commands.append(lambda n: Move(distance, lambda _: n))
        return self
    
    def turn(self, angle: float) -> Self:
        self._commands.append(lambda n: Turn(angle, lambda _: n))
        return self
    
    def set_mode(self, mode: CleaningMode) -> Self:
        self._commands.append(lambda n: SetMode(mode, lambda _: n))
        return self
    
    def repeat(self, times: int, block: Callable[[Self], None]) -> Self:
        sub_dsl = RobotDSL()
        block(sub_dsl) # type: ignore
        for _ in range(times):
            self._commands.extend(sub_dsl._commands)
        return self

    def sequence(self, *funcs: Callable[[Self], None]) -> Self:
        for func in funcs:
            func(self)
        return self
    
    def build(self) -> RobotProgram:
        prog: RobotProgram = Stop()
        for cmd_factory in reversed(self._commands):
            prog = cmd_factory(prog)
        return prog