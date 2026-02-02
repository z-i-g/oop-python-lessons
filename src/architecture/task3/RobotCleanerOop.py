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
            cmd_arg = self.get_cmd_arg(cmd_and_arg)

            if cmd == "move":
                self.move(cmd_arg)

            elif cmd == "turn":
                self.turn(cmd_arg)
                
            elif cmd == "set":
                self.set(cmd_arg)

            elif cmd == "start":
                self.start()

            elif cmd == "stop":
                self.stop()

    def get_cmd_arg(self, cmd_and_arg):
        return cmd_and_arg[1] if len(cmd_and_arg) > 1 else None

    def move(self, cmd_arg):
        radians = math.radians(self.angle)
        self.x += int(cmd_arg) * math.cos(radians)
        self.y += int(cmd_arg) * math.sin(radians)
        print(f"POS {self.x}, {self.y}")

    def turn(self, cmd_arg):
        self.angle += int(cmd_arg)
        print("ANGLE", self.angle)

    def set(self, cmd_arg):
        if cmd_arg == "water":
            self.state = cmd_arg
        elif cmd_arg == "soap":
            self.state = cmd_arg
        elif cmd_arg == "brush":
            self.state = cmd_arg
        print("STATE", self.state)

    def start(self):
        print("START WITH", self.state)

    def stop(self):
        print("STOP")


work_programm = ("move 100", "turn -90", "set soap", "start", "move 50", "stop")

robot = RobotCleaner()
robot.execute(work_programm)