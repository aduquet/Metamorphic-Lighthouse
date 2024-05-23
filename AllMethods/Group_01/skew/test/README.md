# Testing `skewness` Function

This repository provides a suite of tests for the `skewness` function, which calculates the skewness of a list of numbers.

## Tests Explanation:

- `test_skewness_of_numbers`: Tests the function on a list of numbers.
- `test_two_elements`: Tests the function's behavior with two elements in the list.
- `test_empty_list`: Tests the function's behavior with an empty list.
- `test_invalid_input_string_list`: Checks the function's response when provided with a list of strings.
- `test_invalid_input_string`: Checks the function's response when given a single string.

## Running the Tests:

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_skewness.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_skewness.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_skewness.py
   ```

Ensure that the `skewness_function.py` is in the same directory as the test script.
