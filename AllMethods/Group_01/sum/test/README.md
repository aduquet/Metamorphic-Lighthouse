# Testing `sum` Function

This repository provides a suite of tests for the `sum` function, which calculates the sum of elements in a list of numbers.

## Tests Explanation:

- `test_sum_normal`: Tests the function on a list of numbers.
- `test_sum_empty`: Tests the function's behavior with an empty list.
- `test_sum_invalid_input`: Checks the function's response when given a single string.
- `test_sum_strings_in_list`: Checks the function's response when provided with a list of strings.

## Running the Tests:

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_sum.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_sum.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_sum.py
   ```
