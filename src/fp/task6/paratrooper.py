from pymonad.tools import curry
from pymonad.state import State
from pymonad.list import ListMonad
import sys

sys.setrecursionlimit(3000)

@curry(3)
def get_neighbors(n, m, cell):
    x, y = cell
    raw_moves = ListMonad((x, y), (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
    return [(cx, cy) for cx, cy in raw_moves if 1 <= cx <= n and 1 <= cy <= m]

@curry(3)
def simulate_day(n, m, current_day):
    def state_computation(captured_cells):
        next_generation = {
            neighbor 
            for cell in captured_cells 
            for neighbor in get_neighbors(n, m, cell)
        }
        return current_day + 1, next_generation
    return State(state_computation)


def ConquestCampaign(N, M, L, battalion):
    initial_coordinates = [(battalion[i], battalion[i+1]) for i in range(0, len(battalion), 2)]
    initial_state = set(initial_coordinates)
    total_cells = N * M

    start_plan = State.insert(1)

    def run_simulation(current_plan, cells_set):
        if len(cells_set) >= total_cells:
            day_result, _ = current_plan.run(cells_set)
            return day_result
        
        next_plan = current_plan.then(simulate_day(N, M))
        _, updated_cells = next_plan.run(cells_set)
        
        return run_simulation(next_plan, updated_cells)
    return run_simulation(start_plan, initial_state)

N = 3
M = 4
L = 2
battalion = [2, 2, 3, 4]

result_day = ConquestCampaign(N, M, L, battalion)
print(f"Day number: {result_day}")
