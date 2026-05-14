from pymonad.tools import curry
from pymonad.maybe import Just, Nothing

@curry(2)
def to_left(num, pole):
    left, right = pole
    if abs((left + num) - right) > 4:
        return Nothing
    return Just((left + num, right))

@curry(2)
def to_right(num, pole):
    left, right = pole
    if abs(right + num - left) > 4:
        return Nothing
    return Just((left, right + num))

def banana(pole):
    return Nothing

def show(maybe_monad):
    if maybe_monad == Nothing:
        print("The tightrope walker has fallen!")
    else:
        print(f"He's holding up fine. Birds on a pole (left, right): {maybe_monad.value}")


print("Test 1: Successful balance")
sim1 = Just((0, 0)).bind(to_left(2)).bind(to_right(3)).bind(to_left(1))
show(sim1)

print("\nTest2: Falling due to imbalance")
sim2 = Just((0, 0)).bind(to_left(1)).bind(to_right(6)).bind(to_left(1))
show(sim2)

print("\nTest 3: Falling on a banana")
sim3 = Just((0, 0)).bind(to_left(2)).bind(banana).bind(to_right(2))
show(sim3)