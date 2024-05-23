# Testing `max` Function

This repository provides a suite of tests for the `max` function, which determines the maximum value from a given list of numbers.

## Tests Explanation:

- `test_max_of_integers`: Tests finding the maximum of a list of integers.
- `test_max_with_negative_numbers`: Tests finding the maximum when the list contains negative numbers.
- `test_max_of_single_element`: Tests the maximum of a list with a single element.
- `test_max_of_floats`: Tests finding the maximum of a list of floating-point numbers.
- `test_empty_list`: Tests the function's response to an empty list.
- `test_invalid_data_string`: Tests the function's response to a list of strings.
- `test_invalid_data_mixed`: Tests the function's response to a mixed list of numbers and strings.

## Running the Tests:

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_max.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_max.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_max.py
   ```

Ensure that the `test_max.py` is in the same directory as the test script.
```
