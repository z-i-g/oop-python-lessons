import math
from typing import List

state = 1
x = 0.0
y = 0.0
angle = 0


# выполнить
def execute(commands: List[str]):
    for command in commands:
        cmd_and_arg = command.split()
        cmd = cmd_and_arg[0]
        cmd_arg = get_cmd_arg(cmd_and_arg)

        if cmd == "move":
            move(cmd_arg)

        elif cmd == "turn":
            turn(cmd_arg)
                
        elif cmd == "set":
            set(cmd_arg)

        elif cmd == "start":
            start()

        elif cmd == "stop":
            stop()

def get_cmd_arg(cmd_and_arg):
    return cmd_and_arg[1] if len(cmd_and_arg) > 1 else None

def move(cmd_arg):
    global x, y
    radians = math.radians(angle)
    x += int(cmd_arg) * math.cos(radians)
    y += int(cmd_arg) * math.sin(radians)
    print(f"POS {x}, {y}")

def turn(cmd_arg):
    global angle
    angle += int(cmd_arg)
    print("ANGLE", angle)

def set(cmd_arg):
    global state
    if cmd_arg == "water":
        state = cmd_arg
    elif cmd_arg == "soap":
        state = cmd_arg
    elif cmd_arg == "brush":
        state = cmd_arg
    print("STATE", state)

def start():
    print("START WITH", state)

def stop():
    print("STOP")


work_programm = ("move 100", "turn -90", "set soap", "start", "move 50", "stop")

execute(work_programm)