import pure_robot

class RobotCleanerApi:

    def setup(self, fnc, f_transfer):
        self.f_transfer = f_transfer
        self.fnc = fnc

    def make(self, command):
        if not hasattr(self, 'cleaner_state'):
            self.cleaner_state = pure_robot.RobotState(0.0, 0.0, 0, pure_robot.WATER)

        cmd = command.split(' ')
        if cmd[0]=='move':
             self.cleaner_state = self.f_move(self.f_transfer,int(cmd[1]), 
                 self.cleaner_state) 
        elif cmd[0]=='turn':
            self.cleaner_state = self.f_turn(self.f_transfer,int(cmd[1]), 
                 self.cleaner_state)
        elif cmd[0]=='set':
            self.cleaner_state = self.f_set_state(self.f_transfer,cmd[1], 
                 self.cleaner_state) 
        elif cmd[0]=='start':
            self.cleaner_state = self.f_start(self.f_transfer, 
               self.cleaner_state)
        elif cmd[0]=='stop':
            self.cleaner_state = self.f_stop(self.f_transfer, 
               self.cleaner_state)
        return self.cleaner_state

    def __call__(self, command):
        return self.make(command)


def transfer_to_cleaner(message):
    print (message)

def double_move(transfer,dist,state):
    return pure_robot.move(transfer,dist*2,state)

# Передаем все в одной функции
def robotAction(cmd):
    if cmd[0]=='move':
        return pure_robot.move
    elif cmd[0]=='turn':
        return pure_robot.turn  
    elif cmd[0]=='set':
        return pure_robot.set_state 
    elif cmd[0]=='start':
        return pure_robot.start
    elif cmd[0]=='stop':
        return pure_robot.stop 
    return None

api = RobotCleanerApi()    
api.setup(robotAction, transfer_to_cleaner)
