def max(data):
    if not data:
        raise ValueError('Empty list has no maximum value.')

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError('All elements must be numeric.')

    maximum = data[0]

    for num in data:
        if num > maximum:
            maximum = num

    return maximum