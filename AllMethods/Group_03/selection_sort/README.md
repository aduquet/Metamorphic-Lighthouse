---------------------------------------------------------------
    selection_sort Function
---------------------------------------------------------------

Overview:
---------
- Sorts a list using the selection sort algorithm.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- list1 (list): The list to be sorted.

Returns:
--------
- list: The sorted list.

Functionality:
--------------
- Selection Sort Algorithm: Iteratively selects the smallest element from the unsorted portion and swaps it with the first unsorted element.

Example Usage:
--------------
> unsorted_list = [64, 25, 12, 22, 11]
> sorted_list = selection_sort(unsorted_list)
> print(sorted_list)  # Output: [11, 12, 22, 25, 64]

Error Handling:
---------------
- Effectively handles empty lists and lists with a single element.

Test Suite:
-----------
- Tests include sorting a list, handling an empty list, and a list with a single element.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
