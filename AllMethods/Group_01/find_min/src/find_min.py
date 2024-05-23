def find_min(data):
    if not isinstance(data, list):
        raise TypeError("Input should be a list")

    if len(data) == 0:
        raise ValueError("List is empty, cannot determine minimum value")

    if not all(isinstance(i, (int, float)) for i in data):
        raise TypeError("List should contain only numbers")

    mini = data[0]
    for i in data:
        if i < mini:
            mini = i

    return mini
