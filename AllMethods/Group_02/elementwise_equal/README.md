---------------------------------------------------------------
    elementwise_equal Function
---------------------------------------------------------------

Overview:
---------
- Compares two lists element by element to check for equality.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- a (list): The first list for comparison.
- b (list): The second list for comparison.

Returns:
--------
- list: A list of booleans indicating elementwise equality.
- Raises ValueError if lists have different lengths.

Functionality:
--------------
- Input Validation: Checks if both lists are of the same length.
- Comparison: Iterates through the lists and compares each element pair.

Example Usage:
--------------
> list1 = [1, 2, 3]
> list2 = [1, 2, 4]
> result = elementwise_equal(list1, list2)
> print(result)  # Output: [True, True, False]

Error Handling:
---------------
- ValueError: Raised for lists of different lengths.

Test Suite:
-----------
- Tests include typical elementwise comparison and mismatched list lengths.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
