def dividedDifference(x, y):
    if not (isinstance(x, list) and isinstance(y, list)):
        raise TypeError("Both x and y must be lists")

    if len(x) != len(y):
        raise ValueError("Lists x and y must have the same length")

    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = (divdiff[j + 1] - divdiff[j]) / denominator

        a.append(divdiff[0])
    return a
