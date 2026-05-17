from pymonad.tools import curry
from pymonad.state import State

loan_start = State.insert("The application has been created")

@curry(2)
def check_history(has_debts, current_status):
    def state_computation(current_money):
        if has_debts:
            new_status = current_status + " -> Debts have been detected (The limit has been cut)"
            return new_status, current_money - 200000
        else:
            new_status = current_status + " -> The story is clean"
            return new_status, current_money
    return State(state_computation)

@curry(2)
def check_employment(is_employed, current_status):
    def state_computation(current_money):
        if is_employed:
            new_status = current_status + " -> The job is confirmed"
            return new_status, current_money
        else:
            new_status = current_status + " -> Unemployed (Refusal)"
            return new_status, 0
    return State(state_computation)

loan_pipeline = (
    loan_start
    .then(check_history(True))
    .then(check_employment(True))
)

final_status, final_money = loan_pipeline.run(500000)

print("Status history:\n", final_status)

print("\nTotal available amount:", final_money)