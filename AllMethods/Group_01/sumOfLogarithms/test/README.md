# Testing `sum_of_logarithms` Function

This repository provides a suite of tests for the `sum_of_logarithms` function, which calculates the sum of logarithms of numbers in a list.

## Tests Explanation:

- `test_sum_log_normal`: Tests the function on a list of positive numbers.
- `test_sum_log_empty`: Tests the function's behavior with an empty list.
- `test_sum_log_invalid_input`: Checks the function's response when given a single string.
- `test_sum_log_strings_in_list`: Checks the function's response when provided with a list of strings.
- `test_sum_log_negative_numbers`: Checks the function's behavior with negative numbers.

## Running the Tests:

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_logarithm_sum.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_logarithm_sum.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_logarithm_sum.py
   ```