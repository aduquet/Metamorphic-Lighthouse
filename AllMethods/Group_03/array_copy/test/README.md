
# Testing `array_copy` Function

This repository provides a suite of tests for the `array_copy` function, which creates a copy of a given list.

## Tests Explanation

- `test_copy_empty_list`: Tests copying an empty list.
- `test_copy_integer_list`: Tests copying a list of integers.
- `test_copy_string_list`: Tests copying a list of strings.
- `test_copy_mixed_list`: Tests copying a mixed list containing integers, strings, and floating-point numbers.

## Running the Tests

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_array_copy.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_array_copy.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_array_copy.py
   ```