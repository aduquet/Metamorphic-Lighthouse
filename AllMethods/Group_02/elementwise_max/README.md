---------------------------------------------------------------
    elementwise_max Function
---------------------------------------------------------------

Overview:
---------
- Computes the elementwise maximum of two lists.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- a (list): The first list for comparison.
- b (list): The second list for comparison.

Returns:
--------
- list: A list containing the maximum value of each element pair from a and b.
- Raises ValueError if lists have different lengths.

Functionality:
--------------
- Input Validation: Ensures both lists are of the same length.
- Maximum Calculation: Determines the maximum value for each element pair.

Example Usage:
--------------
> list1 = [1, 4, 3]
> list2 = [2, 2, 2]
> result = elementwise_max(list1, list2)
> print(result)  # Output: [2, 4, 3]

Error Handling:
---------------
- ValueError: Raised for lists of different lengths.

Test Suite:
-----------
- Tests include typical elementwise maximum calculation and mismatched list lengths.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
