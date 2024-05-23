
def product(data):
    if not isinstance(data, list):
        raise TypeError("Input should be a list")

    if len(data) == 0:
        raise ValueError("List is empty")

    if not all(isinstance(i, (int, float)) for i in data):
        raise TypeError("List should contain only numbers")

    prod = 1
    for value in data:
        prod *= value

    return prod
