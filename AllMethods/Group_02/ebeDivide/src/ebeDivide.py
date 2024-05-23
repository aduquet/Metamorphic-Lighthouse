def ebeDivide(a, b):
    if not (isinstance(a, list) and isinstance(b, list)):
        raise TypeError("Both inputs must be lists")

    if len(a) != len(b):
        raise ValueError("Input lists must have the same length")

    result = []
    for i in range(len(a)):
        if b[i] == 0:
            raise ValueError("Division by zero encountered at index {}".format(i))
        result.append(a[i] / b[i])

    return result
