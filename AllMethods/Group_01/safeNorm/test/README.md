# Testing `safeNorm` Function

This repository provides a suite of tests for the `safeNorm` function, which returns the safe norm of a given list of numbers.

## Tests Explanation:

- `test_norm_of_numbers`: Tests the function on a list of numbers.
- `test_norm_single_element`: Tests the function on a list with a single element.
- `test_empty_list`: Tests the function's response to an empty list.
- `test_invalid_input_string_list`: Tests the function's response when given a list of strings.
- `test_invalid_input_string`: Tests the function's response when given a single string.

## Running the Tests:

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_safeNorm.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_safeNorm.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_safeNorm.py
   ```

Ensure that the `safeNorm_function.py` is in the same directory as the test script.
