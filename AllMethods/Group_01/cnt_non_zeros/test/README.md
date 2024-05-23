
# Testing `count_non_zeros` Function

This repository contains tests for the `count_non_zeros` function, which counts the number of non-zero elements in a given list.

## Tests Explanation:

- `test_empty_list`: Tests counting non-zeros in an empty list.
- `test_integer_list`: Tests counting non-zeros in a list containing only integers.
- `test_none_values_in_list`: Tests counting non-zeros in a list containing `None` values.
- `test_string_values_in_list`: Tests counting non-zeros in a list containing string values.
- `test_invalid_input_type`: Checks for a `TypeError` when the input is not a list.

## Running the Tests:

1. **Using unittest from Command Line**:
   ```bash
   python -m unittest test_count_non_zeros.py
   ```

2. **Running the Script Directly**:
   ```bash
   python test_count_non_zeros.py
   ```

For a more detailed output, add `-v` to the command:
   ```bash
   python -m unittest -v test_count_non_zeros.py
   ```
