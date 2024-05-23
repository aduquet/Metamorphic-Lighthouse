---------------------------------------------------------------
    ebeAdd Function
---------------------------------------------------------------

Overview:
---------
- Performs element-by-element addition of two lists.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- a (list): The first list for addition.
- b (list): The second list for addition.

Returns:
--------
- list: A new list containing the element-wise sum of a and b.
- Raises TypeError if inputs are not lists.
- Raises ValueError if lists have different lengths.

Functionality:
--------------
- Input Validation: Checks if inputs are lists and of the same length.
- EBE Addition: Iterates through the lists and adds corresponding elements.

Example Usage:
--------------
> list1 = [1, 2, 3]
> list2 = [4, 5, 6]
> result = ebeAdd(list1, list2)
> print(result)  # Output: [5, 7, 9]

Error Handling:
---------------
- TypeError: Raised for non-list inputs.
- ValueError: Raised for lists of different lengths.

Test Suite:
-----------
- Tests include typical EBE addition, invalid input types, and mismatched list lengths.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
