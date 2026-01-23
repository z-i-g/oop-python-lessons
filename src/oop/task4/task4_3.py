import random
from typing import List

class Animal:
    def foo(self):
        pass

class Cat(Animal):
    def foo(self):
        print("The cat purrs")

class Bird(Animal):
    def foo(self):
        print("The bird sings")

def clear_and_random_fill(animals: List[Animal]):
    print(f'List before: {len(animals)}')
    animals.clear()
    for _ in range(5):
        animals.append(random.choice([Cat, Bird])()) 

    for animal in animals:
        animal.foo()

cat = Cat()
bird = Bird()
animals: List[Animal] = [cat, bird]
clear_and_random_fill(animals)

# Выводы каждый раз будут разные, т.к. каждый раз вызывается метод наследников
# Выводы
# The cat purrs
# The bird sings
# The bird sings
# The bird sings
# The bird sings

# The bird sings
# The cat purrs
# The cat purrs
# The bird sings
# The bird sings