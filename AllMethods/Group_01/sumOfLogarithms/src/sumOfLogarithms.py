import math

def sumOfLogarithms(elements):
    if not isinstance(elements, list):
        raise TypeError("Input should be a list of numbers.")

    if not all(isinstance(i, (int, float)) for i in elements):
        raise ValueError("List should contain only numbers.")

    if any(i <= 0 for i in elements):
        raise ValueError("All numbers in the list should be positive to compute the logarithm.")

    return sum(math.log(element) for element in elements)
