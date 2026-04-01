import pure_robot
from pymonad.operators.maybe import Just, Maybe

class TurnCommand:
    def __init__(self, angle):
        self.angle = angle

    def execute(self, state_list: list) -> Maybe:
        res = pure_robot.turn(pure_robot.transfer_to_cleaner, self.angle, state_list[-1])
        state_list.append(res)
        return Just(state_ls)

# Предположу решение через паттерн команда
class CommandFactory:

    @staticmethod
    def turn(angle):
        return TurnCommand(angle)