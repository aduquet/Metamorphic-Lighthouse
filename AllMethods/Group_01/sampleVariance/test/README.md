# Testing `sample_variance` Function

This repository provides a suite of tests for the `sample_variance` function, which calculates the sample variance of a list of numbers.

## Tests Explanation:

- `test_variance_of_numbers`: Tests the function on a list of numbers.
- `test_single_element`: Tests the function's behavior with a single element list.
- `test_empty_list`: Tests the function's behavior with an empty list.
- `test_invalid_input_string_list`: Checks the function's response when provided with a list of strings.
- `test_invalid_input_string`: Checks the function's response when given a single string.

## Running the Tests:

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_sample_variance.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_sample_variance.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_sample_variance.py
   ```

Ensure that the `sample_variance_function.py` is in the same directory as the test script.