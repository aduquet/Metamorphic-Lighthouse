---------------------------------------------------------------
    elementwise_min Function
---------------------------------------------------------------

Overview:
---------
- Computes the elementwise minimum of two lists.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- a (list): The first list for comparison.
- b (list): The second list for comparison.

Returns:
--------
- list: A list containing the minimum value of each element pair from a and b.
- Raises ValueError if lists have different lengths.

Functionality:
--------------
- Input Validation: Ensures both lists are of the same length.
- Minimum Calculation: Determines the minimum value for each element pair.

Example Usage:
--------------
> list1 = [1, 4, 3]
> list2 = [2, 2, 2]
> result = elementwise_min(list1, list2)
> print(result)  # Output: [1, 2, 2]

Error Handling:
---------------
- ValueError: Raised for lists of different lengths.

Test Suite:
-----------
- Tests include typical elementwise minimum calculation and mismatched list lengths.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
