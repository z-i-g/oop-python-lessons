from dataclasses import dataclass
from enum import Enum
import math


# Состояние робота
@dataclass
class RobotState:
    x: float
    y: float
    angle: float
    state: int

# Режимы работы
class CleaningMode(Enum):
    WATER = 1
    SOAP = 2
    BRUSH = 3

def move(dist, state):
    angle_rads = state.angle * (math.pi / 180.0)
    new_state = RobotState(
        state.x + dist * math.cos(angle_rads),
        state.y + dist * math.sin(angle_rads),
        state.angle,
        state.state)
    return new_state
    
@dataclass
class Event:
    description: str
    state: RobotState

    def execute(self):
        pass

class MoveEvent(Event):
    def __init__(self, dist, state):
        self.description = 'Move'
        self.dist = dist
        self.state = state

    def exec(self):
        self.state = move(self.dist, self.state)
        return self
    
class EventStore:
    def __init__(self):
        self.events = []

    def add_event(self, event: Event):
        self.events.append(event)

    def get_state(self):
        if len(self.events) == 0:
            return initial_state
        else:
            return self.events[-1].state
    
initial_state = RobotState(0.0, 0.0, 0, CleaningMode.WATER.value)