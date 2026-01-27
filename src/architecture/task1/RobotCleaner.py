import math
from typing import List

class RobotCleaner:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.angle = 0
        self.state = "water"

    # выполнить
    def execute(self, commands: List[str]):
        for command in commands:
            cmd_and_arg = command.split()
            cmd = cmd_and_arg[0]
            cmd_arg = cmd_and_arg[1] if len(cmd_and_arg) > 1 else None

            if cmd == "move":
                radians = math.radians(self.angle)
                self.x += int(cmd_arg) * math.cos(radians)
                self.y += int(cmd_arg) * math.sin(radians)
                print(f"POS {self.x}, {self.y}")

            elif cmd == "turn":
                self.angle += int(cmd_arg)
                print("ANGLE", self.angle)

            elif cmd == "set":
                if cmd_arg == "water":
                    self.state = cmd_arg
                elif cmd_arg == "soap":
                    self.state = cmd_arg
                elif cmd_arg == "brush":
                    self.state = cmd_arg
                print("STATE", self.state)

            elif cmd == "start":
                print("START WITH", self.state)

            elif cmd == "stop":
                print("STOP")


work_programm = ("move 100", "turn -90", "set soap", "start", "move 50", "stop")

robot = RobotCleaner()
robot.execute(work_programm)
