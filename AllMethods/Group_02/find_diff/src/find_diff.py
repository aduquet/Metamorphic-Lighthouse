def find_diff(a, b):
    if len(a) != len(b):
        raise ValueError("Input lists must have the same length")

    c = []
    for i in range(len(a)):
        c.append(a[i] - b[i])

    return c
