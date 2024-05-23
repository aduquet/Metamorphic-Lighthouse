def sum(values):

    if not isinstance(values, list):
        raise TypeError("Input should be a list of numbers.")

    if not all(isinstance(i, (int, float)) for i in values):
        raise ValueError("List should contain only numbers.")
    total = 0

    for i in values:
        total += i

    return total

