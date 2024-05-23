def is_valid_input(input_data):
    """
    Checks if the given input is valid. Valid input can be a list of integers,
    a single integer, or a list containing lists and/or integers.

    :param input_data: The input data to be checked.
    :return: True if input is valid, False otherwise.
    """
    # Check if the input is a single integer
    if isinstance(input_data, int):
        return True

    # Check if the input is a list
    if not isinstance(input_data, list):
        return False

    # Check each element in the list
    for element in input_data:
        if not (isinstance(element, list) or isinstance(element, int)):
            return False

    return True

# Example Usage
input_data1 = [[1, 2, 3], [4, 5, 6]]
input_data2 = [1, 2, 3]
input_data3 = "not a list"
input_data4 = [[1, 2, 3, 4], 90]

print(is_valid_input(input_data1))  # Should return True

print(is_valid_input(input_data2))
print(is_valid_input(input_data3))# Should return True
print(is_valid_input(input_data4))
