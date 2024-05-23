def elementwise_min(a, b):
    if len(a) != len(b):
        raise ValueError("Input lists must have the same length")

    r = []
    for i in range(len(a)):
        r.append(min(a[i], b[i]))

    return r
