import architecture.task6.pure_robot as pure_robot

class RobotCleanerApi:
    def __init__(self):
        self.cleaner_state = pure_robot.RobotState(0.0, 0.0, pure_robot.WATER)

# взаимодействие с роботом вынесено в отдельную функцию
def transfer_to_cleaner(message):
    print (message)

def execute_clean(self, code):
    for command in code:
        cmd = command.split(' ')
        cmd_arg = cmd[0]
        if cmd_arg == 'move':
            self.cleaner_state = pure_robot.move(self.transfer_to_cleaner, int(cmd[1]), self.cleaner_state)
        elif cmd_arg == 'turn':
            self.cleaner_state = pure_robot.turn(self.transfer_to_cleaner, int(cmd[1]), self.cleaner_state)
        elif cmd_arg == 'set':
            self.cleaner_state = pure_robot.set_state(self.transfer_to_cleaner, cmd[1], self.cleaner_state) 
        elif cmd_arg == 'start':
            self.cleaner_state = pure_robot.start(self.transfer_to_cleaner, self.cleaner_state)
        elif cmd_arg == 'stop':
            self.cleaner_state = pure_robot.stop(self.transfer_to_cleaner, self.cleaner_state)