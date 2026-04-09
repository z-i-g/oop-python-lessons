import math
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Callable

class Event:
    pass

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
class MoveRequestedEvent(Event):
    distance: float

@dataclass
class RobotMovedEvent(Event):
    distance: float

@dataclass
class TurnRequestedEvent(Event):
    angle: float

@dataclass
class RobotTurnedEvent(Event):
    angle: float

class EventStore:
    def __init__(self):
        self._events: Dict[str, List[Event]] = {}
        self._subscribers: List[Callable[[str, Event], None]] = []

    def subscribe(self, handler: Callable[[str, Event], None]):
        self._subscribers.append(handler)

    def append_event(self, robot_id: str, event: Event):
        if robot_id not in self._events:
            self._events[robot_id] = []
        self._events[robot_id].append(event)
        for sub in self._subscribers:
            sub(robot_id, event)

    def get_events(self, robot_id: str) -> List[Event]:
        return self._events.get(robot_id, [])

class StateProjector:
    @staticmethod
    def project(events: List[Event]) -> RobotState:
        state = RobotState(0.0, 0.0, 0, CleaningMode.WATER.value)
        for ev in events:
            if isinstance(ev, RobotMovedEvent):
                rads = state.angle * (math.pi / 180.0)
                state.x += ev.distance * math.cos(rads)
                state.y += ev.distance * math.sin(rads)
            elif isinstance(ev, RobotTurnedEvent):
                state.angle += ev.angle
        return state

class MoveProcessor:
    def __init__(self, store: EventStore):
        self.store = store

    def __call__(self, robot_id: str, event: Event):
        if isinstance(event, MoveRequestedEvent):
            self.store.append_event(robot_id, RobotMovedEvent(event.distance))

class TurnProcessor:
    def __init__(self, store: EventStore):
        self.store = store

    def __call__(self, robot_id: str, event: Event):
        if isinstance(event, TurnRequestedEvent):
            self.store.append_event(robot_id, RobotTurnedEvent(event.angle))

class CommandHandler:
    def __init__(self, store: EventStore):
        self.store = store

    def handle(self, robot_id: str, command_type: str, value: float):
        if command_type == "MOVE":
            self.store.append_event(robot_id, MoveRequestedEvent(value))
        elif command_type == "TURN":
            self.store.append_event(robot_id, TurnRequestedEvent(value))

def main():
    store = EventStore()
    store.subscribe(MoveProcessor(store))
    store.subscribe(TurnProcessor(store))
    
    handler = CommandHandler(store)
    robot_id = "robot_1"
    
    handler.handle(robot_id, "MOVE", 100)
    handler.handle(robot_id, "TURN", 90)
    
    events = store.get_events(robot_id)
    final_state = StateProjector.project(events)

if __name__ == "__main__":
    main()
