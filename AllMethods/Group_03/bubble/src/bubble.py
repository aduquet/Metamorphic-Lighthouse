def bubble(elements):
    if not isinstance(elements, list):
        raise TypeError("Input must be a list")

    # Check if all elements in the list are of the same type
    first_elem_type = type(elements[0]) if elements else None
    for elem in elements:
        if type(elem) != first_elem_type:
            raise ValueError("All elements in the list must be of the same type")

    for n in range(len(elements) - 1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
