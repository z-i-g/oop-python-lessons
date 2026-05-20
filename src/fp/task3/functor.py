from pymonad.tools import curry
from pymonad.maybe import Maybe, Just, Nothing
from pymonad.list import ListMonad

@curry(2)
def add(x, y):
    return x + y

add10_maybe = Maybe.apply(add).to_arguments(Just(10))
print(add10_maybe.amap(Just(5)))
print(add10_maybe.amap(Nothing))

add10_list = ListMonad.apply(add).to_argum45788754
ents(ListMonad(10))
print(add10_list.amap(ListMonad(1, 2, 3)))