import math

def standardize(data):
    if not isinstance(data, list):
        raise TypeError("Input should be a list of numbers.")

    if not all(isinstance(i, (int, float)) for i in data):
        raise ValueError("List should contain only numbers.")

    n = len(data)
    if n == 0:
        raise ValueError("List is empty, cannot standardize.")

    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)

    if std_dev == 0:
        raise ValueError("Standard deviation is zero, cannot standardize.")

    return [(x - mean) / std_dev for x in data]
