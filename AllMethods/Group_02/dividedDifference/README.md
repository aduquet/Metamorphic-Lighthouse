---------------------------------------------------------------
    DividedDifference Function
---------------------------------------------------------------

Overview:
---------
- Computes the divided differences for given x and y values.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- x (list): List of x values.
- y (list): List of y values.

Returns:
--------
- list: Divided differences calculated from x and y.
- Raises TypeError for non-list inputs.
- Raises ValueError for lists of different lengths.

Functionality:
--------------
- Input Validation: Checks if x and y are lists of the same length.
- Calculation: Computes the divided differences using the given x and y values.

Example Usage:
--------------
> x_values = [1, 2, 3, 4]
> y_values = [1, 2, 4, 8]
> result = computeDividedDifference(x_values, y_values)
> print(result)  # Output: [Calculated divided differences]

Error Handling:
---------------
- TypeError: Raised for non-list inputs.
- ValueError: Raised for lists of different lengths.

Test Suite:
-----------
- Includes tests for typical calculations, invalid input types, and mismatched list lengths.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
