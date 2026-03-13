import pure_robot

class RobotCleanerApi:

    def __init__(self, move_func, tern_func, set_state_func, start_func, stop_func):
        self.move_func = move_func
        self.tern_func = tern_func
        self.set_state_func = set_state_func
        self.start_func = start_func
        self.stop_func = stop_func

    def transfer_to_cleaner(self, message):
        print (message)

    def execute(self, code):
        self.cleaner_state = pure_robot.RobotState(0.0, 0.0, pure_robot.WATER)
        for command in code:
            cmd_and_arg = command.split()
            cmd = cmd_and_arg[0]
            cmd_arg = cmd_and_arg[1] if len(cmd_and_arg) > 1 else None

            if cmd == "move":
                self.cleaner_state = self.move_func(self.transfer_to_cleaner, cmd_arg, self.cleaner_state)
            elif cmd == "turn":
                self.cleaner_state = self.tern_func(self.transfer_to_cleaner, cmd_arg, self.cleaner_state)
            elif cmd == "set":
                self.cleaner_state = self.set_state_func(self.transfer_to_cleaner, cmd_arg, self.cleaner_state)
            elif cmd == "start":
                self.cleaner_state = self.start_func(self.transfer_to_cleaner, cmd_arg, self.cleaner_state)
            elif cmd == "stop":
                self.cleaner_state = self.stop_func(self.transfer_to_cleaner, cmd_arg, self.cleaner_state)

robotCleanerApi = RobotCleanerApi(
    pure_robot.move,
    pure_robot.turn,
    pure_robot.set_state,
    pure_robot.start, pure_robot.stop)