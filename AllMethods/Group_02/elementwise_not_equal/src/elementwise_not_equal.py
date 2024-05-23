def elementwise_not_equal(a, b):
    if len(a) != len(b):
        raise ValueError("Input lists must have the same length")

    r = []
    for i in range(len(a)):
        r.append(a[i] != b[i])

    return r
