import math
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Callable, Union

class MoveResponse:
    OK = "MOVE_OK"
    BARRIER = "HIT_BARRIER"

class SetStateResponse:
    OK = "STATE_OK"
    NO_WATER = "OUT_OF_WATER"
    NO_SOAP = "OUT_OF_SOAP"

class Event: pass

@dataclass
class MoveRequestedEvent(Event):
    distance: float

@dataclass
class RobotMovedEvent(Event):
    distance: float
    status: str

@dataclass
class StateChangeRequestedEvent(Event):
    new_mode: int

@dataclass
class StateChangedEvent(Event):
    new_mode: int
    status: str

def check_position(x: float, y: float) -> tuple[float, float, str]:
    constrained_x = max(0, min(100, x))
    constrained_y = max(0, min(100, y))
    if x == constrained_x and y == constrained_y:
        return x, y, MoveResponse.OK
    return constrained_x, constrained_y, MoveResponse.BARRIER

def check_resources(new_mode: int) -> str:
    if new_mode == 1:
        return SetStateResponse.NO_WATER
    return SetStateResponse.OK

class EventStore:
    def __init__(self):
        self._events: Dict[str, List[Event]] = {}
        self._subscribers: List[Callable[[str, Event], None]] = []

    def subscribe(self, handler: Callable[[str, Event], None]):
        self._subscribers.append(handler)

    def append_event(self, robot_id: str, event: Event):
        self._events.setdefault(robot_id, []).append(event)
        for sub in self._subscribers:
            sub(robot_id, event)

    def get_events(self, robot_id: str) -> List[Event]:
        return self._events.get(robot_id, [])

class StateProjector:
    @staticmethod
    def project(events: List[Event]) -> 'RobotState':
        state = RobotState(0.0, 0.0, 0, 1)
        for ev in events:
            if isinstance(ev, RobotMovedEvent) and ev.status == MoveResponse.OK:
                rads = state.angle * (math.pi / 180.0)
                state.x += ev.distance * math.cos(rads)
                state.y += ev.distance * math.sin(rads)
            elif isinstance(ev, StateChangedEvent) and ev.status == SetStateResponse.OK:
                state.state = ev.new_mode
        return state

@dataclass
class RobotState:
    x: float; y: float; angle: float; state: int

class MoveProcessor:
    def __init__(self, store: EventStore):
        self.store = store

    def __call__(self, robot_id: str, event: Event):
        if isinstance(event, MoveRequestedEvent):
            current_events = self.store.get_events(robot_id)
            state = StateProjector.project(current_events)
            
            rads = state.angle * (math.pi / 180.0)
            target_x = state.x + event.distance * math.cos(rads)
            target_y = state.y + event.distance * math.sin(rads)
            
            _, _, status = check_position(target_x, target_y)
            
            self.store.append_event(robot_id, RobotMovedEvent(event.distance, status))

class ResourceProcessor:
    def __init__(self, store: EventStore):
        self.store = store

    def __call__(self, robot_id: str, event: Event):
        if isinstance(event, StateChangeRequestedEvent):
            status = check_resources(event.new_mode)
            self.store.append_event(robot_id, StateChangedEvent(event.new_mode, status))

class CommandHandler:
    def __init__(self, store: EventStore):
        self.store = store

    def handle(self, robot_id: str, cmd: str, val: Union[float, int]):
        if cmd == "MOVE":
            self.store.append_event(robot_id, MoveRequestedEvent(val))
        elif cmd == "SET_STATE":
            self.store.append_event(robot_id, StateChangeRequestedEvent(int(val)))
