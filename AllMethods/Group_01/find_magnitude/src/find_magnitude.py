import math

def find_magnitude(a):
    if not isinstance(a, list):
        raise TypeError("Input should be a list of numbers")

    if not a:
        raise ValueError("Input list should not be empty")

    return math.sqrt(sum([x**2 for x in a]))
