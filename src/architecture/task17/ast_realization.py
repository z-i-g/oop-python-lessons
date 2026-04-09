import math
from typing import Callable, Any, Optional

class Response:
    OK = "OK"
    ERROR = "ERROR"

class CommandNode:
    def interpret(self, robot):
        raise NotImplementedError()

class Stop(CommandNode):
    def interpret(self, robot):
        return robot

class Move(CommandNode):
    def __init__(self, distance: float, next_func: Callable[[str], CommandNode] = lambda _: Stop()):
        self.distance = distance
        self.next_func = next_func

    def interpret(self, robot):
        response = robot.execute_move(self.distance)
        next_node = self.next_func(response)
        return next_node.interpret(robot)

class Turn(CommandNode):
    def __init__(self, angle: float, next_func: Callable[[str], CommandNode] = lambda _: Stop()):
        self.angle = angle
        self.next_func = next_func

    def interpret(self, robot):
        response = robot.execute_turn(self.angle)
        next_node = self.next_func(response)
        return next_node.interpret(robot)

class SetState(CommandNode):
    def __init__(self, state: int, next_func: Callable[[str], CommandNode] = lambda _: Stop()):
        self.state = state
        self.next_func = next_func

    def interpret(self, robot):
        response = robot.execute_set_state(self.state)
        next_node = self.next_func(response)
        return next_node.interpret(robot)

class Robot:
    def __init__(self, x=0.0, y=0.0, angle=0, mode=1):
        self.x, self.y, self.angle, self.mode = x, y, angle, mode
        self.log = []

    def execute_move(self, dist):
        rad = math.radians(self.angle)
        nx, ny = self.x + dist * math.cos(rad), self.y + dist * math.sin(rad)
        
        if 0 <= nx <= 100 and 0 <= ny <= 100:
            self.x, self.y = nx, ny
            res = Response.OK
        else:
            self.x, self.y = max(0, min(100, nx)), max(0, min(100, ny))
            res = "HIT_BARRIER"
        
        self.log.append(f"MOVE to ({int(self.x)}, {int(self.y)}) -> {res}")
        return res

    def execute_turn(self, angle):
        self.angle += angle
        self.log.append(f"TURN to {self.angle}")
        return Response.OK

    def execute_set_state(self, mode):
        if mode == 2: # SOAP
            res = "OUT_OF_SOAP"
        else:
            self.mode = mode
            res = Response.OK
        
        self.log.append(f"SET_STATE {mode} -> {res}")
        return res

program = Move(150, lambda res: 
    SetState(2, lambda res2: 
        Turn(-90, lambda res3: 
            Move(50) if res2 == Response.OK else Stop()
        )
    )
)

robot = Robot()
program.interpret(robot)

for entry in robot.log:
    print(entry)
