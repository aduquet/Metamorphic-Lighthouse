def ebeAdd(a, b):
    if not (isinstance(a, list) and isinstance(b, list)):
        raise TypeError("Both inputs must be lists")

    if len(a) != len(b):
        raise ValueError("Input lists must have the same length")

    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])

    return result
