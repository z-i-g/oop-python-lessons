import functools

def odometer_elegant(oksana):
    spd = oksana[0::2]
    tim = oksana[1::2]

    diff = list(map(lambda x, y: x - y, tim, [0] + tim[:-1]))
    
    return functools.reduce(lambda a, b: a + b, map(lambda s, d: s * d, spd, diff))

print(odometer_elegant([10, 1, 20, 2]))
print(odometer_elegant([15, 1, 25, 2, 30, 3, 10, 5]))