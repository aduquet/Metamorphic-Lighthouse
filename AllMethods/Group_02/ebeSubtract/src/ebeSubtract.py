def ebeSubtract(a, b):
    if len(a) != len(b):
        raise ValueError("The lists must have the same length.")

    result = a.copy()
    for i in range(len(a)):
        result[i] -= b[i]

    return result
