---------------------------------------------------------------
    find_diff Function
---------------------------------------------------------------

Overview:
---------
- Calculates the element-wise difference between two lists.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- a (list): The first list for comparison.
- b (list): The second list for comparison.

Returns:
--------
- list: A new list containing the element-wise differences of a and b.
- Raises ValueError if lists have different lengths.

Functionality:
--------------
- Input Validation: Ensures both lists are of the same length.
- Difference Calculation: Subtracts each element of b from the corresponding element in a.

Example Usage:
--------------
> list1 = [1, 2, 3]
> list2 = [4, 5, 6]
> result = find_diff(list1, list2)
> print(result)  # Output: [-3, -3, -3]

Error Handling:
---------------
- ValueError: Raised for lists of different lengths.

Test Suite:
-----------
- Tests include typical element-wise difference calculation and mismatched list lengths.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
