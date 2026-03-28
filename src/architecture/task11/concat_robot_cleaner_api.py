import pure_robot

class ConcatRobotCleanerApi:

    def __init__(self):
        self.stack = []
        self.stack.append(pure_robot.RobotState(0.0, 0.0, 0, pure_robot.WATER))


    def execute(self, commands):
        commands_list = commands.split(' ')
        for command in commands_list:
            self.parse(command)
        return self.stack[0]

    def parse(self, command):
        if command == 'move':
            command_value = self.pop()
            old_state = self.pop()
            new_state = pure_robot.move(transfer_to_cleaner, int(command_value), old_state) 
            self.push(new_state)
        elif command == 'turn':
            command_value = self.pop()
            old_state = self.pop()
            new_state = pure_robot.turn(transfer_to_cleaner, int(command_value), old_state) 
            self.push(new_state)
        elif command == 'set':
            command_value = self.pop()
            old_state = self.pop()
            new_state = pure_robot.set_state(transfer_to_cleaner, command_value, old_state) 
            self.push(new_state)
        elif command == 'start':
            old_state = self.pop()
            new_state = pure_robot.start(transfer_to_cleaner, old_state) 
            self.push(new_state)
        elif command == 'stop':
            old_state = self.pop()
            new_state = pure_robot.stop(transfer_to_cleaner, old_state) 
            self.push(new_state)
        else:
            self.push(command)

    def pop(self):
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

def transfer_to_cleaner(message):
    print (message)