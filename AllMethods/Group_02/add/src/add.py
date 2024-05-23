def add(array1, array2):
    """
    Adds corresponding elements of two arrays of equal length.

    :param array1: First array of integers.
    :param array2: Second array of integers.
    :return: An array where each element is the sum of elements from array1 and array2 at the same index.
    :raises ValueError: If the lengths of the input arrays are not equal.
    """
    if len(array1) != len(array2):
        raise ValueError("array1 and array2 must have the same length")

    for i in range(len(array1)):
        array1[i] += array2[i]

    return array1
