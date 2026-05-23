import functools

def find_second_max(numbers):
    initial_state = (-float('inf'), -float('inf'))
    
    def update_max(acc, x):
        max1, max2 = acc
        if x >= max1:
            return (x, max1)
        elif x > max2:
            return (max1, x)
        return (max1, max2)

    final_max1, final_max2 = functools.reduce(update_max, numbers, initial_state)
    
    return final_max2

print(find_second_max([5, 4, 3, 2, 5]))
print(find_second_max([233, 202, 302, 403]))
print(find_second_max([12, 19, 15, 21]))