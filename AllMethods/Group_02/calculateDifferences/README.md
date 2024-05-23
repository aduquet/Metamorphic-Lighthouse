---------------------------------------------------------------
        calculateDifferences Function
---------------------------------------------------------------

Overview:
---------
- Calculates the difference between corresponding elements of two lists.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- x (list): The first list of numbers.
- y (list): The second list of numbers.

Returns:
--------
- list: A new list containing the differences of corresponding elements in x and y.

Functionality:
--------------
- Input Validation: Checks if both x and y are lists and have the same length.
- Difference Calculation: Iterates through the lists, calculating the difference between corresponding elements.

Example Usage:
--------------
> first_list = [1, 2, 3]
> second_list = [4, 5, 6]
> result = calculateDifferences(first_list, second_list)
> print(result)  # Output: [3, 3, 3]

Error Handling:
---------------
- Raises TypeError if inputs are not lists.
- Raises ValueError if lists have different lengths.

---------------------------------------------------------------
