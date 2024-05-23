# Testing `find_min` Function

This repository provides a suite of tests for the `find_min` function, which identifies the smallest element of a given list.

## Tests Explanation

- `test_empty_list`: Tests finding the minimum of an empty list and expects a ValueError.
- `test_min_integer_list`: Tests finding the minimum in a list of integers.
- `test_min_float_list`: Tests finding the minimum in a list of floating-point numbers.
- `test_min_mixed_list`: Tests finding the minimum in a mixed list containing both integers and floating-point numbers.
- `test_min_single_element_list`: Tests finding the minimum in a list with a single element.
- `test_invalid_input_string`: Tests the minimum calculation for a list of strings and expects a TypeError.
- `test_invalid_input_mixed_list`: Tests the minimum calculation for a list containing a mix of numbers and strings and expects a TypeError.

## Running the Tests

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_find_min.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_find_min.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_find_min.py
   ```