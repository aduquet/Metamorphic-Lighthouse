# Testing `insertion_sort` Function

This repository provides a suite of tests for the `insertion_sort` function, which sorts a given list using the insertion sort algorithm.

## Tests Explanation:

- `test_sort_integer_list`: Tests sorting a list of integers.
- `test_sort_float_list`: Tests sorting a list of floating-point numbers.
- `test_sort_mixed_numbers`: Tests sorting a mixed list containing both integers and floats.
- `test_empty_list`: Tests sorting an empty list.
- `test_invalid_input_string`: Tests whether the function raises a TypeError when given a list of strings.
- `test_invalid_input_mixed`: Tests whether the function raises a TypeError when given a mixed list of numbers and strings.

## Running the Tests:

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_insertion_sort.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_insertion_sort.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_insertion_sort.py
   ```

Ensure you've imported the `insertion_sort` function correctly in the test module.
```