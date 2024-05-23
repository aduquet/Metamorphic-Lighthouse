---------------------------------------------------------------
    ebeMultiply Function
---------------------------------------------------------------

Overview:
---------
- Performs element-by-element multiplication of two lists.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- a (list): The first list for multiplication.
- b (list): The second list for multiplication.

Returns:
--------
- list: A new list containing the element-wise product of a and b.
- Raises TypeError if inputs are not lists.
- Raises ValueError if lists have different lengths.

Functionality:
--------------
- Input Validation: Ensures inputs are lists and of the same length.
- Multiplication: Multiplies corresponding elements of list a by list b.

Example Usage:
--------------
> list1 = [1, 2, 3]
> list2 = [4, 5, 6]
> result = ebeMultiply(list1, list2)
> print(result)  # Output: [4, 10, 18]

Error Handling:
---------------
- TypeError: Raised for non-list inputs.
- ValueError: Raised for lists of different lengths.

Test Suite:
-----------
- Tests include typical EBE multiplication, invalid input types, and mismatched list lengths.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
