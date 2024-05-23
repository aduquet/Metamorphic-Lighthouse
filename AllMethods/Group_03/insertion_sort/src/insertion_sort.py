def insertion_sort(arrays):
    if not isinstance(arrays, list):
        raise TypeError("Input should be a list")
    
    if not all(isinstance(i, (int, float)) for i in arrays):
        raise TypeError("List should contain only numbers")

    for i in range(1, len(arrays)):
        j = i
        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 1
        arrays[j] = B

    return arrays
