---------------------------------------------------------------
    ebeDivide Function
---------------------------------------------------------------

Overview:
---------
- Performs element-by-element division of two lists.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- a (list): The dividend list.
- b (list): The divisor list.

Returns:
--------
- list: A new list containing the element-wise division of a by b.
- Raises TypeError if inputs are not lists.
- Raises ValueError if lists have different lengths or division by zero occurs.

Functionality:
--------------
- Input Validation: Ensures inputs are lists and of the same length.
- Division: Divides corresponding elements of list a by list b.

Example Usage:
--------------
> dividend = [10, 20, 30]
> divisor = [2, 4, 5]
> result = ebeDivide(dividend, divisor)
> print(result)  # Output: [5, 5, 6]

Error Handling:
---------------
- TypeError: Raised for non-list inputs.
- ValueError: Raised for lists of different lengths or division by zero.

Test Suite:
-----------
- Tests include typical EBE division, division by zero, invalid input types, and mismatched list lengths.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
