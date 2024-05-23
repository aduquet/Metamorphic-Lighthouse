# Testing `variance` Function

This repository provides tests for the `variance` function which calculates the variance of a list of numbers.

## Tests Explanation:

- `test_variance_normal`: Tests the function on a regular list of numbers.
- `test_variance_empty`: Tests the function's behavior with an empty list.
- `test_variance_invalid_input`: Checks the function's response when given a single string.
- `test_variance_strings_in_list`: Checks the function's response when provided with a list of strings.

## Running the Tests:

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_variance_calc.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_variance_calc.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_variance_calc.py
   ```

Ensure that the `variance_calc.py` is in the same directory as the test script.
