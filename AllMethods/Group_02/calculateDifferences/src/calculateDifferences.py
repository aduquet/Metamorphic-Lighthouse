def calculateDifferences(x, y):
    if not isinstance(x, list) or not isinstance(y, list):
        raise TypeError("Both inputs must be lists")

    if len(x) != len(y):
        raise ValueError("Both lists must have the same length")

    z = []
    for i in range(len(x)):
        z.append(y[i] - x[i])

    return z
