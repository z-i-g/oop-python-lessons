from pymonad.tools import curry

@curry(2)
def add(x, y): 
    return x + y

@curry(4)
def add_second(x, y, z, l): 
    return x + y + l + z;

hello_add = add('Hello, ')
print(hello_add('world'))

hello_add_second = add_second('Hello')(', ')('!')
print(hello_add_second('Ayrat'))