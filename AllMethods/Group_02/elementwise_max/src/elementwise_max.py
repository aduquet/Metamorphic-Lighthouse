def elementwise_max(a, b):
    if len(a) != len(b):
        raise ValueError("Input lists must have the same length")

    r = []
    for i in range(len(a)):
        r.append(max(a[i], b[i]))

    return r
