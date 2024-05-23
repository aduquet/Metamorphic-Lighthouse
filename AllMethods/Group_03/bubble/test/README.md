
# Testing `bubble` Function

This repository contains tests for the `bubble` function, which sorts a list of elements using the bubble sort algorithm.

## Tests Explanation:

- `test_empty_list`: Tests sorting an empty list.
- `test_integer_list`: Tests sorting a list containing only integers.
- `test_string_list`: Tests sorting a list containing only strings.
- `test_invalid_mixed_list`: Checks for a `ValueError` when the list contains mixed types.
- `test_invalid_input_type`: Checks for a `TypeError` when the input is not a list.

## Running the Tests:

1. **Using unittest from Command Line**:
   ```bash
   python -m unittest test_bubble_sort.py
   ```

2. **Running the Script Directly**:
   ```bash
   python test_bubble_sort.py
   ```

For a more detailed output, add `-v` to the command:
   ```bash
   python -m unittest -v test_bubble_sort.py
   ```