# Testing `find_magnitude` Function

This repository provides a suite of tests for the `find_magnitude` function, which calculates the magnitude (or Euclidean norm) of a given list.

## Tests Explanation

- `test_valid_input`: Ensures the function correctly computes the magnitude for a standard list of numbers.
- `test_zero_vector`: Verifies that the function handles a zero vector correctly.
- `test_negative_elements`: Validates the function's computation with negative elements in the list.
- `test_single_element`: Checks the function's behavior for a list with only a single element.
- `test_empty_list`: Tests the function's response to an empty list.
- `test_invalid_input_type`: Assures the function raises an error when provided with an input that isn't a list.

## Running the Tests

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_find_magnitude.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_find_magnitude.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_find_magnitude.py
   ```
