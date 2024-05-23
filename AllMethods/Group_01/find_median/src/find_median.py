def find_median(data):
    if not isinstance(data, list):
        raise TypeError("Input should be a list of numbers")

    if not data:  # Check for empty list
        raise ValueError("List cannot be empty")

    if not all(isinstance(i, (int, float)) for i in data):  # Check if all elements are numbers
        raise ValueError("All elements in the list should be numbers")

    data.sort()

    n = len(data)
    if n % 2 == 0:
        median = (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        median = data[n // 2]

    return median
