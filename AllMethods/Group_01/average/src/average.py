def average(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    
    if len(data) == 0:
        return None  # Use None to represent the average of an empty list

    sum_data = 0
    for item in data:
        if not isinstance(item, (int, float)):
            raise ValueError("All elements in the list must be int or float")
        sum_data += item

    return sum_data / len(data)
