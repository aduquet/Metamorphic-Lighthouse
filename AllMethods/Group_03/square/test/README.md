
# Testing `square` Function

This repository provides a suite of tests for the `square` function, which squares each element of a list of numbers.

## Tests Explanation:

- `test_square_of_numbers`: Tests the function on a list of positive numbers.
- `test_square_of_negative_numbers`: Tests the function on a list of negative numbers.
- `test_square_of_empty_list`: Tests the function's behavior with an empty list.
- `test_invalid_input_string_list`: Checks the function's response when provided with a list of strings.
- `test_invalid_input_type`: Checks the function's response when given a single string.

## Running the Tests:

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_square.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_square.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_square.py
   ```

Ensure that the `square.py` is in the same directory as the test script.
