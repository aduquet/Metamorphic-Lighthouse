def dec(array1, array2):
    # Preconditions check: Ensure both arrays have the same length
    if len(array1) != len(array2):
        raise ValueError("array1.length != array2.length")

    # Perform element-wise subtraction
    for i in range(len(array1)):
        array1[i] = array1[i] - array2[i]

    return array1
