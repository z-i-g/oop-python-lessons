from dataclasses import dataclass
from typing import Protocol, Callable, TypeVar, Generic, Any
from enum import Enum
import math

T = TypeVar('T')
R = TypeVar('R')

@dataclass
class RobotState:
    x: float
    y: float
    angle: float
    state: int

class CleaningMode(Enum):
    WATER = 1
    SOAP = 2
    BRUSH = 3

@dataclass
class MoveResponse:
    distance_moved: float
    success: bool

@dataclass
class TurnResponse:
    angle_turned: float
    success: bool

@dataclass
class StateResponse:
    mode: CleaningMode
    success: bool

class RobotProgram(Protocol):
    def interpret(self, state: RobotState) -> tuple[Any, RobotState]:
        pass

class Stop:
    def interpret(self, state: RobotState) -> tuple[None, RobotState]:
        return None, state

@dataclass
class Move(Generic[T]):
    distance: float
    next: Callable[[MoveResponse], T]
    
    def interpret(self, state: RobotState) -> tuple[T, RobotState]:
        angle_rads = state.angle * (math.pi/180.0)
        new_state = RobotState(
            x=state.x + self.distance * math.cos(angle_rads),
            y=state.y + self.distance * math.sin(angle_rads),
            angle=state.angle,
            state=state.state
        )
        response = MoveResponse(self.distance, True)
        next_program = self.next(response)
        return next_program, new_state

@dataclass
class Turn(Generic[T]):
    angle: float
    next: Callable[[TurnResponse], T]
    
    def interpret(self, state: RobotState) -> tuple[T, RobotState]:
        new_state = RobotState(
            x=state.x,
            y=state.y,
            angle=state.angle + self.angle,
            state=state.state
        )
        response = TurnResponse(self.angle, True)
        return self.next(response), new_state

@dataclass
class SetState(Generic[T]):
    new_state: CleaningMode
    next: Callable[[StateResponse], T]
    
    def interpret(self, state: RobotState) -> tuple[T, RobotState]:
        new_state = RobotState(
            x=state.x,
            y=state.y,
            angle=state.angle,
            state=self.new_state.value
        )
        response = StateResponse(self.new_state, True)
        return self.next(response), new_state

class Interpreter:
    def run(self, program: RobotProgram, initial_state: RobotState) -> RobotState:
        current_program = program
        current_state = initial_state
        while current_program is not None and not isinstance(current_program, Stop):
            next_program, current_state = current_program.interpret(current_state)
            current_program = next_program
        return current_state