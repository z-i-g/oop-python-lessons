from architecture.task12.pure_robot import transfer_to_cleaner
from architecture.task12 import pure_robot
from pymonad.operators.maybe import Just, Maybe

# Предположу что достаточно обернуть целевые цункции и возвращать внутреннюю
def mon_move(dist):
    def mon(state_list: list):
        new_state = pure_robot.move(transfer_to_cleaner, dist, state_list[-1])
        state_list.append(new_state)
        return Just(state_list)
    return mon