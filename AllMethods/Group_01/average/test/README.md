# Testing `average` Function

This repository provides tests for the `average` function, which computes the average of the elements in a list.

## Tests Explanation

- `test_empty_list`: Tests the average of an empty list.
- `test_integer_list`: Tests the average of a list containing only integers.
- `test_float_list`: Tests the average of a list containing only floating-point numbers.
- `test_mixed_list`: Tests the average of a list containing a mix of integers and floats.
- `test_invalid_input_string`: Checks for a `ValueError` when the list contains strings.
- `test_invalid_input_type`: Checks for a `TypeError` when the input is not a list.

## Running the Tests

1. **Using unittest from Command Line**:
   ```bash
   python -m unittest test_average.py
   ```

2. **Running the Script Directly**:
   ```bash
   python test_average.py
   ```

For more detailed output, add `-v` to the command:
   ```bash
   python -m unittest -v test_average.py
   ```