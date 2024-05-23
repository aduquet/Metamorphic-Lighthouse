def variance(data):
    if not isinstance(data, list):
        raise TypeError("Input should be a list of numbers.")

    if not all(isinstance(i, (int, float)) for i in data):
        raise ValueError("List should contain only numbers.")

    if len(data) == 0:
        raise ValueError("List cannot be empty.")

    mean = sum(data) / len(data)
    return sum((i - mean) ** 2 for i in data) / len(data)
